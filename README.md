# Workflows on OSCAR

This repo tracks the development of a user-friendly CLI tool for installing and configuring Nextflow and Snakemake workflow management tools on Brown's HPC 
cluster, OSCAR, so that users can easily and efficiently deploy reproducible, scalable pipelines for compute intensive tasks. 

To set up Nextflow and Snakemake for OSCAR, just `git clone` this repo into your `HOME` directory on OSCAR. Once this is done, copy and paste the following command into your terminal: 

```bash ~/workflows_on_OSCAR/install_me/install.sh && source ~/.bashrc```

Typing the above command will walk the user through a user-friendly guide to setting up and configuring Nextflow and Snakemake to run on OSCAR according to the user's computing needs. 

# Nextflow 

When launched, the CLI tool will prompt the user to type the name of the software they wish to install and set up.  Just enter `Nextflow` and you will be guided through the rest of the installation and configuration process. During this process, the guide will prompt you to answer a few simple questions, after which the software handles the majority of the configuration details for you. 

Once the installation and configuration process is done, users can run nextflow pipelines using their own custom workflows, workflows from GitHub repos, 
or workflows from nf-core. The use of singularity containers is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines. 

### Important Nextflow commands

a.) To be able to run Nextflow commands, first type: `nextflow_start` 

This command enters you into an environment where you can run Nextflow. To exit out of this workflow session, just type `quit_workflow`. 

**NOTE:** you can use the `nextflow_start` command in an interactive session on OSCAR (via `interact`) or in an sbatch script by putting the `nextflow_start` command before any `nextflow run` commands in the script. 

b.) To uninstall (delete) Nextflow and all its commands, type: `nextflow_remove`

# Snakemake

When prompted by the CLI tool to type the name of the software you wish to install and set up, just enter `Snakemake` and you will be guided through the rest of the installation and configuration process. During this process, the guide will prompt you to answer a few simple questions, after which the software handles the majority of the configuration details for you.

Once the installation and configuration process is done, users can run snakemake pipelines using their own custom workflows or workflows from elsewhere (such as GitHub) via snakefiles. The use of singularity is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines via .sif files. 

### Important Snakemake commands

a.) To be able to run Snakemake commands, first type: `snakemake_start` 

This command enters you into an environment where you can run Snakemake. Like with Nextflow, to exit out of this workflow session, just type `quit_workflow`. 

**NOTE:** you can use the `snakemake_start` command in an interactive session on OSCAR (via `interact`) or in an sbatch script by putting the `snakemake_start` command before any `snakemake` commands in the script. 

b.) To uninstall (delete) Snakemake and all its commands, type: `snakemake_remove`
