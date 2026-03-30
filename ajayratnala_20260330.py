#Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class function>
print(x)<function <lambda> id>
for  y  in   x:
	print(y)#(3   70   10/7    17)
print(x[0](9 , 2))#11
print(x[1])#3
print(x())#error


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
print(a())#Sec   Cyb  Hyb


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #class function
print(a) #function <lambda> id
for  x  in  a:
	print(x)#ERROR, function is not iterable
a() 
print(a[0]())#error
