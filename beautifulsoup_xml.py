from bs4 import BeautifulSoup
import csv


def parse_non_strict_xml(xml_file):
    with open(xml_file, 'r') as file:
        xml_content = file.read()

    soup = BeautifulSoup(xml_content, 'xml')
    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(["CHIP","STANDARD_NAME", "SYSTEMATIC_NAME", "ORGANISM","CATEGORY_CODE","SUB_CATEGORY_CODE", "DESCRIPTION_BRIEF", "MEMBERS"])
        for geneset in soup.find_all('GENESET'):
            standard_name = geneset.get('STANDARD_NAME','')
            systematic_name = geneset.get('SYSTEMATIC_NAME','')
            organism = geneset.get('ORGANISM','')
            chip = geneset.get('CHIP','')
            category_code = geneset.get('CATEGORY_CODE','')
            sub_category_code = geneset.get('SUB_CATEGORY_CODE','')
            description_brief = geneset.get('DESCRIPTION_BRIEF', '')
            members = geneset.get('MEMBERS', '')
            member_symbolized = geneset.get('MEMBERS_SYMBOLIZED','')
            print(standard_name)
            csv_writer.writerow([chip, standard_name, systematic_name, organism, description_brief,  member_symbolized])

        
    

if __name__ == "__main__":
    xml_file = "/scratch/sah2p/datasets/2023_11_04_BurkeLab/output/10_fgsea/msigdb_v2023.xml"  # Replace with your actual XML file name
    parse_non_strict_xml(xml_file)
