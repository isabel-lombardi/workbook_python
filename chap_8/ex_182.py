# Spelling with element Symbols
from re import split


def check_element(word, s, i=0, result=""):
    if word[i].capitalize() in s:
        result += word[i].capitalize()
        i += 1

        if i == len(word):
            return result
        else:
            return check_element(word, s, i, result)

    if i < len(word) - 1:
        if word[i].capitalize() + word[i + 1] in s:
            result += word[i].capitalize() + word[i + 1]
            i += 2

            if i == len(word):
                return result
            else:
                return check_element(word, s, i, result)
    else:
        return False


elements = open("elements.txt")
symb = []
elem = []


def main():
    for line in elements:
        line = line.replace("\n", "")
        line = split(",", line)

        symb.append(line[1])
        elem.append(line[2])

    us_word = input("Enter a word to  spelled using only element symbols: ")
    print()
    if check_element(us_word, symb):
        print("{} can be spelled as: ".format(us_word), check_element(us_word, symb))
    else:
        print("Your word can't be spelled using only element symbols")

    print("-" * 70)
    print("The element names that can be spelled using only element symbols are:")
    print()
    for e in range(len(elem)):
        if check_element(elem[e], symb):
            print("{} can be spelled as: ".format(elem[e]), check_element(elem[e], symb))
            print()


main()
