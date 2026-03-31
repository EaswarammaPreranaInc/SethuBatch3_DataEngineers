# Tricky  program
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b 
print(type(x)) #<class tuple>
print(x) #<class function>  address of lambda 3,70,1.42 
for  y  in   x:
	print(y) 
'''
<class function>  address
3
70
1.42
'''
print(x[0](9 , 2)) # 11
print(x[1]) #3
print(x()) #Error


#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a()) #Sec  Cyb  Hyd None


# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a()) #Sec   Cyb    Hyd



# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')
print(type(a)) #class tuple
print(a) # class function lambda 
for  x  in  a:
	print(x)
a() 
print(a[0]()) 
'''
sec
cyb
<class 'tuple'>
(<function <lambda> at 0x7c72d2384180>, None, None)
<function <lambda> at 0x7c72d2384180>
None
None
Hyd
None

'''

