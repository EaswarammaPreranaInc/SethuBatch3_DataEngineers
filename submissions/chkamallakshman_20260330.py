# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'tuple'>
print(x) # ( <class 'function'> and address in hexadecimal , 3 , 70 , 1.43)
for  y  in   x:
print(y) # <class 'function'> and address in hexadecimal <nextline> 3 <nextline> 70 <nextline> 1.43
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # Error tuple is not callable

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

''' Output:
Sec
Cyb
Hyd
None '''

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

''' Output:
Sec
Cyb
Hyd
'''

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') # Sec <nextline> Cyb
print(type(a)) # <class 'tuple'>
print(a) # # ( <class 'function'> and address in hexa decimal , None , None)
for  x  in  a:
	print(x) # <class 'function'> and address in hexa decimal <nextline> None <nextline> None
a() # Error tuple is not callable
print(a[0]()) # Hyd <nextline> None