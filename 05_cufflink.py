import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"4_sorted_bam/files" # without last slash
required_extension = ".sam"
output_directory = context_path+"5_cufflinks_result/files/"
folder_names_file = "folder_names.txt"
ref_annotation = "/scratch/sah2p/datasets/hg38/annotation/Homo_sapiens.GRCh38.110.gff3"


# create output and log directory if not present
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# open file with folder names
folders = open(folder_names_file, "r")

# iterate over each folder name and run fastqc
for folder_name in folders:
    folder_name = folder_name.strip("\n")

    input_file = input_directory + "/" + folder_name + "_sorted" + required_extension
    
    # create a file name for the output sam file
    output_file_name = output_directory + folder_name

    # create a command to run cufflinks
    command = "cufflinks -p 4 -G " + ref_annotation + " " + input_file + " -o " + output_file_name + " &"
    # print the command to the screen
    print(command)
    # run the command
    os.system(command)
    

# cufflinks -p 4 -G refgenome_arabidopsisthaliana/Arabidopsis_thaliana.TAIR10.54.gff3 /data/six2h/RonsNewData/usftp21.novogene.com/sorted_bams/"+tname+" -o /data/six2h/RonsNewData/usftp21.novogene.com/cufflinks_result/"+fname+"