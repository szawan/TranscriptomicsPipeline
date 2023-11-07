import os
import pandas as pd
import math

# SET PATHS
input_directory = "../output/8_cuffdiff/extracted_results/"
ref_annotation_location = "../others/Athaliana_ProteinAnnotation_TAIR10.csv"
output_directory = "../output/8_cuffdiff/extracted_results_with_annotation/"

# CREATE OUTPUT DIRECTORY IF NOT EXISTS
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# READ REFERENCE ANNOTATION FILE
ref_annotation = pd.read_csv(ref_annotation_location)
# in ref annotation file, remove everything after "." in gene column
ref_annotation['gene'] = ref_annotation['gene'].str.split('.').str[0]
print(ref_annotation.head())

# LOOP THROUGH CSV FILES IN INPUT DIRECTORY
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        # READ CSV FILE
        input_file = pd.read_csv(os.path.join(input_directory, filename), sep='\t')
        print(input_file.head())
        # in input file, rename replace "gene:" with "" in gene column
        input_file['gene'] = input_file['gene'].str.replace('gene:', '')
        print(input_file.head())

        # MERGE WITH REFERENCE ANNOTATION FILE
        merged_file = pd.merge(input_file, ref_annotation, on='gene')

        # get column names
        column_names = list(merged_file.columns.values)
        print(column_names)
        # rearrange columns
        merged_file = merged_file[['gene', 'Annotation', 'p_value', 'q_value', 'significant', 'foldchange']]

        print(merged_file.head())
        # WRITE MERGED FILE TO OUTPUT DIRECTORY
        merged_file.to_csv(os.path.join(output_directory, filename), index=False)

        # write merged file to output directory in xlsx format
        merged_file.to_excel(os.path.join(output_directory, filename.replace('.csv', '.xlsx')), index=False)


