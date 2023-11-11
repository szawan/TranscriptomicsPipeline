# import required modules
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"processed/"
required_extension = ".fastq.gz"
output_directory = context_path+"2_trimmed_output/trimmed_files/"
logs_directory = context_path+"2_trimmed_output/trim_logs/"
folder_names_file = "folder_names.txt"

# create output and log directory if not present
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

if not os.path.exists(logs_directory):
    os.makedirs(logs_directory)

# open file with folder names
folders = open(folder_names_file, "r")

# iterate over each folder name and run fastqc
for folder_name in folders:
    folder_name = folder_name.strip("\n")

    first_file = input_directory + folder_name + "/" + folder_name + "_1" + required_extension
    second_file = input_directory + folder_name + "/" + folder_name + "_2" + required_extension
    log_file_name = logs_directory + folder_name + ".log"
    
    # run trim_galore
    command = "trim_galore --output_dir " + output_directory + " --paired " + first_file + " " + second_file + " > " + log_file_name + "  2>&1 &"
    print(command)
    os.system(command)