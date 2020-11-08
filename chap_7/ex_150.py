# Display the Tail of a File (last 10 lines)

import sys

num_lines = 10

if len(sys.argv) != 2:
    print("Enter the file name as a command line argument.")
    quit()

try:
    with open(sys.argv[1], "r") as file:
        for line in (file.readlines()[-num_lines:]):
            print(line, end="")

except IOError:
    print("Something went wrong while accessing the file.")