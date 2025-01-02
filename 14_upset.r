library(UpSetR)
library(ggplot2)
library(dplyr)

# set input and output file paths
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG/"
output_directory <- '/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new_v2/'

cellline = 'E07_vs_c36'
# read the CSV file (tab-delimited)
# mydata <- read.delim(paste0(input_directory, "01_1_",cellline,"_DEGenesList.csv"))
mydata <-read.delim("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new_v2/DEG_Summary/01_2FC_greaterthan_0.5_DEGenesList.csv")
# print header
filtereddata<- mydata %>% 
        select(c('A549_E07_vs_A549_C36', 'H820_E07_vs_H820_C36', 'H1975_E07_vs_H1975_C36', 'H3255_E07_vs_H3255_C36'))
colnames(filtereddata) <- c('A549', 'H820', 'H1975', 'H3255')
head(filtereddata)
converted_data <- fromList(filtereddata)
# print converted data

write.csv(converted_data, file = paste0(output_directory, "03_1_",cellline,"_DEGenesList_converted.csv"), quote = FALSE, row.names = FALSE)

# count the number of genes in each column
gene_count <- colSums(converted_data)
# print gene count
gene_count

# png(filename = file.path(output_directory, paste0(cellline,"_upset_plot.png")), width = 21, height = 7, units = "in", res = 300)
# upset(converted_data, nsets = ncol(converted_data), nintersects = NA,
# show.numbers = TRUE,
# 	point.size = 2, 
# 	line.size = 1,
# )
# dev.off()

main_bar_col <- c("black")
sets_bar_col <- c("black")

text_scale_options1 <- c(1, 1, 1, 1, 0.75, 1)
text_scale_options2 <- c(1.3, 1.3, 1, 1, 2, 0.75)
text_scale_options3 <- c(1.5, 1.25, 1.25, 1, 2, 3)
cat(rep("\n", 2))
png(filename = file.path(output_directory, paste0(cellline,"_upset_plot_freq_desc.png")), width = 21, height = 7, units = "in", res = 300)
upset(converted_data, nsets = ncol(converted_data), nintersects = NA,
# show.numbers = TRUE, 
mainbar.y.label = "Counts of Overlapping Genes", 

sets.x.label = "Counts by Condition",
	point.size = 10, 
        text.scale=text_scale_options3,
        main.bar.color = main_bar_col,
	sets.bar.color = sets_bar_col,
	line.size = 5,

 decreasing = TRUE, order.by = "freq")
dev.off()

# cat(rep("\n", 2))
# png(filename = file.path(output_directory, paste0(cellline,"_upset_plot_degree_desc.png")), width = 21, height = 7, units = "in", res = 300)
# upset(converted_data, nsets = ncol(converted_data), nintersects = NA, decreasing = TRUE, order.by = "degree")
# dev.off()