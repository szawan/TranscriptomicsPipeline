import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance_matrix

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"9_DEG_new_v2"
output_directory = context_path+"10_DistanceMatrix/"

dfs = []
# loop through all files in input directory
for filename in os.listdir(input_directory):
    if filename == 'DEG_Summary':
        continue
    # read file
    df = pd.read_csv(os.path.join(input_directory, filename), sep="\t", header=0, index_col=0)
    
    df.drop_duplicates(inplace=True)
    df = df[df['q_value'] < 0.05]
    # get filename without extension
    filename = os.path.splitext(filename)[0]
    # rename column
    df.rename(columns={"foldchange": filename}, inplace=True)
    # just keep foldchange column
    df = df[filename]
    # append dataframe to list
    dfs.append(df)

# merge all dataframes in list
merged_df = pd.concat(dfs, axis=1, sort=False)

# write merged dataframe to csv
merged_df.to_csv(os.path.join(output_directory, "All_DEGs_v2.csv"))
