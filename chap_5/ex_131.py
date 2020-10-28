# Infix to Postfix
from chap_5.ex_130 import unary
from chap_5.ex_129 import token


def is_integer(s):
    s = s.strip()
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False


def precedence(x):
    if x == "-" or x == "+":
        res = 1
    elif x == "*" or x == "/":
        res = 2
    elif x == "u+" or x == "u-":
        res = 3
    elif x == "ˆ":
        res = 4
    else:
        res = -1
        print("Is not an operator")
    return res


def algorithm(tokens):
    marked = unary(tokens)
    operators = []
    postfix = []

    for ch in marked:
        if is_integer(ch):
            postfix.append(ch)
        elif ch == "+" or ch == "-" or ch == "*" or ch == "/" or ch == "^" or ch == "u-" or ch == "u+":
            while operators != [] and operators[len(operators)-1] != '(' \
              and precedence(ch) < precedence(operators[len(operators) - 1]):
                x = operators.pop(len(operators)-1)
                postfix.append(x)
            operators.append(ch)
        elif ch == "(":
            operators.append(ch)
        elif ch == ")":
            while operators[len(operators)-1] != "(":
                x = operators.pop(len(operators)-1)
                postfix.append(x)
            operators.remove("(")

    while operators:
        x = operators.pop(len(operators)-1)
        postfix.append(x)

    return postfix


def main():
    exp = input("Enter a mathematical expression: ")
    tokens = token(exp)
    print(algorithm(tokens))


main()
