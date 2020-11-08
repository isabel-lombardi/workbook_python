# Display the head of a file (first 10 lines)

import sys

num_lines = 10

if len(sys.argv) != 2:
    print("Enter the file name as a command line argument.")
    quit()

try:
    with open(sys.argv[1], "r") as file:
        line = file.readline()
        count = 0

        while count < num_lines and line != "":
            line = line.rstrip()
            count += 1
            print(line)
            line = file.readline()
except IOError:
    print("Something went wrong while accessing the file.")

