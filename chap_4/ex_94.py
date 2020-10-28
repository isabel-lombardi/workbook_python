# Random Password

from random import randint
n = randint(7, 10)


def r_pass():
    password = ""
    for x in range(n):
        x = randint(33, 127)
        c = chr(x)
        password += c
    return password


def main():
    result = r_pass()
    print("The password generated for you with {} length: ".format(n))
    print(result)


if __name__ == "__main__":
    main()
