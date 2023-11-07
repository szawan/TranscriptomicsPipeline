import os
import pandas as pd

# SET PATHS
input_directory = "../output/8_cuffdiff/extracted_results_with_annotation/"
output_directory = "../output/8_cuffdiff/extracted_results_with_annotation/"

# CREATE OUTPUT DIRECTORY IF NOT EXISTS
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Create an empty list to store DataFrames from each CSV file
dataframes = []

# Loop through all CSV files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Set the first index to the file name (without extension)
        df['FirstIndex'] = os.path.splitext(filename)[0]
        # Set the second index to the 'gene' column
        df.set_index(['FirstIndex', 'gene'], inplace=True)
        dataframes.append(df)

# Merge the DataFrames on the 'gene' column
merged_df = pd.concat(dataframes)

# Reset the index to make the 'gene' column a regular column
merged_df.reset_index(level=1, inplace=True)
merged_df.reset_index(level=0, inplace=True)

# Export the merged DataFrame to an Excel file
merged_df.to_excel(os.path.join(output_directory, "merged_data.xlsx"), index=False)
