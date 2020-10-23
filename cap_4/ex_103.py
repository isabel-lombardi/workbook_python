# Magic date
from cap_4.ex_100 import day_in_a_month


def magic_date(d, m, y):
    if d * m == y % 100:
        return True
    return False


def main():
    for y in range(1900, 2000):
        for m in range(1, 13):
            for d in range(1, day_in_a_month(m, y) + 1):
                if magic_date(d, m, y):
                    print("{} {} {} is a magic date!".format(d, m, y))


main()

