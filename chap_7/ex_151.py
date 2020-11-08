# Concatenate Multiple Files
"""
For the exercise I used:
first file = file1.txt
second file = file2.txt
They are present in the folder
"""
import sys

if len(sys.argv) != 3:
    print("Enter the names of the 2 files as command line argument")
    quit()

try:
    file_names = [sys.argv[1], sys.argv[2]]
    with open("file3.txt", "w") as file:
        for names in file_names:
            with open(names, "r") as in_file:
                file.write(in_file.read())
            file.write("\n")

except IOError:
    print("Something went wrong while accessing the file.")
