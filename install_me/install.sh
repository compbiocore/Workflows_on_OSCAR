#!bin/bash

# Back up .bashrc, just in case 
cp ~/.bashrc ~/.bashrc.bak
# Copy installation folders 
cp -r ~/workflows_on_OSCAR/install_me/nextflow_setup ~/nextflow_setup
# Run Python script 
python3 $HOME/workflows_on_OSCAR/workflows.py 
