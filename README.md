# MathLLM Finetune

This repository contains code to finetune MathLLM models.

## Contents

The repository focus on:

* **LCE format math supervised fine-tuning:** finetune LLMs with Natural Language, Code, and Execution (LCE) format solutions.

## Installation instructions

To run the code in this project, first, create a Python virtual environment using e.g. Conda:

```shell
conda create -n mathllmenv python=3.10 && conda activate mathllmenv
```

Next, install PyTorch `v2.1.2` - the precise version is important for reproducibility! Since this is hardware-dependent, we
direct you to the [PyTorch Installation Page](https://pytorch.org/get-started/locally/).

You can then install the remaining package dependencies as follows:

```shell
git clone https://github.com/mathllm/mathllm-finetune.git
cd ./mathllm-finetune/
python -m pip install .
```

You will also need Flash Attention 2 installed, which can be done by running:

```shell
python -m pip install flash-attn --no-build-isolation
```

> **Note**
> If your machine has less than 96GB of RAM and many CPU cores, reduce the `MAX_JOBS` arguments, e.g. `MAX_JOBS=4 pip install flash-attn --no-build-isolation`

To log training metrics using wandb, run:

```shell
pip install wandb
```

## Finetuning

To finetune MathCoder models, first, download the MathCodeInstruct dataset from [MathCodeInstruct](https://huggingface.co/datasets/MathLLMs/MathCodeInstruct). To split the dataset into training set and testing set, use script `./src/tools/process_split_train_test.py`. Modify `in_files` and `out_dir` by replacing them with the path to the jsonl file `MathCodeInstruct/train_80k.jsonl` and the path to which the split dataset is saved, which we call `/path/to/data/MathCodeInstruct` (replace `/path/to/data` with your own path). Run the following command:

```shell
python ./src/tools/process_split_train_test.py
```

The scripts to train MathCoder-CL-7B and MathCoder-CL-34B are in `recipes`. To train MathCoder-CL-7B, modify `./recipes/MathCoder-CL-7B/sft/config_full.yaml` by replacing `/path/to/models/CodeLlama-7b-Instruct-hf` and `/path/to/output/models/MathCoder-CodeLlama-7B_sft` with your own absolute paths. Replace `wandb token` in `./recipes/MathCoder-CL-7B/sft/sft_8gpu.sh` with our own wandb token. Then run the following command:

```shell
bash ./recipes/MathCoder-CL-7B/sft/sft_8gpu.sh ./recipes/MathCoder-CL-7B/sft/config_full.yaml
```

Distributed training scripts to train MathCoder-CL-34B are in `./recipes/MathCoder-CL-34B/sft`. You likely need to modify them based on your own distributed training environment.

## Project structure

```
├── LICENSE
├── Makefile                    <- Makefile with commands like `make style`
├── README.md                   <- The top-level README
├── recipes                     <- Recipe configs, accelerate configs, slurm scripts
├── scripts                     <- Scripts to train and evaluate chat models
├── setup.cfg                   <- Installation config (mostly used for configuring code quality & tests)
├── setup.py                    <- Makes project pip installable (pip install -e .) so `alignment` can be imported
└── src                         <- Source code for use in this project
```


