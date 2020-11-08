# Consistent Line Lengths
"""
Il programma funziona corettamente tranne per i vari paragrafi
Con lo split ogni parola presente viene messa nella lista e vengono
omessi i vari spazi.
"""


text = open("Alice’s_Adventures_in_Wonderland.txt", "r").read()
max_length = 50

text = text.split()
edit = [""]
i = 0
for word in text:
    line = edit[i] + " " + word
    if edit[i] == "":
        line = word
    if len(word) > max_length:
        while len(word) > max_length:
            print(word[:max_length])
            i += 1
            word = word[max_length:]
        i += 1
        edit.append(word)
    elif len(line) > max_length:
        edit.append(word)
        i += 1
    else:
        edit[i] = line

print("\n".join(edit))
