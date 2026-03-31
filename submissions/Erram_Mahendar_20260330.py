# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) #function
print(x)       #typr and address

for  y  in   x:
	print(y) #17 , 3, 70, 1.4
print(x[0](9 , 2)) #11
print(x[1])   #3
print(x())   # #17 , 3, 70, 1.4



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

#sec
cyb
Hyd


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

#sec
cyb
Hyd

 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  #class function
print(a)  #type and address
for  x  in  a:
	print(x) #Hyd
a() #None
print(a[0]()) #type