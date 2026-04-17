# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class'tuple'>
print(x) # (17 , 3 , 70 , 1.42)
for  y  in   x:
	print(y) # (17 , 3 , 70 , 1.42)
print(x[0](9 , 2)) ((9 , 2),  3 , 70 ,1.42)
print(x[1]) # 3
print(x()) # type and addr of function


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec
             Cyb
             Hyd
             None


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # Sec
             Cyb
             Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'lambda'>
print(a)  # Sec
             Cyb
             Hyd
for  x  in  a:
	print(x) #Sec
                  Cyb
                  Hyd
a() # type and addr of lambda
print(a[0]()) # Error