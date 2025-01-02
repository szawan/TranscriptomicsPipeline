# install.packages("ggVennDiagram", repos="https://cran.r-project.org")
library(ggVennDiagram)
library(dplyr)
library(ggplot2)

# List of items

filtered_df <-read.delim("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new_v2/DEG_Summary/01_2FC_greaterthan_0.5_DEGenesList.csv")
# print header
x <- list(A549 = na.omit(unique(filtered_df$A549_E07_vs_A549_C36)),
           H820 = na.omit(unique(filtered_df$H820_E07_vs_H820_C36)), 
           H1975 = na.omit(unique(filtered_df$H1975_E07_vs_H1975_C36)),
        H3255 = na.omit(unique(filtered_df$H3255_E07_vs_H3255_C36)))

# 4D Venn diagram
pdf("testVenn.pdf") # Opens a PNG device
ggVennDiagram(x) + scale_fill_gradient(low="blue", high = "red")
dev.off()
