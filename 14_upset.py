import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# SET PATHS
input_directory = "../output/8_cuffdiff/"
output_directory = "../output/8_cuffdiff/"

# Load your gene matrix data into a Pandas DataFrame
gene_matrix = pd.read_csv(input_directory + "01_DEGenesList.csv", sep="\t", index_col=0)

# Remove non-numeric values, such as gene identifiers, from the DataFrame
gene_matrix = gene_matrix.applymap(lambda x: 1 if x else 0)

# Calculate the intersections and generate labels
intersections = gene_matrix.sum(axis=1)

# Create a Plotly subplot
fig = make_subplots(rows=1, cols=1)

# Create the UpSet plot
upset_trace = go.Scatter(x=intersections.index, y=intersections.values, mode='markers+lines', marker=dict(size=10))
fig.add_trace(upset_trace, row=1, col=1)

# Customize the plot layout
fig.update_layout(
    title='Interactive UpSet Plot',
    xaxis_title='Gene Sets',
    yaxis_title='Intersection Count',
)

# Show the interactive plot in a Jupyter Notebook or save it as an HTML file
fig.show()
