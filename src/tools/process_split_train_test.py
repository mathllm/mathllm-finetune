import json
import os
import re
from tqdm import tqdm
import time
from argparse import ArgumentParser
from random import shuffle, seed

def save_jsonl(datas, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for data in datas:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

def load_jsonl(in_file):
    with open(in_file, "r", encoding="utf-8") as f:
        datas = [json.loads(line) for line in f]
    return datas

def process_to_alignment(in_files, out_file_train, out_file_test):

    new_datas = []

    for in_file in in_files:
        new_datas.extend(load_jsonl(in_file))

    seed(3407)
    shuffle(new_datas)
    
    test_train_split = int(0.001 * len(new_datas))
    save_jsonl(new_datas[:test_train_split], out_file_test)
    save_jsonl(new_datas, out_file_train)


def main():
    in_files = [
        "/path/to/data/data_file.jsonl",
    ]
    out_dir = f"/path/to/our_dir"
    if not os.path.exists(f"{out_dir}/data/train/"):
        os.makedirs(f"{out_dir}/data/train/")
    if not os.path.exists(f"{out_dir}/data/test/"):
        os.makedirs(f"{out_dir}/data/test/")
    out_train_file = f"{out_dir}/data/train/train.jsonl"
    out_test_file = f"{out_dir}/data/test/test.jsonl"
    process_to_alignment(in_files, out_train_file, out_test_file)


if __name__ == "__main__":
    main()