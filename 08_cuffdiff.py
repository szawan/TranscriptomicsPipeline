import csv
import os
import glob
import pandas as pd

# SET PATHS
input_directory = "../output/4_sorted_bam/files" # without last slash
required_extension = ".sam"
output_directory = "../output/5_cufflinks_result/files/"
folder_names_file = "folder_names.txt"

reference_file = "../annotation/Arabidopsis_thaliana.TAIR10.57.gff3"
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
    if not os.path.exists('../output/8_cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/'):
        os.makedirs('../output/8_cuffdiff/'+comp.iloc[index].Condition+'/logs_cuffdiff/')

#    if not os.path.exists('./counts/count_logs/'):
#        os.makedirs('./counts/count_logs/')

    #if comp.iloc[index].Condition != condition[0]:
    str1 = \
        "(cuffdiff -p 8 -o ../output/8_cuffdiff/"+comp.iloc[index].Condition+"/"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference \
        +" "\
        \
        + reference_file+" "+comp.iloc[index].den+" "+comp.iloc[index].num \
        \
        +input_directory+"/"+comp.iloc[index].Reference+"1_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Reference+"2_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Reference+"3_sorted.sam"\
        \
        +" "\
        \
        +input_directory+"/"+comp.iloc[index].Experiment+"1_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Experiment+"2_sorted.sam"+','+input_directory+"/"+comp.iloc[index].Experiment+"3_sorted.sam"\
        \
        +") >> ../output/8_cuffdiff/"+comp.iloc[index].Condition+"/logs_cuffdiff/log_"+comp.iloc[index].Experiment+"_vs_"+comp.iloc[index].Reference+".txt 2>&1 &"
        
    print(str1+"\n")
    os.system(str1)