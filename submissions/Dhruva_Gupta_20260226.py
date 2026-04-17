1)
 import math
a=eval(input("Enter 1st number: "))
b=eval(input("Enter 2nd number: "))
c=eval(input("Enter 3rd number: "))
if a==b==c:
    print("Equilateral triangle")
area=math.sqrt(3)*a*a/4
print(f”{area=}")

2)
import math
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
if a != b and b != c and a != c:
    print("Scalene triangle")
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"{area=}")
perimeter = (a + b + c)
print(f”{perimeter=}")

3)
import math
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a == b or a == c or b == c:
    print("Isosceles Triangle")

print(f"Perimeter={a+b+c}")

4)
import math
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))

if a+b>c and a+c>b and c+b>a:
    print("Valid triangle")
else: 
    print("Invalid triangle")

5)
import math
import cmath
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
d = b**2 - 4*a*c   # discriminant
if d < 0:
    print("Roots are imaginary (or) complex")
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
else:
    print("Roots are real")
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
print("Root 1 :", root1)
print("Root 2 :", root2)

6)
import math
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
d = b**2 - 4*a*c   # discriminant
if d == 0:
    print("Roots are real and equal")
    root = -b / (2*a)
    print("Root 1 :", root)
    print("Root 2 :", root)

7)
import math
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
d = b**2 - 4*a*c   # discriminant
if d > 0:
    print("Roots are real and distinct")
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Root 1 :", round(root1, 2))
    print("Root 2 :", round(root2, 2))

8)
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

9)
units = int(input('Enter units : '))
match units:
    case u if u <= 100:
        cost = u * 3.00
    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50
    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00
    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50
    case _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (units - 700) * 5.00
print('Bill amount : ', cost)

10)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print(‘Bye')

#Bye

11)
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print(‘Bye')

#Default case should be at end

12)
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print(‘End')

#Syntax error

13)#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print(‘Bye')

#Error

14)
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
print(‘Bye')

#Book
#Bye

15)
1) What  are  the  outputs  if  input  is  -6 ? —> Hyd Sec Cyb Bye(new lines)
2) What  are  the  outputs  if  input  is  15  ?  —> One Two Three Bye(new lines)
3) What  are  the  outputs  if  input  is  10.8  ?  —> India China Use bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd Sec Cyb Bye(new lines)
5) What  are  the  outputs  if  input  is  -10  ?  ---> One Two Three Bye(new lines)
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd Sec Cyb Bye(new lines)
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

16)
1) What  is  the  output  when  input  is  (-10 , -20) ?  —> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  —>x axis
3) What  is  the  output  when  input  is  (0 , -20) ?  —>y axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  —>not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->not a point
8) What  is  the  output  when  input  is  ()  ?  --->not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->not a point
10) What  is  the  output  when  input  is  (25,) ?  --->not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->not a point
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
		print('Not  a  point’)

17)
#  Find  outputs
while  True:
	print('Hello')
print(‘Bye') 

#Hello….never stops

18)
#  Find  outputs
while  False:
	print('Hello')
print(‘Bye')

#Bye
