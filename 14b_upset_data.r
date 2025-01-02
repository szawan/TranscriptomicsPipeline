install.packages('VennDiagram')
library(VennDiagram)
library(tidyverse)
library(openxlsx)

# set input and output file paths
context_path = 
input_directory <- "../output/8_cuffdiff/"
output_directory <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG"

# Create a new Excel workbook
wb <- createWorkbook()
addWorksheet(wb, sheetName = "summary")

# read the CSV file (tab-delimited)
mydata <- read.delim("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/9_DEG/10_DEG_LIST01_(2)1_DEGenesList.csv")

# get unique partitions
unique.partition <- VennDiagram::get.venn.partitions(mydata)

# sort by count
unique.partition <- unique.partition[order(unique.partition$..count.., decreasing = TRUE),]

# create an empty list
list <- list()

# loop through each row and print
for (i in 1:nrow(unique.partition)) {
    # print(unique.partition[i,])
    # read coloumn ..set..
    set <- unique.partition[i,]$`..set..`
    genes <- unique.partition[i,]$..values..
    count <- unique.partition[i,]$..count..

    # parse set till "∖"
    set_parsed <- strsplit(set, "∖")[[1]][1]

    # create a row for the list
    row <- c(i, set_parsed, count)

    # add row to list
    list[[i]] <- row

    string_var <- paste("", i)
    addWorksheet(wb, sheetName = string_var)
    writeData(wb, sheet = string_var, x = genes)
}

# create header for dataframe
header <- c("id", "set", "count")

# create dataframe
df <- as.data.frame(do.call(rbind, list), stringsAsFactors = FALSE)

# assign header to dataframe
names(df) <- header
# print(df)

writeData(wb, sheet = "summary", x = df)
saveWorkbook(wb, file = paste0(output_directory,"upset_data.xlsx"), overwrite = TRUE)