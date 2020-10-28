# Recursive Decimal to Binary

def decimal_to_binary(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end="")


def main():
    decimal = int(input("Enter the decimal number to convert to binary number: "))
    print("The decimal number {} corresponds to the binary number: ".format(decimal))
    decimal_to_binary(decimal)


main()
