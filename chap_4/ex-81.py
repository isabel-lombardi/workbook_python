# Compute the Hypotenuse
from math import sqrt

c_a = int(input("Enter the first side: "))
c_b = int(input("Enter the second side: "))


def t_pythagoras(a, b):
    h = sqrt((a ** 2) + (b ** 2))
    print(h)


t_pythagoras(c_a, c_b)
