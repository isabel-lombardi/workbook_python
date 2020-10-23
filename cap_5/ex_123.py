# Pig Latin Improved

def pig_latin(word):
    result = ""
    if word[0] in "aeiouAEIOU":
        result = word + "way"
        if word[-1] in "!?.,:;-":
            result = word[:-1] + "way" + word[-1]
    else:
        result = word[1:] + word[0] + "ay"
        if word[0].isupper():
            x = word[1:]
            result = x[0].upper() + x[1:] + word[0].lower() + "ay"
            if word[-1] in "!?.,:;-":
                result = x[0].upper() + word[1:-1] + word[0].lower() + "ay" + word[-1]
    return result


us_text = input("Enter a sentence you want to convert to pig latin: ")
print(' '.join(pig_latin(word) for word in us_text.split()))

pig_latin(us_text)
