 # Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))  # <class function>
print(x)    #  <function <lambda>  >
for  y  in   x:
	print(y)   #   17 3 70  1.43
print(x[0](9 , 2))    # 11    (9,2)
print(x[1])    #  3  (10,3)
print(x())   #  Error



 #  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())      #  Sec  Cyb  Hyd  None



 # Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())     #  Sec  Cyb  Hyd



 # Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # <  class function >
print(a)     #  < function <lambda>  and address>
for  x  in  a:
	print(x)    #  Error
a()      #   Hyd  Sec   Cyb
print(a[0]())  #   Error
