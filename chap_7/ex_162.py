# A Book with No E...
from string import ascii_uppercase

file_name = input("Enter the name of the file you want to check: ")
with open(file_name, "r") as file:
    dict_words = {}
    for ch in ascii_uppercase:
        dict_words[ch] = 0
    num_words = 0
    for word in file:
        word = word.upper().rstrip()
        unique = []
        for ch in word:
            if ch not in unique and "A" <= ch <= "Z":
                unique.append(ch)
        for ch in unique:
            dict_words[ch] = dict_words[ch] + 1
        num_words += 1
smallest_count = min(dict_words.values())
for ch in sorted(dict_words):
    if dict_words[ch] == smallest_count:
        smallest_letter = ch
    percentage = dict_words[ch] / num_words * 100
    print("{} occurs in {:.2f}% of words".format(ch, percentage))

print()
print("The letter that is easiest to avoid is", smallest_letter)