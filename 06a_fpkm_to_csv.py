import csv
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
folder_names_file = "folder_names.txt"
input_directory = context_path+"5_cufflinks_result/files" # without last slash
required_extension = ".fpkm_tracking"
output_directory = context_path+"/06_fpkm_csv"

# create output and log directory if not present
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# open file with folder names
folders = open(folder_names_file, "r")

for fname in folders:  
    fname = fname.strip("\r\n")
    input_file = input_directory + "/" + fname + "/genes" + required_extension
    print(input_file)

    # Initialize empty lists to store the extracted data
    gene_ids = []
    fpkms = []

    # Open the CSV file
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        
        # Get the header row to identify column indices
        header = next(csvreader)
        gene_id_index = header.index('gene_id')
        fpkm_index = header.index('FPKM')

        # Iterate through the rows and extract the data
        for row in csvreader:
            gene_ids.append(row[gene_id_index])
            fpkms.append(float(row[fpkm_index]))  # Assuming FPKM values are floats

    # Now, gene_ids and fpkms lists contain the extracted data
    # print("Gene IDs:", gene_ids)
    # print("FPKM values:", fpkms)

    # Write the extracted data to a CSV file
    output_file = output_directory + "/" + fname + "_fpkm" +".csv"
    with open(output_file, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['gene_id', fname])
        for i in range(len(gene_ids)):
            csvwriter.writerow([gene_ids[i], fpkms[i]])
