# Days in a Month

def day_in_a_month(m, y):
    leap = 0
    if y % 400 == 0:
        leap = 1
    elif y % 100 == 0:
        leap = 0
    elif y % 4 == 0:
        leap = 1
    if m == 2:
        return 28 + leap
    m31 = [1, 3, 5, 7, 8, 10, 12]
    if m in m31:
        return 31
    return 30


def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    result = day_in_a_month(month, year)
    if result:
        print(result)


main()
