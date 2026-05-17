1) Write  a  program  to  convert  prefix  to  postfix

def prefix_to_postfix(expression):
    stack = []

    for ch in reversed(expression):

        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            temp = op1 + op2 + ch
            stack.append(temp)

    return stack[-1]


prefix = input("Enter Prefix Expression: ")

postfix = prefix_to_postfix(prefix)

print("Postfix Expression:", postfix)