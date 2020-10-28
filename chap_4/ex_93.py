# Next Prime
from chap_4 import ex_92


def next_prime(n):
    while ex_92.number_prime(n) is False:
        n += 1
    return n


def main():
    n = int(input("Enter a number: "))
    result = next_prime(n)
    print("The prime number closer {} is {}".format(n, result))


main()
