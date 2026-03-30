# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # < class 'tuple'>
print(x) # (<function <lambda>> , 3, 70 ,1.428)
for  y  in   x:
	print(y) # <function <lambda>>
			 # 3
			 # 70
			 # 1.428
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # Error

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
print(type(a)) # <class 'tuple'>
print(a) # (<function <lambda>> at 0x12345 , None , None)
for  x  in  a:
	print(x) # <function <lambda>> at 0x12345
			 # None
			 # None
a() # Error
print(a[0]()) # Hyd
			  # None
