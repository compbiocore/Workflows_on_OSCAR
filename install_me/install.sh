#!bin/bash

# Back up .bashrc, just in case 
cp ~/.bashrc ~/.bashrc.bak
# Load needed modules 
module load python/3.9.0
module load java/jdk-11.0.11
# Run Python script 
python3 $HOME/workflows_on_OSCAR/workflows.py 
