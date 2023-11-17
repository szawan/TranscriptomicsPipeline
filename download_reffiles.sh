#!/bin/bash

#  wget https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.toplevel.fa.gz

#  wget https://ftp.ensembl.org/pub/release-110/gff3/homo_sapiens/Homo_sapiens.GRCh38.110.gff3.gz

#  awk 'NF > 1{ a[$1] = a[$1]"\t"$2} END {for( I in a ) print I a[i]}' /scratch/sah2p/datasets/2023_11_04_BurkeLab/output/7_htseq_result/files/*.txt > merged.htseq

#!/bin/bash
FILES=$(ls -t -v /scratch/sah2p/datasets/2023_11_04_BurkeLab/output/7_htseq_result/files/*.txt | tr '\n' ' ');
awk 'NF > 1{ a[$1] = a[$1]"\t"$2} END {for( I in a ) print I a[i]}' $FILES > merged.tmp
