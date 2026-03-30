# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))# <class 'tuple'>
print(x)# (17,3,70,1.42)
for  y  in   x:
	print(y) # 17<nl>3<nl>60<nl>1.42
print(x[0](9 , 2))# 11
print(x[1])# 3
print(x())# Error

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec<nl>Cyb<nl>Hyd<nl>None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())# Sec<nl>Cyb<nl>Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<class 'tuple'>
print(a) # (typr and address, None, None)
for  x  in  a:
	print(x) # Type and address<nl>None<nl>None
#a() # Error, bcz is typle which is not callable
print(a[0]())# Hyd<nl>None