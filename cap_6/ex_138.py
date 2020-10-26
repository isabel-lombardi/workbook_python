# Text Messaging
keypad = {
    "1": ["", ".", ",", "?", "!", ":"],
    "2": ["", "A", "B", "C"],
    "3": ["", "D", "E", "F"],
    "4": ["", "G", "H", "I"],
    "5": ["", "J", "K", "L"],
    "6": ["", "M", "N", "O"],
    "7": ["", "P", "Q", "R", "S"],
    "8": ["", "T", "U", "V"],
    "9": ["", "W", "X", "Y", "Z"],
    "0": ["", " "]
}

text = input("Enter a text so i show you how to type it on your phone: ").upper()
result = ""
for letter in text:
    for key, value in keypad.items():
        if letter in value:
            for a in range(value.index(letter)):
                result += key

print("Result: {}".format(result))