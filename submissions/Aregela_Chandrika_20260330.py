# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class'tuple'>
print(x) # (<function, 3, 70, 1.4)
for  y  in   x:
	print(y) # 3 <nextLine> 70 <nextLIne> 1.2
print(x[0](9 , 2))  # 9+2=11
print(x[1]) # 3
print(x()) # 



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # sec <nextLine> Cyb <nextLine> Hyd <nextLIne> None


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # sec <nextLine> Cyb <nextLine> Hyd



# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a))  # <class 'tuple'>
print(a)  # <function..lambda>
for  x  in  a:
	print(x)
a() 
print(a[0]())