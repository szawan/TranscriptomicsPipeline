library(DOSE)
data(geneList)
de <- names(geneList)[abs(geneList) > 2]
edo <- enrichDGN(de)
print(head(edo))