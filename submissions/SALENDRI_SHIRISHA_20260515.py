#  Write  a  program  to  convert  prefix  to  postfix

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']
def prefix_to_postfix(prefix):
    stack = []
    for char in reversed(prefix):
        if is_operator(char):
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + char
            stack.append(temp)
        else:
            stack.append(char)
    return stack[-1]
prefix = "*+AB-CD"
postfix = prefix_to_postfix(prefix)
print("Prefix Expression :", prefix)
print("Postfix Expression:", postfix)
