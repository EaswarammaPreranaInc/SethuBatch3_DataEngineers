# Write a program to convert prefix to postfix
def is_operator(ch):
    return ch in '+-*/^'

def tokenize(expr):
    expr = expr.strip()
    if ' ' in expr:
        return [tok for tok in expr.split() if tok]
    return list(expr)

def prefix_to_postfix(prefix):
    tokens = tokenize(prefix)
    stack = []
    for ch in reversed(tokens):
        if ch == '':
            continue
        if is_operator(ch):
            if len(stack) < 2:
                raise ValueError('Invalid prefix expression')
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + ' ' + op2 + ' ' + ch)
        else:
            stack.append(ch)
    if len(stack) != 1:
        raise ValueError('Invalid prefix expression')
    return stack[0]

expr = input('Enter prefix expression : ')
try:
    print('Postfix expression :', prefix_to_postfix(expr))
except ValueError as e:
    print(e)
