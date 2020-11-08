# Remove Comments

try:
    base_name = input("Enter the file name: ")
    base_file = open(base_name, "r")

except:
    print("Something went wrong while accessing the file.")
    quit()
try:
    edit_name = input("Enter the name of a output file: ")
    edit_file = open(edit_name, "w")

except:
    base_file.close()
    print("Something went wrong while accessing the output file")
    quit()
try:
    for line in base_file:
        symb = line.find("#")
        if symb > -1:
            line = line[0: symb]
            line += "\n"
        edit_file.write(line)
    base_file.close()
except:
    print("Something went wrong while accessing the files. ")
