# Tricky  program 
# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b
print(type(x))      #<class 'tuple'>
print(x)            #(<function <lambda> at 0x000001AFD9054680>, 3, 70, 1.4285714285714286)
for  y  in   x:
	print(y)        #<function <lambda> at 0x00000255318FA340>
                    #3
					#70
					#1.4285714285714286
print(x[0](9 , 2))  #11
print(x[1])         #3
print(x())          #Error due to tuple object is not callable



# Find  outputs (Home  work)
a  =  lambda  :   'Hyd' ;  print('Sec') ;  print('Cyb')
print(a())      #Sec
                #Cyb
                #Hyd



#  Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')
print(a())      #Sec
                #Cyb
                #Hyd    
                #None


# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')   #Sec
                                                                #Cyb
print(type(a))  #<class 'tuple'>
print(a)        #(<function <lambda> at 0x000003E5AB5AA340>, None, None)
for  x  in  a:
	print(x)    #<function <lambda> at 0x0000012038D3A340>
                #None
                #None
a()             # Error due to tuple object is not callable
print(a[0]())   #Hyd
                #None