import zipfile
import sys
import os

files = sys.argv
for file in files:
    with zipfile.ZipFile() as f:
        pass