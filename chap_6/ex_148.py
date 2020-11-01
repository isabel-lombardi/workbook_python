from random import randrange
from chap_6.ex_146 import create_card, print_dict_table


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


all_games = []
count = 0


def game(card):
    global count
    while check_win(card) is False:
        choice = randrange(1, 75 + 1)
        for value in card.values():
            for i, e in enumerate(value):
                if e == choice:
                    value[i] = "∎"
                    count += 1
    all_games.append(count)
    count = 0

    return card


def main():
    for gm in range(1000 + 1):
        print()
        actual_game = create_card()
        print_dict_table(game(actual_game))
        print("-" * 18)

    print("Out of 1000 games, the minimum, maximum and average number before you have a winning card is: \n"
          "Minimum: {}".format(min(all_games)),
          "\nMaximum: {}".format(max(all_games)),
          "\nAverage: {:.0f}".format(sum(all_games) / len(all_games)))


main()