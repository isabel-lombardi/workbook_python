# Element Sequences
from re import split


def sequence(start, words):
    if start == "":
        return []
    best_seq = []
    last_letter = start[len(start) - 1].lower()
    for i in range(0, len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            current_seq = sequence(words[i], words[0: i] + words[i + 1: len(words)])
            if len(current_seq) > len(best_seq):
                best_seq = current_seq
    return [start] + best_seq


def elem_names():
    elements = open("elements.txt")
    names = []
    for line in elements:
        line = line.replace("\n", "")
        line = split(",", line)
        names.append(line[2])
    elements.close()
    return names


def main():
    names = elem_names()
    start = input("Enter the name of an element: ").capitalize()
    print("-" * 50)
    if start not in names:
        print("That wasn’t a valid element name")
    else:
        names.remove(start)
        seq = sequence(start, names)
        print("A longest sequence that starts with {} is:".format(start))
        for element in seq:
            print(" ", element)
        print("-" * 50)
        print("The length of the sequence is: {}".format(len(seq)))


main()
