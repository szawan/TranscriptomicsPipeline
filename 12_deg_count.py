import os
import pandas as pd

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"8_cuffdiff_result/Cuffdiff/"
output_directory = context_path+"9_DEG/"

subfolders = []

for item in os.listdir(input_directory):
    item_path = os.path.join(input_directory, item)
    if os.path.isdir(item_path):
        subfolders.append(item)

columns = ['file_name', 'significant_genes', 'up_regulated', 'down_regulated']
df_results = pd.DataFrame(columns=columns)

for fname  in subfolders:  
    fname = fname.strip("\r\n")
    if(fname != 'logs_cuffdiff'):
        df = pd.read_csv(input_directory+fname+"/gene_exp.diff",sep='\t')
        cnt =0
        upregulated = 0
        downregulated = 0
        for index, row in df.iterrows():
            if(row['q_value'] <= 0.05):
                cnt = cnt+1
                if(row['log2(fold_change)'] > 0):
                    upregulated = upregulated+1
                else:
                    downregulated = downregulated+1
        print(fname)
        print(cnt)
        print("\n")
        df_results = df_results.append({'file_name': fname, 'significant_genes': cnt, 'up_regulated': upregulated, 'down_regulated': downregulated}, ignore_index=True)

df_results.to_csv(output_directory+'02_DEGenesCount.csv', sep='\t', encoding='utf-8', index=False)