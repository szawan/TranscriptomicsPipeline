import pandas as pd 
import os
TF_file = "/scratch/sah2p/datasets/hg38/homoSapiens_TranscriptionFactors.csv"

df_tf = pd.read_csv(TF_file)
print((df_tf.head()))
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
output_dir = context_path+"TF_identification/"

TF_condition_dir = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/TF/"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



for files in os.listdir(TF_condition_dir):
    new_file_name = files.split(".")[0]+"_TF_found.csv"
    print(new_file_name)
    df_data = pd.read_csv(TF_condition_dir+files, sep='\t')
    df_data['pathway_gene'] = df_data['pathway'].str.split("_",expand=True)[0]
    df_data_tf = df_data.merge(df_tf, left_on='pathway_gene', right_on='Symbol', how='inner')  
    print(df_data_tf)
    df_data_tf.to_csv(output_dir+new_file_name, sep="\t")
      