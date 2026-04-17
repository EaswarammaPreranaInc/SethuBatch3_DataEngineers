# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # <class 'tuple'>
print(x) # 3, 70, 1.42
for  y  in   x:
	print(y) #  3 <next line> 70 <next line> 1.42
print(x[0](9 , 2)) # 11
print(x[1]) # 3
print(x()) # error


#---------------------------------------------------------------
#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())

#output 
Sec
Cyb
Hyd
None
#------------------------------------------------------------------

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())

#output---------

Sec
Cyb
Hyd

#------------------------------------------------------------------------------


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #"sec", "Cyd"  <class "tuple">
print(a) 
for  x  in  a:
	print(x) # "Hyd" , "sec", "Cyd"
a() # Hyd
print(a[0]()) # none