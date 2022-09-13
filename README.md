# Workflows on OSCAR

This repo tracks the development of a user-friendly CLI tool for installing and configuring Nextflow and Snakemake workflow management tools on Brown's HPC 
cluster, OSCAR, so that users can easily and efficiently deploy reproducible, scalable pipelines for compute intensive tasks. 

To set up Nextflow and Snakemake for OSCAR, just `git clone` this repo into your `HOME` directory on OSCAR. Once this is done, you can then type the following command: 

```bash ~/Workflows_on_OSCAR/install_me/install.sh```

Typing the above command will walk the user through a user-friendly guide to setting up and configuring Nextflow and Snakemake to run on OSCAR according to the user's computing needs. 

## 1. Configuring and running Nextflow 

When launched, the CLI tool will prompt the user to type the name of the software they wish to install and set up.  Just enter `Nextflow` and you will be guided through the rest. 

Once the installation and configuration process is done, users can run nextflow pipelines using their own custom workflows, workflows from github repos, 
or workflows from nf-core. The use of singularity containers is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines. 

To run Nextflow, first enter: `nextflow_start` 
\n***Note that you can use the above `nextflow_start` command in an interactive session on OSCAR (via `interact`) or in an sbatch script by putting the `nextflow_start` command before any `nextflow run` commands in the script. 

To uninstall (delete) Nextflow, type: `nextflow_remove`

## 2. Configuring and running Snakemake

Snakemake has not been implemented yet and is forthcoming..
