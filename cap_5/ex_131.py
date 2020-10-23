# Infix to Postfix
OPERATORS = {'+', '-', '*', '/', '(', ')', '^'}
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_to_postfix(exp):
    stack = []
    postfix = ''

    for ch in exp:
        if ch not in OPERATORS:
            postfix += ch
        elif ch == '(':  #
            stack.append('(')
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                postfix += stack.pop()
            stack.append(ch)
        while stack:
            postfix += stack.pop()
    return postfix


expression = input('Enter infix expression: ')
print('Infix expression: ', expression)
print('Postfix expression: ', infix_to_postfix(expression))
