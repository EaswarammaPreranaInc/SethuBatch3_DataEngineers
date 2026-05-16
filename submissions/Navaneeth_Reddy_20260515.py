#  Write  a  program  to  convert  prefix  to  postfix

from prog7b import *      
def prefix_postfix(prefix):
    s = stack()           
    prefix = prefix[::-1]
    for ch in prefix:     
        if ch.isalnum():      
            s.push(ch)        
        else:                 
            op1 = s.pop()     
            op2 = s.pop()     
            new = op1 + op2 + ch   
            s.push(new)            
    return s.pop()           

infix = input('Enter Infix expression : ')
prefix = convert(infix)     
print('Postfix expression :', prefix_postfix(prefix))