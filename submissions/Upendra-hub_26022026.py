1.# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
#output:-Bye(bcz there is no case 4)

2.# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#output:-Syntax error(bcz '_' it should be at the end of the match but not in the middle of the match)

3.# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')
#output:-error

4.#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
#output:-Hyd
        Bye

5.# Find  outputs  (Home  work)
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
#output:-Book
        Bye


6.'''
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
#output:-
If Input is: -6
Hyd
Sec
Cyb
Bye
If Input is:7
Hyd
Sec
Cyb
Bye
If Input is:0
Hyd
Sec
Cyb
Bye

If Input is:-10
One
Two
Three
Bye
If Input is:15
One
Two
Three
Bye

If Input is:_
India
China
Usa

7.'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not  a  point
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

8.#  Find  outputs
while  True:
	print('Hello')
print('Bye')
#output:-Hello
         Hello(continuously prints Hello)

9.#  Find  outputs
while  False:
	print('Hello')
print('Bye')
# output:-Bye

10.'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle-----> sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle -----> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
    What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

5) Hint: Use  nested  if
'''

import math
a = float(input("Enter 1st side: "))
b = float(input("Enter 2nd side: "))
c = float(input("Enter 3rd side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    # 1) Equilateral Triangle (All sides same)
    if a == b == c:
        print("Type: Equilateral Triangle")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print(f"Area: {area:.2f}")
    # 2) Isosceles Triangle (two sides same)
    elif a == b or b == c or a == c:
        print("Type: Isosceles Triangle")
        perimeter = a + b + c
        print(f"Perimeter: {perimeter:.2f}")
    # 3) Scalene Triangle (All sides different)
    else:
        print("Type: Scalene Triangle")
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Perimeter: {perimeter:.2f}")
        print(f"Area: {area:.2f}")
else:
    print("\nStatus: NOT a triangle.")

10.'''
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
def determine_roots():
    #print("--- Quadratic Equation Solver ---")
    a = float(input("Enter coefficient a : "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    if a == 0:
        print("It is not a quadratic equation")
        return
    disc = b**2 - 4*a*c
    if disc > 0:
        print("Nature of roots: Real and distinct")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif disc == 0:
        print("Nature of roots: Real and same")
        root = -b / (2*a)
        print(f"Root: {root}")
    else:
        print("Nature of roots: Complex (or) Imaginary roots")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print(f"Root 1: {real_part} + {imag_part}j")
        print(f"Root 2: {real_part} - {imag_part}j")
determine_roots()


11.'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
import math
x = float(input("Enter the x-coordinate : "))
y = float(input("Enter the y-coordinate : "))
r = float(input("Enter the radius(r): "))
distance = math.sqrt(x**2 + y**2)
print(f"Radius: {r}")
if distance > r:
    print("Result: The point lies Outside the circle.")
elif distance < r:
    print("Result: The point lies Inside the circle.")
else:
    print("Result: The point is on the circle.")

12.'''
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

units = int(input('Enter  units :   '))  
match units:
    case u if u <= 100:
        cost = u * 3.00

    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50

    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00

    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50

    case u if u > 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + \
               (300 * 4.50) + (u - 700) * 5.00

print('Bill amount : ', cost)

































