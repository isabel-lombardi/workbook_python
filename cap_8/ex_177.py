# Roman Numerals
roman_numbers = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def roman_to_number(s):
    if s in roman_numbers:
        return roman_numbers[s]
    first, second = map(roman_to_number, s[:2])
    if first < second:
        return second - first + roman_to_number(s[2:])
    else:
        return first + roman_to_number(s[1:])


def main():
    user_roman = input("Enter a roman number to convert: ").upper()
    print(roman_to_number(user_roman))


main()
