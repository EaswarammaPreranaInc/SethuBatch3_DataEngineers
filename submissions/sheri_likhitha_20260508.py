# prog2.py
# Program to reverse a string using stack
# Reusing Stack class from prog1b.py

from prog1b import Stack

# create stack object
s = Stack()

# read string from keyboard
str1 = input("Enter a string : ")

# push each character into stack
for ch in str1:
    s.push(ch)

# remove each character from stack
# and concatenate to result
result = ""

while not s.is_empty():
    result = result + s.pop()

# print reversed string
print("Reverse string :", result)





# prog3.py
# Program to perform parentheses matching
# Reusing Stack class from prog1b.py

from prog1b import Stack

# create stack object
s = Stack()

# read expression
exp = input("Enter expression : ")

valid = True

# check each character in expression
for ch in exp:

    # if character is '(' push into stack
    if ch == '(':
        s.push(ch)

    # if character is ')' pop from stack
    elif ch == ')':

        x = s.pop()

        # pop() returns None means excess ')'
        if x is None:
            print("Invalid Expression due to excess )")
            valid = False
            break

# after checking complete expression
if valid:

    # stack empty means valid expression
    if s.is_empty():
        print("Valid Expression")

    # stack not empty means excess '('
    else:
        print("Invalid Expression due to excess (")





