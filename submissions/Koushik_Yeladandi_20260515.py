#  Write  a  program  to  convert  prefix  to  postfix 



def prefix_to_postfix(exp):

    stack = []

    # traverse from right to left
    for ch in reversed(exp):

        # if operand
        if ch.isalnum():
            stack.append(ch)

        # if operator
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            temp = op1 + op2 + ch

            stack.append(temp)

    return stack[-1]


exp = input("Enter prefix expression: ")

print("Postfix expression:", prefix_to_postfix(exp))