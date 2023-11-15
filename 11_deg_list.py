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

re = pd.DataFrame() 

for fname  in subfolders:
    #print fname
    fname = fname.strip("\r\n")
    if(fname != 'logs_cuffdiff'):
        df = pd.read_csv(input_directory+fname+"/gene_exp.diff",sep='\t')
        cnt =0
        tt= df[df['q_value']<=0.05]['gene_id']
        print(type(tt))
        print(type(df))
        tt = tt.rename(fname)
    # tt.rename(columns = {'gene_id':fname})
    # tt.rename
    # print(len(tt))
        re = pd.concat([re, tt], axis=1) 
    # re[fname] = tt
    # for index, row in df.iterrows():
    #     if(row['q_value'] <= 0.05):
            
# x = df[df['q_value']<=0.05].count()
# x = df[df['q_value']<=0.05 and df['']].count()
re.to_csv(output_directory+'01_DEGenesList.csv', sep='\t', encoding='utf-8', index=False)
print(re)

