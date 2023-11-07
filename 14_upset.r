library(UpSetR)
library(ggplot2)

# set input and output file paths
input_directory <- "../output/8_cuffdiff/"
output_directory <- "../output/8_cuffdiff/"

# read the CSV file (tab-delimited)
mydata <- read.delim(paste0(input_directory, "01_DEGenesList.csv"))

# print header
head(mydata)

converted_data <- fromList(mydata)
# print converted data
head(converted_data)

write.csv(converted_data, file = paste0(output_directory, "03_DEGenesList_converted.csv"), quote = FALSE, row.names = FALSE)

# count the number of genes in each column
gene_count <- colSums(converted_data)
# print gene count
gene_count

png(filename = file.path(output_directory, "upset_plot.png"), width = 21, height = 7, units = "in", res = 300)
upset(converted_data, nsets = ncol(converted_data), nintersects = NA)
dev.off()

cat(rep("\n", 2))
png(filename = file.path(output_directory, "upset_plot_freq_desc.png"), width = 21, height = 7, units = "in", res = 300)
upset(converted_data, nsets = ncol(converted_data), nintersects = NA, decreasing = TRUE, order.by = "freq")
dev.off()

cat(rep("\n", 2))
png(filename = file.path(output_directory, "upset_plot_degree_desc.png"), width = 21, height = 7, units = "in", res = 300)
upset(converted_data, nsets = ncol(converted_data), nintersects = NA, decreasing = TRUE, order.by = "degree")
dev.off()