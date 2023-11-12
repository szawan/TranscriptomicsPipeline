import csv
import os
import glob
import pandas as pd

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"4_sorted_bam/files" # without last slash
required_extension = ".sam"
output_directory = context_path+"8_cuffdiff_result/files/"
logs_directory = "/8_cuffdiff_results/logs/"
folder_names_file = "folder_names.txt"

reference_file = "/scratch/sah2p/datasets/hg38/annotation/GRCh38_latest_genomic.gff"
comp_file = "comp.csv"
comp = pd.read_csv(comp_file)

comp['den'] = ""

for index,row in comp.iterrows():
    #value = []
    value = ""
    print(comp.iloc[index].Reference+"*")
    for filenames in glob.glob(comp.iloc[index].Reference+"*"):
        #value.append(filenames+",")
        if value == "":
            value = filenames
        else:
            value = value + "," + filenames
    comp.at[index,'den'] = value
    
comp['num'] = ""

for index,row in comp.iterrows():
    #value = []
    value = ""
    print(comp.iloc[index].Experiment+"*")
    for filenames in glob.glob(comp.iloc[index].Experiment+"*"):
        #value.append(filenames+",")
        if value == "":
            value = filenames
        else:
            value = value + "," + filenames
    comp.at[index,'num'] = value

#print(comp)
condition = comp['Condition'].unique()

for index,row in comp.iterrows():
    if not os.path.exists(output_directory+comp.iloc[index].Condition+logs_directory):
        os.makedirs(output_directory+comp.iloc[index].Condition+logs_directory)

#    if not os.path.exists('./counts/count_logs/'):
#        os.makedirs('./counts/count_logs/')

    #if comp.iloc[index].Condition != condition[0]:
    str1 = \
        "(cuffdiff -p 8 -o" + output_directory +comp.iloc[index].Condition+"/"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference \
        +" "\
        \
        + reference_file+" "+comp.iloc[index].den+" "+comp.iloc[index].num \
        \
        +input_directory+"/"+comp.iloc[index].Reference+"_1_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Reference+"_2_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Reference+"_3_sorted.sam"\
        \
        +" "\
        \
        +input_directory+"/"+comp.iloc[index].Experiment+"_1_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Experiment+"_2_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Experiment+"_3_sorted.sam"\
        \
        +") >> "+output_directory+comp.iloc[index].Condition+logs_directory+"log_"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference+".txt 2>&1 &"
        
    print(str1+"\n")
    os.system(str1)