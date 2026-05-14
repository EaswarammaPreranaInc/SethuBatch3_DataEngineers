'''
Write  a  program  to  evaluate  postfix  expression

Input :  3 4 5 * + 6 2 / -
Output :  20
'''
def  eval_post(postfix):
	stack=[]
	for ch in postfix:
		if  ch in '+-*%/^':
				y=stack.pop()
				x=stack.pop()
				stack.append(eval(f'{x}{ch}{y}'))
		else:  
				stack.append(ch)						
	return  stack[0]
#  End  of  the  function
postfix=input()
print('Result : ' , eval_post(postfix))









'''
Write  a  program  to  convert  infix  to  prefix

Hint:  Modify  following  program  to  convert  infix  to  prefix
'''
from  prog1b   import  stack
def  icp(operator):
    if o in '+-':
		return 2
	if o in '*/%':
		return 3
	if o =='^':
		return 4
	if o == ')':
		return 5
	  

def  isp(operator):
    if o in '+-':
		return 1
	if o in '*/%':
		return 2
	if o =='#':
		return -1
	if o =='^':
		return 4
	if o == ')':
		return 0
	
def  convert(infix):  #  Modify  the  function  to  convert  infix  to  prefix
        infix = infix[::-1]
	s = []  
	s . apppend('#') 
	postfix = ''  
	for  ch  in  infix: 
		if  ch . isalnum():  
			prefix +=  ch  
		elif  ch == '(':
			while  s[-1] !=  ')': 
					prefix  += s.pop()  
			s . pop() 
		else:
			while  icp(ch) <= isp(s[-1]):  
				prefix += s . pop()  
			s . append(ch)  
	#  End  of  for  loop
	while  s[-1] !=  '#':  
			prefix += s . pop() 
	return  prefix
#  End  of  the  function
infix = input('Enter  infix  expression  :  ')  
prefix = convert(infix)  
print('Prefix  expression :  ' , prefix[::-1])