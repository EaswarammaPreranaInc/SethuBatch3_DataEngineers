# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'tuple'>
print(x) # <function <lambda at 0x7f8c9c1e5ee0>, 3, 70, 1.4285714285714286>
for  y  in   x:
	print(y) # <function <lambda at 0x7f8c9c1e5ee0> , 3, 70, 1.4285714285714286 
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # 'tuple' object is not callable

# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec Cyb Hyd None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec Cyb Hyd

#Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'tuple>
print(a) # <function <lambda> at 0x7f8c9c1e5ee0>, None, None
for  x  in  a:
	print(x) # <function <lambda> at 0x7f8c9c1e5ee0>, None, None
a() # tuple object is not callable
print(a[0]()) # 'tuple' object is not subscriptable