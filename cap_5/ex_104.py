# Sorted Order

num_l = []

while True:
    number = int(input("Enter the number (0 to exit): "))
    if number == 0:
        break
    num_l.append(number)

num_l.sort()
print("The numbers entered, in ascending order are: ")
for n in num_l:
    print(n)
