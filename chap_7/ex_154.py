# Letter Frequencies
import sys
from string import punctuation
from operator import itemgetter   # *


if len(sys.argv) != 2:
    print("Enter the file name as a command line argument.")
    quit()

try:
    letters = dict()
    with open(sys.argv[1], "r") as file:
        for lines in file:
            lines = lines.replace(" ", "")
            lines = lines.replace("\n", "")
            lines = lines.translate(str.maketrans("", "", punctuation)).lower()
            for word in lines:
                for letter in word:
                    letters[letter] = letters.get(letter, 0) + 1
        print(sorted(letters.items(), key=itemgetter(1), reverse=True))

except IOError:
    print("Something went wrong while accessing the file.")