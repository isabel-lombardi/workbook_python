# Shuffling a Deck of Cards
from random import randrange


def createDeck():
    cards = []
    for suit in ["♥", "♠", "♣", "♦"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
            cards.append(value + suit)
    return cards


def shuffle(cards):
    for i in range(0, len(cards)):
        pos = randrange(i, len(cards))
        temp = cards[i]
        cards[i] = cards[pos]
        cards[pos] = temp


def main():
    cards = createDeck()
    print("The original deck of cards is: ")
    print(cards)
    print()
    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)


if __name__ == "__main__":
    main()
