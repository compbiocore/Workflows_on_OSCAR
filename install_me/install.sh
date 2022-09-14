#!bin/bash

# First time we run install, back up .bashrc, just in case 
if [ ! -f "$HOME/.bashrc.bak" ]; then cp ~/.bashrc ~/.bashrc.bak; fi 
# Copy installation folders 
cp -r ~/workflows_on_OSCAR/install_me/nextflow_setup ~/nextflow_setup
# Run Python script 
python3 $HOME/workflows_on_OSCAR/workflows.py 
