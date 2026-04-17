# Tricky  program
# Find  outputs
# a = 10
# b = 7
# x = lambda  a , b :  a + b ,  a - b , a * b , a / b
# print(type(x))#<class 'tuple'>
# print(x)#17  3  70  10/7
# for  y  in   x:
# 	print(y) # 3 <nextline> 70<nextline>  10/7
# print(x[0](9 , 2))#11
# print(x[1])#3
# print(x())#error

#  Tricky  program
# Find  outputs
# a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
# print(a())#Sec<nextline>Cyb<nextline>Hyd<nextline>none

# Find  outputs (Home  work)
# a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
# print(a())#Sec<nextline>Cyb<nextline>Hyd

# Find  outputs   (Home  work)
# a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
# print(type(a))#<function <lambda> address> 
# print(a)#Sec<nextline>Cyb<nextline>Hyd<nextline>none 
# for  x  in  a:
# 	print(x)#Hyd
# a()#error 
# print(a[0]())#None
