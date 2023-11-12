import csv
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output"
folder_names_file = "folder_names.txt"
input_directory = context_path+"/06_fpkm_csv" # without last slash
required_extension = ".csv"
output_directory = input_directory

# open file with folder names
folders = open(folder_names_file, "r")

# get all the lines in list from folders
list_of_files = []
for file_name in folders:
    file_name = file_name.strip("\r\n")
    list_of_files.append(file_name)
print(list_of_files)


# Initialize a dictionary to store the combined data
combined_data = {}

for fname in list_of_files:  
    fname = fname.strip("\r\n")
    input_file = input_directory + "/" + fname + "_fpkm" + required_extension
    print(input_file)
    csv_reader = csv.DictReader(open(input_file, 'r'), delimiter=',')

    
    # Iterate through the rows in the current CSV file
    for row in csv_reader:
        # print(row)
        gene_id = row['gene_id']
        fpkm_value = row[fname]
        
        # If the gene_id is not in the combined_data dictionary, initialize it with an empty dictionary
        if gene_id not in combined_data:
            combined_data[gene_id] = {}
        
        # Store the fpkm_value in the combined_data dictionary under the file_name key
        combined_data[gene_id][fname] = fpkm_value

# Create a list of unique gene IDs
unique_gene_ids = list(combined_data.keys())

# Create the header row for the combined CSV file
header = ['gene_id'] + list_of_files

# Write the combined data to a new CSV file
output_file = output_directory + "/combined_data.csv"
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(header)
    
    # Write the data rows
    for gene_id in unique_gene_ids:
        row_data = [gene_id] + [combined_data[gene_id].get(file_name, '') for file_name in list_of_files]
        csv_writer.writerow(row_data)

print("Combined data saved to: ", output_file)