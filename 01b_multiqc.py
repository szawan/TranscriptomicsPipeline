# import the required modules
import os

# SET PATHS
input_directory = "../output/1_initial_qc/fastqc/"
result_directory = "../output/1_initial_qc/multiqc/"

# create result directory if not present
if not os.path.exists(result_directory):
    os.makedirs(result_directory)

command = "multiqc " + input_directory + " -o " + result_directory
print(command)
os.system (command)
