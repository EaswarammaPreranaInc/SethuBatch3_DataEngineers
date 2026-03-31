# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class 'tuple'>
print(x)#(17,3,70,1.42)
for  y  in   x:
	print(y)#17<\n>3<\n>70<\n>1.42
print(x[0](9 , 2))#11
print(x[1])#3
print(x())#error
# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')#Sec<\n>Cyb
print(a())#Hyd
#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())#Sec<\n>Cyb<\n>Hyd<\n>None
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')#Sec<\n>Cyb
print(type(a)) #<class 'function'>
print(a) #Hyd<\n>None
for  x  in  a:
	print(x)#Hyd
a() 
print(a[0]())#Hyd