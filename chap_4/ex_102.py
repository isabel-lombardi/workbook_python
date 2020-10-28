# Reduce Measures

tp_in_s = 3
tp_in_cup = 48


def reduce_measures(number, unit):
    unit = unit.lower()

    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = number
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = number * tp_in_s
    elif unit == "cup" or unit == "cups":
        teaspoons = number * tp_in_cup

    cups = teaspoons // tp_in_cup
    teaspoons = teaspoons - cups * tp_in_cup
    tablespoons = teaspoons // tp_in_s
    teaspoons = teaspoons - tablespoons * tp_in_s
    result = ""

    if cups > 0:
        result += str(cups) + " cup"
        if cups > 1:
            result += "s"

    if tablespoons > 0:
        if result != "":
            result += ", "
        result += str(tablespoons) + " tablespoon"
        if tablespoons > 1:
            result += "s"
    if teaspoons > 0:
        if result != "":
            result += ","
        result += str(teaspoons) + " teaspoon"
        if teaspoons > 1:
            result += "s"
    if result == "":
        result = "0 teaspoons"

    return result


def main():
    print("59 teaspoons is: {}".format(reduce_measures(59, "teaspoons")))


main()
