# Infix to Postfix
from cap_5.ex_130 import unary
from cap_5.ex_129 import token

o = ["+", "-", "*", "/", "u-", "u+", "^"]


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
        print("Is not operator ")
    return res


def infix_to_postfix(exp):
    marked = unary(exp)
    operators = []
    postfix = []

    for ch in marked:
        if ch not in o:
            postfix.append(ch)
        elif ch in o:
            while operators != [] and operators[len(operators) - 1] != "(" and \
                    precedence(ch) < precedence(operators[len(operators) - 1]):
                x = operators.pop(len(operators) - 1)
                postfix.append(x)
            operators.append(ch)

        elif ch == "(":
            operators.append(ch)
        elif ch == ")":
            while operators[len(operators) - 1] != "(":
                x = operators.pop(len(operators) - 1)
                postfix.append(x)
            operators.remove("(")

    while operators != []:
        x = operators.pop(len(operators) - 1)
        postfix.append(x)

    return postfix


def main():
    expression = input("Enter infix expression: ").replace(" ", "")
    exp = token(expression)
    print("Postfix expression: {}".format(infix_to_postfix(exp)))


main()
