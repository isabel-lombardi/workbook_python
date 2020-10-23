# Is a Number Prime?

def number_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input("Enter a number: "))
    result = number_prime(n)
    if result:
        print(result)
    else:
        print(result)


if __name__ == '__main__':
    main()