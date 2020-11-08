from string import punctuation
# try with list comp

follow = []
not_follow = []


# file = ("Twenty-Thousand-Leagues-Under-the-Sea-by-Jules-Verne.txt")
file = input("Enter the file name where you want to check whether or not the rule is respected: ")
with open(file, "r") as file:
    line = file.read()
    line = line.translate(str.maketrans('', '', punctuation)).lower()  # remove punct + all lower
    words = line.split()
    for i in range(len(words)):

        if "cie" in words[i]:
            if words[i] not in not_follow:
                not_follow.append(words[i])

        if "ie" in words[i]:
            if words[i] not in follow:
                if words[i] not in not_follow:
                    follow.append(words[i])

        if "cei" in words[i]:
            if words[i] not in follow:
                follow.append(words[i])

        if "ei" in words[i]:
            if words[i] not in not_follow:
                if words[i] not in follow:
                    not_follow.append(words[i])


print("The words that follow the rule are:\n", follow)
print("-" * 160)
print("The words that do not follow the rule are:\n", not_follow)
print("-" * 160)
percentage = len(follow) / len(words) * 100
print("The {:.2f}% of words follow the rule".format(percentage))