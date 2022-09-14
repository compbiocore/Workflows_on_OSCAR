#!bin/bash

# First time we run install, back up .bashrc, just in case 
if [ ! -f "$HOME/.bashrc.bak" ]; then cp ~/.bashrc ~/.bashrc.bak; fi 
# Create a user-friendly alias to shut off virtual environments 
if [ "$(type -t quit)" = "alias" ] && [! alias | grep -q "quit='deactivate'" ]; then echo "$(echo $(type quit)) and is being overwritten"; fi 
grep -qxF 'alias quit="deactivate"' ~/.bashrc || echo 'alias quit="deactivate"' >> ~/.bashrc; 
# Load needed modules 
module load python/3.9.0
module load java/jdk-11.0.11
# Run Python script 
python3 $HOME/workflows_on_OSCAR/workflows.py 
