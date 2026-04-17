# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class 'tuple'>
print(x)# Type and address
for  y  in   x:
	print(y) # 3 70 1.4
print(x[0](9 , 2))#11
print(x[1])#3
print(x())#error


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())#Sec\nCyb\nHyd\nNone


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())#Sec\nCyb\nHyd


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')#Sec\nCyb\nHyd\nNone
print(type(a)) # <class 'function'>
print(a) #Type and address
for  x  in  a:
	print(x)
a() #error
print(a[0]())
