# Operator Precedence

def precedence(o):
    if o == "+" or o == "-":
        return 1
    elif o == "*" or o == "/":
        return 2
    elif o == "^":
        return 3
    else:
        return 0


def main():
    o = input("Enter an operator: ")
    result = precedence(o)
    if result == 0:
        print("The symbol is not valid")
    else:
        print(result)


if __name__ == '__main__':
    main()

