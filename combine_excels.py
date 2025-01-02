import pandas as pd
import os

# Set the directory where your Excel files are located
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_dir = context_path +"IMpress/results/"
output_dir = context_path + "IMpress/"

# Get a list of all Excel files in the directory
excel_files = [file for file in os.listdir(input_dir) if file.endswith(".xlsx")]

# Initialize an empty list to store dataframes
dfs_list = []

# Loop through each Excel file and read it into a dataframe
for file in excel_files:
    print(file)
    df = pd.read_excel(os.path.join(input_dir, file))
    if file == "H820_E07_vs_C36.xlsx":
       continue

    dfs_list.append(df)

# Combine all dataframes into one using pandas' concat
combined_df = pd.concat(dfs_list, ignore_index=True)

# Display the combined dataframe
print(combined_df)
combined_df.to_excel(output_dir+"Impress_enrichment_map.xlsx")
