# What’s that Element Again?
from re import split

while True:
    print("-" * 70)
    user_input = input("Enter the number of protons or the name or symbol of the element: ").lower()
    if user_input == "":
        break
    with open("elements.txt", "r") as file:
        elements = {}
        for line in file:
            line = line.replace("\n", "").lower()
            line = split(",", line)

            line[0] = int(line[0])  # transform number(str) into integer

            elements[line[0]] = line[1:]
    try:
        user_input = int(user_input)
        if user_input in elements.keys():
            # print(elements[user_input])
            print("The number of protons corresponds to", ' '.join(elements[user_input]))
        else:
            print("There is no element with {} protons numbers. Try again".format(user_input))

    except ValueError:
        for key, value in elements.items():
            if user_input in value:
                print("The symbol or name corresponds to {} proton number(s)".format(key))

"""     if user_input not in elements.values():
            print("This element does not exist. Try again")"""

"""
Problemi con le ultime due righe. Se viene inserito un nome o simbolo presente, 
stampa il corrispondente ma riporta subito sotto la stringa di errore. 
"""