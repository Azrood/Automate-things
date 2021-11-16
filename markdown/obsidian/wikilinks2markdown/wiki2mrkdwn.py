import re
import argparse
import os
import pathlib
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument("path", default=".", type=pathlib.Path)
args = parser.parse_args()


def map_files(path):
    files = [os.path.join(root, files) for root, dirs, files in os.walk(path)]
    return files

def convert_wikilinks(string):
    pattern = re.compile(r"(!?\[\[(.+)\]\])",re.MULTILINE)
    m = pattern.findall(string)
    for msg in m:
        wikilink, file_url = map(str.strip, msg)
        url_link = urllib.parse.quote(file_url.strip())
        string = string.replace(wikilink, f"[{file_url}]({url_link})")
    return string
