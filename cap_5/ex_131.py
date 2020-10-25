# Infix to Postfix
"""I had trouble doing these two exercises with algorithms"""
operators = {"+", "-", "*", "/", "(", ")", "^"}
priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(exp):
    stack = []
    postfix = ''

    for ch in exp:
        if ch not in operators:
            postfix += ch
        elif ch == "(":
            stack.append("(")
        elif ch == ")":
            while stack and stack[-1] != "(":
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and priority[ch] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(ch)
        while stack:
            postfix += stack.pop()

    return postfix


expression = input("Enter infix expression: ")
print("Infix expression: {}".format(expression))
print("Postfix expression: {}".format(infix_to_postfix(expression)))
