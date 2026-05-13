'''
Write  a  program  to  evaluate  postfix  expression
Input :  3 4 5 * + 6 2 / -
Output :  20
'''
def eval(postfix):
    lst = []
    for char in postfix:
        if char.isdigit():
            lst.append(int(char))
        elif char != ' ':
            b = lst.pop()
            a = lst.pop()
            if char == '+':
                result = a + b
            elif char == '-':
                result = a - b
            elif char == '*':
                result = a * b
            elif char == '/':
                result = a // b
            lst.append(result)
    return lst.pop()
postfix = input('Enter postfix expression : ')
print('Result :', eval(postfix))

'''
Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from prog1b import stack
def icp(operator):
    if operator == '+' | operator == '-':
        return 1
    elif operator == '*' | operator == '/':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 4
    elif operator == '#':
        return 0
def isp(operator):
    if operator == '+' | operator == '-':
        return 1
    elif operator == '*' | operator == '/':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
def convert(infix):
    s = stack()
    s.push('#')
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == ')':
            while s.peek() != '(':
                postfix += s.pop()
            s.pop()
        else:
            while icp(ch) <= isp(s.peek()):
                postfix += s.pop()
            s.push(ch)
    while s.peek() != '#':
        postfix += s.pop()
    return postfix
infix = input('Enter infix expression : ')
postfix = convert(infix)
print('Postfix expression :', postfix)