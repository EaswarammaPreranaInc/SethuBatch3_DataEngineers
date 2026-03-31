# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#class 'typle'
print(x)#(function type and address, 3 70 , 142)
for  y  in   x:
	print(y)#function type and address <nextline> 3 <nextline> 70 <nextline> 1.42
print(x[0](9 , 2))#11
print(x[1])#3
print(x())#error


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')#Sec <nextline> Cyb <nextline> 
print(a())Hyd <nextline> None


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')#Sec <nextline> Cyb
print(a())#Hyb


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')#Sec <nextline> Cyb
print(type(a)) #class 'typle'
print(a)#(function type and address of the function, None, None)
for  x  in  a:
	print(x)#function type and address <nextline> None <nextline> None
a()#error
print(a[0]())#Hyd <nextline> None


