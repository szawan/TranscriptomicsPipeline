# import required modules
import os

# SET PATHS
input_directory = "../output/2_trimmed_output/trimmed_files" # without last slash
required_extension = ".fq.gz"
output_directory = "../output/3_aligned_sequences/files/"
logs_directory = "../output/3_aligned_sequences/logs/"
reference_genome = "../ref_genome/hisat2_index/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa"
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

    first_file = input_directory + "/" + folder_name + "_1_val_1" + required_extension
    second_file = input_directory + "/" + folder_name + "_2_val_2" + required_extension
    log_file_name = logs_directory + folder_name + ".log"
    
    # create a file name for the output sam file
    output_file_name = output_directory + folder_name + "_aligned" + ".sam"
    # create a file name for the log file
    log_file_name = logs_directory + folder_name + "_hisat.log"
    # create a command to run hisat2
    command = "hisat2 -p 4 --dta-cufflinks -x " + reference_genome + " -1 " + first_file + " -2 " + second_file + " -S " + output_file_name + " > " + log_file_name + "  2>&1 &"
    # print the command to the screen
    print(command)
    # run the command
    os.system(command)


# hisat2 -p 4 --dta-cufflinks -x refgenome_arabidopsisthaliana/Arabidopsis_thaliana.TAIR10.dna.toplevel
# -1 /data/six2h/RonsNewData/usftp21.novogene.com/Trimmed_data_09_08_2022/"+fname+"_1_val_1.fq.gz -2 /data/six2h/RonsNewData/usftp21.novogene.com/Trimmed_data_09_08_2022/"+fname+"_2_val_2.fq.gz -S /data/six2h/RonsNewData/usftp21.novogene.com/sam_output_edgeR/"+fname+".sam) 
# >& /data/six2h/RonsNewData/usftp21.novogene.com/sam_output_edgeR/"+fname+"_hisat_log.txt &

# hisat2 -p 4 --dta-cufflinks -x /scratch/ag5cg/tomato/ref_genome/hisat2_index/Slycopersicum_796_ITAG5.0 -1 /scratch/ag5cg/tomato/output/2_trimmed_output/trimmed_files/M36_1.fq.gz -2 /scratch/ag5cg/tomato/output/2_trimmed_output/trimmed_files/M36_2.fq.gz -S /scratch/ag5cg/tomato/output/3_aligned_sequences/files/M36.sam > /scratch/ag5cg/tomato/output/3_aligned_sequences/logs/M36_hisat_log.txt &

        
        