import csv
import os

# SET PATHS
input_directory = "../output/6_fpkm_csv" # without last slash
required_extension = ".csv"
output_directory = "../output/6_fpkm_csv"

# read csv file
reader = csv.reader(open(input_directory + "/combined_data.csv", "r"), delimiter=",")

# transpose csv file
transposed = zip(*reader)

# write transpose csv file

with open(output_directory + "/combined_data_transposed.csv", "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(transposed)