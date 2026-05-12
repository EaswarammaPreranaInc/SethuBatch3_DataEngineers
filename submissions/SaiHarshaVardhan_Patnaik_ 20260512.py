def eval_postfix(postfix):
    stack = []
    for token in postfix.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)  # integer division
    return stack[0]





def infix_to_postfix(infix):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    output = []
    for token in infix.split():
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while stack and precedence.get(stack[-1],0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

# Example usage
infix_expr = "3 + 4 * 5 - 6 / 2"
postfix_expr = infix_to_postfix(infix_expr)
print("Postfix:", postfix_expr)
print("Result:", eval_postfix(postfix_expr))


from prog1b import stack

def icp(op):
    if op in ['+', '-']: return 1
    if op in ['*', '/']: return 2
    if op == '^': return 3
    if op == '(': return 4
    return 0

def isp(op):
    if op in ['+', '-']: return 1
    if op in ['*', '/']: return 2
    if op == '^': return 3
    if op == '(': return 0
    if op == '#': return -1
    return 0

def convert(infix):
    # Step 1: reverse infix and swap brackets
    infix = infix[::-1]
    infix = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix])

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

    # Step 2: reverse postfix → prefix
    return postfix[::-1]

# Example run
infix = input("Enter infix expression: ")
prefix = convert(infix)
print("Prefix expression:", prefix)