# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))#<class 'tuple'>
print(x) # (<function <lambda>>, 3, 70, 1.4285714285714286)

for  y  in   x:
	print(y)
'''
<function <lambda>>
3 
70 
1.4285714285714286'''

print(x[0](9 , 2))#11
print(x[1])#3
print(x())#error,tuple is not callable



# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd



 #  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())
'''
Sec
Cyb
Hyd
None


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #<class 'tuple'>
print(a) #
#Sec Cyb Hyd
for  x  in  a:
	print(x)
'''Sec
Cyb
Hyd'''
a() 
print(a[0]())