# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))
print(x) 
for  y  in   x:
	print(y)
print(x[0](9 , 2))
print(x[1])
print(x())
'''
<class 'tuple'>
 type and address
 17
 3
 70
1.42
error as we cant call the tuple  
'''


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
None
'''

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
'''

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a() 
print(a[0]())
'''
Sec
Cyb
<class 'tuple'>
type and address
lambda func
None
None
error as tuple obj not callable
Hyd
None





