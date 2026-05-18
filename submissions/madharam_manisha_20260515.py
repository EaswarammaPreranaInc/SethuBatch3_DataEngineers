#  Write  a  program  to  convert  prefix  to  postfix
def prefix_to_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in expression[::-1]:
        if char not in operators:
            stack.append(char)
        else:
            if len(stack) < 2:
                return "Invalid prefix expression"
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + op2 + char
            stack.append(new_expr)
    return stack.pop() if stack else "Invalid prefix expression"
prefix = "*+AB-CD"
print(f"Prefix: {prefix}")
print(f"Postfix: {prefix_to_postfix(prefix)}") # Output: AB+CD-*