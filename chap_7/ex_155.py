# Words that Occur Most
from string import digits, punctuation
from operator import itemgetter  # *

file_name = input("Enter the name of the file you want to count words from: ")
words = dict()

try:
    with open(file_name, "r") as file:
        for line in file:
            for word in line.split():
                word = word.replace(" ", "")
                word = word.translate(str.maketrans("", "", punctuation)).lower()
                word = word.translate(str.maketrans("", "", digits))

                words[word] = words.get(word, 0) + 1
    print(sorted(words.items(), key=itemgetter(1), reverse=True))

except IOError:
    print("Something went wrong while accessing the file.")

