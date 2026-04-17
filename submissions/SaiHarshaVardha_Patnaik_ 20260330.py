# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'tuple'>
print(x) # (<function <lambda> at 0x7f8c8c8c8c80>, 3, 70, 1.4285714285714286)
for  y  in   x:
	print(y) # 17 3 70 1.4285714285714286
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) #Error 

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Hyd  Sec  Cyb  None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec  Cyb  None

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'function'>
print(a) # <function <lambda> at 0x7f8c8c8c8d30>
for  x  in  a:
	print(x) #Error
a() # Hyd  Sec  Cyb
print(a[0]()) #Error