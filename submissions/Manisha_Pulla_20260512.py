'''
Write  a  program  to  evaluate  postfix  expression

Input :  3 4 5 * + 6 2 / -
Output :  20
'''
'''
Write a program to evaluate postfix expression

Input :  3 4 5 * + 6 2 / -
Output :  20
'''

def eval(postfix):
    stack = []

    # iterate through postfix expression
    for ch in postfix.split():

        # if operand
        if ch.isdigit():
            stack.append(int(ch))

        else:
            # remove 2 operands from stack
            b = stack.pop()
            a = stack.pop()

            # perform operation
            if ch == '+':
                stack.append(a + b)

            elif ch == '-':
                stack.append(a - b)

            elif ch == '*':
                stack.append(a * b)

            elif ch == '/':
                stack.append(a // b)

    # result of postfix expression
    return stack.pop()

# read postfix expression
postfix = input('Enter postfix expression : ')

print('Result : ', eval(postfix))





 '''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
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
    elif operator == '#':
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

def convert(infix):

    # reverse infix expression
    infix = infix[::-1]

    # interchange brackets
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

    # reverse postfix to get prefix
    prefix = postfix[::-1]

    return prefix

# read infix expression
infix = input('Enter infix expression : ')

prefix = convert(infix)

print('Prefix expression : ', prefix)