# Median of Three Values
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))


def median(a, b, c):
    l = [a, b, c]
    l1 = sorted(l)
    m = l1[1:2]
    print("".join(map(str, m)))


print("The median value of {}, {} and {} is:".format(n1, n2, n3))
median(n1, n2, n3)