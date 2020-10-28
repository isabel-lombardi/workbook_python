# Checking for a Winning Card
from chap_6.ex_146 import *
from random import randrange


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


def main():
    print()
    print("〚〚〚 WELCOME TO ISABEL'S BINGO 〛〛〛 \n      The game works like this:  ")
    print()
    print("Horizontal line like: ")
    print("----------------------")
    horizontal_test = create_card()
    horizontal_test["B"][0] = "∎"
    horizontal_test["I"][0] = "∎"
    horizontal_test["N"][0] = "∎"
    horizontal_test["G"][0] = "∎"
    horizontal_test["O"][0] = "∎"
    print_dict_table(horizontal_test)

    print()
    print("Vertical line like: ")
    print("----------------------")
    vertical_test = create_card()
    vertical_test["I"][0] = "∎"
    vertical_test["I"][1] = "∎"
    vertical_test["I"][2] = "∎"
    vertical_test["I"][3] = "∎"
    vertical_test["I"][4] = "∎"
    print_dict_table(vertical_test)

    print()
    print("Diagonal line like: ")
    print("----------------------")
    diagonal_test = create_card()
    diagonal_test["B"][0] = "∎"
    diagonal_test["I"][1] = "∎"
    diagonal_test["N"][3] = "∎"
    diagonal_test["G"][4] = "∎"
    print_dict_table(diagonal_test)

    cards = create_card()
    print()
    print("►►► Now is your time! ◄◄◄")
    extraction = int(input("Select the number of extraction and you will be assigned a card: "))
    print()
    for r in range(extraction):
        generate_card(cards)

    print_dict_table(generate_card(cards))
    print()
    if check_win(cards):
        print("     You Win!    ")
    else:
        print("You Lose. Try again")
    print()


main()
