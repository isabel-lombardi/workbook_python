# Play Bingo

from random import shuffle
from cap_6.ex_146 import *
#from cap_6.ex_147 import check_win


def generate_card(card):
    numbers = [n for n in range(1, 75 + 1)]
    shuffle(numbers)

    ext = []
    for number in numbers:
        for value in card.values():
            for i, e in enumerate(value):
                if e == number:
                    value[i] = "∎"
                    ext.append(number)
    print(ext)





    """def generate_card(card):
    choice = randrange(1, 75 + 1)
    for value in card.values():
        for i, e in enumerate(value):
            if e == choice:
                value[i] = "∎"
    return card"""

    return card


card = create_card()
print_dict_table(generate_card(card))