# activate conda
__conda_setup="$('/usr/local/lib/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/usr/local/lib/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/usr/local/lib/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/usr/local/lib/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup

conda activate mathllmenv
cd /path/to/project/mathllm-finetune

wandb login "wandb token"

CONFIG=${1}

ACCELERATE_LOG_LEVEL=info accelerate launch --config_file ./recipes/accelerate_configs/deepspeed_zero3_4gpu.yaml ./scripts/run_sft_lce.py ${CONFIG}