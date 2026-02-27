'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''

import math
def triangle(x,y,z):
    if(not(x+y > z and y+z > x and z+x > y)):
        print("Not a Triangle")
    elif(x == y and y == z):
        print("Equilateral triangle")
        print(F'Area : {(math.sqrt(3)/4)*(x**2):.2f}')
    elif(x == y or y == z or x==z):
        print("Isosceles triangle")
        print(F'Perimeter : {(x+y+z):.1f}')
    else:
        s=(x+y+z)/2
        print("Scalene triangle")
        print(F'Area : {math.sqrt(s*(s-x)*(s-y)*(s-z)):.2f}')
        print(F'Perimeter : {(x+y+z):.1f}')
    
a=float(input('Enter 1st side :'))
b=float(input('Enter 2nd side :'))
c=float(input('Enter 3rd side :'))
triangle(a,b,c)
        
'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  --->   (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  --->  (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j
'''
def roots():
    a=float(input('Enter value of a :'))
    if(a==0):
        print('Value of a can not be 0')
        return; # or exit()
    b=float(input('Enter value of b :'))
    c=float(input('Enter value of c :'))
    d=(b**2)-(4*a*c)
    if(d==0):
        print("Roots are real and equal")
        r = -b/(2*a)
        print(F"Root 1 : {r:.1f} \nRoot 1 : {r:.1f}")
    elif(d>0):
        print("Roots are real and distinct")
        print(F'Root 1 : {(-b+(d**0.5))/(2*a):.2f} \nRoot 2 : {(-b-(d**0.5))/(2*a):.2f}')
    else:
        print("Roots are imaginary (or) complex")
        print(F'Root 1 : {(-b+(d**0.5))/(2*a):.1f} \nRoot 2 : {(-b-(d**0.5))/(2*a):.1f}')
        
roots()
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math
def distance(x,y,r):
    d=math.sqrt(x*x +y*y)
    if(d==r):
        print('Point is on the  circle')
    elif(d>r):
        print("Point is outside the  circle")
    else:
        print("Point is inside the  circle")
x = float(input('Enter value of x : ')) 
y = float(input('Enter value of y : ')) 
r = float(input('Enter radius of circle : ')) 
distance(x,y,r)

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
#Bye
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:            # case _ must be used at end
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') 
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')
#Hello
#End

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
#Hyd
#Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')
#Book
#Bye
'''
1) What  are  the  outputs  if  input  is  -6 ? --->
#Hyd
#Sec
#Cyb
#Bye

2) What  are  the  outputs  if  input  is  15  ?  --->
#One
#Two
#Three
#Bye

3) What  are  the  outputs  if  input  is  10.8  ?  --->
#India
#China
#Usa
#Bye

4) What  are  the  outputs  if  input  is  0  ?  --->
#Hyd
#Sec
#Cyb
#Bye

5) What  are  the  outputs  if  input  is  -10  ?  --->
#One
#Two
#Three
#Bye

6) What  are  the  outputs  if  input  is  7  ?  --->
#Hyd
#Sec
#Cyb
#Bye


'''
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---># #Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---># x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---># y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---># Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->#Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> #Not  a  point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->#Not  a  point
8) What  is  the  output  when  input  is  ()  ?  --->#Not  a Point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->#Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->#Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->#Not  a  point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')

'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units					Rs. 3.00 / unit

Next  100  units				    Rs. 3.50 / unit

Next  200  units		    	         Rs. 4.00 / unit

Next  300  units				Rs. 4.50 / unit

Above  700  units				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))  
match  ???:
	case  ??:
				cost = 
	case  ???:
				cost =  
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)

'''
units = int(input('Enter  units in 100"s only :   '))  
match  units//100:
	case  1:
				cost = units*3.0
	case  2:
				cost = 100*3.0+units*3.50 
	case  3:
				cost = 100*3.0+100*3.50+units*4.50
	case  4:
				cost = 100*3.0+100*3.50+units*4.50
	case  5:
				cost = 100*3.0+100*3.50+units*4.50
	case  6:
				cost = 100*3.0+100*3.50+units*4.50
	case  7:
				cost = 100*3.0+100*3.50+units*4.50
	case  _ :
				cost = 100*3.0+100*3.50+200**4.50+units*5.00
	
print('Bill  amount  :  ' , cost)

#  Find  outputs
while  True:
	print('Hello')
print('Bye')
#Hello
#Hello
#Hello
:
:
:
stack out of memory error
#  Find  outputs
while  False:
	print('Hello')
print('Bye')

#Bye

