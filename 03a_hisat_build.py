# import required modules
import os

# SET PATHS
reference_fasta = "../ref_genome/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa"
output_location = "../ref_genome/hisat2_index/"
index_basename = "Arabidopsis_thaliana.TAIR10.dna.toplevel.fa"

# if output location does not exist, create it
if not os.path.exists(output_location):
    os.makedirs(output_location)


command = "hisat2-build " + reference_fasta + " " + output_location + index_basename

print(command)
os.system (command)