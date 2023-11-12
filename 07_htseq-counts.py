import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"4_sorted_bam/files" # without last slash
required_extension = ".sam"
output_directory = context_path+"7_htseq_result/files/"
folder_names_file = "folder_names.txt"
logs_directory = context_path+"7_htseq_result/logs/"
ref_annotation = "/scratch/sah2p/datasets/hg38/annotation/GRCh38_latest_genomic.gff"


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

    input_file = input_directory + "/" + folder_name + "_sorted" + required_extension

    # create a file name for the output sam file
    output_file_name = output_directory + folder_name

    log_file_name = logs_directory + folder_name + "_htseq.log"

    # create a command to run cufflinks
    # command = "cufflinks -p 4 -G " + ref_annotation + " " + input_file + " -o " + output_file_name + " > " + log_file_name + "  2>&1 &"
    # print the command to the screen
    command = "htseq-count "+ input_file + " "+ref_annotation+" -i ID -t gene -f bam > " + output_file_name + " > " + log_file_name + "  2>&1 &"
    print(command)
    # run the command
    os.system(command)
    

# cufflinks -p 4 -G refgenome_arabidopsisthaliana/Arabidopsis_thaliana.TAIR10.54.gff3 /data/six2h/RonsNewData/usftp21.novogene.com/sorted_bams/"+tname+" -o /data/six2h/RonsNewData/usftp21.novogene.com/cufflinks_result/"+fname+"