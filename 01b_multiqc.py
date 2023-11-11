# import the required modules
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"1_initial_qc/fastqc/"
result_directory = context_path+"1_initial_qc/multiqc/"

# create result directory if not present
if not os.path.exists(result_directory):
    os.makedirs(result_directory)

command = "multiqc " + input_directory + " -o " + result_directory +" &"
print(command)
os.system (command)
