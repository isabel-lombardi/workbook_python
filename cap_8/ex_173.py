# Total the Values

def user_total():
    line = input("Enter a number (blank to quit): ")
    if line == "":  # Base case
        return 0
    else:  # Recursive case
        return float(line) + user_total()


def main():
    total = user_total()
    print("The total of all those values is: {}".format(total))


main()
