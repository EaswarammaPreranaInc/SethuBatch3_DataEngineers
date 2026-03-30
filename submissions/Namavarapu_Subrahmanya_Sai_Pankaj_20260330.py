# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'Tuple'>
print(x) # tuple
for  y  in   x:
	print(y) # 17, 3, 70, 1.3
print(x[0](9 , 2)) # 11
print(x[1]) # 3
#print(x()) # error


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # None

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # 'Hyd'

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # <class 'Nonetype'>
print(a)  # None
for  x  in  a:
	print(x) # none type is not iterable
#a()  # None
print(a[0]()) # hyd, none

