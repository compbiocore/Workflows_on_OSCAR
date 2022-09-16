#!/bin/bash


env_var="nextflow_env_${USER}"
cd $HOME
if [ ! -d "$HOME/$env_var" ]; then
    echo "Setting up and installing Nextflow.." 
    # Create virutal environment for user 
    virtualenv $env_var
    source $HOME/$env_var/bin/activate 
    wget -qO- https://get.nextflow.io | bash
    # Make nextflow executable and move to path 
    chmod +x nextflow
    mv nextflow $HOME/$env_var/bin
    deactivate
    echo "Nextflow software installed, initializing configuration..." 
else 
    echo "Nextflow software detected, initializing configuration..."
fi 

# change .bashrc and source aliases to make it more user-friendly 
if [ ! -f "$HOME/.nextflow_specific_aliases" ]; then touch ~/.nextflow_specific_aliases; fi 
echo 'alias nextflow_start="if ! echo $PATH | grep -oq 'java/jdk-11.0.11'; then module load java/jdk-11.0.11; fi && source ~/nextflow_env_${USER}/bin/activate"' >> $HOME/.nextflow_specific_aliases 
echo 'alias nextflow_remove="rm -rf ~/nextflow_env_${USER} ~/.nextflow ~/nextflow_setup ~/.nextflow_specific_aliases; unalias nextflow_start; unalias nextflow_remove"' >> $HOME/.nextflow_specific_aliases 
grep -qxF 'if [ -e $HOME/.nextflow_specific_aliases ]; then source $HOME/.nextflow_specific_aliases; fi' ~/.bashrc || echo 'if [ -e $HOME/.nextflow_specific_aliases ]; then source $HOME/.nextflow_specific_aliases; fi' >> ~/.bashrc


