library(org.Hs.eg.db)
library(clusterProfiler)
# install.packages("openxlsx", repos = "https://cran.r-project.org")
library(openxlsx)
library(dplyr)

context_path<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_dir <- file.path(paste0(context_path, "Enrichement_data/scores/"))
output_dir <- file.path(paste0(context_path, "IMpress/"))
excel_file_path <- paste0(output_dir, "ImpressMapping_gsea_gprofiler.xlsx")

if (!dir.exists(output_dir)) {
  dir.create(paste0(output_dir))
}

# Replace 'your_file.xlsx' with the actual path to your Excel file
excel_data <- read.xlsx(paste0(output_dir,"ImpressMapping.xlsx"))

setwd(input_dir)
files <- list.files(pattern = "\\.csv$")

for (file in files) {
file_name = file
print(file_name)
file_name <- sub("\\.csv$", "", file_name)
name_parts <- strsplit(file_name, "_")[[1]]
# Extract values for Cell_line and Condition
cell_line <- name_parts[1]
print(cell_line)
condition <- paste(name_parts[-1], collapse = "_")
print(condition)
df_scores <- read.csv(file)
kegg_ids = bitr(df_scores$gene, fromType="SYMBOL", toType="ENTREZID", OrgDb=org.Hs.eg.db)
# print(colnames(kegg_ids))
colnames(kegg_ids) <- c("gene","KEGG_id")
if (file_name == "H820_E07_vs_C36"){
  df_scores = df_scores[,c('gene','is_enriched')]

}
else{
df_scores = df_scores[,c('gene','gsea_enriched','gprof_enriched')]
}
result <- left_join(df_scores, kegg_ids, by = "gene")
result <- result %>% mutate(KEGG_id= paste("hsa",KEGG_id, sep=":"))
# print(head(result))
filtered_data_subset <- excel_data[excel_data$cell_line == cell_line & excel_data$condition == condition,]
print(head(filtered_data_subset))
all_results <- left_join(filtered_data_subset, result, by="KEGG_id")

write.xlsx(all_results, file = paste0(output_dir,file_name,".xlsx"))
}






