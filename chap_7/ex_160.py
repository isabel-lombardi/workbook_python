from string import punctuation
# try with list comp

# follow the rule
ie = []
cei = []
# not follow the rule
ei = []
cie = []

# file = ("Twenty-Thousand-Leagues-Under-the-Sea-by-Jules-Verne.txt")
file = input("Enter the file name where you want to check whether or not the rule is respected: ")
with open(file, "r") as file:
    line = file.read()
    line = line.translate(str.maketrans('', '', punctuation)).lower()  # remove punct + all lower
    words = line.split()
    for i in range(len(words)):

        if "cie" in words[i]:
            if words[i] not in cie:
                cie.append(words[i])

        if "ie" in words[i]:
            if words[i] not in ie:
                if words[i] not in cie:
                    ie.append(words[i])

        if "cei" in words[i]:
            if words[i] not in cei:
                cei.append(words[i])

        if "ei" in words[i]:
            if words[i] not in ei:
                if words[i] not in cei:
                    ei.append(words[i])


print()
print("The following lists follow the rule “I before E except after C” :")
print("Words with 'ie' ", ie)
print("Words with 'cei'", cei)
print("-" * 160)
print("The following lists do not follow the rule:")
print("Words with 'cie' ", cie)
print("Words with 'ei' ", ei)
print("-" * 160)
percentage = (len(ie) + len(cei)) / len(words) * 100
print("The {:.2f}% of words follow the rule".format(percentage))
