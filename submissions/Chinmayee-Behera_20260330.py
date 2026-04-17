# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) #<class 'tuple'>
print(x) # tuple and address
for  y  in   x:
	print(y)
#17
#3
#70
1.42

print(x[0](9 , 2))
#11
print(x[1])
#3
print(x())
#(17, 3, 70, 1.42)

 #  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
#Sec
#Cyb
#Hyd
#None

 # Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
#Sec
#Cyb
#Hyd

 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<class 'tuple'>
print(a) # function and address
for  x  in  a:
	print(x)
#Hyd
#None
#Sec
#None
#Cyb
#None
a() 
#Hyd
#Sec
#Cyb

print(a[0]())
#Hyd
#None