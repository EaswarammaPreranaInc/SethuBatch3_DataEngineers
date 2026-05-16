#  Write  a  program  to  convert  prefix  to  postfix

isp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 4,
    '(': 0
}

icp = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 5,
    '(': 6
}



def infix_to_postfix(exp):
    stack = []
    result = ""

    for ch in exp:

        if ch.isalnum():
            result += ch

        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack and isp[stack[-1]] >= icp[ch]:
                result += stack.pop()

            stack.append(ch)

    while stack:
        result += stack.pop()

    return result



def infix_to_prefix(exp):

    exp = exp[::-1]

    temp = ""

    for ch in exp:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch

    postfix = infix_to_postfix(temp)

    return postfix[::-1]



def prefix_to_postfix(exp):
    stack = []

    for ch in reversed(exp):

        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            stack.append(op1 + op2 + ch)

    return stack[0]



exp = input("Enter Infix Expression : ")

prefix = infix_to_prefix(exp)
postfix = prefix_to_postfix(prefix)

print("Prefix Expression :", prefix)
print("Postfix Expression :", postfix)