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
x=float(input("Enter 1st side:"))
y=float(input("Enter 2nd side:"))
z=float(input("Enter 3rd side:"))

if x+y>z and y+z>x and x+z>y:
    if x ==y ==z:
    	print("Equilateral Triangle")
    	area=math.sqrt(3)/4 * x**2
    	print(f"area:{area}")
    elif x==y or y==z or x==z:
        print("Isosceles trianlge")
        perimeter = x+y+z
        print(f"perimeter:{perimeter}")
    else:
        print("scalene triangle")
        s=(x+y+z)/2
        area=math.sqrt(s*(s-x)*(s-y)*(s-z))
        perimeter=x+y+z
        print(f"area:{area}")
        print(f"perimeter:{perimeter}")
else:
    print("Not a triangle")








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

import math
a=eval(input("Enter value of a :"))
b=eval(input("Enter value of b :"))
c=eval(input("Enter value of c :"))

D=b**2-4*a*c
print(D)

if D>0:
    print("roots are real and distinct")
    root_1 = (-b + math.sqrt(disc)) / 2*a
    root_2 = (-b - math.sqrt(disc)) / 2*a
    print(f"root_1:{root_1}")
    print(f"root_2:{root_2}")
    
elif D<0:
    print("roots are complex or imaginary")
    real_part = -b / 2*a
    imag_part = math.sqrt(-D) / 2*a
    print(f"root_1:{real_part}")
    print(f"root_2:{imag_part}")
    
else:
    print("roots are real and same")
    root= -b/2*a
    print(f"root:{root}")



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  radius ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < radius ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  radius   are  same ?  ---> On  the  circle
'''


import math

x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
r = float(input("Enter radius of circle: "))

distance = math.sqrt(x**2 + y**2)

if distance > r:
    print("Point is outside the circle")
elif distance < r:
    print("Point is inside the circle")
else:
    print("Point is on the circle")






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
#O/P: Bye


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#O/P: error,wildcard '_' makes remaining patterns unreachable



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
#O/P: error,wildcard '_' makes remaining patterns unreachable


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

#O/P: 
Hyd 
Sec
Cyb
Bye


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
#O/P: 
Book
Bye



'''
1) What  are  the  outputs  if  input  is  -6 ? --->
2) What  are  the  outputs  if  input  is  15  ?  --->
3) What  are  the  outputs  if  input  is  10.8  ?  --->
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->
6) What  are  the  outputs  if  input  is  7  ?  --->
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

#output:
if  input  is  -6 ? --->
Hyd
Sec
Cyb
Bye
if  input  is  15  ?  --->
One
Two
Three
Bye
if  input  is  10.8  ?  --->
India
China
Usa
Bye
if  input  is  0  ?  --->
Hyd
Sec
Cyb
Bye
if  input  is  -10  ?  --->
One
Two
Three
Bye
if  input  is  7  ?  --->
Hyd
Sec
Cyb
Bye





'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> #O/P:Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->#O/P: x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->#O/P:y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->#O/P:Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> #O/P:Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->#O/P:Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->#O/P:y-axis
8) What  is  the  output  when  input  is  ()  ?  --->#O/P:not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->#O/P:Not a quadrant
10) What  is  the  output  when  input  is  (25,) ?  --->#O/P:Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->#O/P:Not a point
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

Next  100  units				        Rs. 3.50 / unit

Next  200  units		    	                Rs. 4.00 / unit

Next  300  units			        	Rs. 4.50 / unit

Above  700  units				        Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''	

units = int(input("Enter units: "))

bill = 0

match units:
    
    case u if u <= 100:
        bill = u * 3.00

    case u if u <= 200:
        bill = 100 * 3.00 + (u - 100) * 3.50

    case u if u <= 400:
        bill = (100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00)

    case u if u <= 700:
        bill = (100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (u - 400) * 4.50)

    case u if u > 700:
        bill = (100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (u - 700) * 5.00)

print("Bill amount:", bill)






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
print('Bill  amount  :  ' , cost)'''




#  Find  outputs
while  True:
	print('Hello')
print('Bye')

#O/P:
Hello
Hello
Hello
Hello
Hello
....infinite times


#  Find  outputs
while  False:
	print('Hello')
print('Bye')

#O/P:
Bye