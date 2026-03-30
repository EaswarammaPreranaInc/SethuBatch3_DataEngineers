# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))
print(x)
for  y  in   x:
	print(y)
print(x[0](9 , 2))
print(x[1])
print(x())

<class 'tuple'>
(<function <lambda> at 0x79548b37c220>, 3, 70, 1.4285714285714286)
<function <lambda> at 0x79548b37c220>
3
70
1.4285714285714286
<function <lambda> at 0x79548b37c220>
3





#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
Sec
Cyb
Hyd
None




# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
Sec
Cyb
Hyd





# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) 
print(a) 
for  x  in  a:
	print(x)
a()  --> error
print(a[0]()) 

Sec
Cyb
<class 'tuple'>
(<function <lambda> at 0x7c9ee4f2c180>, None, None)
<function <lambda> at 0x7c9ee4f2c180>
None
None
Hyd
None


 