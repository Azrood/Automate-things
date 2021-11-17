#!/usr/bin/env python3
import re
import argparse
import os
import pathlib
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("path", default=".",nargs="?" ,type=pathlib.Path, help="Path of the folder where the attachments are.")
parser.add_argument("file", nargs="+", help="The file whose wikilinks you want to convert.")
args = parser.parse_args()
# TODO : option to input multiple files
# TODO : "--all" to convert all ASCII readable files' wikilinks
def map_files(path):
    """
    Search files recursively and builds an array with their paths joined
    Example:

    ```
    docs/
    └── doc1.odt
    pics/
    todo.txt
    ```

    The function will return :
    ["./docs/doc1.odt", "./todo.txt"]
    """
    f=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            f.append(os.path.join(root, file))
    return f

def get_path(filename):
    """ Search the files array and get the path of the file provided in argument"""
    for file in files:
        if filename == os.path.basename(file):
            return file
    return filename


def convert_wikilinks(string):
    pattern = re.compile(r"(\[\[(.+)\]\])",re.MULTILINE)
    m = pattern.findall(string)
    for msg in m:
        wikilink, file_url = map(str.strip, msg)
        file_url =  os.path.relpath(get_path(file_url), start=args.path)
        url_link = urllib.parse.quote(file_url)
        string = string.replace(wikilink, f"[{os.path.basename(file_url)}]({url_link})")
    return string

if __name__ == "__main__":
    print(f"Reading directories recursively from : {args.path} ")
    files = map_files(args.path)
    print("Done...")
    print("Reading the file to convert wikilinks...")
    with open(args.file, "r") as file:
        content = file.read()
    print("Converting wikilinks to markdown links...")
    converted_content = convert_wikilinks(content)
    print("Writing the file with converted links...")
    with open(args.file, "w") as file:
        file.write(converted_content)
    print("Done !")
    
    