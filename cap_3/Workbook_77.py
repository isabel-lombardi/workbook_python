# Binary to Decimal

bin_number = input("Enter the binary number to be covered in decimal number: ")

reverse = bin_number[::-1]
bin_len = len(bin_number)

decimal = 0
exp = 0    # exponent

while exp < bin_len:
    if reverse[exp] == "1":
        decimal += 2 ** int(exp)
    exp += 1

print("The binary number {} corresponds to the decimal number: {}".format(bin_number, decimal))

