# Spell Checker
import sys
from string import digits, punctuation

print("Enter on the command line the name of the file you want to check the spelling for:")
if len(sys.argv) != 2:
    print("Enter the file name as a command line argument.")
    quit()
try:
    user_file = open(sys.argv[1], "r")

except IOError:
    print("File opening error, please try again.")

words_file = "words.txt"
valid_words = {}
with open(words_file, "r") as words_file:
    for word in words_file:
        word = word.lower().rstrip()
        valid_words[word] = None  # or 0

wrong = []
for line in user_file:
    line = line.translate(str.maketrans('', '', digits))
    line = line.translate(str.maketrans('', '', punctuation)).lower()
    for word in line.split():
        if word not in valid_words and word not in wrong:
            wrong.append(word)
user_file.close()

if len(wrong) == 0:
    print("No words were misspelled.")
else:
    print("The following words are misspelled:")
for word in wrong:
    print(" ", word)
