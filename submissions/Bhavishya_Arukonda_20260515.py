#  Write  a  program  to  convert  prefix  to  postfix



def prefix_to_postfix(prefix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for ch in reversed(prefix):
        if ch == ' ':
            continue
        if ch not in operators:
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + ch)

    return stack[-1]

prefix = input("Enter prefix expression: ")
print("Postfix expression:", prefix_to_postfix(prefix))