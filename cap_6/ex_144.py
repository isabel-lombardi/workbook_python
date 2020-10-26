# Anagrams

def anagrams(s):
    counts = {}
    for ch in s:
        if ch in counts != "!?,.:":
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
    return counts


def main():
    s1 = input("Enter the first string: ").lower().replace(" ", "")
    s2 = input("Enter the second string: ").lower().replace(" ", "")

    counts1 = anagrams(s1)
    counts2 = anagrams(s2)
    if counts1 == counts2:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


main()