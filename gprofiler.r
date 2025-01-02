library(gprofiler2)

# SET PATHS

input_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG_new"
output_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_gprofiler/"
file_name <- "01_FC1_DEGenesList.csv"

# if output directory does not exist, create it
if (!dir.exists(output_directory)) {
  dir.create(output_directory)
}

# read the csv file
df <- read.csv(file.path(input_directory, file_name), sep='\t', header=TRUE)
print(head(df))

# loop to extract columns one by one and save them as a list (first value is experiment name)
for (column in colnames(df)) {
  # take out column name and save it as a variable
  experiment_name <- column
  print(experiment_name)

  # convert the column to a list
  gene_list <- na.omit(df[[column]])

  # remove gene: from the gene names (as gprofiler does not recognize it)
  gene_list <- gsub('gene-', '', gene_list)

  # print the length of the gene list
  print(length(gene_list))

  results <- gost(organism='hsapiens',query=gene_list)
   
gostplot(results, capped = FALSE, interactive = FALSE)
    
  

  
  print(results)
}
  # write the results to a csv file
  write.table(results, file.path(output_directory, paste0(experiment_name, '_gprofilerR_1.csv')), sep='\t', row.names=FALSE)

#   # result to excel file
#   write.xlsx(results, file.path(output_directory, paste0(experiment_name, '_gprofilerR_1.xlsx')
