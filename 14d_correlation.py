import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial import distance_matrix

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"9_DEG/10_DEG_LIST/"
output_directory = context_path+"10_DistanceMatrix/"



data = pd.read_csv('/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/06_fpkm_csv/fpkm_all_samples_avg.csv', index_col=0)  
print(data.dtypes)

# Calculate the Euclidean distance matrix
corr_matrix = data.corr('pearson')# # Create a clustering for the Euclidean distance matrix
plt.figure(figsize=(8, 6))
clustermap = sns.clustermap(corr_matrix, cmap='viridis', annot=True, fmt='.2f', cbar_pos=(0.93, 0.10, 0.03, 0.3),
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
plt.savefig(output_directory+'heatmap_correlation.png',bbox_inches='tight', dpi=300)