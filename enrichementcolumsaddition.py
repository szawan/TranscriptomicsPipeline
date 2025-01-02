import pandas as pd
import ast
import os




def enriched_in_gsea(df, df_master, cell, condition):
     
    li_data = []
    df_filtered = df_master[(df_master["cell_line"] == cell) & (df_master['condition']== condition)]
    input_gene_list= df_filtered['gene'].unique()
    print(len(input_gene_list))
    
    df_sign = df[(df['pval']< 0.05)]
    df_sign['intersections'] = df_sign['leadingEdge'].apply(lambda x: x.split(" "))
    df_results = pd.DataFrame()
    if not df_sign.empty:
        all_genes = list(set(df_sign['intersections'].sum()))


        for gene in input_gene_list:
            is_enriched = 0
            
            if gene in all_genes:
                 is_enriched = 1
            
            li_data.append({
                      'gene': gene,
                      'is_enriched': is_enriched,
                      'Enrichment': 'GSEA',
                      'Cell_line' : cell,
                      'condition':condition
                 })
        
        df_results = pd.DataFrame(li_data)
        
        
        
    return df_results
    

def enriched_in_gprofiler(df, df_master, cell, condition):
    
  
    li_data = []
    df_filtered = df_master[(df_master["cell_line"] == cell) & (df_master['condition']== condition)]
    input_gene_list= df_filtered['gene'].unique()
    print(len(input_gene_list))
    
    df_sign = df[(df['p_value']< 0.05) & (df["source"].isin(['KEGG', 'REAC','WP']))]
    

    df_results = pd.DataFrame()
    if not df_sign.empty:
        df_sign['int_list'] = df_sign['intersections'].apply(ast.literal_eval)
        all_genes = list(set(df_sign['int_list'].sum()))


        for gene in input_gene_list:
            is_enriched = 0
            
            if gene in all_genes:
                 is_enriched = 1
            
            li_data.append({
                      'gene': gene,
                      'is_enriched': is_enriched,
                      'Enrichment': 'Gprofiler',
                      'Cell_line' : cell,
                      'condition':condition
                 })
        
        df_results = pd.DataFrame(li_data)
        
        
        
    return df_results
    
    




if __name__ == "__main__":
      
      context_path = '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/'
      input_dir = context_path + '11-GProfiler/raw/'
      output_dir = context_path + 'Enrichement_data/'
      gsea_output_dir = context_path + 'Enrichement_data/gsea/'

      gsea_dir = context_path + '10_fgsea/all/'
      masterfile = context_path+"IMpress/ImpressMapping.xlsx"
      li_data = []

      df_master = pd.read_excel(masterfile, sheet_name="Sheet 1")

      
      for file in os.listdir(input_dir):
            df_enrichment = pd.read_csv(input_dir+file, sep='\t')
            cell_line = file.split("_")[0]
            condition = "_".join(file.split(".")[0].split("_")[1:4])
            df_data = enriched_in_gprofiler(df_enrichment, df_master, cell_line, condition)
            
            if not df_data.empty:
                df_data.to_csv(output_dir+cell_line+"_"+condition+".csv")
      
      for file in os.listdir(gsea_dir):
            li_pathways = []
            df_final = pd.DataFrame()
            cell_line = file.split("_")[0]
            condition = "_".join(file.split(".")[0].split("_")[1:4])
            for name in ['KEGG', 'REACTOME','WIKI']:
                print(name)
                # dataset_kegg = pd.read_excel(gsea_dir)
                df_gsea_enrichment = pd.read_excel(gsea_dir+file, sheet_name=name)
                df_data = enriched_in_gsea(df_gsea_enrichment, df_master, cell_line, condition)
                li_pathways.append(df_data)
                print(df_data.head())
            df_final = pd.concat(li_pathways)
            df_output = df_final.groupby(['gene','Enrichment','Cell_line','condition'])\
                .agg({'is_enriched':'sum'}).reset_index()
            df_output[df_output['is_enriched']>1]['is_enriched'] = 1
            print(df_output)
            df_output.to_csv(gsea_output_dir+cell_line+"_"+condition+".csv")

