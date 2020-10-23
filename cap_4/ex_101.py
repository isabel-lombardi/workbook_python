# Reduce a Fraction to Lowest Terms

def gcd(n, m):
    d = min(n, m)
    while n % d != 0 or m % d != 0:
        d -= 1
    return d


def reduce(num, den):
    if num == 0:
        return 0, 1
    g = gcd(num, den)
    return num // g, den // g


def main():
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))
    (n, d) = reduce(num, den)
    print("%d/%d can be reduced to %d/%d" % (num, den, n, d))


main()

