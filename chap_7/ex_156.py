# Sum a Collection of Numbers

number = input("-Enter a number: ")
total = 0
while number != "":
    try:
        number = float(number)
        total += number
        print("      The current total is: {}".format(total))
    except ValueError:
        print("It is not a number")

    number = input("-Enter a number: ")

print("-" * 45)
print("The total of all numbers entered is: {}".format(total))