#Outputs Homework #1
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # 'Bye'


#Outputs Homework #2
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # error because _ object needs to be at the end of all cases


#Outputs Homework #3
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # error because _ object needs to be at the end of all cases


#Outputs Homework #4
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # 'Hyd' <> 'Bye'


#Outputs Homework #5
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
print('Bye') # 'Book' <> 'Bye'


#Outputs Homework #6
'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # 'Hyd' <> 'Sec' <> 'Cyb' <> 'Bye'
2) What  are  the  outputs  if  input  is  15  ?  ---> # 'One' <> 'Two' <> 'Three' <> 'Bye'
3) What  are  the  outputs  if  input  is  10.8  ?  ---> # 'India' <> 'China' <> 'Bye'
4) What  are  the  outputs  if  input  is  0  ?  ---> # 'Hyd' <> 'Sec' <> 'Cyb <> 'Bye'
5) What  are  the  outputs  if  input  is  -10  ?  ---> # 'One' <> 'Two' <> 'Three' <> 'Bye'
6) What  are  the  outputs  if  input  is  7  ?  ---> # 'Hyd' <> 'Sec' <> 'Cyb <> 'Bye'
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


#Outputs Homework #7
'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> # 'Quadrant'
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> # 'x-axis'
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> # 'y-axis'
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> # 'Origin'
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> # 'Not a point'
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> # 'Quadrant'
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> # 'Not a point'
8) What  is  the  output  when  input  is  ()  ?  ---> # 'Not a point'
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> # 'Not a point'
10) What  is  the  output  when  input  is  (25,) ?  ---> # 'Not a point'
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # 'Not a point'
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


#Outputs Homework #8
while  True:
	print('Hello')
print('Bye') # infinite loop of 'Hello'


#Outputs Homework #9
while  False:
	print('Hello')
print('Bye') # 'Bye'



#Programming Homework #1
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
'''
Sample Output 1:

Enter 1st side : 3

Enter 2nd side : 4

Enter 3rd side : 5

Scalene triangle

Area : 6.00

Perimeter : 12.0
Press any key to continue...


Sample Output 2:

Enter 1st side : 7

Enter 2nd side : 8

Enter 3rd side : 7

Isoscles triangle

Perimeter : 22.0
Press any key to continue...


Sample Output 3:

Enter 1st side : 7

Enter 2nd side : 7

Enter 3rd side : 7

Equilateral triangle

Area : 21.22
Press any key to continue...

Sample Output 4:

Enter 1st side : 7

Enter 2nd side : 8

Enter 3rd side : 16

Not a triangle
Press any key to continue...
'''
import math

try:
    a = float(input('Enter the length of the 1st side:'))
    b = float(input('Enter the length of the 2nd side:'))
    c = float(input('Enter the length of the 3rd side:'))

    s = (a + b + c)/2

    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print('The given sides make an Equilateral Triangle.')
            print(f'Area: {math.sqrt(3) / 4 * a ** 2:.2f}')
        elif a == b or a == c or b == c:
            print('The given sides make an Isoceles Triangle.')
            print(f'Perimeter: {a + b + c}')
        else:
            print('The given sides make an Scalene Triangle.')
            print(f'Area: {math.sqrt(s * (s - a) * (s - b) * (s - c)):.2f}')
            print(f'Perimeter: {a + b + c}')
    else:
        print('The given sides do not make a Triangle.')
except:
    print('The given inputs can either be an integer or a float number.')



#Programming Homework #2
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
'''
Sample Output 1:

Enter value of a : 5

Enter value of b : 6

Enter value of c : 5

Roots are imaginary (or) complex

Root 1 : -0.6 + 0.8j

Root 2 : -0.6 - 0.8j
Press any key to continue...


Sample Output 2:

Enter value of a : 5

Enter value of b : 10

Enter value of c : 5

Roots are real and equal

Root 1 : -0.1

Root 2 : -0.1
Press any key to continue...


Sample Output 3:

Enter value of a : 3

Enter value of b : 10

Enter value of c : 3

Roots are real and distinct

Root 1 : -0.33

Root 2 : -3.00
Press any key to continue...


Sample Output 4:

Enter value of a : 0

Value of a can not be 0
Press any key to continue...
'''
import math

try:
    a = float(input('Enter the value of a:'))
    b = float(input('Enter the value of b:'))
    c = float(input('Enter the value of c:'))

    d = b ** 2 - 4 * a * c

    if a != 0:
        if d > 0:
            print('The roots are Real and Distinct.')
            print(f'Root 1: {(-b + math.sqrt(d)) / (2 * a):.2f}')
            print(f'Root 2: {(-b - math.sqrt(d)) / (2 * a):.2f}')

        elif d == 0:
            print('The roots are Real and Same.')
            print(f'Root 1: {-b / (2 * a):.2f}')
            print(f'Root 2: {-b / (2 * a):.2f}')
        else:
            print('The roots are Complex (or) Imaginary.')
            r = -b / (2 * a)
            i = math.sqrt(-d) / (2 * a)
            print(f'Root 1: {r:.2f} + {i:.2f}j')
            print(f'Root 2: {r:.2f} - {i:.2f}j')
    else:
        print('The value of "a" cannot be 0.')
except:
    print('The values of the inputs need to be either integers or float values.')


    
#Programming Homework #3
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
'''
Sample Output:

Enter the value of x : 3

Enter the value of y : 4

Enter the radius of circle : 5

Point is on the circle
Press any key to continue...
'''
import math

try:
    x = float(input('Enter the value of x:'))
    y = float(input('Enter the value of y:'))
    r = float(input('Enter the radius of the circle:'))

    d = math.sqrt(x ** 2 + y ** 2)

    if d == r:
        print('The point is on the circle.')
    elif d > r:
        print('The point is outside the circle.')
    else:
        print('The point is inside the circle.')
except:
    print('The inputs must be either integer numbers or float numbers.')



#Programming Homework #4
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
'''
#Code Not Working (Doubt)

units = int(input('Enter  units :   '))  
match  units:
    case range(0 , 101):
        cost = (units * 3.00)
    case range(101 , 201):
        cost = (100 * 3.00) + ((units - 100) * 3.50)
    case  range(201 , 401):
        cost = (100 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)
    case  range(401 , 701):
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + ((units - 400) * 4.50)
    case  _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + ((units - 700) * 5.00)
print('Bill  amount  :  ' , cost)
'''
units = int(input('Enter  units :   '))  
match  units:
    case units if units in range(0 , 101):
        cost = (units * 3.00)
    case units if units in range(101 , 201):
        cost = (100 * 3.00) + ((units - 100) * 3.50)
    case  units if units in range(201 , 401):
        cost = (100 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)
    case  units if units in range(401 , 701):
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + ((units - 400) * 4.50)
    case  _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + ((units - 700) * 5.00)
print('Bill  amount  :  ' , cost)

