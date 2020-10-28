# Formatting a List


def formatting_list(s):
    result = ""
    for x in range(0, len(s) - 2):
        result += str(s[x]) + ", "

    if len(s) == 0:
        return "Enter an item"
    if len(s) == 1:
        return str(s[0])

    result += str(s[len(s) - 2]) + " and "
    result += str(s[len(s) - 1])
    return result


def main():
    item = []
    while True:
        us_item = input("Enter an item (blank to quit): ")
        if us_item == "":
            break
        item.append(us_item)
    print("The items are {}".format(formatting_list(item)))


main()
