# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'function'>
print(x) # Type and  address  of  lambda  function
for  y  in   x:
	print(y) 
'''
3
70
1.42
'''
print(x[0](9 , 2)) # 11
print(x[1]) # 3
#print(x()) # Error a, b have no parameter


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec
           # Cyb  
		   # Hyd 
	        # None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec 
           # Cyb 
		   # Hyd 
		


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'function'>
print(a) # # Type and  address  of  lambda  function
for  x  in  a:
	print(x)
	'''
	None
	None
	'''
#a() # Error 
print(a[0]()) 
'''
Hyd
None
'''
