from random import randrange
from cap_6.ex_146 import create_card, print_dict_table


def generate_card(card):
    choice = randrange(1, 75 + 1)
    for value in card.values():
        for i, e in enumerate(value):
            if e == choice:
                value[i] = "∎"
    return card


def check_win(card):
    win = False
    if card["B"][0] == "∎" and card["I"][1] == "∎" and card["N"][2] == "∎" and card["G"][3] == "∎" \
            and card["O"][4] == "∎":
        win = True
    elif card["O"][0] == "∎" and card["G"][1] == "∎" and card["N"][2] == "∎" and card["I"][3] == "∎" \
            and card["B"][4] == "∎":
        win = True
    elif card["B"][0] == "∎" and card["O"][4] == "∎" and card["B"][4] == "∎" and card["O"][0] == "∎":
        win = True
    for letter in card:
        if len(set(card[letter])) == 1:
            win = True
    for letter in card:
        for number in letter:
            i = 0
            if card[letter][i] == "∎":
                i += 1
            if i == 5:
                win = True
            break
    return win


def my_card(card):
    while True:
        generate_card(card)
        if check_win(card) is True:
            break
    return card


card = create_card()
print_dict_table(my_card(card))

