import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy

# Replace 'gene_exp.diff' with the actual path to your cuffdiff output file
cuffdiff_result = pd.read_csv('/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/8_cuffdiff_result/Cuffdiff/A549_E07_vs_A549_C36/gene_exp.diff', sep='\t')
cuffdiff_result.replace(",?,",",,", inplace=True)
# Filter differentially expressed genes (adjust the condition based on your needs)
differentially_expressed_genes = cuffdiff_result[cuffdiff_result['significant'] == 'yes']

# Extract relevant columns for clustering
gene_sample_matrix = differentially_expressed_genes[['gene_id', 'sample_1', 'sample_2', 'log2(fold_change)']]

# Pivot the data for better visualization
gene_sample_matrix_pivoted = gene_sample_matrix.pivot(index='gene_id', columns='sample_1', values='log2(fold_change)').fillna(0)
print(gene_sample_matrix_pivoted)
# # Perform hierarchical clustering
gene_cluster = hierarchy.linkage(gene_sample_matrix_pivoted, method='average', metric='euclidean')

# # Get the order of genes after clustering
gene_order = hierarchy.leaves_list(gene_cluster)

# # Reorder the rows of the matrix based on clustering
gene_sample_matrix_pivoted = gene_sample_matrix_pivoted.iloc[gene_order]

# # Cluster samples based on the correlation between gene expression profiles
sample_cluster = hierarchy.linkage(gene_sample_matrix_pivoted.transpose(), method='average', metric='correlation')

# # Get the order of samples after clustering
sample_order = hierarchy.leaves_list(sample_cluster)

# # Reorder the columns of the matrix based on clustering
gene_sample_matrix_pivoted = gene_sample_matrix_pivoted.iloc[:, sample_order]

# # Set up the size of the heatmap
plt.figure(figsize=(10, 8))

# # Create the heatmap
sns.heatmap(gene_sample_matrix_pivoted, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=.5)

# # Set labels and title
plt.xlabel('Samples')
plt.ylabel('Genes')
# plt.title('Hierarchical Clustering Heatmap of Differentially Expressed Genes')

# # Show the plot
plt.show()
