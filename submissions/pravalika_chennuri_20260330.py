# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # class tuple
print(x) # (17,3,70,1.4)
for  y  in   x:
	print(y) # 17 <nextline> 3 <nextline> 70 <nextline> 1.4
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # error

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb') #Sec <nextline> Cyb <nextline>
print(a()) # Hyd

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb') # Sec <nextline> Cyb <nextline>
print(a()) # Hyd

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # function
print(a)  # function <nextline> None, <nextline> None
for  x  in  a:
	print(x) # None,None,Hyd
a()  # error
print(a[0]()) # None