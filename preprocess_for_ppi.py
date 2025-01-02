import pandas as pd 
import numpy as np
import os


def get_condition(file_name):
    """This function takes in file name and then split the file name"""
    
    li_filename = file_name.split("_")
    subset = [li_filename[i] for i in [1,2,4]]
    file_name = ("_".join(subset)).replace("2FC","")
    return file_name


def extract_all_data_degs(input_dir,cell_lines, output_dir):
    
    li_cell = []
    cell_line_files = []

    if os.path.exists(input_dir):
        for cell_line in cell_lines:
            print("++++++++++++++++++++++++++++++++")
            print(cell_line)
            for file in os.listdir(input_dir):
                file_path = os.path.join(input_dir,file)
                if os.path.isfile(file_path):
                    if file.startswith(cell_line):
                            condition = get_condition(file)
                            df = pd.read_csv(file_path, sep="\t")
                            df = df[['gene','p_value','q_value','significant','log2(fold_change)']]
                            df['gene'] = df['gene'].str.replace("gene-","")
                            df = df[df['gene'] !='-']
                            df['condition'] = condition
                            df['cell_line'] = cell_line
                            li_cell.append(df)
        df_all = pd.concat(li_cell, ignore_index=True)
        df_all['regulation'] = np.where(df_all['log2(fold_change)'] > 0, 'upregulated', 'downregulated')
        df_all.to_csv(output_dir+"all_genes.csv", sep="\t")
        df_all[df_all['significant'] == 'YES'].to_csv(output_dir+"significant_degs.csv",sep="\t")
        li_genes = df_all[df_all['significant'] == 'YES']['gene'].drop_duplicates()
        df_all[df_all['gene'].isin(li_genes)].to_csv(output_dir+"significant_log2FC.csv", sep='\t')
        li_genes.to_csv(output_dir+"only_genes.csv", index=False)
        print(df_all.shape)
            # print(f'Combined files for {cell_line} written!')  d

    
def condition_cellline_degs(input_dir, cell_lines, output_dir):
    li_cell = []
    cell_line_files = []

    if os.path.exists(input_dir):
        for cell_line in cell_lines:
            print("++++++++++++++++++++++++++++++++")
            print(cell_line)
            for file in os.listdir(input_dir):
                file_path = os.path.join(input_dir,file)
                if os.path.isfile(file_path):
                    if file.startswith(cell_line):
                        if (('C36' in file) and ('E07' in file)):
                            file_name = get_condition(file)
                            print(file_name)
                            df = pd.read_csv(file_path, sep="\t")
                            df = df[['gene','p_value','q_value','significant','log2(fold_change)']]
                            df['gene'] = df['gene'].str.replace("gene-","")
                            df = df[df['gene'] !='-']
                            li_cell.append(df)
            df_all = pd.concat(li_cell, ignore_index=True)
            df_all.to_csv(output_dir+cell_line+"_E07_vs_C36_all_degs.csv",sep="\t")
            
            print(df_all.shape)
            # print(f'Combined files for {cell_line} written!')

def extract_cellwise_log2FC(file_name, output_dir):
    df = pd.read_csv(file_name, sep="\t")
    df['cell_condition'] = df['cell_line'] + "_" + df['condition'] 
    df_pivot = df.pivot(index = ["gene","cell_line","condition","regulation","p_value",'q_value'],
                        columns="cell_condition",values="log2(fold_change)")
    print(df_pivot)
    df_pivot.to_csv(output_dir+"significant_genes_expanded.csv",sep="\t")

    return 1

def  main():

    file_name = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/inputs/significant_degs.csv"
    context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
    input_dir = context_path + "9_DEG_new_v2/"
    output_dir = context_path + "PPI/"

    cell_lines = ['A549', 'H3255', 'H1975', 'H820']
    conditions = ['C36', 'Veh', 'E07']
    
    # condition_cellline_degs(input_dir, cell_lines,output_dir)
    extract_all_data_degs(input_dir,cell_lines, output_dir)

    # extract_cellwise_log2FC(file_name, output_dir)

main()