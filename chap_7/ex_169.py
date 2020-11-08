# Redacting Text in a File
base_name = input("-Enter the name of the text file to check and change: ")
sens_name = input("-Enter the file name with the sensitive words:")
try:
    with open(base_name, "r") as base_file:
        with open(sens_name, "r") as sens_file:
            sens_words = []
            line = sens_file.readline()
            while line != "":
                line = line.rstrip()
                sens_words.append(line)
                line = sens_file.readline()

    new_name = input("Enter the name for the new file that will be created: ")
    with open(new_name, "w") as new_file:
        line = base_file.readline()
        while line != "":
            for word in sens_words:
                line = line.replace(word, "*" * len(word))
            new_file.write(line)
            line = base_file.readline()

except FileNotFoundError:
    print("-" * 75)
    print("Error. One or more files were not found. Please try again")
