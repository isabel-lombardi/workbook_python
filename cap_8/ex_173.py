# Total the Values

def user_total():
    number = input("Enter a number (blank to quit): ")
    if number == "":  # Base case
        return 0
    else:  # Recursive case
        return float(number) + user_total()


def main():
    total = user_total()
    print("The total of all those values is: {}".format(total))


main()
