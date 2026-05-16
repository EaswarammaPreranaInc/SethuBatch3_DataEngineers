# 1) Write a program to convert prefix to postfix

from prog1b import stack
def convert(prefix):
    s = stack()
    for ch in prefix[::-1]:
        if ch.isalnum():
            s.push(ch)
        else:
            op1 = s.pop()
            op2 = s.pop()
            temp = op1 + op2 + ch
            s.push(temp)
    return s.pop()
prefix = input('Enter prefix expression : ')
postfix = convert(prefix)
print('Postfix expression :', postfix)