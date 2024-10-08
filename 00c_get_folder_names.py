# import required modules
import os

# SET PATHS
input_directory = "/data/sah2p/datasets/2023_11_04_infostat_8005/AlzhiemerData-Bulk/fastq"

# Get all the folder names
folder_names = []
for root, dirs, files in os.walk(input_directory, topdown=False):
    for name in dirs:
        folder_names.append(name)
        folder_names.sort()

# save folder names in a file
with open("folder_names.txt", "w") as f:
    for folder_name in folder_names:
        f.write(folder_name+"\n")
    print("Done")