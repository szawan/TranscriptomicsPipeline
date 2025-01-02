# BiocManager::install("clusterProfiler")
# BiocManager::install("pathview")
# BiocManager::install("enrichplot")
# SET THE DESIRED ORGANISM HERE
#Human
organism = "org.Hs.eg.db"
#Glycine Max
organism = "org.Glycine_max.eg.db"
BiocManager::install(organism, character.only = TRUE)
library(organism, character.only = TRUE)
library(DOSE)

# library(ReactomePA)
library(clusterProfiler)
library(enrichplot)
# we use ggplot2 to add x axis labels (ex: ridgeplot)
library(ggplot2)

# Load required library

# Replace 'your_file.csv' with the actual path to your CSV file
# file_path <- "All_DEGs.csv"

# # Load CSV file into a dataframe
# df <- read.csv(file_path)
# df$gene <- sub('gene-', '', df$gene)



# # Display the dataframe structure
# print("Dataframe structure:")


# # Loop through the columns
# print("\nLooping through columns:")
# for (col in colnames(df)) {
#   # we want the log2 fold change 
#   print(col)
#   original_gene_list <- df$col
#   # name the vector
# names(original_gene_list) <- df$X
#   # omit any NA values 
# gene_list<-na.omit(original_gene_list)


input_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new"
output_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_gprofiler/"
file_name <- "All_DEGs.csv"

df_anno <-read.csv("/scratch/sah2p/datasets/hg38/annotation/Homo_sapiens.gene_info.txt", 
sep="\t", header=TRUE)


# if output directory does not exist, create it
if (!dir.exists(output_directory)) {
  dir.create(output_directory)
}

# read the csv file
df <- read.csv(file_name, sep=',', header=TRUE)
# print(head(df))
result_df <- merge(df_anno, df, by.x = "Symbol", by.y = "gene", all.y = TRUE)

# print(colnames(df))
head(result_df)
write.csv(result_df, file = "annotated_DEGS.csv")
# ids<- bitr(df$gene, fromType="ACCNUM", toType='ENTREZID',
# OrgDb="org.Hs.eg.db")

# head(ids)


# # loop to extract columns one by one and save them as a list (first value is experiment name)
# for (column in colnames(df)) {
#   # take out column name and save it as a variable
#   experiment_name <- column
#   print(experiment_name)

#   # convert the column to a list
#   gene_list <- na.omit(df[[column]])

#   # remove gene: from the gene names (as gprofiler does not recognize it)
#   gene_list <- gsub('gene-', '', gene_list)

#   # print the length of the gene list
#   print(length(gene_list))
#   # sort the list in decreasing order (required for clusterProfiler)
# gene_list = sort(gene_list, decreasing = TRUE)
# print(gene_list)
# }

# gse <- enrichGO(geneList=c(ENSG00000121410, ENSG00000184389), 
#              ont ="ALL", 
#              keyType = "ENSEMBL", 
#              nPerm = 10000, 
#              minGSSize = 3, 
#              maxGSSize = 800, 
#              pvalueCutoff = 0.05, 
#              verbose = TRUE, 
#              OrgDb = organism, 
#              pAdjustMethod = "none")


# require(DOSE)
# dotplot(gse, showCategory=10, split=".sign") + facet_grid(.~.sign)