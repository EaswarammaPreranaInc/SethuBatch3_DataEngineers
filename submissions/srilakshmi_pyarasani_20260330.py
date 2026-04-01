1) Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)#<class 'tuple'>
print(x)#Type and address
for  y  in   x:
	print(y)#Type and address
		 3
		 70
		 1.428
print(x[0](9 , 2))#11
print(x[1])#3
print(x())#Error because it has no args

2) outputs 
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())#sec
	   cyb
	   Hyd

3) Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())#sec
	   cyb
	   Hyd
	   None

4) outputs   
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')#sec
							       cyb
print(type(a)) #<class 'tuple>
print(a) # Type and address
for  x  in  a:
	print(x)#Type and address
a() 
print(a[0]())#None







