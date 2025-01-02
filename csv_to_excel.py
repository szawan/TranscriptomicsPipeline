import pandas as pd
import os

# Specify the folder containing CSV files
csv_folder = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new'

# Specify the output folder for Excel files
xlsx_folder = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new/cuffdiff_excel'

# Ensure the output folder exists, create it if necessary
os.makedirs(xlsx_folder, exist_ok=True)

# Loop through each file in the CSV folder
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith('.csv'):
        # Read CSV file into a DataFrame
        df = pd.read_csv(os.path.join(csv_folder, csv_file), sep='\t')

        # Create the output Excel file name by replacing '.csv' with '.xlsx'
        xlsx_file = os.path.join(xlsx_folder, csv_file.replace('.csv', '.xlsx'))

        # Convert and save the DataFrame to Excel
        df.to_excel(xlsx_file, index=False)

        # print(f"Converted {csv_file} to {xlsx_file}")
