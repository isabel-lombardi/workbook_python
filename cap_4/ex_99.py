from cap_4.ex_98 import *


def dec2n(num, new_base):
    result = ""
    q = num

    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    while q > 0:
        r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    return result


def n2dec(num, b):
    decimal = 0

    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])
    return decimal


def main():
    from_base = int(input("Base to convert from (2-16): "))
    if from_base < 2 or from_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    from_num = input("Sequence of digits in that base: ")

    dec = n2dec(from_num, from_base)
    print("That’s %d in base 10." % dec)

    to_base = int(input("Enter the base to convert to (2-16): "))
    if to_base < 2 or to_base > 16:
        print("Only bases between 2 and 16 are supported.")
        print("Quitting...")
        quit()
    to_num = dec2n(dec, to_base)
    print("That’s %s in base %d." % (to_num, to_base))


main()
