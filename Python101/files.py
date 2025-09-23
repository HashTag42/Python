'''
    files.py
    --------
    Illustrates file manipulation.
'''

import tempfile
import os

# Create a temporary file
with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
    print("Temporary file path: ", temp_file.name)

# Write to the file
with open(temp_file.name, 'w') as file:
    file.write("Hello from temp file!")

# Read back the contents
with open(temp_file.name, 'r') as file:
    print("File contents: ", file.read())

# Clean up manually if needed
os.remove(temp_file.name)
