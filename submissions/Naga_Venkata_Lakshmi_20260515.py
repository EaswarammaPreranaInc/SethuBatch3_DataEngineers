from  prog7b  import  *
def   prefix_postfix(prefix):
	s = stack() 
	prefix = prefix[::-1] 
	for  ch  in  prefix:
		
		if  ch . isalpha(): 
			s . push(ch)
		else:	 
			op1 = s . pop()  
			op2 = s . pop()   
			new_expr = op1 + op2 + ch 
			s . push(new_expr)  
	
	return  s . pop()   
#  End  of  the  function
prefix_exp= input('Enter  prefix  expression : ')  
postfix = prefix_postfix(prefix_exp)  
print('Postfix  expression : ' , postfix)
