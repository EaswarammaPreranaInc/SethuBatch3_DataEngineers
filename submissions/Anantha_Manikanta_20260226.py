'''
1) Write  a  program  to  determine  three  sides  form  a  triangle  or  not
'''

import math
a = int(input("Enter  1st  side : "))
b = int(input("Enter  2nd  side : "))
c = int(input("Enter  3rd  side : "))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Equilateral  triangle")
        area = (math.sqrt(3) / 4) * a * a
        print("Area :", round(area, 2))
    elif a == b or b == c or a == c:
        print("Isosceles  triangle")
        perimeter = a + b + c
        print("Perimeter :", perimeter)
    else:
        print("Scalene  triangle")
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Area :", round(area, 2))
        print("Perimeter :", perimeter)
else:
    print("Not  a  triangle")

'''
2) Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
'''
import math
a = int(input("Enter  value  of  a : "))
if a == 0:
    print("Value  of  a  can  not  be  0")
else:
    b = int(input("Enter  value  of  b : "))
    c = int(input("Enter  value  of  c : "))
    disc = b*b - 4*a*c
    if disc > 0:
        print("Roots  are  real  and  distinct")
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
        print("Root 1 :", r1)
        print("Root 2 :", r2)
    elif disc == 0:
        print("Roots  are  real  and  equal")
        r = -b / (2*a)
        print("Root 1 :", r)
        print("Root 2 :", r)
    else:
        print("Roots  are  imaginary  (or)  complex")
        real = -b / (2*a)
        imag = math.sqrt(-disc) / (2*a)
        print("Root 1 :", real, "+",imag, "j")
        print("Root 2 :", real, "-",imag, "j")
'''
3) Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'
'''
import math
x = int(input("Enter  value  of  x : "))
y = int(input("Enter  value  of  y : "))
r = int(input("Enter  radius  of  circle : "))
distance = math.sqrt(x*x + y*y)
if distance > r:
    print("Point  is  outside  the  circle")
elif distance < r:
    print("Point  is  inside  the  circle")
else:
    print("Point  is  on  the  circle")
'''
4) Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Bye
'''
'''
4)  Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')  # Error because _ should be last
'''
'''
5) # Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')  # Error because _ should be last
'''
'''
6)   Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')  # Error because case 1 cant be repeated multiple times
'''
'''
8) # Find  outputs  (Home  work)
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
print('Bye')  # Book <nextline> Bye
'''
''' 9)
1) What  are  the  outputs  if  input  is  -6 ? --->  'Hyd' <nextline> 'Sec' <nextline> 'Cyb' <nextline> 'Bye'
2) What  are  the  outputs  if  input  is  15  ?  ---> 'One' <nextline> 'Two'<nextline> 'Three'  <nextline> 'Bye'
3) What  are  the  outputs  if  input  is  10.8  ?  ---> 'India' <nextline> 'China' <nextline> Usa <nextline> 'Bye'
4) What  are  the  outputs  if  input  is  0  ?  ---> 'Hyd' <nextline> 'Sec' <nextline> 'Cyb' <nextline> 'Bye'
5) What  are  the  outputs  if  input  is  -10  ?  ---> 'One' <nextline> 'Two'<nextline> 'Three'  <nextline> 'Bye'
6) What  are  the  outputs  if  input  is  7  ?  --->  'Hyd' <nextline> 'Sec' <nextline> 'Cyb' <nextline> 'Bye'
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
'''
10)
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->  Not a point
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
'''
11) Write  a  program  to  determine  bill  amount  and  input  is  units
'''
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
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (u - 700) * 5.00
print('Bill  amount  :  ', cost)
'''
# 12) Find  outputs
while  True:
	print('Hello') # Hello
print('Bye')

# 13) Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye