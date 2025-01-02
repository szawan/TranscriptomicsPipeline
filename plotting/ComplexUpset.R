# install.packages("ggplot2", repos="https://cran.r-project.org")
# install.packages("ComplexUpset", repos="https://cran.r-project.org")
if (!requireNamespace("BiocManager", quietly=TRUE))
    install.packages("BiocManager")
BiocManager::install("ComplexHeatmap")
library(ggplot2)
library(ComplexUpset)
library(dplyr)


cellline = 'H1975'
# read the CSV file (tab-delimited)
# mydata <- read.delim(paste0(input_directory, "01_1_",cellline,"_DEGenesList.csv"))
mydata <-read.delim("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new_v2/DEG_Summary/01_2FC_greaterthan_0.5_DEGenesList.csv")
# print header
head(mydata)
filtereddata<- mydata %>% 
        select(c('H1975_E07_vs_H1975_Veh', 'H1975_C36_vs_H1975_Veh', 'H1975_E07_vs_H1975_C36'))

#make combination matrix
# m3 = make_comb_mat(filtereddata)

# Customize the plot as needed
cat(rep("\n", 2))
png(filename = file.path(paste0(cellline,"_upset_plot_degree_desc.png")), width = 21, height = 7, units = "in", res = 300)
Upset(filtered_df)
dev.off()