# import required modules
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
reference_fasta = "/scratch/sah2p/datasets/hg38/GRCh38_latest_genomic.fna"
output_location = "/scratch/sah2p/datasets/hg38/hisat2_index/"
index_basename = "GRCh38_latest_genomic.fna"

# if output location does not exist, create it
if not os.path.exists(output_location):
    os.makedirs(output_location)


command = "hisat2-build " + reference_fasta + " " + output_location + index_basename

print(command)
os.system (command)