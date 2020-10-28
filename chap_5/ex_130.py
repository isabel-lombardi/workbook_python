# Unary and Binary Operators

def unary(s):
    result = [e for e in s]
    symbols = "()*/^-+"
    if result[0] == "+":
        result[0] = "u+"
    if result[0] == "-":
        result[0] = "u-"

    for s in range(len(result)):
        for n in symbols:
            if result[s - 1] == n:
                if result[s] == "+":
                    result[s] = "u+"
                elif result[s] == "-":
                    result[s] = "u-"
    result = [i for i in result if not i.isdigit()]
    return result


def main():
    exp = input("Enter a mathematical expression: ").replace(" ", "")
    print("The Unary and Binary Operators in the string are: {}".format(unary(exp)))


if __name__ == "__main__":
    main()
