# import required modules
import os

# SET PATHS
input_directory = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/processed/"
required_extension = ".fastq.gz"
result_directory = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/1_initial_qc/fastqc/"
folder_names_file = "folder_names.txt"

# create result directory if not present
if not os.path.exists(result_directory):
    os.makedirs(result_directory)

# open file with folder names
folders = open(folder_names_file, "r")

# iterate over each folder name and run fastqc
for folder_name in folders:
    folder_name = folder_name.strip("\n")
    command1 = "fastqc -o " + result_directory + " " + input_directory + folder_name + "/" + folder_name + "_1" + required_extension + " &"
    command2 = "fastqc -o " + result_directory + " " + input_directory + folder_name + "/" + folder_name + "_2" + required_extension + " &"
    
    print(command1)
    os.system (command1)

    print(command2)
    os.system (command2)