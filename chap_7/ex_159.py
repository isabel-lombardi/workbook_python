# Two Word Random Password
from random import randrange

words_file = "words.txt"
words = []
with open(words_file, "r") as file:
    for word in file:
        word = word.rstrip()
        if 3 <= len(word) <= 7:
            words.append(word)

first = words[randrange(0, len(words))].capitalize()
password = first
while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))].capitalize()
    password = first + second
print("The random password is: {}".format(password))
