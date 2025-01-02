import pandas as pd 
from pathlib import Path
from openpyxl import Workbook
import os
context_path = '/scratch/sah2p/'
input_dir = context_path+"datasets/2023_11_04_BurkeLab/output/TF_identification/Genie3/"
output_dir = context_path+"datasets/2023_11_04_BurkeLab/output/TF_identification/Genie3/combined/"
output_file = output_dir + "Genie3_weighted.xlsx"

writer=pd.ExcelWriter(output_file)
li_dfs = []
for file in os.listdir(input_dir):
    if os.path.isfile(input_dir+file):
        print(file)
        df_data = pd.read_csv(input_dir+file)
        df_data = df_data[['regulatoryGene','targetGene','weight']]
        file_name = file.split(".")[0]
        df_data.to_excel(writer, sheet_name=file_name, index=False)

writer.close()

        
        
            
