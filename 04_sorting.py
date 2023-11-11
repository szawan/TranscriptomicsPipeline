import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"3_aligned_sequences/files" # without last slash
required_extension = ".sam"
output_directory = context_path+"4_sorted_bam/files/"
logs_directory = context_path+"4_sorted_bam/logs/"
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

    input_file = input_directory + "/" + folder_name + "_aligned" + required_extension
    log_file_name = logs_directory + folder_name + "_sort" + ".log"
    
    # create a file name for the output sam file
    output_file_name = output_directory + folder_name + "_sorted" + required_extension
    
    # create a file name for the log file
    log_file_name = logs_directory + folder_name + "_sort.log"
    
    # create a command to run samtools sort
    command = "samtools sort -@ 4 -o " + output_file_name + " " + input_file + " > " + log_file_name + "  2>&1 &"
    
    # print the command to the screen
    print(command)
    # run the command
    os.system(command)
    

# samtools sort -@ 4 -o /data/six2h/RonsNewData/usftp21.novogene.com/sorted_bams/"+fname+"_sorted.bam /data/six2h/RonsNewData/usftp21.novogene.com/sam_output_edgeR/"+tname+") >& /data/six2h/RonsNewData/usftp21.novogene.com/sorted_bams/log_sort_"+fname+" &

        