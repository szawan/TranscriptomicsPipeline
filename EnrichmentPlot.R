library(clusterProfiler)
library(enrichplot)
library(scales)

# Assuming `gseaResult` is your GSEA analysis result object

gseaResult <- read.delim("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/dataforplots/H3255_E07_vs_C36_Reactome.csv", header = TRUE, sep = ",", stringsAsFactors = FALSE)
# # Filter for negatively enriched pathways based on NES (Negative Enrichment Score)
# negativelyEnriched <- gseaResult[gseaResult$NES < 0, ]

# # Plot the enrichment result for a negatively enriched pathway
# # Adjust the index `1` to target the specific pathway of interest from your filtered result
# if(nrow(negativelyEnriched) > 0) {
#   enrichplot::gseaplot(gseaResult, geneSetID = rownames(negativelyEnriched)[1], title = negativelyEnriched$Description[1])
# } else {
#   print("No negatively enriched pathways found.")
# }
library(ggplot2)

# Filter for negatively enriched pathways

negativelyEnriched <- gseaResult[gseaResult$NES < 0, ]

# Basic plot of NES
pdf("EnrichmentMap.pdf", width=21, height=7)
ggplot(negativelyEnriched, aes(x = reorder( pathway,NES), y = NES)) +
geom_bar(stat = 'identity', fill = 'firebrick') +
scale_y_continuous(limits=c(-2,2)) +
coord_flip() +  # Flip coordinates for horizontal bars
labs(x = "Gene Set", y = "Normalized Enrichment Score (NES)", title = "Negatively Enriched Pathways") +
theme_minimal()

dev.off()
