env_var="nextflow_env_${USER}"
cd $HOME
if [ ! -d "$HOME/$env_var" ]; then
    echo "Setting up and installing Nextflow.." 
    # Create virutal environment for user 
    virtualenv $env_var
    source $HOME/$env_var/bin/activate 
    pip3 install -r requirements.txt
    wget -qO- https://get.nextflow.io | bash
    # Make nextflow executable and move to path 
    chmod +x nextflow
    mv nextflow $HOME/$env_var/bin
    deactivate
    echo "Nextflow software installed, initializing configuration..." 
else 
    echo "Nextflow software detected, initializing configuration..."
fi 

