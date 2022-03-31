import argparse
import glob
import xml.etree.ElementTree as ET

doi_dump = []

# Function 1: Search for DOI in target files
def search_doi(file_list):
 for filename in file_list:
        with open(filename, 'r', encoding="utf-8") as content:
            tree = ET.parse(content)
            lst_dois = tree.findall('.//article-id')
            for doi in lst_dois:
                doi_dump.append(doi.text)

if __name__ == "__main__":

    # Prase CLI argmuments
    parser = argparse.ArgumentParser(description='Export DOIs from xml files')

    parser.add_argument(
        "-f", "--files",
        type=str,
        nargs="+",
        help='enter target files')

    args = parser.parse_args()

    if args.files:
        file_list = args.files
        search_doi(file_list)
    else:
        file_list = glob.glob("*.xml")
        search_doi(file_list)

# Create output file
with open('chapter_dois.txt', 'w') as f:
    for i in doi_dump:
        f.write(i)
        f.write('\n')

# Terminal output
print("-------> DOIs extracted:")
for item in doi_dump:
    print(item)