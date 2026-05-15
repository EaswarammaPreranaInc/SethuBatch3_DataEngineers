#  Write  a  program  to  convert  prefix  to  postfix

def prefix_to_postfix(expression):

    stack = []
    # Traverse from right to left
    for ch in reversed(expression):

        # If operand
        if ch.isalnum():
            stack.append(ch)

        # If operator
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + ch
            stack.append(temp)
    return stack[0]

exp = "*+AB-CD"

result = prefix_to_postfix(exp)
print("Prefix Expression :", exp)
print("Postfix Expression:", result)