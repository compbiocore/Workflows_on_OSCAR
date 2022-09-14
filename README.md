# Workflows on OSCAR

This repo tracks the development of a user-friendly CLI tool for installing and configuring Nextflow and Snakemake workflow management tools on Brown's HPC 
cluster, OSCAR, so that users can easily and efficiently deploy reproducible, scalable pipelines for compute intensive tasks. Please read this entire README for important information before attempting to run your pipelines using this tool. 

**Note:** This tool is currently still in beta and being tested. If there are any issues or bugs, please report to: [jordan_lawson@brown.edu](mailto:jordan_lawson@brown.edu) 

## Running the Installer

To set up Nextflow and/or Snakemake for OSCAR, just `git clone` this repo into your `HOME` directory on OSCAR. Once this is done, copy and paste the following command into your terminal: 

```bash ~/workflows_on_OSCAR/install_me/install.sh && source ~/.bashrc```

Running the above command in your terminal will initiate the installation and configuration process, walking the user through a user-friendly guide to setting up and configuring Nextflow and Snakemake to run on OSCAR according to the user's computing needs. 

# Nextflow 

When launched, the CLI tool will prompt the user to type the name of the software they wish to install and set up.  Just enter `Nextflow` and you will be guided through the rest of the installation and configuration process. During this process, the guide will prompt you to answer a few simple questions, after which the software handles the majority of the configuration details for you. 

Once the installation and configuration process is done, users can run nextflow pipelines using their own custom workflows, workflows from GitHub repos, 
or workflows from nf-core. The use of singularity containers is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines. 

### Important Nextflow commands

- `nextflow_start` makes it so you're able to run Nextflow. Specifically, it enters you into a virtual environment module where you can run Nextflow commands. You can use this command in an interactive session on OSCAR (via `interact`) or in your sbatch script by putting it before any nextflow commands you use in the script. 
- `nextflow -h` prints helpful information about what commands and options exist for Nextflow software. **Important Note:** this command will only work after you entered the Nextflow session via `nextflow_start`. 
- `nextflow run` executes a pipeline project. This is used with various options along with your project files. **Important Note:** this command will only work after you entered the Nextflow session via `nextflow_start`. 
- `quit_workflow` exits you out of the Nextflow working session you entered into. If you run this, you will be taken out of your session and unable to run any Nextflow commands until you run `nextflow_start` again. Note that you do not put this command in your sbatch scripts.
- `nextflow_remove` uninstalls (deletes) Nextflow and all its commands (i.e., `nextflow_start`, `nextflow run`, `nextflow_remove`) 

### Nextflow Template Script for OSCAR

Once Nextflow has been successfully installed and configured on OSCAR, you will find a script called `nextflow_template_script.sh` in the `~/nextflow_setup` directory on OSCAR. This is a template script that you can easily edit and use to run Nextflow pipelines on OSCAR using the `sbatch` command. To do so, first copy this file to your project directory (or to any other directory you need it) and rename the file. A general example of how to do this would be: 
```cp ~/nextflow_setup/nextflow_template_script.sh /directory/of/your/choosing/nextflow_run.sh```

The above command creates a new script called `nextflow_run.sh`. Once this is done, you can open and edit the copied file using a text editor of your choice (such as `vim`). When you are done editing, exit and save and then run the file using `sbatch`. This will run your Nextflow pipeline. Inside the `nextflow_template_script.sh` file you will find detailed instructions and notes helping you to setup and run the file. Please read and follow these. 

outside the just open and edit this file using a text editor of your choice (such as `vim`). Once it is edited to your needs, save it under a new name (as a new .sh file 

# Snakemake

When prompted by the CLI tool to type the name of the software you wish to install and set up, just enter `Snakemake` and you will be guided through the rest of the installation and configuration process. During this process, the guide will prompt you to answer a few simple questions, after which the software handles the majority of the configuration details for you.

Once the installation and configuration process is done, users can run snakemake pipelines using their own custom workflows or workflows from elsewhere (such as GitHub) via snakefiles. The use of singularity is automatically enabled and users can flexibly incorporate different containers into their workflow pipelines. 

### Important Snakemake commands

- `snakemake_start` makes it so you're able to run Snakemake. Specifically, it enters you into a virtual environment module where you can run Snakemake commands. You can use the snakemake_start command in an interactive session on OSCAR (via `interact`) or in your sbatch script by putting it before any snakemake commands you use in the script. 
- `snakemake -h` prints helpful information about what commands and options exist for Snakemake software. **Important Note:** this command will only work after you entered the Snakemake session via `snakemake_start`. 
- `snakemake -s` executes a workflow, where the `-s` flag is followed by your snakefile. This is used with various options along with project files. **Important Note:** this command will only work after you entered the Snakemake session via `snakemake_start`. 
- `quit_workflow` exits you out of the Snakemake working session you entered into. If you run this, you will be taken out of your session and unable to run any Snakemake commands until you run `snakemake_start` again. Note that you do not put this command in your sbatch scripts.
- `snakemake_remove` uninstalls (deletes) Snakemake and all its commands (i.e., `snakemake_start`, `snakemake`, `snakemake_remove`) 
