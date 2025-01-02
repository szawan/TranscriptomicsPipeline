import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance_matrix

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"9_DEG/10_DEG_LIST/"
output_directory = context_path+"10_DistanceMatrix/"

# combine all files into one file on gene column, filename as column name and foldchange as values
# read all files in input directory
# create empty list for dataframes
dfs = []
# loop through all files in input directory
# for filename in os.listdir(input_directory):
#     # read file
#     df = pd.read_csv(os.path.join(input_directory, filename), sep="\t", header=0, index_col=0)
    
#     df.drop_duplicates(inplace=True)
#     # get filename without extension
#     filename = os.path.splitext(filename)[0]
#     # rename column
#     df.rename(columns={"foldchange": filename}, inplace=True)
#     # just keep foldchange column
#     df = df[filename]
#     # append dataframe to list
#     dfs.append(df)

# # merge all dataframes in list
# merged_df = pd.concat(dfs, axis=1, sort=False)

# # write merged dataframe to csv
# merged_df.to_csv(os.path.join(output_directory, "All_DEGs.csv"))

# # Distance Matrix

# Load your gene expression data from the CSV file
data = pd.read_csv('/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_DistanceMatrix/All_DEGs.csv', index_col=0)  
print(data.dtypes)

# Calculate the Euclidean distance matrix
distance_matrix_df = pd.DataFrame(distance_matrix(data.T, data), index=data.columns, columns=data.columns)
print(distance_matrix_df)
# # Create a clustering for the Euclidean distance matrix
plt.figure(figsize=(8, 6))
clustermap = sns.clustermap(distance_matrix_df, cmap='viridis', annot=True, fmt='.2f', cbar_pos=(0.93, 0.10, 0.03, 0.3),
                            annot_kws={'size': 8}, method='complete', figsize=(10, 8))  

# # Add labels and title
clustermap.ax_heatmap.set_xlabel("Sample Names")
clustermap.ax_heatmap.set_ylabel("Sample Names")
plt.title("Hierarchical Clustering Heatmap with Euclidean Distance")

# # remove the colorbar
clustermap.cax.set_visible(False)

# # Show the heatmap
plt.show()


# # Save the figure
plt.savefig(output_directory+'heatmap.png', dpi=300)