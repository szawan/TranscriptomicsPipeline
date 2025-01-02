# if (!requireNamespace("ComplexHeatmap", quietly = TRUE)) {
#     install.packages("ComplexHeatmap", repos="https://cran.r-project.org")
# }
if (!requireNamespace("matrixStats", quietly = TRUE)) {
    install.packages("matrixStats", repos="https://cran.r-project.org")
}

library(ComplexHeatmap)
library(matrixStats)
library(ggplot2)
library(readxl)
library(dplyr)
library(ComplexHeatmap)
library(pheatmap)
library(RColorBrewer)
library(circlize)


filepath_1<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new_v2/DEG_Summary/OverlappingGenesBetweenH1975&H3255.csv"
filepath_2<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_DistanceMatrix/All_genes_v2.csv"

mydata <-read.csv(filepath_1)
colnames(mydata) <-c('gene')
genes <- as.list(mydata$gene)
print(str(genes))


myalldata <- read.csv(filepath_2)
# myfiltered<- na.omit(myalldata[c("gene","H3255_E07_vs_C36","H1975_E07_vs_C36")])
overlapp_genes <- which(myalldata$gene %in% genes)
rownames(myalldata) <- myalldata$gene
myfiltered<- na.omit(myalldata[overlapp_genes, c("H3255_E07_vs_C36","H1975_E07_vs_C36")])
# rownames(myfiltered) <-myfiltered$gene

print(myfiltered)
gene_var <- rowVars(as.matrix(myfiltered[c('H3255_E07_vs_C36', 'H1975_E07_vs_C36')]))
# print(gene_var)
sorted_genes <- sort(gene_var, decreasing=TRUE)
top_genes <- names(sorted_genes)[1:50]
print(top_genes)

data_highly_variabe <- myalldata[top_genes,]
data_highly_variabe <- data_highly_variabe[c("H3255_E07_vs_C36","H1975_E07_vs_C36","H820_E07_vs_C36","A549_E07_vs_C36")]
colnames(data_highly_variabe) <- c("H3255","H1975", "H820","A549")
# data_highly_variabe <- na.omit(data_highly_variabe)
 print(data_highly_variabe)
 col_fun = colorRamp2(c(-2, 0, 2), c("green", "black", "firebrick"))
col_fun(seq(-3, 3))
# Draw the heatmap
pdf('highly_variable_genes.pdf')
Heatmap(data_highly_variabe[,c("H820","A549","H1975","H3255")],
        name = "Expression",
        row_title = "Highly Variable Genes",
        column_names_side = "bottom",
        row_names_gp = gpar(fontsize = 8),
        column_names_gp = gpar(fontsize = 9), col =col_fun,
        # cluster_rows = FALSE,
        cluster_columns = FALSE)
dev.off()