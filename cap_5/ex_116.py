# Perfect Numbers
"""The previous exercises were done from the first edition of the workbook.
   The exercises that follow will be based on the second edition."""
from cap_5.ex_109 import proper_divisor

test = 10000


def is_perfect(n):  # determina se un intero positivo è perfetto.
    divisors = proper_divisor(n)
    number_sum = sum(divisors)
    if n == number_sum:
        return True
    return False


def main():
    print("The perfect numbers between 1 and {} are: ".format(test))
    for i in range(1, test + 1):
        if is_perfect(i):
            print(" ", i)


main()
