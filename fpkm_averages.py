import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
csv_file_path = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/06_fpkm_csv/combined_data.csv'
output_file = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/06_fpkm_csv/combined_data_avg.csv'
pattern = 'A549_C36'
cellines = ['A549','H820','H1975', 'H3255']
conditions = ['Veh','C36','E07']

# Read CSV into a DataFrame
df = pd.read_csv(csv_file_path)

for cell in cellines:
    for condition in conditions:
        pattern = cell+"_"+condition
        print(pattern)
    # Select columns containing "A549_C36"
        selected_columns = df.filter(like=pattern)
    # Create a new column 'A549_C36' with the average of selected columns
        df[pattern] = selected_columns.mean(axis=1)

# Display the resulting DataFrame
print(df)
df.to_csv(output_file)