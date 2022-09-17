import sys
import os
import glob

# deleting all .srt files in a directory
s = '.srt'  # able to change into any existing file extensions

main_dir = r"C:\Users\Alex\Downloads\The Web Developer Bootcamp 2022"  # main directory

folders = os.listdir(main_dir)

for (dirname, dirs, files) in os.walk(main_dir):
    for file in files:
        if file.endswith(s):
            source_file = os.path.join(dirname, file)
            os.remove(source_file)
