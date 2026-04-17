

#  Write  a  program  to  determine  three  sides  form  a  triangle  or  not

qualification of a triangle 
 try:
     if a+b>c and a+c>b or b+c>a:
         print('It is a triangle')
         if a==b and b==c:
             print("its equilateral")
             area=(math.sqrt(3) / 4) *( a ** 2)
             print(area)
         elif a==b or b==c or a==c:
             print('its isoscles triangle')
             perimeter=(a + b + c)
             print(perimeter)
         else:
             print('its a scalene')
             perimeter=(a+b+c)
             s=perimeter/2
             area=math.sqrt(s * (s - a) * (s - b) * (s - c))
             print(area)
     else:
         print("Its not a Triangle")

 except:
     print('nonnegative input')

    






# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0


'''1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  --->   (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  --->  (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j'''



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

 import math

 def r('(Enter radius)'):
  x=int(input('Enter value of x:'))
 y=int(input('Enter value of y:'))
 r=float(input("Enter radius"))
 distance=math.sqrt(x**2 + y**2)
 if distance>r:
     print(F'({x},{y}) is outside the circle' )
 elif  distance<r:
     print(F'({x},{y}) is inisde the circle')
 else:
     print(F'({a},{b}) is on the circle')


 
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:
		print('One')
		print('Two')
		print('Three')
	case  _:
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')


'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd<next line>Sec<next line>Cyb
2) What  are  the  outputs  if  input  is  15  ?  --->One<next line>Two<next line>Three
3) What  are  the  outputs  if  input  is  10.8  ?  --->India<next line>China<next line>Usa
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd<next line>Sec<next line>Cyb
5) What  are  the  outputs  if  input  is  -10  ?  --->One<next line>Two<next line>Three
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd<next line>Sec<next line>Cyb
'''


  # Find Output
  
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # Bye



# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two') # case opertaor should at last  
print('Bye')




# Print Output

m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # Hello<next line>End 



# Print Output
m = 1
match  m:
	case  1:
		print('Hyd')   # Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')



'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units					Rs. 3.00 / unit

Next  100  units				Rs. 3.50 / unit

Next  200  units		    	Rs. 4.00 / unit

Next  300  units				Rs. 4.50 / unit

Above  700  units				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
# units = int(input('Enter  units :   '))  
# match  1200:
# 	case  100
# 				cost = 3.00
# 	case  100:
# 				cost =  3.50
# 	case  200:
# 				cost =4.00
# 	case  300:
# 				cost = 4.50
# 	case  > 5000:				
# 				cost = 5.00
# print('Bill  amount  :  ' , cost)
 
 
 
 
 #  Find  outputs
while  True:  
	print('Hello')
print('Bye') # Hello <next line> Bye



 #  Find  outputs
while  False:
	print('Hello')
print('Bye')# Bye







