# Tokenizing a String
def token(s):
    symbols = "*/^-+"
    result = [c for c in s for s in symbols if c == s]
    return result


def main():
    exp = input("Enter a mathematical expression: ")
    print("The symbols in the string are: {}".format(token(exp)))


if __name__ == "__main__":
    main()