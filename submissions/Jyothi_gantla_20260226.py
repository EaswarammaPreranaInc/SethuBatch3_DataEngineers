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
a = float(input("Enter 1st side : "))
b = float(input("Enter 2nd side : "))
c = float(input("Enter 3rd side : "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("Equilateral triangle")
        area = (math.sqrt(3) / 4) * a * a
        print("Area :", round(area, 2))
    else:
        if a == b or b == c or a == c:
            print("Isosceles triangle")
            perimeter = a + b + c
            print("Perimeter :", perimeter)
        else:
            print("Scalene triangle")
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter = a + b + c
            print("Area :", round(area, 2))
            print("Perimeter :", perimeter)

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
a = float(input("Enter value of a : "))
if a == 0:
    print("Value of a can not be 0")
else:
    b = float(input("Enter value of b : "))
    c = float(input("Enter value of c : "))

    disc = b**2 - 4*a*c
    if disc > 0:
        print("Roots are real and distinct")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Root 1 :", root1)
        print("Root 2 :", root2)

    elif disc == 0:
        print("Roots are real and equal")
        root = -b / (2*a)
        print("Root 1 :", root)
        print("Root 2 :", root)

    else:
        print("Roots are imaginary (or) complex")
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Root 1 :", real_part, "+", imag_part, "j")
        print("Root 2 :", real_part, "-", imag_part, "j")
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
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


#find outputs(Home Work)
m = 4
match m:
    case 1:
        print('One')      # (No output)
    case 2:
        print('Two')      # (No output)
    case 3:
        print('Three')    # (No output)
print('Bye')              # Bye

#identify error
i = 2
match i:
    case 1:
        print('One')
    case _:#Error
        print('None of the above')
    case 2: # this will never execute
        print('Two')
print('Bye')
#find outputs(Home Work)
m = 2
match m:
    case 1:
        print('One')
    case _:
        print('Hello')    #  SyntaxError here
    case _:               
        print('Bye')
print('End')

#find outputs(Home Work)
m = 1
match m:
    case 1:
        print('Hyd')      # Hyd
    case 1:               # SyntaxError: duplicate pattern  
        print('Sec')
    case 1:
        print('Cyb')
print('Bye')

#find outputs(Home Work)

ch = 'B'
match ch:
    case 'A':
        print('Apple')
    case 'B':
        print('Book')     # Book
    case 'C':
        print('Cafe')
    case _:
        print('None of the above')
print('Bye')              # Bye



'''
1) What  are  the  outputs  if  input  is  -6 ? --->Hyd<next line>Sec<next line>Cyd<next line>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One<next line>Two<next line>Three<next line>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->Does not match any thing ,it goes to case_ India<next line>China<next line>Usa<next line>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd<next line>Sec<next line>Cyd<next line>Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One<next line>Two<next line>Three<next line>Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd<next line>Sec<next line>Cyd<next line>Bye
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
2) What  is  the  output  when  input  is  (10 , 0) ?  --->X-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->Y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Y-axis
8) What  is  the  output  when  input  is  ()  ?  --->Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not a point
10) What  is  the  output  when  input  is  (25,) ?  --->Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not a point
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

Next  100  units				Rs. 3.50 / unit

Next  200  units		    	Rs. 4.00 / unit

Next  300  units				Rs. 4.50 / unit

Above  700  units				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''

units = int(input('Enter units : '))

match units:
    case u if u <= 100:
        cost = u * 3.00
    case u if u <= 200:
        cost = 100 * 3.00 + (u - 100) * 3.50
    case u if u <= 400:
        cost = 100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00
    case u if u <= 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (u - 400) * 4.50
    case u if u > 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (u - 700) * 5.00

print('Bill amount :', cost)


#  Find  outputs
while  True:
	print('Hello')  #Hello<next line>Hello<next line> Hello infinitely
print('Bye')
#  Find  outputs
while  False:
	print('Hello')
print('Bye')  #Bye



		
