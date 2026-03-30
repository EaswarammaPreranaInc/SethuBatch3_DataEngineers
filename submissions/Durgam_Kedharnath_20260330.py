
# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # class tuple
print(x) # class function 3 70 1.4
for  y  in   x:
	print(y) # class function<nextline>3<nextline>70<nextline>1.4
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # 



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec<nextline>Cyb<nextline>Hyd<nextline>None



# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec<nextline>Cyb<nextline>Hyd



# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # class tuple
print(a) # function lambda binary id of the function object
for  x  in  a:
	print(x) # Sec<nextline>Cyb<nextline>Hyd<nextline>None
a() # Sec<nextline>Cyb<nextline>None 
print(a[0]()) # Sec