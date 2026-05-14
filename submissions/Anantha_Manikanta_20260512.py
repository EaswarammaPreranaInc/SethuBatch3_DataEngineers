'''
1) Write a program to evaluate postfix expression

Input : 3 4 5 * + 6 2 / -
Output : 20
'''
def eval(postfix):
    stack = []
    for char in postfix.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    return stack.pop()
postfix = input("Enter postfix expression : ")
print("Result :", eval(postfix))

'''
2) Write a program to convert infix to prefix
'''
from prog1b import stack
def icp(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 4
    return 0
def isp(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
    return 0
def convert(infix):
    infix = infix[::-1]
    temp = ''
    for ch in infix:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch
    infix = temp
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
    prefix = postfix[::-1]
    return prefix
infix = input('Enter infix expression : ')
prefix = convert(infix)
print('Prefix expression :', prefix)