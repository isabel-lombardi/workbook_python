# Number the Lines in a File
"""
For the exercise I used:
words.txt
it is present in the folder
"""


def numbered_lines(file1, file2):
    with open(file1, "r") as base_file:
        line = base_file.readlines()

    with open(file2, "w") as edit_file:
        for (number, line) in enumerate(line):
            edit_file.write("%d:  %s" % (number + 1,  line))


base_name = input("Enter the name of the file where you want to number the lines: ")
edit_name = input("Enter the name of the new file that will be created: ")
numbered_lines(base_name, edit_name)
