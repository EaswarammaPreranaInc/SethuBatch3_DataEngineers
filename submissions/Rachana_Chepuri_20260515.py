# Python program to convert Prefix to Postfix

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def prefix_to_postfix(prefix):
    stack = []

    # Traverse the prefix expression from right to left
    for char in reversed(prefix):

        # If operator, pop two operands
        if is_operator(char):
            op1 = stack.pop()
            op2 = stack.pop()

            # Form postfix expression
            temp = op1 + op2 + char

            # Push back to stack
            stack.append(temp)

        # If operand, push to stack
        else:
            stack.append(char)

    return stack[-1]


# Input prefix expression
prefix = "*+AB-CD"

# Convert to postfix
postfix = prefix_to_postfix(prefix)

# Output
print("Prefix Expression :", prefix)
print("Postfix Expression:", postfix)