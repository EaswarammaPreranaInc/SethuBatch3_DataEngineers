# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class 'tuple'>
print(x)#(10,3,70,1.42)
for  y  in   x:
	print(y)#10<next line>3<next line>70<next line>1.42
print(x[0](9 , 2))#11
print(x[1])#error
print(x())#error

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())#Sec<next line>Cyb<next line>Hyd<next line>None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())#Sec<net line>Cyb<next line>Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<function <lambda> and address in hexa-decimal)
print(a) #Hyd<nextline>Hyd<next line>Hyd
for  x  in  a:
	print(x)#H<next line>y<next line>d
a() #nothing not printed
print(a[0]())#H