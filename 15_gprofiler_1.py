from gprofiler import GProfiler
import pandas as pd
import os

# SET PATHS
input_directory = "../output/8_cuffdiff/"
output_directory = "../output/9_gprofiler/"
file_name = "01_DEGenesList.csv"

# if output directory does not exist, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# read the csv file
df = pd.read_csv(input_directory + file_name, sep='\t', header=0)
print(df.head())

# loop to extract columns one by one and save them as a list (first value is experiment name)
for column in df.columns:
    # take out column name and save it as a variable
    experiment_name = column
    print(experiment_name)

    # convert the column to a list
    gene_list = df[column].values.tolist()

    # remove nan values
    gene_list = [x for x in gene_list if str(x) != 'nan']

    # remove gene: from the gene names (as gprofiler does not recognize it)
    gene_list = [x.replace('gene:','') for x in gene_list]

    # print the length of the gene list
    print(len(gene_list))


    gp = GProfiler(return_dataframe=True)
    results = gp.profile(organism='athaliana', user_threshold = '1', no_evidences=False,
                         query = gene_list)

    # write the results to a csv file
    results.to_csv(output_directory + experiment_name + '_gprofiler_1.csv', sep='\t', index=False)

    # result to excel file
    results.to_excel(output_directory + experiment_name + '_gprofiler_1.xlsx')





    