from random import randrange


def create_card():
    card = {}
    lower = 1
    upper = 1 + 15
    for letter in ["B", "I", "N", "G", "O"]:
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
            if next_num not in card[letter]:
                card[letter].append(next_num)
        lower += 15
        upper += 15
    return card


def print_dict_table(card):
    keys = create_card().keys()
    count = 0
    for i in card.values():
        if isinstance(i, list) and len(i) > count:
            count = len(i)

    for i in keys:
        print(i, end="  " "\t")
    print()

    for i in range(count):
        for j in keys:
            if isinstance(card[j], list) and len(card[j]) >= i:
                print(card[j][i], end="\t")
            else:
                print(card[j], end="\t")
        print()


def main():
    print_dict_table(create_card())


if __name__ == '__main__':
    main()
