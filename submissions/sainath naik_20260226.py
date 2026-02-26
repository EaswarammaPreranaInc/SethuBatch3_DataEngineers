1.Write  a  program  to  determine  three  sides  form  a  triangle  or  not

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

code:

import math

# Read three sides
a = float(input("Enter first side : "))
b = float(input("Enter second side : "))
c = float(input("Enter third side : "))

# Check triangle qualification
if (a + b > c) and (a + c > b) and (b + c > a):
    print("It forms a Triangle")

    # Equilateral Triangle
    if a == b == c:
        area = (math.sqrt(3) / 4) * a ** 2
        print("It is an Equilateral Triangle")
        print(f"Area = {area}")

    # Isosceles Triangle
    elif a == b or b == c or a == c:
        perimeter = a + b + c
        print("It is an Isosceles Triangle")
        print(f"Perimeter = {perimeter}")

    # Scalene Triangle
    else:
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("It is a Scalene Triangle")
        print(f"Perimeter = {perimeter}")
        print(f"Area = {area}")

else:
    print("It does NOT form a Triangle")


output:It forms a Triangle
       It is an Equilateral Triangle
       Area = 3.897114317029974




2.Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

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

code:

import math

# Read inputs
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

# Check a != 0
if a == 0:
    print("It is not a quadratic equation")
else:
    disc = b**2 - 4*a*c
    print(f"Discriminant = {disc}")

    # Case 1: Real and Distinct
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Roots are Real and Distinct")
        print(f"Root1 = {root1}")
        print(f"Root2 = {root2}")

    # Case 2: Real and Same
    elif disc == 0:
        root = -b / (2*a)
        print("Roots are Real and Same")
        print(f"Root1 = {root}")
        print(f"Root2 = {root}")

    # Case 3: Complex / Imaginary
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Roots are Complex (Imaginary)")
        print(f"Root1 = {real_part} + {imag_part}j")
        print(f"Root2 = {real_part} - {imag_part}j")


output: Discriminant = 1
        Roots are Real and Distinct
        Root1 = 3.0
        Root2 = 2.0


3.Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
 
code:

import math

# Read inputs
x = float(input("Enter x coordinate : "))
y = float(input("Enter y coordinate : "))
r = float(input("Enter radius : "))

# Step 1: Find distance from origin
distance = math.sqrt(x**2 + y**2)

print(f"Distance from origin = {distance}")

# Step 2, 3, 4: Compare distance with radius
if distance > r:
    print("Point is Outside the Circle")

elif distance < r:
    print("Point is Inside the Circle")

else:
    print("Point is On the Circle")


output: Distance from origin = 5.0
        Point is On the Circle


4.# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')


output: Bye


5.# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')


output: SynataxError



6.# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')


output: SyntaxError



7.#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')


output: Hyd
        Bye


8.# Find  outputs  (Home  work)
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


output: Book
        Bye

9.
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

code:

x = eval(input('Enter any  number :  '))
match x:
    case 7 | -6 | 0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case _:
        print('India')
        print('China')
        print('Usa')
# End of match
print('Bye')


output: Input = -6
        Hyd
        Sec
        Cyb
        Bye

        Input = 15
        One
        Two
        Three
        Bye

        Input = 10.8
        India
        China
        Usa
        Bye

        Input = 0
        Hyd
        Sec
        Cyb
        Bye

        Input = -10
        One
        Two
        Three
        Bye

        Input = 7
        Hyd
        Sec
        Cyb
        Bye

10.
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->
2) What  is  the  output  when  input  is  (10 , 0) ?  --->
3) What  is  the  output  when  input  is  (0 , -20) ?  --->
4) What  is  the  output  when  input  is  (0 , 0) ?  --->
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
8) What  is  the  output  when  input  is  ()  ?  --->
9) What  is  the  output  when  input  is  {10 , 20} ?  --->
10) What  is  the  output  when  input  is  (25,) ?  --->
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
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


output: 1) Input = (-10, -20)
        Quadrant

        2) Input = (10, 0)
        x - axis

        3) Input = (0, -20)
        y - axis

        4) Input = (0, 0)
        Origin

        5) Input = (10, 20, 30)
        Not a point

        6) Input = [10, 20]
        Quadrant

        7) Input = [0, -25]
        y - axis

        8) Input = ()
        Not a point

        9) Input = {10, 20}
        Not a point

        10) Input = (25,)
        Not a point

        11) Input = {10: 20}
        Not a point


11.Write  a  program  to  determine  bill  amount  and  input  is  units

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


code:

units = int(input('Enter units : '))

match units:
    
    # First 100 units
    case u if u <= 100:
        cost = u * 3.00

    # Next 100 units (101 - 200)
    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50

    # Next 200 units (201 - 400)
    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00

    # Next 300 units (401 - 700)
    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50

    # Above 700 units
    case u if u > 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + \
               (300 * 4.50) + (u - 700) * 5.00

print('Bill amount :', cost)


output: Bill amount : 5300.0


12.#  Find  outputs
while  True:
	print('Hello')
print('Bye')


output: Hello
        Hello
        Hello
        Hello
        Hello
        ...




13#  Find  outputs
while  False:
	print('Hello')
print('Bye')

output : Bye