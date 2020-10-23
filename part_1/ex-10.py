# Arithmetic
from math import log10

# User integers choice
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print("-" * 40)

print("-The sum of {} and {} is: {}".format(a, b, (a + b)))
print("-The difference between {} and {} is: {}".format(b, a, (b - a)))
print("-The product of {} and {} is: {}".format(a, b, (a * b)))
print("-The quotient of {} divided by {} is: {}".format(a, b, (a // b)))
print("-The remainder of {} divided by {} is:{}".format(a, b, (a % b)))
print("-The result of log10 {} is: {:.2f}".format(a, (log10(a))))
print("-The result of {} with exponent {} is: {}".format(a, b, (a ** b)))
