import pandas as pd
import os
import numpy as np
import glob


data_dir = "/scratch/zl7w2/Ron_Arabidopsis/mixomics"
target_dir = "/scratch/zl7w2/Ron_Arabidopsis/annotated"

kegg_f = "/scratch/zl7w2/Ron_Arabidopsis/data/kegg_ath.txt"
kegg_m = pd.read_csv(kegg_f,sep = ' ')
kegg_m['index'] = kegg_m['ath_name'].str.replace('ath:', '')


ensemble_f = "/scratch/zl7w2/Ron_Arabidopsis/data/mart_export.txt"
ensemble_m = pd.read_csv(ensemble_f,sep = ',')
ensemble_m = ensemble_m.rename(columns={'Gene stable ID': 'index'})
ensemble_drop_m = ensemble_m.drop_duplicates(subset='index')


txt_files = glob.glob(os.path.join(data_dir, "*.*.txt"))
for txt_file in txt_files:
    # txt_file = "/scratch/zl7w2/Ron_Arabidopsis/mixomics/corr_logfc1_0.9_all_sorted_filtered.txt"
    print(txt_file)
    matrix = pd.read_csv(txt_file,sep = ' ')
    matrix_melt = pd.melt(matrix.reset_index(),id_vars='index')
    # matrix_melt.to_csv(os.path.join(data_dir,"flower_q0.01_logfc2_cc_reproductive_0.7_melt.txt"), index=False)
    matrix_ensemble = matrix_melt.merge(ensemble_drop_m, how='left', on='index')
    matrix_kegg = matrix_ensemble.merge(kegg_m, how='left', on='index')
    int(txt_file)
    matrix = pd.read_csv(txt_file,sep = ' ')
    matrix_melt = pd.melt(matrix.reset_index(),id_vars='index')
    # matrix_melt.to_csv(os.path.join(data_dir,"flower_q0.01_logfc2_cc_reproductive_0.7_melt.txt"), index=False)
    matrix_ensemble = matrix_melt.merge(ensemble_drop_m, how='left', on='index')
    matrix_kegg = matrix_ensemble.merge(kegg_m, how='left', on='index')

    # result_df = matrix_kegg.groupby('index').agg({
    #     'pathway_name': ';'.join,
    #     'pathway': ';'.join
    # }).reset_index()

    result_df = matrix_kegg.groupby('index').agg({
        'pathway_name': lambda x: ';'.join(x.dropna()) if x.notna().any() else np.nan,
        'pathway': lambda x: ';'.join(x.dropna()) if x.notna().any() else np.nan,
    }).reset_index()

    result_df_merge = matrix_ensemble.merge(result_df, how='left', on='index')

    base_filename = os.path.splitext(os.path.basename(txt_file))[0]
    result_df_merge.to_csv(os.path.join(target_dir, base_filename+"_g2p.csv"), index=False)


    p2g_df = matrix_kegg.groupby('pathway').agg(
        genes=('index', lambda x: ','.join(x)),
        counts=('index', 'size')
    ).reset_index()

    p2g_df.to_csv(os.path.join(target_dir, base_filename+"_p2g.csv"), index=False)                                                                                               66,1          Bot
