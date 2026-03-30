# Tricky  program

# Find  outputs

a = 10
b = 7


x = lambda  a , b :  a + b ,  a - b , a * b , a / b

print(type(x))  = <class 'tuple'>

print(x) = Prints Function Address

for  y  in   x:
	print(y)

print(x[0](9 , 2)) = 11

print(x[1]) = 3

print(x()) = Error

#..............................................................................................>

#  Tricky  program

# Find  outputs

a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')

print(a()) = Sec
             Cyb
             Hyd
             None

#..............................................................................................>

# Find  outputs (Home  work)

a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')

print(a()) = Sec
             Cyb
             Hyd

#..............................................................................................>

# Find  outputs   (Home  work)

a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')

print(type(a)) = <class 'tuple'>

print(a) = Prints Function Address

for  x  in  a:
	print(x)
 
a() = Error

print(a[0]()) = Error

#..............................................................................................>