'''
Write  a  program  to  evaluate  postfix  expression

Input :  3 4 5 * + 6 2 / -
Output :  20
'''
def  eval(postfix):
	for char in postfix:
		if  char.isalnum():
				s.push(int(char)) 
		else:
			op2=s.pop()
			op1=s.pop()
			if char == '+':
                		result = op1 + op2
            		elif char == '-':
                		result = op1 - op2
            		elif char == '*':
                		result = op1 * op2
            		elif char == '/':
                		result = op1 / op2

            		s.push(result)
						
	# End  of  for  loop				
	return  postfix
#  End  of  the  function
infix=input()
postfix=convert(infix)
print('Result : ' , postfix)




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
        return 2
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1


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

print('Prefix expression : ', prefix)