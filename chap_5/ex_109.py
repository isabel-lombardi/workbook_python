# List of Proper Divisors

def proper_divisor(n):
    d = 1
    divisor = []
    while d < n:
        if n % d == 0:
            divisor.append(d)
        d += 1
    return divisor


def main():
    print("The divisors are:")
    print(proper_divisor(100))
    print(proper_divisor(28))


if __name__ == "__main__":
    main()
