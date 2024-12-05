#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

filename = "textfile.txt.bak"

def main():
    # make a duplicate of an existing file
    if path.exists(filename):
        # get the path to the file in the current directory
        src = path.realpath(filename)

        # let's make a backup copy by appending "bak" to the name
        # dst = src + ".bak"
        # shutil.copy(src,dst)

        # rename the original file
        # os.rename(filename, "newfile.txt")

        # now put things into a ZIP archive
        # root_dir, tail = path.split(src)
        # make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()
