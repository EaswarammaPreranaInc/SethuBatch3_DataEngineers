1) Write  a  program  to  evaluate  postfix  expression

Input :  3 4 5 * + 6 2 / -
Output :  20
'''
def  eval(postfix):
	stack = []
	for  ch in postfix.split() #How  to  iterate  thru  postfix  expression
		if ch.isdigit(): #if  char  is  an  operand
			stack.append(int(ch)) #Convert  the  operand  to  integer  and  push  into  the  stack
		else:  
			b = stack.pop()
			a = stack.pop()
			if ch == '+':
                          stack.append(a + b)

                        elif ch == '-':
                          stack.append(a - b)
                        elif ch == '*':
                          stack.append(a * b)

                        elif ch == '/':
                          stack.append(a // b)

                        elif ch == '^':
                          stack.append(a ** b) #How  to  remove  2  operands  from  the  stack,  perform  the  operation  on  the  deleted  operands and  push  the  result  into  the  stack		
	# End  of  for  loop				
	return stack.pop() #result  of  postfix  expression
#  End  of  the  function
postfix = input("Enter postfix Expression:") #How  to  read  infix  expression
How  to  convert  infix  to  postfix
print('Result : ' ,  eval(postfix) #How  to  print  result  of  postfix



2) Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from  prog1b   import  stack
def  icp(operator):
	How  to  return  icp  of  the  operator
'''
icp('+')  --->  2
icp('/') --->  3
icp('^') --->  4
'''
def  isp(operator):
	How  to  return  isp  of  the  operator
'''
isp('-')  --->  1
isp('*')  ---> 2
isp('^')  ---> 4
isp('(')  ---> 0
isp('#')  ---> -1
'''
def  convert(infix):  #  Modify  the  function  to  convert  infix  to  prefix
	s = stack()  
	s . push('#') 
	postfix = ''  
	for  ch  in  infix: 
		if  ch . isalnum():  
			postfix +=  ch  
		elif  ch == ')':
			while  s . peek()  !=  '(': 
					postfix  += s . pop()  
			s . pop() 
		else:
			while  icp(ch) <= isp(s . peek()):  
				postfix += s . pop()  
			s . push(ch)  
	#  End  of  for  loop
	while  s . peek() !=  '#':  
			postfix += s . pop() 
	return  postfix
#  End  of  the  function
infix = input('Enter  infix  expression  :  ')  
postfix = convert(infix)  
print('Postfix  expression :  ' , postfix)

-----------------------------
from  prog1b   import  stack
def  icp(operator):
	How  to  return  icp  of  the  operator
'''
icp('+')  --->  2
icp('/') --->  3
icp('^') --->  4
'''
def  isp(operator):
	How  to  return  isp  of  the  operator
'''
isp('-')  --->  1
isp('*')  ---> 2
isp('^')  ---> 4
isp('(')  ---> 0
isp('#')  ---> -1
'''
def  convert(infix):  #  Modify  the  function  to  convert  infix  to  prefix
    s = stack()
    s.push('#')
    postfix = ''
    for ch in infix:
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            s.push(ch)
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

def reverse_expression(exp):
    rev = ''
    for ch in exp[::-1]:
        if ch == '(':
            rev += ')'
        elif ch == ')':
            rev += '('
        else:
            rev += ch
    return rev

def infix_to_prefix(infix):
    rev = reverse_expression(infix)
    postfix = infix_to_postfix(rev)
    prefix = postfix[::-1]
    return prefix
#  End  of  the  function
infix = input('Enter  infix  expression  :  ')  
prefix = convert(infix)  
print('Prefix  expression :  ' , prefix)
