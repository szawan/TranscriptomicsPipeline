# if (!require("BiocManager", quietly = TRUE))
#     install.packages("BiocManager",repos = "https://cran.r-project.org")

# BiocManager::install("GENIE3")

library(GENIE3)
set.seed(123) 

############### FILE PATHS ###########################
context_path<- "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_dir <- file.path(paste0(context_path, "06_fpkm_csv/"))
output_dir <- file.path(paste0(context_path, "TF_identification/Genie3/"))

exp_file = paste0(input_dir,"combined_data.csv")
reg = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/TF_identification/all_li_transciption_factors.csv"


# 0. Create output directory if it doesn't exist ######
if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}

# 1. Reading data ######################################
# Expression Matrix (fpkm)
df_exp_data <- read.csv(exp_file, header=TRUE, row.names = 1)

# Regulators 
df_regulators <- read.csv(reg, header =TRUE)

li_regulators <- list(df_regulators)
remove_regulators <- c(
  "ARNTL2","MYCL1", "ARNTL",
  "KIAA2018", "SCXB", "SCXA", 
  "LOC388553","C13orf38-SOHLH2","CSDA",
  "FOXD4L2", "KIAA0415", "WHSC1", "LASS4", 
  "LASS5", "LASS2", "LASS3", "LASS6", "CCDC79",
  "C11orf9", "LOC729991-MEF2B", "T", "PRKRIR",
   "ZNF295", "ZNF238", "ZFP161", "C11orf95", "ZFP112",
   "ZNF193", "ZNF434", "ZNF322A", "HKR1", "ZNF643", "ZNF642", 
   "ZNF322B", "ZNF167", "ZNF498", "LOC100287841", "ZNF192", 
   "LOC100131539", "LOC100132396", "ZNF323", "MYST2", "C16orf5")

filtered_regulators <- df_regulators[!(df_regulators$TF %in% remove_regulators),]
print(filtered_regulators)
# li_regulators <- c("IRF2","E2F1","STAT5B","GTF3A","STAT3", 
# "ATF5","DLX2","IRF7","LHX3","ZNF436","PAX2",
# "TFAM","GATA6","LEF1", "TCF4", "IRF1","STAT5A",
#  "GATA1","POU3F2","CEBPA","STAT6","FOXR2", 
#  "YY1", "RFX7","ZNF101","NFXL1","SIX1", "CIC", "MYBL1", "MAF", 
#  "TERF1","ZNF16", "PAX4", "SP1", "NR1I2", "PIAS4", "MSX1", 
#    "HSF1", "ZNF433", "SRF", "DMRT1", "ELK1", "NR1H4")
#  print(li_regulators)

# df_exp_data <- df_exp_data[df_exp_data$gene_id %in% li_regulators,]
# print(df_exp_data)
########### checking for one cell line
conditions = list(
A549_C36 = c("A549_C36_1", "A549_C36_2", "A549_C36_3"),
A549_E07 = c("A549_E07_1", "A549_E07_2", "A549_E07_3"),
A549_Veh = c("A549_Veh_1", "A549_Veh_2", "A549_Veh_3"), 
H3255_C36 = c("H3255_C36_1", "H3255_C36_2", "H3255_C36_3"),
H3255_E07 = c("H3255_E07_1", "H3255_E07_2", "H3255_E07_3"),
H3255_Veh = c("H3255_Veh_1", "H3255_Veh_2", "H3255_Veh_3"),
H1975_C36 = c("H1975_C36_1", "H1975_C36_2", "H1975_C36_3"),
H1975_E07 = c("H1975_E07_1", "H1975_E07_2", "H1975_E07_3"),
H1975_Veh = c("H1975_Veh_1", "H1975_Veh_2", "H1975_Veh_3"),
H820_C36 = c("H820_C36_1", "H820_C36_2", "H820_C36_3"),
H820_E07 = c("H820_E07_1", "H820_E07_2", "H820_E07_3"),
H820_Veh = c("H820_Veh_1", "H820_Veh_2", "H820_Veh_3")
)

# Define a function to run GENIE3, get link list, and write to file
run_genie3 <- function(exprMatr, condition_name, regulators) {
  # Run GENIE3
  top_count <- 5000
  weightMat <- GENIE3(exprMatr, regulators = regulators) 
  # Get the link list
  linkList <- getLinkList(weightMat, reportMax = top_count)
  print(linkList)
  
  # Write link list to file
  write.csv(linkList, file = paste0(output_dir, condition_name, "_linkList.csv"))
}

for (condition_name in names(conditions)) {
  exprMatr <- as.matrix(df_exp_data[, conditions[[condition_name]]])
  run_genie3(exprMatr, condition_name, filtered_regulators)
}
