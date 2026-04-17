# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) #class tuple
print(x) #function lambda at address (17,3,70,1.42)
for  y  in   x:
	print(y) # 17    3     70     1.42
print(x[0](9 , 2)) #11
print(x[1]) #3
#print(x())# error
#=========================================================================================================================
#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')  #Sec    Cyb
print(a())   # Hyd  None
#=========================================================================================================================
# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')  #Sec   Cyb
print(a())#  Hyd
#=========================================================================================================================
# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') #Sec    Cyb
print(type(a)) #class tuple
print(a) # function lambda at address , None ,None
for  x  in  a:
	print(x) #None  None  
#a() #error
print(a[0]()) #   Hyd    None 
