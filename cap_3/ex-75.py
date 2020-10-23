# Greatest Common Divisor

n = int(input("Enter the first positive integer: "))
m = int(input("Enter the second positive integer: "))

d = min(n, m)

while n % d != 0 or m % d != 0:
    d += -1

print("The GCD of {} and {} is: {}".format(n, m, d))
