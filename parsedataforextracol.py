import pandas as pd
import os

dir_path  = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new/cuffdiff_excel"
output_dir = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new/cuffdiff_excel/out"

for file in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path,file)):
        df = pd.read_excel(os.path.join(dir_path,file))
        df = df[['gene', 'p_value','q_value','significant','foldchange']]
        df = df[~(df['gene']== '-')]
        df.to_excel(os.path.join(output_dir,file))
        print(df.head(5))
    # print(file)