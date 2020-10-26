# Infix to Postfix
from WB90 import is_integer
from WB130 import unary
from WB91 import precedence


def infix_to_postfix(exp):
    symbols = ["(", ")", "*", "/", "-", "+"]
    operators = []
    postfix = []
    for t in exp:
        if is_integer(t):
            postfix.append(t)
        if t in symbols:
            while len(operators) != 0 and operators[-1] != "(" and \
                    precedence(t) < precedence(operators[-1]):
                operators.pop(-1) and postfix.append(operators[-1])
            operators.append(t)
        if t == "(":
            operators.append(t)
        if t == ")":
            while operators[-1] != "(":
                operators.pop(-1) and postfix.append(operators[-1])
            #operators.pop("(")
    while len(operators) != 0:
        postfix.append(operators[-1]) and operators.pop(-1)

    return postfix


str1 = "3 - 1  +4 * 2".replace(" ", "")
str2 = unary(str1)
print(infix_to_postfix(str1))

"""for x in range(len(exp)):
        for n in symbols:
            if exp[x] == n:
                if x != "1234567890":
                    for x in operators:
                        if operators[-1] != "(" and precedence(x) < precedence(operators[-1]):
                            operators.pop(-1) and postfix.append(operators[-1])
        operators.append(x)"""