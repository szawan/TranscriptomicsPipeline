from gprofiler import GProfiler
import pandas as pd
import os

# SET PATHS
context_path = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/"
input_directory = context_path+"9_DEG_new_v2/DEG_Summary/"
output_directory = context_path+"11-GProfiler/"
file_name = "01_2FC_greaterthan_0.5_DEGenesList.csv"
organism = "hsapiens"
user_threshold = 1
prefix = 'p_val_1'


# if output directory does not exist, create it
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# read the csv file
df = pd.read_csv(input_directory + file_name, sep='\t', header=0)
print(df.head())

# # loop to extract columns one by one and save them as a list (first value is experiment name)
# for column in df.columns:
#     # take out column name and save it as a variable
#     experiment_name = column
#     print(experiment_name)

#     # convert the column to a list
#     gene_list = df[column].values.tolist()

#     # remove nan values
#     gene_list = [x for x in gene_list if str(x) != 'nan']

#     # remove gene: from the gene names (as gprofiler does not recognize it)
#     gene_list = [x.replace('gene-','') for x in gene_list]

#     # print the length of the gene list
#     print(len(gene_list))


#     gp = GProfiler(return_dataframe=True)
#     results = gp.profile(organism=organism, user_threshold = user_threshold, no_evidences=False,
#                          query = gene_list)

    # write the results to a csv file
    # results.to_csv(output_directory + experiment_name + '_gprofiler_'+prefix+'.csv', sep='\t', index=False)

    # result to excel file
    # results.to_excel(output_directory + experiment_name + '_gprofiler_'+prefix+'.xlsx')

gene_list = ['ABHD4', 'ACE', 'ACKR3', 'ACOX2', 'ACP5', 'ACSF2', 'ADA', 'ADGRV1', 'AEN', 'AGT', 'AHNAK2', 'AKR1B10', 'AKR1C1', 'AKR1C3', 'AMOTL1', 'AMZ2P1', 'ANGPTL4', 'ANKLE1', 'APCDD1L', 'APOBR', 'AQP1', 'AQP11', 'ARHGAP22', 'ARHGAP30', 'ARHGAP31', 'ASF1B', 'ATP1A2', 'C11orf24', 'C1S', 'C1orf21', 'C3', 'C4B', 'C5AR1', 'CA9', 'CACNA1H', 'CARF', 'CCN5', 'CCNF', 'CD177', 'CDC20P1', 'CDC25A', 'CDC6', 'CDC7', 'CDCA7L', 'CDH11', 'CDH5', 'CDKN3', 'CHI3L2', 'CHRNB4', 'CLDN2', 'COL12A1', 'COL13A1', 'COL1A1', 'COL1A2', 'COL26A1', 'CPE', 'CREB3L3', 'CREB5', 'CRIP1', 'CSDC2', 'CSPG4', 'CT45A2', 'CYP27A1', 'CYP4F12', 'DAXX-5', 'DCAF11', 'DCAF15-2', 'DCP1B', 'DDO', 'DGKG', 'DIO2', 'DKC1', 'DNAJC27-AS1', 'DNMBP', 'DTL', 'DUSP2', 'DUSP7', 'E2F1', 'EBNA1BP2', 'EFNB2', 'EMP1', 'ERCC6L', 'EXO1', 'FAM111B', 'FAT2', 'FBXO2', 'FEN1', 'FPR1', 'FYB1', 'G0S2', 'GABRB3', 'GASK1B', 'GBP2', 'GLP2R', 'GPATCH4-2', 'GPR132', 'GPR173', 'GRIN2A', 'GTF2IP1', 'H2AC11', 'H2AC13', 'H2AC8', 'H2BC11', 'H3C10', 'HAUS8', 'HCAR2', 'HDAC5', 'HIKESHIP2', 'HLA-B', 'HNRNPH1', 'HOGA1', 'HPCAL1', 'HS3ST1', 'HSP90AA3P', 'HTR3A', 'IFITM10', 'IFITM10-2', 'IFRD2', 'IGFBP4', 'IGFBP5', 'IGFL2-AS1', 'IGSF9B', 'IL11', 'IL17REL', 'IL2RB', 'IL7R', 'INSL3', 'IQCN', 'IRX3', 'ITGA6', 'JAK3', 'JAKMIP1', 'KANK2', 'KBTBD4-2', 'KCNB1', 'KCNE4', 'KCTD12', 'KIF18A', 'KLHDC8B', 'LAMB1', 'LINC00324', 'LINC00973', 'LINC02298', 'LINC02577', 'LLGL2', 'LMO1', 'LOC105369370', 'LOC105371912', 'LOC105372310', 'LOC105372773', 'LOC105374715', 'LOC105375221', 'LOC105375222', 'LOC105379549', 'LOC124900275', 'LOC124902871', 'LOC124905557', 'LOC124907946', 'LOC728688', 'LRG1', 'LSM10', 'MAML1-2', 'MAMLD1', 'MANCR', 'MAOB', 'MAPK8IP2', 'MARCHF4', 'MCHR1', 'MCM10', 'MCM3', 'MCM4', 'MED10-2', 'MED16-2', 'METTL9-2', 'MGP', 'MIR222HG', 'MLXIP-2', 'MORC4', 'MSX1', 'MTX1-2', 'MYBBP1A', 'MYLK', 'MYO15B', 'NDRG4', 'NFE2', 'NIM1K', 'NNMT', 'NOL4L', 'NOX5', 'NPAS2', 'NRARP', 'NRG1', 'NT5E', 'NUPR1', 'OLFML3', 'PAK1IP1-2', 'PDGFRB', 'PFAS', 'PFDN2', 'PLA2G6', 'PLEKHG4', 'PODXL', 'POLR3G', 'PPL', 'PRRT3', 'PRSS8', 'PRUNE2', 'PSG3', 'PSG4', 'PSMG1', 'PTX3', 'PXK', 'RAB17', 'RAB26', 'RASSF10', 'RGS4', 'RHOBTB3', 'RND1', 'RNF187', 'RPS2', 'SALL2', 'SCARA5', 'SCG2', 'SCGB2A1', 'SDC3', 'SERPINB3', 'SERPINB4', 'SESN3', 'SFTA1P', 'SH2B3', 'SH2D2A', 'SLC16A5', 'SLC25A18', 'SLC25A19', 'SLC25A24', 'SLC43A3', 'SLC7A8', 'SLC9A9', 'SLPI', 'SMTN', 'SNHG1', 'SPC25-2', 'SPDL1', 'SSC5D', 'STING1-2', 'STON2', 'STYXL2', 'SYNPO2', 'SYT5', 'TEP1', 'TFEB', 'TGM2', 'TIMP2', 'TIMP4', 'TMEM100', 'TMEM158', 'TMEM37', 'TMEM63C', 'TMEM86A', 'TMT1A', 'TNFRSF14', 'TNFRSF6B', 'TNFSF10', 'TOX2', 'TRPM2', 'TRPV2', 'TSHZ2', 'TUBAP13', 'TUBB2A', 'TUBGCP5-3', 'UBA2', 'UBA7', 'UCA1', 'UHRF1', 'UTP11', 'VTN', 'WDR31', 'WDR76', 'XDH', 'XRCC2', 'YBX2', 'ZBTB20', 'ZFP2', 'ZGRF1', 'ZNF367', 'ZNF467', 'ZNF558-2', 'ZNF579', 'ZNF676', 'ZSCAN31', 'FLOT1-4', 'NEURL4-2', 'RPS6KA1-2', 'SAMD9L', 'SMDT1-2', 'ABCG2', 'ABR', 'ACCS', 'ACTR3B', 'ACY3', 'ADAMTS7', 'ADGRB2', 'ADGRF1', 'AFAP1L2', 'AGPAT5-2', 'AHR', 'ANAPC7', 'ANK3', 'ANXA9', 'APOL3', 'APOLD1', 'ARHGAP24', 'ATAD3A', 'ATF6B-2', 'ATOSA', 'ATP8B1', 'ATP9A', 'BEND3', 'BOLA2-SMG1P6', 'BTG1', 'C19orf48P', 'C1QTNF1', 'C2CD2L', 'C4A', 'C4orf19', 'CACNG8', 'CALCR', 'CAMKK1', 'CAPN5', 'CASP10', 'CCDC124', 'CCDC3', 'CCDC80', 'CCN3', 'CD59', 'CD70', 'CD79A', 'CDCP1', 'CDH15', 'CDH18', 'CDK15', 'CEACAM6', 'CENPP', 'CFAP206', 'CFI', 'CGNL1', 'CIMAP3', 'CLDN11', 'CLN5', 'CNN1', 'CNTNAP1', 'CRABP2', 'CRISPLD2', 'CRLF1', 'CSF2', 'CT45A3', 'CTDP1-2', 'CTHRC1', 'CTSB', 'CYP24A1', 'CYP2T1P', 'DAXX', 'DBF4B', 'DBH-AS1', 'DCTPP1', 'DCUN1D5', 'DENND2D', 'DES', 'DHRS4L1', 'DHRS9', 'DKFZP586I1420', 'DNAH2', 'DNAJA4', 'DPH2', 'E2F8', 'ECEL1P2', 'EDIL3', 'EEF1A1P16', 'EEF1A1P29', 'EEF1AKMT4', 'ELF3', 'EPCAM-DT', 'EPN3', 'ERCC6', 'ERP27', 'ESPN', 'EVI2A-2', 'EXOC3L4', 'EXOG', 'EXPH5', 'F8A2', 'FAM171B', 'FKBPL-3', 'FRK', 'FTH1', 'FUS', 'GAL3ST4', 'GATM', 'GEMIN5', 'GGT8P', 'GIMAP2', 'GLDN', 'GMCL2', 'GMNN', 'GOLGA2P10-2', 'GPC4', 'GPR162', 'GTF2I', 'H2AC17', 'H2BC12', 'H2BC8', 'HASPIN', 'HBP1', 'HCAR1', 'HCN2', 'HECW2', 'HLA-A-3', 'HLA-B-5', 'HLA-C-7', 'HLA-DMA-4', 'HLA-DQB1', 'HLA-DRA-8', 'HPGD', 'HPSE', 'HS6ST1P1', 'HSD17B7', 'HSP90AB2P', 'HSPA8P1', 'HSPB1', 'ICAM3', 'IFI27L2', 'IKZF2', 'ILF3', 'IMPDH1P3', 'IPO4', 'KLF9', 'KRBA2', 'KRI1', 'KRT18P38', 'LAMA5', 'LGALS12', 'LHX1-DT', 'LIMA1', 'LIMCH1', 'LINC00842', 'LINC01460', 'LINC01504', 'LINC01770', 'LINC01778', 'LINC01825', 'LINC02035', 'LINC02693', 'LINC02861', 'LINP1', 'LOC100996660', 'LOC101928505', 'LOC101929638', 'LOC102723834', 'LOC102724428', 'LOC105369325', 'LOC105370092', 'LOC105370462', 'LOC105371114', 'LOC105372338', 'LOC105375321', 'LOC105376369', 'LOC112267932', 'LOC124900605', 'LOC124901456', 'LOC124901789', 'LOC124904632', 'LOC124905103', 'LOC389831', 'LOC645405', 'LOC728392', 'LOC728743', 'LOC729973', 'LOC84214', 'LONRF1', 'LOXL4', 'LRRC10B', 'LYNX1', 'LYPD1', 'LYPD3', 'MAP7D2', 'MAST1', 'MCAM', 'MCM2', 'MCTP2', 'MDK', 'MEGF6', 'MINDY1', 'MINDY4', 'MKX', 'MLLT6-2', 'MLXIPL', 'MON1A', 'MOSPD1', 'MRPL52', 'MRPS12-2', 'MUC1', 'MYC', 'MYH16', 'NABP1', 'NAV3', 'NFYB', 'NICOL1', 'NLGN2-2', 'NOL8-2', 'NPM1P46', 'NRGN', 'OLFML2B', 'ORAI1-2', 'PCK2', 'PDE4DIP', 'PDE5A', 'PDGFD', 'PGRMC2', 'PHLDA3', 'PIF1', 'PIK3R3', 'PIM2-2', 'PLEKHA7', 'PLIN5', 'POLD3', 'POLRMTP1', 'PPM1H', 'PROS1', 'PRR36', 'PSTPIP2', 'PTGS1', 'PTMAP4', 'RAB11FIP4', 'RAB30', 'RAB3D', 'RAD17', 'RAD51', 'RARRES1', 'RASD2', 'RBFOX2-2', 'REL', 'RGS7', 'RIMBP3', 'RNF227', 'RPIA', 'RPL41P1', 'RPL4P3', 'RPL7P47', 'RPS15P5', 'RPS26P10', 'RPS27P17', 'RTL5', 'RUNX3-AS1', 'S1PR1', 'SASH1', 'SCN1B', 'SCN4B', 'SDHAP1', 'SEMA5B', 'SERBP1P6', 'SERPINA5', 'SESN2-2', 'SHOC1', 'SLC17A9', 'SLC27A2', 'SLC28A1', 'SLC2A5', 'SLC34A2', 'SLC39A4-2', 'SLC4A4', 'SMG1P7', 'SMIM10', 'SMIM10L2A', 'SNAR-B1', 'SNHG15', 'SNHG17', 'SORBS1', 'SORT1', 'SOWAHB', 'SOX18', 'SPC25', 'SPMIP1', 'SPP1', 'SPRY1', 'SRGAP3', 'SRGN', 'SRSF4', 'SSBP2', 'ST8SIA1', 'STEAP4', 'SUMO2P21', 'TACSTD2', 'TBC1D8B', 'TENM2', 'TENT4A', 'TINCR', 'TJAP1', 'TLE2', 'TMEM138', 'TMEM163', 'TNFRSF18', 'TP63', 'TPBG-2', 'TPD52L1', 'TRAPPC12-2', 'TRIM2', 'TRIM55', 'TRPS1', 'TSPAN33', 'TTC3P1', 'TUBE1', 'UBE2G2', 'UBL3', 'UNC93A', 'USP36', 'VAV3', 'VIPR1', 'VPS13C', 'VWA1', 'VWA5A', 'WASH8P', 'WDR62', 'XKR3', 'YEATS4', 'ZMYND19', 'ZNF235', 'ZNF620', 'ZNF713', 'ZNF726', 'ZNF85-2']

gp = GProfiler(return_dataframe=True)
results = gp.profile(organism=organism, user_threshold = user_threshold, no_evidences=False,
                         query = gene_list)

results.to_excel(output_directory + "H1975_unique" + '_gprofiler_'+prefix+'.xlsx')



    
