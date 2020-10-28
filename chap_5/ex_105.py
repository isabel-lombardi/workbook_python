# Reverse Order

num_l = []

while True:
    number = int(input("Enter the number (0 to exit): "))
    if number == 0:
        break
    num_l.append(number)

num_l.reverse()
print("The numbers entered, in reverse order are:")
for n in num_l:
    print(n)
