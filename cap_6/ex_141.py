# Write out Numbers in English
from random import randint

number = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
          0: "zero", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
          16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
          40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

thousand = 1000


def number_english(n):
    if n < 20:
        return number[n]

    if n < 100:
        if n % 10 == 0:
            return number[n]
        else:
            return number[n // 10 * 10] + " " + number[n % 10]

    if n < thousand:
        if n % 100 == 0:
            return number[n // 100] + " hundred"
        else:
            return number[n // 100] + " hundred " + number_english(n % 100)


def main():
    choice = int(randint(10, 999))
    print(number_english(choice))
    for x in range(1, 999):
        print(number_english(x))


main()
