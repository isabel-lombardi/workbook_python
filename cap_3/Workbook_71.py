# Square root

x = int(input("Enter the number: "))
a = 3
while True:
    y = (a + x / a) / 2
    if y == a:
        break
    a = y
print(a)
