# Install and load the required packages
install.packages("AnnotationDbi", repos = "https://cran.r-project.org")
install.packages("org.Hs.eg.db", repos = "https://cran.r-project.org")
install.packages("R.utils", repos = "https://cran.r-project.org")
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cran.r-project.org")

BiocManager::install("GSEABase")
R.utils::setOption("clusterProfiler.download.method","auto")

library(AnnotationDbi)
library(org.Hs.eg.db)
library(DOSE)
library(clusterProfiler)
library(enrichplot)
# we use ggplot2 to add x axis labels (ex: ridgeplot)
library(ggplot2)


# Assuming cuffdiff_results is your Cuffdiff results data frame
df <- read.csv("/scratch/sah2p/projects/RNASeqPipeline/annotated_DEGS.csv")
selected_df <- df[,c("Symbol","GeneID","description","type_of_gene","A549_Veh_vs_A549_E07")]
print(columns(org.Hs.eg.db))
# Create a sample Cuffdiff results data frame
k <- head(keys(org.Hs.eg.db,keytype="SYMBOL"))
k_2 <- head(keys(org.Hs.eg.db,keytype="SYMBOL"))
# Convert gene_id to geneol using AnnotationDbi
gene_symbol <- mapIds(org.Hs.eg.db, keys = k, column = "SYMBOL", keytype = "SYMBOL")
ENTREZID <- mapIds(org.Hs.eg.db, keys = k, column = "ENTREZID", keytype = "SYMBOL")

# Add the gene_symbol column to the Cuffdiff results data frame
selected_df$gene_symbol <- gene_symbol
selected_df$entrezid <- ENTREZID

# print(selected_df)
# ids <- bitr(selected_df$gene_symbol, fromType="SYMBOL", toType='ENTREZID',
# OrgDb=org.Hs.eg.db)

# print(ids$ENTREZID)

# ids_kegg <- bitr_kegg(ids$ENTREZID, fromType="kegg", toType='', organism='hsa')


# print(ids_kegg)
# Display the results
# print(selected_df)


#Using cluster Profiler with results
# gse <- enrichGO(selected_df$gene_symbol, 
#              ont ="ALL", 
#              keyType = "SYMBOL", 
#              minGSSize = 3, 
#              maxGSSize = 800, 
#              pvalueCutoff = 0.05, 
#              OrgDb = org.Hs.eg.db, 
#              pAdjustMethod = "none")

# print(gse)

# Rank results for GSEA; put in decreasing order.
# Arrange the DataFrame by descending A549_Veh_vs_A549_E07
selected_df <- selected_df[order(-selected_df$A549_Veh_vs_A549_E07), ]

# # Create a named vector with log fold changes
GSEA_data <- setNames(selected_df$A549_Veh_vs_A549_E07, selected_df$gene_symbol)
GSEA_id_data <- setNames(selected_df$A549_Veh_vs_A549_E07, selected_df$entrezid)


# set.seed(123)
gsea_go <- gseGO(GSEA_data,
              OrgDb = org.Hs.eg.db,
              ont = "ALL",
              pvalueCutoff =0.05,
              keyType = "SYMBOL",
              seed=TRUE)

print(gsea_go)

# kk2 <- (geneList     = GSEA_id_data,
#                organism     = 'hsa',
#                keyType = 'kegg',
#                minGSSize    = 120,
#                pvalueCutoff = 0.05,
#                verbose      = FALSE)
               
# print(kk2)

# data <- read.gmt("./Human_GOBP_AllPathways_no_GO_iea_January_01_2024_symbol.gmt")
# print(data)
# GSEA_res <- GSEA(
#     GSEA_data,
# TERM2GENE = NA)
# print(GSEA_res)
# print(search_kegg_organism('hsa', by='kegg_code'))


#Wiki Pathways
# print(GSEA_id_data)
# WP <- gseWP(GSE_id_data, organism = "Homo sapiens")
# print(get_wp_organisms())
# print(enrichWP(GSE_id_data, organism = "Homo sapiens"))
# get_wp_organisms()
