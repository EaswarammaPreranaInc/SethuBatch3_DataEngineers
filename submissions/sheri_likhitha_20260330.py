# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))		#<class 'tuple'>	
print(x)		#(<function <lambda> at address of thge object, 3, 70, 1.42)
for  y  in   x:
	print(y)	#<function <lambda> , address of the object<next line>3<next line>70<next line>1.42 
print(x[0](9 , 2))	#11  
print(x[1])		#3
print(x())		#error tuple object is not callable



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())	#Sec <next line> Cyb <next line> Hyd <next line> None
 


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')	#Sec <next line> Cyb
print(type(a))	#<class 'tuple'> 
print(a) 	#(<function <lambda> , address of the object None None)
for  x  in  a:
	print(x)	#<function <lambda> , address of the object<next line>None<next line>None
a()	#error 
print(a[0]())	#Hyd <next line> None