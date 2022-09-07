# Workflows on OSCAR

This repo tracks the development of a user-friendly CLI tool for installing and configuring Nextflow and Snakemake workflow management tools on Brown's HPC 
cluster, OSCAR, so that users can easily and efficiently deploy reproducible, scalable pipelines for compute intensive tasks. 


## 1. Configuring and running Nextflow 

The nextflow_setup folder contains all the pieces neccessary to install, configure, and run nextflow pipelines on OSCAR. To install and configure, just 
`git clone` this repo into your `HOME` directory on OSCAR. Once this is done, move the `nextflow_setup` folder inside of the repo folder to your `HOME` directory using the command: 

`mv ~/Workflows_on_OSCAR/nextflow_setup ~/nextflow_setup`

Then to install everything, you simply type the following command:

```bash ~/nextflow_setup/install_me/install.sh```

Typing the above command will walk the user through a user-friendly guide to setting up and configuring Nextflow to run on OSCAR according to
the user's computing needs. 

Once the installation and configuration process is done, users can run nextflow pipelines using their own custom workflows, workflows from github repos, 
or workflows from nf-core. The use of singularity containers is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines. 

## 2. Configuring and running Snakemake

Snakemake has not been implemented yet and is forthcoming..
