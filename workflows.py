################################################################
# Python Script for Setting Up and Running Workflows on OSCAR 
################################################################

from getpass import getpass, getuser
from subprocess import call, PIPE, Popen
import shlex 
#import fileinput
#import sys
import os  
import re 

# Important Notes: 
#
# Requires python 3 to run 
#
# This python script asks the user for some basic inputs and then, based on these inputs, runs their desired workflow 
# on OSCAR using Nextflow and Snakemake software. 
#
# At the moment, only Nextflow is supported; however, Snakemake will be added soon. 

# Create a function to replace text in config file that gets used in main while loop 
def replacetext(search_text,replace_text, file_changing):
    # Opening the file in read and write mode
    with open(file_changing,'r+') as f:
        # Reading the file data and store it in a file variable
        file = f.read()
        # Replacing the pattern with the string in the file data
        file = re.sub(search_text, replace_text, file)
        # Setting the position to the top of the page to insert data
        f.seek(0)
        # Writing replaced data in the file
        f.write(file)
        # Truncating the file size
        f.truncate()
    # Return string updating user
    return "HPC Default Resources Updated"

# Create function to get Nextflow system defaults
def get_defaults(string_you_want):
    cmd = "grep %s %s" % (string_you_want, next_config)
    args = shlex.split(cmd)
    process = Popen(args, stdout=PIPE, stderr=PIPE)
    result = process.communicate()
    result=result[0]
    result=result[2:len(result)]
    result=str(result).replace("b'memory", "memory")
    result=result.replace("//default mem", "")
    result=result.replace("//default time", "")
    result=result.replace("//default cpus", "")
    result=result.split("\n")[0]
    result=result.replace("\\n", "")
    result=result[0:len(result)-1]
    result=re.sub(' +', ' ', result) 
    return result

# Introductory message 
print("\nWelcome to a program designed to help you easily set up and run workflow management systems on OSCAR!\n")
# get home directory and username information for use later 
homedir = os.path.expanduser("~")
username = getuser()
next_config=homedir + '/nextflow_setup/nextflow.config' 
snake_config=homedir + '/.config/snakemake/oscar/config.yaml'

# Main while loop 
while True: 
    # First ask user if they'd like to use Nextflow or Snakemake - only wrote functionality for Nextflow so far 
    program=input("Please type which software you wish to use: Nextflow or Snakemake? ")
    program=program.lower()
    program=program.strip()
    # If Nextflow, we first make sure we have set up the environment so that user can run Nextflow on OSCAR 
    if program in ("nextflow", "snakemake"):
        # Nextflow software 
        if program=="nextflow":
            # Set up environment, if it doesnt exist 
            try: 
                os.system('cp -r ~/workflows_on_OSCAR/install_me/nextflow_setup ~/nextflow_setup') 
                bash_file='bash ' + homedir + '/nextflow_setup/nextflow_env.sh'
                call(shlex.split(bash_file)) 
            except OSError:
                print("Nextflow software setup error, please contact: jordan_lawson@brown.edu")
                break
            # Ask for inputs for scm file so that Nextflow has github access 
            git_user=input("What is your GitHub user name? ")
            git_token = getpass(prompt="What is your GitHub token (we will keep this secret) - [Hit Enter when Done]? ")
            # Reconfigure scm file 
            scm_file=homedir + '/nextflow_setup/scm'
            newfile=open(scm_file,'w')
            txt= "providers {\n\n  github {\n    user = " + git_user + "\n    password = " + git_token + "\n   }\n\n}"
            newfile.write(txt)
            # Make scm file readable, writeable only by user to protect git token 
            os.system('chmod u+rw,go-rw ' + scm_file)
            # Move to needed location in order for nextflow to work with nf-core 
            os.system('mv ' + scm_file + ' $HOME/.nextflow/scm')
            # Prompt user to specify HPC resources, if desired 
            default_resources=get_defaults("//default")
            print("Currently the Nextflow default for HPC resources is: " + default_resources)
            hpc="empty"
            while True:
                if hpc in ("yes", "no"):
                    break
                else:
                    hpc=input("Do you want to change these default resources for your Nextflow pipeline [Yes or No]? ")
                    hpc=hpc.lower()
                    hpc=hpc.strip()
                    if hpc not in ("yes", "no"):
                        print("Please enter either Yes or No.")
            if hpc=="yes": 
                while True: 
                    try:
                        mem=input("How much memory (in GB) would you like? ")
                        mem=int(''.join(filter(str.isdigit, mem)))
                        if mem < 1 :
                            print("Enter an integer greater than zero.") 
                        else: 
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                while True: 
                    try:
                        time=input("How much time (in hours, with 1 being the minimum) would you like? ")
                        time=int(''.join(filter(str.isdigit, time)))
                        if time < 1: 
                            print("Please enter an integer greater than zero.")
                        else:
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                while True: 
                    try:
                        cpu_request=input("How many cores (i.e., cpus) would you like? ")
                        cpu_request=int(''.join(filter(str.isdigit, cpu_request)))
                        if cpu_request < 1:
                            print("Please enter an integer greater than zero.")
                        else: 
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                default_numbers=[int(s) for s in default_resources.replace(".", " ").split() if s.isdigit()]
                replacements = {"memory = " + str(default_numbers[0]) + ".GB  //default mem": 'memory = ' + str(mem) + '.GB  //default mem', 
                'time = ' + str(default_numbers[1]) + '.h  //default time':'time = ' + str(time) + '.h  //default time', 
                'cpus = ' + str(default_numbers[2]) +  '  //default cpus':'cpus = ' + str(cpu_request) + '  //default cpus'}
                for i in replacements.keys():
                    replacetext(i, replacements[i], next_config)
                # Move nextflow.config file to .nextflow folder so it is a software default 
                os.system('cp ' + next_config + ' $HOME/.nextflow/config')
                # Print output messaging for user 
                print("\nOUTPUT MESSAGE:")
                header="""
                ******************************************************************
                 NEXTFLOW is now set up and configured and ready to run on OSCAR!
                ******************************************************************
                """
                print(header)
                print_1=get_defaults("//default")
                print("\nYour default resources for Nextflow are: " + print_1 + "\n")
                instructions = """
                To further customize your pipeline for efficiency, you can enter the following 
                label '<LabelName>' options right within processes in your Nextflow .nf script:
                1. label 'OSCAR_small_job' (comes with memory = 4 GB, time = 1 hour, cpus = 1)
                2. label 'OSCAR_medium_job' (comes with memory = 8 GB, time = 16 hours, cpus = 2)
                3. label 'OSCAR_large_job' (comes with memory = 16 GB, time = 24 hours, cpus = 2)
                """
                print(instructions)
                print("\nREADME:\n") 
                print("\nPlease see https://github.com/compbiocore/workflows_on_OSCAR for further details on how to add the above label options to your workflow.\n")
                print("Note the setup is designed such that pipelines downloaded from nf-core with their own resource specs within the .nf script will override your defaults.\n")
                next_dir=homedir + "/nextflow_env_" + username + "/bin/activate"
                print("To run Nextflow, you must first type and run the nextflow_start command.\n")
                print("To further learn how to easily run your Nextflow pipelines on OSCAR, use the Nextflow template shell script located in your ~/nextflow_setup directory.\n") 
            if hpc=="no":
                # Move nextflow.config file to .nextflow folder so it is a software default 
                os.system('cp ' + next_config + ' $HOME/.nextflow/config')
                # Print output messaging for user 
                print("Keeping defaults!")
                print("\nOUTPUT MESSAGE:")
                header="""
                ******************************************************************
                 NEXTFLOW is now set up and configured and ready to run on OSCAR!
                ******************************************************************
                """
                print(header)
                print_2=get_defaults("//default")
                print("\nYour default resources for Nextflow are: " + print_2 + "\n")
                instructions = """
                To further customize your pipeline for efficiency, you can enter the following 
                label '<LabelName>' options right within processes in your Nextflow .nf script:
                1. label 'OSCAR_small_job' (comes with memory = 4 GB, time = 1 hour, cpus = 1)
                2. label 'OSCAR_medium_job' (comes with memory = 8 GB, time = 16 hours, cpus = 2)
                3. label 'OSCAR_large_job' (comes with memory = 16 GB, time = 24 hours, cpus = 2)
                """
                print(instructions)
                print("\nREADME:\n")
                print("\nPlease see https://github.com/compbiocore/workflows_on_OSCAR for further details on how to add the above label options to your workflow.\n")
                print("Note the setup is designed such that pipelines downloaded from nf-core with their own resource specs within the .nf script will override your defaults.\n")
                next_dir=homedir + "/nextflow_env_" + username + "/bin/activate"
                print("To run Nextflow, you must first type and run the nextflow_start command.\n")
                print("To further learn how to easily run your Nextflow pipelines on OSCAR, use the Nextflow template shell script located in your ~/nextflow_setup directory.\n") 
            break
        # Snakemake software 
        if program=="snakemake":
            # Set up environment, if it doesnt exist 
            try: 
                os.system('cp -r ~/workflows_on_OSCAR/install_me/snakemake_setup ~/snakemake_setup')
                bash_file='bash ' + homedir + '/snakemake_setup/snakemake_env.sh'
                call(shlex.split(bash_file)) 
            except OSError:
                print("Snakemake software setup error, please contact: jordan_lawson@brown.edu")
                break
            # Ask for inputs for configuring setup 
            user_email=input("\nWhat is your Brown email address? ")
            new_mail="mail-user: " + user_email
            os.system("sed -i.bak 's/mail-user:.*/" + new_mail + "/g' " + snake_config)
            # Prompt user to specify HPC resources, if desired 
            default_resources=os.popen('grep "^default-resources:" ' + snake_config).read()
            default_resources=default_resources.split('[', 1)[1].split(']')[0]
            print("\nCurrently the Snakeflow default for HPC resources is: " + default_resources)
            hpc="empty"
            while True:
                if hpc in ("yes", "no"):
                    break
                else:
                    hpc=input("Do you want to change these default resources for your Snakemake pipeline [Yes or No]? ")
                    hpc=hpc.lower()
                    hpc=hpc.strip()
                    if hpc not in ("yes", "no"):
                        print("Please enter either Yes or No.")
            if hpc=="yes": 
                while True: 
                    try:
                        mem=input("How much memory (in GB) would you like? ")
                        mem=int(''.join(filter(str.isdigit, mem)))
                        mem=int(mem)*1000
                        if mem < 1000 or mem >= 200000:
                            print("Enter an integer greater than zero and less than 200.") 
                        else: 
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                while True: 
                    try:
                        time=input("How much time (in minutes, with 5 being the minimum) would you like? ")
                        time=int(''.join(filter(str.isdigit, time)))
                        if time < 5: 
                            print("Please enter an integer equal to or greater than 5.")
                        else:
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                while True: 
                    try:
                        cpu_request=input("How many cores (i.e., cpus) would you like? ")
                        cpu_request=int(''.join(filter(str.isdigit, cpu_request)))
                        if cpu_request < 1 or cpu_request >= 32:
                            print("Please enter an integer greater than zero and less than 32.")
                        else: 
                            break 
                    except ValueError: 
                        print("Invalid entry, please give a number.")
                default_numbers=default_resources.replace("=", " ")
                default_numbers=default_numbers.replace(",", " ")
                default_numbers=[int(s) for s in default_numbers.split() if s.isdigit()]
                replacements = {"cpus=" + str(default_numbers[0]) + ",": 'cpus=' + str(cpu_request) + ',', 
                'mem_mb=' + str(default_numbers[1]) + ',':'mem_mb=' + str(mem) + ',', 
                'time_min=' + str(default_numbers[2]) +  ']':'time_min=' + str(time) + ']'}
                for i in replacements.keys():
                    replacetext(i, replacements[i], snake_config)
                # Print output messaging for user 
                print("\nOUTPUT MESSAGE:")
                header="""
                ***********************************************************************
                 ~~Snakemake~~ is now set up and configured and ready to run on OSCAR!
                ***********************************************************************
                """
                print(header)
                print_1=os.popen('grep "^default-resources:" ' + snake_config).read()
                print_1=print_1.split('[', 1)[1].split(']')[0]
                print("\nYour default resources for Snakemake are: " + print_1 + "\n")
                print("\nREADME:\n") 
                print("\nPlease see https://github.com/compbiocore/workflows_on_OSCAR for further details on how to configure and run your Snakemake workflows.\n")
                print("Note that the setup is designed such that snakefiles can specify tasks with their own resource specs that override the defaults.\n")
                print("To run Snakemake, you must first type and run the snakemake_start command.\n")
                print("To further learn now to easily run your Snakemake pipelines on OSCAR, use the Snakemake template shell script located in your ~/snakemake_setup directory.\n") 
            if hpc=="no":
                # Print output messaging for user 
                print("Keeping defaults!")
                print("\nOUTPUT MESSAGE:")
                header="""
                ***********************************************************************
                 ~~Snakemake~~ is now set up and configured and ready to run on OSCAR!
                ***********************************************************************
                """
                print(header)
                print_1=os.popen('grep "^default-resources:" ' + snake_config).read()
                print_1=print_1.split('[', 1)[1].split(']')[0]
                print("\nYour default resources for Snakemake are: " + print_1 + "\n")
                print("\nREADME:\n")
                print("\nPlease see https://github.com/compbiocore/workflows_on_OSCAR for further details on how to configure and run your Snakemake workflows.\n")
                print("Note that the setup is designed such that snakefiles can specify tasks with their own resource specs that override the defaults.\n")
                print("To run Snakemake, you must first type and run the snakemake_start command.\n")
                print("To further learn how to easily run your Snakemake pipelines on OSCAR, use the Snakemake template shell script located in your ~/snakemake_setup directory.\n") 
            break
    else: 
        print("Please re-enter a valid option.")

