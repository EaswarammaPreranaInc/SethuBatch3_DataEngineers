'''
1) # Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))  # <class 'tuple'>
print(x)  # (<function <lambda> at 432)
for  y  in   x:
	print(y)  # <function <lambda> at 123> <nextline> 3 <nextline> 70 <nextline> 1.42
print(x[0](9 , 2))  # 11
print(x[1])  # 3
print(x())  # Error because tuple is not callable
'''
'''
2) #  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())  # Sec <nextline> Cyb <nextline> Hyd <nextline> None
'''
'''
3) # Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())  # Sec <nextline> Cyb <nextline> Hyd
'''
'''
4) # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')  # Sec <nextline> Cyb
print(type(a))  # <class 'tuple'>
print(a)  # <function <lambda> at 123>, None, None
for  x  in  a:
	print(x)  # <function <lambda> at ...> <nextline> None <nextline> None
a()  # Error because tuple is not callable
print(a[0]())  # Hyd <nextline> None
'''