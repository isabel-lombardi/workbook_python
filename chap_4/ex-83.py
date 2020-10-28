# Shipping Calculator
quantity = int(input("Enter the number of purchased item: "))
first_item = 10.95
other_item = 2.95


def total_ship(n):
    if n == 1:
        print("${}".format(first_item))
    else:
        total = n * other_item + first_item
        print("${}".format(total))


print("The total of the shipment will be: ")
total_ship(quantity)