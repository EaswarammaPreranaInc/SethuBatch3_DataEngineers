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
import math

a = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))

# Equilateral Triangle
if a == b == c:
    print("The triangle is Equilateral")
    area_of_equilateral = (math.sqrt(3) / 4) * a ** 2
    print("Area of equilateral triangle:", area_of_equilateral)
    perimeter = 3 * a
    print("Perimeter:", perimeter)

# Isosceles Triangle
elif a == b or b == c or a == c:
    print("The triangle is Isosceles")
    perimeter = a + b + c
    print("Perimeter of isosceles triangle:", perimeter)

# Scalene Triangle
else:
    print("The triangle is Scalene")
    s = (a + b + c) / 2
    area_of_scalene = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of scalene triangle:", area_of_scalene)
    perimeter = a + b + c
    print("Perimeter of scalene triangle:", perimeter)
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
##code:
import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

if a == 0:
    print("Invalid input because a should not be 0")
else:
    disc = b**2 - 4*a*c
    print("Discriminant =", disc)

    # Case 1: Real and distinct
    if disc > 0:
        print("Roots are Real and Distinct")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Root1 =", root1)
        print("Root2 =", root2)

    # Case 2: Real and same
    elif disc == 0:
        print("Roots are Real and Same")
        root = -b / (2*a)
        print("Root1 =", root)
        print("Root2 =", root)

    # Case 3: Complex / Imaginary
    else:
        print("Roots are Complex (Imaginary)")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)

        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)

        print("Root1 =", root1)
        print("Root2 =", root2)
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
##code
import math

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
r = float(input("Enter radius: "))

# Distance from origin to point (x, y)
distance = math.sqrt(x*2 + y*2)

print("Distance from origin =", distance)

if distance > r:
    print("Point is Outside the circle")

elif distance < r:
    print("Point is Inside the circle")

else:
    print("Point is On the circle")
 # Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')#Bye
 # Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')#Bye
: # Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')#Hello
	case  _:  
		print('Bye')#Bye
print('End')#End
 #  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')#Bye
 # Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')'''
1) What  are  the  outputs  if  input  is  -6 ? --->#Hyd Sec Cyb
2) What  are  the  outputs  if  input  is  15  ?  ---> One Two Three
3) What  are  the  outputs  if  input  is  10.8  ?  --->India China Usa
4) What  are  the  outputs  if  input  is  0  ?  --->#Hyd Sec Cyb
5) What  are  the  outputs  if  input  is  -10  ?  --->One Two Three
6) What  are  the  outputs  if  input  is  7  ?  --->#Hyd Sec Cyb
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y-axis
8) What  is  the  output  when  input  is  ()  ?  --->not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->not a point
10) What  is  the  output  when  input  is  (25,) ?  --->not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->not a point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (…
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
units = int(input('Enter  units :   '))  
match  ???:
	case  ??:
				cost = 100*3.00
	case  ???:
				cost =  100*3.50
	case  ???:
				cost = 200*4.00
	case  ???:
				cost = 300*4.50
	case  ???:				
				cost = 500*5.00
print('Bill  amount  :  ' , cost)#5300.0
 #  Find  outputs
while  True:
	print('Hello')#Hello
print('Bye')#Bye
#  Find  outputs
while  False:
	print('Hello')
print('Bye')