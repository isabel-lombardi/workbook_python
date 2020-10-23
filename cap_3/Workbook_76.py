# Prime Factors
n = int(input("Enter an integer (2 or greater): "))
f = 2

if n >= f:
    print("The prime factor of {} are :".format(n))
else:
    print("The value is less than 2. Insert a larger number")
while f <= n:
    if n % f == 0:
        print(f)
        n = n // f
    else:
        f += 1