import pandas as pd 
from pathlib import Path
from openpyxl import Workbook
import os

pathway_list = ['GO','KEGG','IMMUNODB','WIKI','REACTOME']
cell_lines = ['A549','H820', 'H3255','H1975']
conditions = ['E07_vs_Veh', 'E07_vs_C36','C36_vs_Veh']
input_dir = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/"
output_dir = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/all/"


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for cell in cell_lines:
    for condition in conditions:
        
        output_file = output_dir+cell+"_"+condition+".xlsx"
        writer=pd.ExcelWriter(output_file)
        li_dfs = []
        for path in pathway_list:
        
            file_name = path+"_"+cell+"_"+condition+"_gsea_results.tsv"
            df_data = pd.read_csv(input_dir+"/"+path+"/"+file_name, sep="\t")
            li_dfs.append(df_data)
        print(len(li_dfs))
        
        _ = [A.to_excel(writer,sheet_name="{0}".format(pathway_list[i])) for i, A in enumerate(li_dfs)]
        writer.close()
        
            
