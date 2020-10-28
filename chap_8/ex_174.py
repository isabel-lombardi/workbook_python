# Greatest Common Divisor


def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)


print("►►► This program calculates the greatest common divisor of two numbers ◄◄◄")
print("-" * 75)
first_num = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print("-" * 75)
print("The greatest common divisor of {} and {} is: {}".format(first_num, second_number, gcd(first_num, second_number)))
