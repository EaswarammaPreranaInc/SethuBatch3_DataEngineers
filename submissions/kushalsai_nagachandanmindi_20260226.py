# Write  a  program  to  determine  three  sides  form  a  triangle  or  not
from math import *
a = float(input("Enter 1st side : "))
b = float(input("Enter 2nd side : "))
c = float(input("Enter 3rd side : "))
if (a+b>c) and (b+c>a) and (a+c>b):
    if a==b==c:
        print("Equilateral triangle")
        print("Area : ", sqrt(3) / 4 * a ** 2)
    else :
        if a==b or b==c or a==c:
            print("Isoscles triangle")
            print("Perimeter : ", a + b + c)
        else:
            print("Scalene triangle")
            s=(a + b + c) / 2
            print("Area : ", sqrt(s * (s - a) * (s - b) * (s - c)))
            print("Perimeter : ", a + b + c)
else:
    print("Not a Triangle")

#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
from math import *
a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
if a!=0:
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        print("Real  and  distinct")
        print("Root1 : ", (-b + sqrt(disc)) / (2 * a))
        print("Root2 : ", (-b - sqrt(disc)) / (2 * a))
    elif disc == 0:
        print("Real  and  same")
        print("Root1 : ", (-b + sqrt(disc)) / (2 * a))
        print("Root2 : ", (-b - sqrt(disc)) / (2 * a))
    elif disc < 0:
        print("Complex  (or)  Imaginary  roots")
        real = -b / (2 * a)
        imag = sqrt(-disc) / (2 * a)
        print("Root 1 :", round(real,2), "+", round(imag,2), "j")
        print("Root 2 :", round(real,2), "-", round(imag,2), "j")
else:
    print("Value of a can not be 0")

#Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle. Center  is  origin  and  radius  is  'r'
from math import *
x = float(input("Enter value of x : "))
y = float(input("Enter value of x : "))
r = float(input("Enter radius of circle : "))
distance = sqrt(x**2 + y**2)
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
print('Bye')        # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')        # Error underscore is not implemented in middle 

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # Error

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
print('Bye')    # Book <Nextline> Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <nextline> Sec <nextline> Cyb <nextline> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One <nextline> Two <nextline> Three <nextline> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India <nextline> China <nextline> Usa <nextline> Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd <nextline> Sec <nextline> Cyb <nextline> Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One <nextline> Two <nextline> Three <nextline> Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd <nextline> Sec <nextline> Cyb <nextline> Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y - axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not  a  point
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
	
#Write  a  program  to  determine  bill  amount  and  input  is  units
units = int(input('Enter  units :   '))  
match  units:
	case  100:
				cost = 3.00
	case  200:
				cost = 3.50
	case  400:
				cost = 4.00
	case  700:
				cost = 4.50
	case  _:				
				cost = 5.00
print('Bill  amount  : ' , cost)

#  Find  outputs
while  True:
	print('Hello')
print('Bye')     # Hello <nextline> ....infinty times Bye will be never executed 

#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye asloop is false so exit's the loop