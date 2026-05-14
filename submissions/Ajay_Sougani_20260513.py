from prog1a import stack
def  eval(postfix):
	for ch in postfix: #How  to  iterate  thru  postfix  expression
		if  ch.isdigit():
				s.push(int(ch)) #Convert  the  operand  to  integer  and  push  into  the  stack
		else:  
				y=s.pop() 
				x=s.pop()#How  to  remove  2  operands  from  the  stack,  perform  the  operation  on  the  deleted  operands
				s.push(x+y) #and  push  the  result  into  the  stack		
	# End  of  for  loop				
	return  s.list[0]
#  End  of  the  function
infix=input("Enter Infix : ") #How  to  read  infix  expression
s=stack() 
postfix=convert(infix)#How  to  convert  infix  to  postfix
print('Result : ' ,  eval(postfix))


def  convert(rev_infix):  #  Modify  the  function  to  convert  infix  to  prefix
	s = stack()  
	s . push('#') 
	prefix = ''  
	for  ch  in  rev_infix: 
		if  ch . isalnum():  
			prefix +=  ch  
		elif  ch == '(':
			while  s . peek()  !=  ')': 
					prefix  += s . pop()  
			s . pop() 
		else:
			while  icp(ch) <= isp(s . peek()):  
				prefix += s . pop()  
			s . push(ch)  
	#  End  of  for  loop
	while  s . peek() !=  '#':  
			prefix += s . pop() 
	return  prefix[::-1]
#  End  of  the  function
infix = input('Enter  infix  expression  :  ') 
rev_infix=infix[::-1]
prefix = convert(rev_infix)  
print('Postfix  expression :  ' , prefix)
