import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Replace this with your actual gene expression data
# Assume 'df' is your DataFrame with FPKM values, similar to the previous examples
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"9_DEG/10_DEG_LIST/"
output_directory = context_path+"10_DistanceMatrix/"



data = pd.read_csv('/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/06_fpkm_csv/combined_data.csv', index_col=0)  
print(data.dtypes)
# (Optional) Subset the data to a smaller number of samples for better visualization

# Create a pair plot
pair_plot = sns.pairplot(data)
pair_plot.fig.suptitle('Pairwise Plot of FPKM Values for Selected Genes', y=1.02)
# # Save the figure
plt.savefig(output_directory+'pairwise_plot.png',bbox_inches='tight', dpi=300)

