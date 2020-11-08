# Find the Longest Word in a File

def longest_words(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        n = 0
        words_l = []
        for word in lines:
            if len(word) > n:
                words_l = [word]
                n = len(word)
            elif len(word) == n:
                words_l.append(word)
        print(words_l)


longest_words("words.txt")
