# write a python code to perform PCA on the data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os
import plotly.express as px

# create folder for output
if not os.path.exists('../output/7_pca'):
    os.makedirs('../output/7_pca')

# read in the data
df = pd.read_csv('../output/6_fpkm_csv/combined_data_transposed.csv')
print(df.head())

# extract the experiment names
experiments = df['gene_id']
print(experiments.head())

# extract the fpkm values
fpkm = df.iloc[:,1:]
print(fpkm.head())

# standardize the data
fpkm_std = StandardScaler().fit_transform(fpkm)
print(fpkm_std)

# perform PCA
pca = PCA(n_components=2)
pca.fit(fpkm_std)
pca_data = pca.transform(fpkm_std)
print(pca_data)

# create a dataframe with the pca data
pca_df = pd.DataFrame(data=pca_data, columns=['PC1', 'PC2'])
print(pca_df.head())

# add the experiment names to the pca dataframe
pca_df = pd.concat([pca_df, experiments], axis=1)
print(pca_df.head())

# plot the pca data
fig, ax = plt.subplots()
ax.scatter(pca_df['PC1'], pca_df['PC2'])
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title('PCA')
plt.savefig('../output/7_pca/pca.png')
plt.close()

# plot the pca data with the experiment names
fig, ax = plt.subplots()
ax.scatter(pca_df['PC1'], pca_df['PC2'])
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title('PCA')
#######################
# reduce the text size
plt.rcParams.update({'font.size': 10})
# reduce the dot size
ax.scatter(pca_df['PC1'], pca_df['PC2'], s=5)
# increate the plot size
fig.set_size_inches(10, 10)
#######################
# define the colors for the experiments
colors = {
    'CO1': 'red',
    'CO2': 'red',
    'CO3': 'red',
    'CT1': 'blue',
    'CT2': 'blue',
    'CT3': 'blue',
    'HS1': 'green',
    'HS2': 'green',
    'HS3': 'green',
    'HSCO1': 'orange',
    'HSCO2': 'orange',
    'HSCO3': 'orange',
    'WD1': 'purple',
    'WD2': 'purple',
    'WD3': 'purple',
    'WDCO1': 'yellow',
    'WDCO2': 'yellow',
    'WDCO3': 'yellow',
    'WDHS1': 'black',
    'WDHS2': 'black',
    'WDHS3': 'black',
    'WDHSCO1': 'pink',
    'WDHSCO2': 'pink',
    'WDHSCO3': 'pink'
}
# create a list of colors for each experiment
experiment_colors = [colors[x] for x in pca_df['gene_id']]
# plot with colors
ax.scatter(pca_df['PC1'], pca_df['PC2'], c=experiment_colors)
# add the experiment names
for i, txt in enumerate(pca_df['gene_id']):
    ax.annotate(txt, (pca_df['PC1'][i], pca_df['PC2'][i]))
# save the figure
plt.savefig('../output/7_pca/pca_experiment_names_colors.png')
plt.close()



# Plotly version

# Create a DataFrame for Plotly
pca_df['experiment_names'] = pca_df['gene_id'].apply(lambda x: x[:-1])  # Remove the last character to show group names

# Define the color mapping
colors = {
    'CO': 'red',
    'CT': 'blue',
    'HS': 'green',
    'HSCO': 'orange',
    'WD': 'purple',
    'WDCO': 'yellow',
    'WDHS': 'black',
    'WDHSCO': 'pink'
}

pca_df['color'] = pca_df['gene_id'].apply(lambda x: colors.get(x[:-1], 'black'))

# Create the Plotly scatter plot
fig = px.scatter(
    pca_df, x='PC1', y='PC2', color='experiment_names',
    hover_name='experiment_names', title='PCA Plot',
    labels={'experiment_names': 'Experiment Group'}
)

# Customize the marker size and legend font size
fig.update_traces(marker=dict(size=10))  # Increase marker size
fig.update_layout(legend=dict(font=dict(size=14)))  # Increase legend font size

# Save the Plotly plot as an HTML file
fig.write_html('../output/7_pca/pca_plotly.html')

fig.show()