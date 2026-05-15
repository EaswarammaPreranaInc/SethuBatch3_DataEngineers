# Write a program to convert Prefix to Postfix

from prog7b import *    
def postfix(prefix):
    s = stack()   # Creates empty stack
    for ch in reversed(prefix):
        if ch.isalnum():
            s.push(ch)
        else:
            op1 = s.pop()   
            op2 = s.pop()   
            new_expr = op1 + op2 + ch
            s.push(new_expr)
    return s.pop()
prefix = input("Enter Prefix expression : ")
print("Postfix expression :", postfix(prefix)