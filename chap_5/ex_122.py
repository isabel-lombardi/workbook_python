# Pig Latin Improved

def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


us_text = input("Enter a sentence you want to convert to pig latin: ")
print(' '.join(pig_latin(word) for word in us_text.split()))

pig_latin(us_text)