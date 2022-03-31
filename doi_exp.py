import argparse
import glob
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='Export DOIs from xml files')

parser.add_argument(
    "-f", "--files",
    type=str,
    nargs="+",
    help='enter target files')

args = parser.parse_args()

file_list = args.files

"""filenames = glob.glob("*.xml")  # change the pattern to match your case"""

for filename in file_list:

    with open(filename, 'r', encoding="utf-8") as content:

        tree = ET.parse(content)

        lst_dois = tree.findall('.//article-id')

        for doi in lst_dois:

            print (doi.text)