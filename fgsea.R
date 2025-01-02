if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager", repos = "https://cran.r-project.org")

# The following initializes usage of Bioc devel
# BiocManager::install(version='devel')
# BiocManager::install("org.Hs.eg.db")
# install.packages("AnnotationDbi", repos = "https://cran.r-project.org")
# BiocManager::install("cogena")
# BiocManager::install("GSEABase")
# BiocManager::install("reactome.db")


library(GSEABase)
library(tidyverse) # includes ggplot2, for data visualisation. dplyr, for data manipulation.
library(RColorBrewer) # for a colourful plot
library(fgsea)
library(org.Hs.eg.db)
library(reactome.db)
library(dplyr)
set.seed(123456)
db <- "IMMUNODB"

context_path<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_dir <- file.path(paste0(context_path, "10_fgsea/inputs/"))
output_dir <- file.path(paste0(context_path, "10_fgsea/",db, "/"))
# file_name = "significant_degs.csv"
file_name = "all_genes.csv"
gmt_dir <- file.path(paste0(context_path,"10_fgsea/inputs/gmt_database"))
gmt_file <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/inputs/gmt_database/c5.go.v2023.2.Hs.symbols.gmt"
# if output directory does not exist, create it
if (!dir.exists(output_dir)) {
  dir.create(paste0(output_dir))
}
# Function: Read files to list -------------------------
read_files_to_list <- function(directory_path) {
  # List all files in the directory
  file_list <- list.files(path = directory_path, full.names = TRUE)
  
  
  return(file_list)
}

# Function: Adjacency matrix to list -------------------------
matrix_to_list <- function(pws){
  pws.l <- list()
  for (pw in colnames(pws)) {
    pws.l[[pw]] <- rownames(pws)[as.logical(pws[, pw])]
  }
  return(pws.l)
}

## Function: prepare_gmt --------------------------------------
prepare_gmt <- function(gmt_file, genes_in_data, savefile = FALSE){
  # for debug
  #file <- gmt_files[1]
  #genes_in_data <- df$gene_symbol
  
  # Read in gmt file
  gmt <- gmtPathways(gmt_file)
  hidden <- unique(unlist(gmt))
  
  # Convert gmt file to a matrix with the genes as rows and for each go annotation (columns) the values are 0 or 1
  mat <- matrix(NA, dimnames = list(hidden, names(gmt)),
                nrow = length(hidden), ncol = length(gmt))
  for (i in 1:dim(mat)[2]){
    mat[,i] <- as.numeric(hidden %in% gmt[[i]])
  }
  
  #Subset to the genes that are present in our data to avoid bias
  hidden1 <- intersect(genes_in_data, hidden)
  mat <- mat[hidden1, colnames(mat)[which(colSums(mat[hidden1,])>2)]] # filter for gene sets with more than 5 genes annotated
  # And get the list again
  final_list <- matrix_to_list(mat) # for this we use the function we previously defined
  if(savefile){
    saveRDS(final_list, file = paste0(gsub('.gmt', '', gmt_file), '_subset_', format(Sys.time(), '%d%m'), '.RData'))
  }
  
  print('.gmt conversion successfull!:)')
  return(final_list)
}

## Function: run GSEA()
run_gsea <- function(df_filtered){
  
gmt_file <- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/inputs/gmt_database/c7.immunesigdb.v2023.2.Hs.symbols.gmt"
## 2. Read in data -----------------------------------------------------------
      my_genes <- df_filtered$gene
      bg_genes <- prepare_gmt(gmt_file, my_genes, savefile = FALSE)
      # print(bg_genes)

      ##3 . Ranking gesn -------------------------------------------------------------
      rankings <- sign(df_filtered$"log2.fold_change.")*(-log10(df_filtered$p_value)) # we will use the signed p values from spatial DGE as ranking
      names(rankings) <- df_filtered$gene

      rankings <- sort(rankings, decreasing = TRUE) # sort genes by ranking

      # Some genes have such low p values that the signed pval is +- inf, we need to change it to the maximum * constant to avoid problems with fgsea
      max_ranking <- max(rankings[is.finite(rankings)])
      min_ranking <- min(rankings[is.finite(rankings)])
      rankings <- replace(rankings, rankings > max_ranking, max_ranking * 10)
      rankings <- replace(rankings, rankings < min_ranking, min_ranking * 10)
      rankings <- sort(rankings, decreasing = TRUE) # sort genes by ranking

      ## 4. Run GSEA ---------------------------------------------------------------
      GSEAres <- fgsea(pathways = bg_genes, # List of gene sets to check
                      stats = rankings,
                      scoreType = 'std', # in this case we have both pos and neg rankings. if only pos or neg, set to 'pos', 'neg'
                      minSize = 10,
                      maxSize = 500,
                      nproc = 1) # for parallelisation

      print(GSEAres)
      return (GSEAres)
}


# Analysis ====================================================
# read the csv file
df <- read.csv(file.path(paste0(input_dir,file_name)), sep='\t', header=TRUE)
li_conditions = unique(df$condition)
li_cell_line = unique(df$cell_line)
print(li_cell_line)


for (cell_line in li_cell_line) {
  filtered_cell <- df[df$cell_line == cell_line, ]
  for (condition in li_conditions){
    
    
    df_filtered <- df[df$condition == condition & df$cell_line == cell_line,]
    Gsea_results <- run_gsea(df_filtered)
    head(Gsea_results)

    filename <- paste0(output_dir,db,"_",cell_line,"_",condition)
    # saveRDS(Gsea_results, file = paste0(filename, '_gsea_results.RDS'))
    data.table::fwrite(Gsea_results, file = paste0(filename, '_gsea_results.tsv'), sep = "\t", sep2 = c("", " ", ""))


  }
} 




