# Python code​​​​​​‌‌​​​​‌‌‌‌‌‌‌​​‌​‌‌​‌​‌‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import os

def file_info():
    # Your code goes here.

    target_dir = 'deps'
    directory = os.path.join(os.curdir, target_dir)
    extension = '.txt'

    total_size = 0

    for root, dir, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                total_size += os.path.getsize(os.path.join(root, file))

    return total_size