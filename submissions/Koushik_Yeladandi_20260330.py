# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # Class function
print(x) # Error
for  y  in   x:
	print(y) # Error
print(x[0](9 , 2)) # Error
print(x[1]) #Error
print(x())  # Error




#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

# 'Sec'
  'Cyb'
  'Hyd'
  
  


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # class funtion
print(a)  # 'Hyd'
for  x  in  a:
	print(x)  # Error
a() 
print(a[0]()) # Error
print(a())    # Error








