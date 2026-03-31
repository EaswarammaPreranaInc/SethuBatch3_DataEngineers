# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))# <class 'tuple'>
print(x) # Type and address
for  y  in   x:
	print(y) # Type and address <nextline>3<nextline>70<nextline>1.43
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # Error because tuple can't be called

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
print(type(a)) #<class 'tuple'>
print(a) # (Type and address, None, None)
for  x  in  a:
	print(x) # Type and address<nextline> None<nextline>None
a() # Error because tuple can't be called
print(a[0]()) # Hyd <nextline>None