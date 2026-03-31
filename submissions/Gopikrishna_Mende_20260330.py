# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x)) # < class tuple>
print(x) #  (function and address)
for  y  in   x:
	print(y) # <function <lambda> at 0x...> 
                                # 3
                                # 70
                                # 1.4285714285714286
print(x[0](9 , 2)) # 11
print(x[1]) #3
print(x())

# ===============================================================

#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) # Sec < next line> cyb <next line> Hyd < next line>

# =================================================================

# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) # sec <next line> Cyb <next line> Hyd <next line>

# ================================================================

# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb') # Hyd <next line> cyb <next line> sec <next line>
print(type(a))  # <class tuple>
print(a)  # 
for  x  in  a:
	print(x) # <lambda function  and address>
a() 
print(a[0]()) # none