# Admission Price
charges = []

while True:
    age = input("Enter the guest's age: ")

    if age == "":
        break

    price = 0
    age_int = int(age)
    if age_int <= 2:
        price = 0
    elif 3 <= age_int < 12:
        price = 14
    elif age_int >= 65:
        price = 18
    else:
        price = 23
    charges.append(price)

total = 0.00
for price in charges:
    total += price

print("Total for this group is ${:.2f}".format(total))


