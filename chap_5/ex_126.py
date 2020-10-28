# Dealing Hands of Cards
from chap_5.ex_125 import *


def deal(players, num_cards, deck):

    hands = [[] for players in range(players)]
    for c in range(num_cards):
        for hand in hands:
            hand.append(deck.pop(0))

    return hands


def main():
    deck = createDeck()
    shuffle(deck)
    print("Cards for each hand dealt:")
    print(deal(4, 5, deck))
    print()
    print("Cards remaining:")
    print(deck)


main()



