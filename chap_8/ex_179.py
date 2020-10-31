# Square root
"""
abs() ???
"""


def square_root(n, guess=1.0):
    if abs(guess ** 2 - n) < 10 ** (-12) * n:
        return guess
    else:
        guess = (guess + (n / guess)) / 2
        return square_root(n, guess)


def main():
    print()
    print("The square root of 10: \n"
          "--------------------------------\n"
          "Expected value  3.162277660168379")
    print("Result         ", square_root(10))
    print()

    print("The square root of 120: \n"
          "--------------------------------\n"
          "Expected value  10.954451150103322")
    print("Result         ", square_root(120))


main()