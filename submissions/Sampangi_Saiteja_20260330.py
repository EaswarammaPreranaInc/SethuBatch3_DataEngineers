# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b

print(type(x))        # <class 'tuple'>
print(x)              # (<function <lambda> at 0x...>, 3, 70, 1.4285714285714286)

for  y  in   x:
	print(y)
# <function <lambda> at 0x...>
# 3
# 70
# 1.4285714285714286

print(x[0](9 , 2))    # 11
print(x[1])           # 3
print(x())            # ERROR 


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
# Sec
# Cyb

print(a())  
# Hyd
# None


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
# Sec
# Cyb

print(a())  
# Hyd


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')

print(type(a))        # <class 'tuple'>
print(a)              # (<function <lambda> at 0x...>, None, None)

for  x  in  a:
	print(x)
# <function <lambda> at 0x...>
# None
# None

a()  
# ERROR (tuple is not callable)

print(a[0]())  
# Hyd
# None