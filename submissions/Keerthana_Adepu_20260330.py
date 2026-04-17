# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'function'>
print(x) # type and address of lambda function
for  y  in   x:
	print(y) # 17 <> 3 <> 70 <> 1.42
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # (17 , 3 , 70 , 1.42)


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) 
'''
'Sec'
'Cyb'
'Hyd'
None
'''

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())
'''
'Sec'
'Cyb'
'Hyd'
'''


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) # <class 'tuple'>
print(a) # type and address of the lambda function 
for  x  in  a:
	print(x) # 'Hyd' <> 'Sec' <> 'Cyb'
a() # 'Hyd' <> 'Sec' <> 'Cyb'
print(a[0]()) # None
