
# if (!require("BiocManager", quietly = TRUE))
#     install.packages("BiocManager", repos = "https://cran.r-project.org")
# install.packages("circlize", repos = "https://cran.r-project.org")
# install.packages("pheatmap", repos = "https://cran.r-project.org")

# BiocManager::install("ComplexHeatmap")
# install.packages("readxl", repos="https://cran.r-project.org")
# install.packages("dplyr", repos="https://cran.r-project.org")
library(readxl)
library(dplyr)
library(ComplexHeatmap)
library(pheatmap)
library(RColorBrewer)
library(circlize)

# df <-read.csv("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_DistanceMatrix/All_genes_v2.csv", header=TRUE)
# df[is.na(df)] <- 0


# # # Reading an Excel file
# excel_path <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/gene_pathway/H3255_pathways.xlsx" # Update this path to your Excel file
# df1 <- read_excel(excel_path, sheet = 'g2p')

# # # Extracting the "gene_" column into a list
# gene_list <- df1$gene_ # Assuming 'gene_' is the name of the column


# filtered_df <- df %>% filter(df$gene %in% gene_list) # Replace 'gene_column_in_df2' with the actual column name in df2 that corresponds to 'gene_'

# # # Viewing the filtered dataframe
# # colnames(filtered_df)
# subset_df  <- filtered_df %>%
#                 select('gene','A549_E07_vs_A549_C362FC_greaterthan_.0.5.',
#                 'H1975_E07_vs_H1975_C362FC_greaterthan_.0.5.',
#                 'H3255_E07_vs_H3255_C362FC_greaterthan_.0.5.',
#                 'H820_E07_vs_H820_C362FC_greaterthan_.0.5.')
# row.names(subset_df) <- subset_df$gene
# colnames(subset_df) <- c('gene','A549',
#                 'H1975',
#                 'H3255',
#                 'H820')
# subset_df$gene <- NULL
# # # png(paste0(output_path,"correlation_heatmap.png")) # Opens a PNG device

# # pheatmap(subset_df, 
# # #              scale = 'row', 
# # #             #  cutree_cols = 2, 
# # #             #  cutree_rows = 2,
# # #              fontsize_row = 4,
# # #              show_rownames = TRUE,
# # #              color=colorRampPalette(c("green", "black", "fireBrick"))(50),
        
# # #             )
# # # dev.off()
col_fun = colorRamp2(c(-2, 0, 2), c("green", "black", "firebrick"))
col_fun(seq(-3, 3))

path  <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/gene_pathway/H3255_immune_genes.csv"
df_immune <- read.csv(path, row.names = 2)
df_immune[is.na(df_immune)] <- 0
df_immune <- df_immune[c('A549','H820','H1975','H3255')]
head(df_immune)
output_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/plots/heatmap/"
pdf(paste0(output_path,"immune_genes_H3255.pdf")) # Opens a PNG device
Heatmap(df_immune, name = "log2FC", 
column_names_gp = grid::gpar(fontsize = 8),
  row_names_gp = grid::gpar(fontsize = 8),
    col = col_fun)
dev.off()  # Closes the device
# # df_fpkms <- read.csv("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/06_fpkm_csv/fpkm_all_samples_avg.csv", row.names = 1)
# # cor_mat <- cor(df_fpkms)
# # png(paste0(output_path,"peasron-correlation_heatmap.png")) # Opens a PNG device
# # Heatmap(cor_mat, name = "Pearson", 
# #     cell_fun = function(j, i, x, y, width, height, fill) {
# #         grid.text(sprintf("%.1f", cor_mat[i, j]), x, y, gp = gpar(fontsize = 10))
# # })
# # dev.off() 


# #Ligand headmap
# # column_font_colors <- c("white", "white","black","white")

# col_fun = colorRamp2(c(-2,0, 2), c("green","black","firebrick"))
# col_fun(seq(-3, 3))
# path  <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/gene_pathway/H3255_immune_genes.csv"
# df = read.csv(path, row.names = 1)
# pdf(paste0(output_path,"H3255_immune.pdf")) # Opens a PNG device
# Heatmap(df, col=col_fun, name= 
# "log2FC",
# cell_fun = function(j, i, x, y, width, height, fill) {
#         # font_col = column_font_colors[j]
#         grid.text(sprintf("%.1f", df[i, j]), x, y, gp = gpar(fontsize = 20, col=font_col))
# },
# heatmap_legend_param = list(
#             # title = "Log2 Fold Change", # Customize your legend title
#             # title_gp = gpar(fontsize = 14), # Adjust legend title size
#             # labels_gp = gpar(fontsize = 12) # Adjust legend labels/text size
#             legend_symbol_size = unit(20, "mm") # Example to adjust symbol size

#         )


# )
# dev.off() 