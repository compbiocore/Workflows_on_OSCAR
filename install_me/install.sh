# Back up .bashrc, just in case 
cp ~/.bashrc ~/.bashrc.bak
# Load needed modules 
module load python/3.9.0
module load java/jdk-11.0.11
# Move setup folders to HOME directory 
mv ~/Workflows_on_OSCAR/install_me/nextflow_setup ~/nextflow_setup
# Run Python script 
python3 $HOME/Workflows_on_OSCAR/workflows.py
