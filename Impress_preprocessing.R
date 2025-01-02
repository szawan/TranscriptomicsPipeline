library(org.Hs.eg.db)
library(clusterProfiler)
# install.packages("openxlsx", repos = "https://cran.r-project.org")
library(openxlsx)
library(dplyr)

context_path<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
# input_dir <- file.path(paste0(context_path, "10_fgsea/inputs/"))
output_dir <- file.path(paste0(context_path, "IMpress/"))
excel_file_path <- paste0(output_dir, "ImpressMapping.xlsx")

if (!dir.exists(output_dir)) {
  dir.create(paste0(output_dir))
}

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_data <- read.xlsx("/scratch/sah2p/datasets/hg38/impress_master_file/human_mastersheet_V1.xlsx")

all_degs <- read.csv("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/PPI/all_degs.csv", sep="\t")
# View the data
print(head(all_degs))

##Toy example symbols:
# sym = c("AKT3","CDH1")
sym = c("IRF2","E2F1","STAT5B","GTF3A","STAT3", 
"ATF5","DLX2","IRF7","LHX3","ZNF436","PAX2",
"TFAM","GATA6","LEF1", "TCF4", "IRF1","STAT5A",
 "GATA1","POU3F2","CEBPA","STAT6","FOXR2", 
 "YY1", "RFX7","ZNF101","NFXL1","SIX1", "CIC", "MYBL1", "MAF", 
 "TERF1","ZNF16", "PAX4", "SP1", "NR1I2", "PIAS4", "MSX1", 
   "HSF1", "ZNF433", "SRF", "DMRT1", "ELK1", "NR1H4")
##Get the Entrez gene IDs associated with those symbols
# EG_IDs = mget(sym, revmap(org.Hs.egSYMBOL),ifnotfound=NA)

##Then get the KEGG IDs associated with those entrez genes.
# KEGG_IDs = mget(as.character(EG_IDs), org.Hs.egPATH,ifnotfound=NA)
# print(KEGG_IDs)
# sym = as.list(all_degs$kegg_ids)
kegg_ids = bitr(all_degs$gene, fromType="SYMBOL", toType="ENTREZID", OrgDb=org.Hs.eg.db)
print(colnames(kegg_ids))
colnames(kegg_ids) <- c("gene","KEGG_id")
result <- left_join(all_degs, kegg_ids, by = "gene")
# result <- result %>% mutate(KEGG_id= paste("hsa",KEGG_id, sep=":"))
# all_results <- left_join(excel_data, result, by="KEGG_id")
# print(head(all_results))
print(result)
write.xlsx(result, file = paste0('output_dir','kegg_gene_mapping.xlsx'))



