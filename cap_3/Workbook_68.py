# Parity Bits
us_bit = input("Enter 8 bits in binary: ")

while us_bit != "":
    if us_bit.count("1") + us_bit.count("0") != 8:
        print("Not 8 bits. Try again")
    elif us_bit.count("1") % 2 == 0:
        print("Parity bit should be 0.")
    else:
        print("Parity bit should be 1")
    us_bit = input("Enter 8 bits in binary: ")