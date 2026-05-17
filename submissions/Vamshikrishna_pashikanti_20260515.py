#  Write  a  program  to  convert  prefix  to  postfix
def prefix_to_postfix(prefix_exp):
    stack = []
    operators = set('+-*/^')
    
    for char in reversed(prefix_exp):
        if char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + char
            stack.append(temp)
        else:
            stack.append(char)
    
    return stack[0] if stack else ""

test_cases = [
    "*-A/BC-/AKL",
    "+AB",
    "*+ABC",
    "+*ABC",
]
    
print("Prefix to Postfix Conversion Program")
print("=" * 50)
    
for prefix in test_cases:
    postfix = prefix_to_postfix(prefix)
    print(f"Prefix:  {prefix}")
    print(f"Postfix: {postfix}")
    print("-" * 50)
