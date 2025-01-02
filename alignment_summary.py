import os
import pandas as pd

# Path to the logs folder
logs_folder_path = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/3_aligned_sequences/logs'
li_df = []
# Function to extract the last line from a file
def get_last_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if lines:
            return lines[-1].strip()
        else:
            return None

# Iterate over files in the logs folder
for filename in os.listdir(logs_folder_path):
    file_path = os.path.join(logs_folder_path, filename)

    # Check if the path is a file (not a subdirectory)
    if os.path.isfile(file_path):
        last_line = get_last_line(file_path)
        li_last_line = last_line.split(" ")[0]
        file = filename.replace("_hisat.log","")
        data_to_append = {'filename': file, 'alignment_rate':li_last_line}
        li_df.append(data_to_append)

df = pd.DataFrame(li_df)

df.to_csv(logs_folder_path+"/alignment_summary.csv")


import plotly.express as px
fig = px.line(df, x='filename', y='alignment_rate', markers=True)
fig.show()
# Save the Plotly plot as an HTML file
fig.write_html(logs_folder_path+'/al.html')