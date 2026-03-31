# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))   <class 'function'>
print(x)   #  17
for  y  in   x:
	print(y)
print(x[0](9 , 2))
print(x[1])
print(x())




# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

#   Sec
    Cyb
    Hyd



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) 

#  Sec
   Cyb
   Hyd
   None



# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))   #  address of lambda function , none , none
print(a)   # address 
for  x  in  a:
	print(x)
a() 
print(a[0]())