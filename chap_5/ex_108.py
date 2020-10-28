# Negatives,Zeros and Positives

negative = []
zero = []
integer = []

while True:
    number = input("Enter the number (blank to quit): ")
    if number == "":
        break
    number = int(number)
    if number < 0:
        negative.append(number)
    if number == 0:
        zero.append(number)
    if number > 0:
        integer.append(number)

for n in negative:
    print(n)
for n in zero:
    print(n)
for n in integer:
    print(n)


