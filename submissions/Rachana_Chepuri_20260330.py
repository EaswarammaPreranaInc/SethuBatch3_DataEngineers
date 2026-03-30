''' Tricky  program'''
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class 'tuple'>
print(x)#17<next line>3<next line>70<next line>1.42
for  y  in   x:
	print(y)#Type and address
print(x[0](9 , 2))#(11 , 7 , 18, 4.5)
print(x[1])#Type and address
print(x())#Error---expecting arguments
'''Tricky  program'''
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''output'''
# Sec
# Cyb
# Hyd
# None
'''Find  outputs (Home  work)'''
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''output'''
# Sec
# Cyb
# Hyd
'''Find  outputs   (Home  work)'''
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
#a() 
print(a[0]())
'''output'''
# Sec
# Cyb
# <class 'tuple'>
# type and address
# type and address
# None
# None
# Hyd
# None
