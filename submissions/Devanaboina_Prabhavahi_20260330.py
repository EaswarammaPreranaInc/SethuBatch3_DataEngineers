# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) #<class tuple>
print(x) # 70 , 3, 1,428 , 17
for  y  in   x:
	print(y) # 
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # Type error



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')  # Sec, Cyb , Hyd
print(a()) # None



# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb') # Sec, Cyb
print(a())  # Hyd


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class tuple> 
print(a)  # Sec, Cyb
for  x  in  a:
	print(x) # error
a() 
print(a[0]()) # error