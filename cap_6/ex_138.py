# Text Messaging
keypad = {
    '1': ["", '.', ',', '?', '!', ':'],
    '2': ["", 'A', 'B', ' C'],
    '3': ["", 'D', 'E', 'F'],
    '4': ["", 'G', 'H', 'I'],
    '5': ["", 'J', 'K', 'L'],
    '6': ["", 'M', 'N', 'O'],
    '7': ["", 'P', 'Q', 'R', 'S'],
    '8': ["", 'T', 'U', 'V'],
    '9': ["", 'W', 'X', 'Y', 'Z'],
    '0': ["", ' ']
}

text = list(input("Please input a text so I can show you how to type it on your phone: ").upper())
result = ""
for i in text:
    for k, v in keypad.items():
        if i in v:
            for a in range(v.index(i)):
                result += k

print("Result:   {}".format(result))
print("Expected: 4433555555666110966677755531111.")