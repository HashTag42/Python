#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    filename = "textfile.txt"

    # Check for item existence and type
    print("Item exists:", str(path.exists(filename)))
    print("Item is a file:", path.isfile(filename))
    print("Item is a directory:", path.isdir(filename))

    # Work with file paths
    print("Item's path:", path.realpath(filename))
    print("Item's path and name:", path.split(path.realpath(filename)))

    # Get the modification time
    t = time.ctime(path.getmtime(filename))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime(filename)))

    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(filename))
    print("It has been", td, "since the file was modified")
    print("Or,", td.total_seconds(), "seconds")

if __name__ == "__main__":
    main()
