import argparse
import glob
import xml.etree.ElementTree as ET

doi_dump = []

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Export DOIs from xml files')

    parser.add_argument(
        "-f", "--files",
        type=str,
        nargs="+",
        help='enter target files')
    parser.add_argument(
        "-a", "--all",
        help='target all .xml files in current directory'
    )

    args = parser.parse_args()

    file_list = args.files

    """filenames = glob.glob("*.xml")  # change the pattern to match your case"""

    for filename in file_list:

        with open(filename, 'r', encoding="utf-8") as content:

            tree = ET.parse(content)

            lst_dois = tree.findall('.//article-id')

            for doi in lst_dois:

                doi_dump.append(doi.text)

with open('chapter_dois.txt', 'w') as f:
    for i in doi_dump:
        f.write(i)
        f.write('\n')

print("DOIs extracted: \n ------------------------------")
for item in doi_dump:
    print(item)