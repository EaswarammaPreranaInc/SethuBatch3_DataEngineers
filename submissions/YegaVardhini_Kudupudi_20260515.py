#  Write  a  program  to  convert  prefix  to  postfix


def prefix_to_postfix(prefix):
    stack = []
    prefix = prefix[::-1]
    for ch in prefix:
        if is_operator(ch):
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + ch
            stack.append(temp)
        else:
            stack.append(ch)
    return stack[0]
prefix = input("Enter prefix expression : ")
print('Prefix:',prefix)
postfix = prefix_to_postfix(prefix)
print("Postfix expression :", postfix)