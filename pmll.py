import csv
import xml.etree.ElementTree as ET

def parse_xml(xf):
    tree = ET.parse(xf)
    root = tree.getroot()


    # data_list = []

    # for geneset in root.findall('.//GENESET'):
    #     standard_name = geneset.get('STANDARD_NAME', '')
    #     systematic_name = geneset.get('SYSTEMATIC_NAME', '')
    #     organism = geneset.get('ORGANISM', '')
    #     description_brief = geneset.get('DESCRIPTION_BRIEF', '')
    #     members = geneset.get('MEMBERS', '')

    #     data_list.append([standard_name, systematic_name, organism, description_brief, members])

    # return data_list
def test_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for element in root:
        print(f"{element.tag}: {element.text}")

# if __name__ == "__main__":
    # xml_file = "your_file.xml"  # Replace with your actual XML file name
    # parse_xml(xml_file)
# def write_to_csv(data_list, csv_file):
#     with open(csv_file, 'w', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(['Standard_Name', 'Systematic_Name', 'Organism', 'Description_Brief', 'Members'])  # Add header row

#         for row in data_list:
#             csv_writer.writerow(row)

if __name__ == "__main__":
    
    # xml_file = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/msigdb_v2023.2.Hs.xml"
    # csv_file = "output.csv"

    # data_list = parse_xml(xml_file)
    # write_to_csv(data_list, csv_file)
    test_xml("/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/msigdb_v2023.xml")