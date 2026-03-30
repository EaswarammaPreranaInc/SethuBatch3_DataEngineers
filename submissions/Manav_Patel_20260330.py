

1)
# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) #class tuple
print(x) #type and id
for  y  in   x:
	print(y) #type and id,3,70,1.4 all in new line
print(x[0](9 , 2)) #11
print(x[1]) #3 
print(x()) #Error

2)
#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

Output-
Sec
Cyb
Hyd
None

3)
# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

Output-
Sec
Cyb
Hyd

4)
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a() 
print(a[0]())

Output-
Sec
Cyb
Class tuple
(Type and id, None, None)
Type and id
None
Error
