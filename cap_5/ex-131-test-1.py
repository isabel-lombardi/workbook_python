# Infix to Postfix
from WB90 import is_integer
from WB130 import unary
from WB91 import precedence


def infix_to_postfix(s):
    symbols = "()*/^-+"
    operators = []
    postfix = []
    for t in s:
        if is_integer(t):
            postfix.append(t)
        if t in symbols:
            while len(operators) != 0 and \
                    operators[-1] != "(" and \
                    precedence(t) < precedence(operators[-1]):
                operators.remove(operators[-1]) and postfix.append(operators[-1])
            operators.append(t)
        if t == "(":
            operators.append(t)
        if t == ")":
            while operators[-1] != "(":
                operators.remove(operators[-1]) and postfix.append(operators[-1])
            operators.remove("(")

    while operators is not len(operators) == 0:
        operators.remove(operators[-1]) and postfix.append(operators[-1])
    return postfix


def main():
    exp = input("Enter a mathematical expression: ").replace(" ", "")
    exp_token = unary(exp)
    print(infix_to_postfix(exp_token))


main()
