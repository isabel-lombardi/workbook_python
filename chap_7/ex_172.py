# Words with Six Vowels in Order
file_name = input("Enter the name of the file to check: ")

with open(file_name, "r") as file:
    try:
        for lines in file:
            for word in lines:
                vowels = "aeiouy"
                accumulate = ""

                for ch in word.lower():
                    if ch in vowels:
                        accumulate += ch
                        if len(accumulate) == len(vowels):
                            print(accumulate == vowels)
    except IOError:
        print("Something went wrong while running the file")
        quit()
