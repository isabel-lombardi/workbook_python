# Evaluate Postfix

"""not completed"""
from cap_5.ex_131 import infix_to_postfix
from cap_5.ex_130 import unary

exp = "2 * 3 - -5 + 2"
postfix_exp = infix_to_postfix(exp)

values = []

for token in postfix_exp:
    if token.isdigit():
        token = int(token) and values.append(token)
    if token == "u+" or token == "u-":
        values.pop(-1)

