import pandas as pd
import os
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
gsea_path = context_path+"Enrichement_data/gsea/"
grofiler_path = context_path+"Enrichement_data/gprofiler/"
output_path = context_path+"Enrichement_data/scores/"
li_files = [file for i,file in enumerate(os.listdir(gsea_path))]

for file in li_files:
    df_gsea = pd.read_csv(gsea_path+file)
    print(df_gsea.head(5))
    df_r_gsea = df_gsea.groupby(['gene']).agg({'is_enriched':sum}).reset_index()
    df_r_gsea.columns = ['gene','gsea_enriched']
    if file != "H820_E07_vs_C36.csv":
        df_gprof = pd.read_csv(grofiler_path+file)
        df_r_gprof = df_gprof.groupby(['gene']).agg({'is_enriched':sum}).reset_index()
        df_r_gprof.columns = ['gene','gprof_enriched']
        print(df_r_gprof)
        df_resultant = df_r_gsea.merge(df_r_gprof, on='gene',how='left')
        cell_line = file.split('_')[0]
        condition = "_".join(file.split(".")[0].split("_")[1:4])
        df_resultant['cell_line'] = cell_line
        df_resultant['condition'] = condition
    else:
        df_resultant = df_gsea
    print(df_resultant)
    df_resultant.to_csv(output_path+file)