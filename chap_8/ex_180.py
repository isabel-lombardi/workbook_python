# String edit Distance

def string_distance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[len(s) - 1] != t[len(t) - 1]:
            cost += 1
        d1 = string_distance(s[0: len(s) - 1], t) + 1
        d2 = string_distance(s, t[0: len(t) - 1]) + 1
        d3 = string_distance(s[0: len(s) - 1], t[0: len(t) - 1]) + cost
        return min(d1, d2, d3)


def main():
    txt1 = input("Enter the first word: ")
    txt2 = input("Enter the second word:")
    print("The edit distance between {} and {} is: {}".format(txt1, txt2, string_distance(txt1, txt2)))


main()