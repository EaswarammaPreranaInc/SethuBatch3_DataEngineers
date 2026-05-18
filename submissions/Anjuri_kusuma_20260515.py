#  Write  a  program  to  convert  prefix  to  postfix


stack = []

prefix = input("Enter prefix expression : ")


for ch in reversed(prefix):
    if ch.isalnum():
        stack.append(ch)
    else:
        op1 = stack.pop()
        op2 = stack.pop()

        temp = op1 + op2 + ch

        stack.append(temp)

print("Postfix expression :", stack[0])