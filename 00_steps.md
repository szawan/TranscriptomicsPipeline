# Annotation
1. mkdir annotation
2. download latest Host Genome (gff3) file
3. unzip using **gzip -d Slycopersicum_796_ITAG5.0.gene.gff3.gz**

# 0. Data preprocessing
00a_handle_multiplexing.py
00b_renaming_files.py
00c_get_folder_names.py

# 1. QC
01a_fastqc.py
01b_multiqc.py

# 2. Trim
02_trim.py

# 3. Hisat
1. Download the latest dna.toplevel.fa from ensembl
2. Navigate to directory and extract .gz **gzip Slycopersicum_796_ITAG5.0.fa.gz**
2. Run the 03a_hisat_build.py and get index file ".ht2" format
3. Finaly run 03b_hisat.py

03a_hisat_build.py
03b_hisat.py

# 4. Sorting
04_sorting.py

# 5. Cufflink
05_cufflink.py

# 6. FPKM Matrix
06a_fpkm_to_csv.py
06b_combine_fpkm.py
06c_transpose.py

# 7. PCA
07_pca.py

# 8. Cuffdiff
08_cuffdiff.py
