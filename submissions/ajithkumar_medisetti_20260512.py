'''
Write  a  program  to  evaluate  postfix  expression
Input :  3 4 5 * + 6 2 / -
Output :  20
'''
from  prog7b  import  *  
def  eval(postfix):
	s = stack() 
	for  ch  in  postfix:  
		if  ch . isdigit(): 
				s . push(int(ch)) 
		else:  
				y = s . pop()  
				x = s . pop()  
				match  ch:  
					case   '+':
								s . push(x + y)  
					case   '-':
								s . push(x - y)  
					case   '*':
								s . push(x * y)  
					case   '/':
								s . push(x // y)   
					case   '^':
								s . push(x ** y)  
	return  s . pop()  
infix =  input('Enter  infix  expression  :  ')  
postfix = convert(infix)  
print('Result : ' ,  eval(postfix))



'''
Write  a  program  to  convert  infix  to  prefix
Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from  prog1b  import   stack   
def  icp(operator):
	if  operator   in   '+-':
		return  2  
	if  operator   in   '*/%':
		return  3 
	if  operator  ==  '^':
		return  4
	if  operator  ==  ')':
		return  5
def  isp(operator):
	match  operator:
		case   '+' | '-':
			return  1
		case   '*' | '/' | '%':
			return  2
		case   '^':
			return  4
		case   ')':
			return  0
		case   '#':
			return  -1
def  convert(infix):
		infix = infix[::-1]  
		s = stack()   
		s . push('#')  
		prefix = ''  
		for  ch  in  infix:  
			if  ch . isdigit():  
					prefix += ch  
			elif  ch  ==  '(':
					while  s . peek()  !=  ')':  
							prefix  += s.pop() 
					s . pop() 
			else:
					while  icp(ch) <= isp(s . peek()):  
							prefix += s . pop()  
					s . push(ch)  
		while  s . peek() !=  '#':  
				prefix += s . pop()  
		return  prefix[::-1]  
infix = input('Enter Infix expression : ')
prefix = convert(infix)
print('Prefix expression : ' ,  prefix)