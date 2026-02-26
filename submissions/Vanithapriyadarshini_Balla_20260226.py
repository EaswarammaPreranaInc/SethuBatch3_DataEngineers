# Write  a  program  to  determine  three  sides  form  a  triangle  or  not

import math
try:
    x=float(input("Enter 1st input : "))
    y=float(input("Enter 2nd input : "))
    z=float(input("Enter 3rd input : "))
    perimeter= x+y+z
    if x+y > z and y+z and x and z+x > y :
        if x==y and y==z and z==x :
            print('Equilateral triangle')
            Area= math.sqrt(3)/4 * x**2
            print(f'Area : {Area:.2f}')
        elif (x==y and x!=z and y!=z) or (y==z and z!=x and y!=x) or (z==x and z!=y and x!=y) :
            print('Isoscles triangle')
            print(f'Perimeter : {perimeter}')
        else :
            s= (x+y+z)/2
            Area= math.sqrt(s*((s-x)*(s-y)*(s-z)))
            print('Scalene triangle')
            Area= math.sqrt(s*((s-x)*(s-y)*(s-z)))
            print(f'Area :  {Area:.2f}')
            print(f'Perimeter : {perimeter}')
    else :
        print('Not a triangle')
except :
    print('Invalid input')

# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import cmath
import math
try:
    a = float(input("Enter value a: "))
    if a==0 :
        print('Value of a cannot be 0 ')
    else :
        b = float(input("Enter value b: "))
        c = float(input("Enter value c: "))
        dis = (b**2) - (4*a*c)
        if dis < 0 :
            print("Roots are Real and Imaginary")
            r1 = (-b + cmath.sqrt(dis)) / (2*a)
            r2 = (-b - cmath.sqrt(dis)) / (2*a)
            print(f' Root 1 : {r1}')
            print(f' Root 2 : {r2}')
        elif dis > 0 :
            print("Roots are Real and Distinct")
            r1 = (-b + math.sqrt(dis)) / (2*a)
            r2 = (-b - math.sqrt(dis)) / (2*a)
            print(f' Root 1 : {r1:.2f}')
            print(f' Root 2 : {r2}')
            
        else :
            r1 = (-b / (2*a))
            r2 = r1
            print("Roots are Real and Equal")
            print(f' Root 1 : {r1}')
            print(f' Root 2 : {r2}')
except:
    print("Input should be integer or float")

# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

import math
try:
    x = float(input("Enter value of x : "))
    y = float(input("Enter value of y : "))
    r = float(input("Enter radius of circle : "))
    dis = math.sqrt(x**2 + y**2)
    if dis > r :
        print("Point is Outside the circle")
    elif dis < r :
        print("Point is inside the circle")
    else :
         print("Point is on Circle")
except:
     print("Input should be an number")

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:                 # 'case_' should be at the end of cases
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
	case  _:               #  Error bcz, only one anonymous should be present
		print('Bye')
print('End')

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # Hyd 
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')                 # Bye


# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')   # Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')                    # Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? --->  Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One<nextline>Two<nextline>Three<nextline><Bye>
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India<nextline>China<nextline>Usa<nextline>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->  Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One<nextline>Two<nextline>Three<nextline><Bye>
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
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
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y -- axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y -- axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Quadrant 
10) What  is  the  output  when  input  is  (25,) ?  ---> Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not a point
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


# Write  a  program  to  determine  bill  amount  and  input  is  units


unit = int(input('Enter  units :   '))  
match  unit:
	case  unit if unit<=100:
				cost = unit * 3.00
	case  unit if unit<=200:
				cost = 100*3.00 + (unit - 100)*3.50
	case  unit if unit<=400:
				cost = 100*3.00 + 100*3.50 + (unit - 200)*4.00
	case  unit if unit<=700:
				cost = 100*3.00 + 100*3.50 + 200*4.00 + (unit - 400)*4.50
	case  _:				
				cost = 100*3.00 + 100*3.50 + 200*4.00 + 300*4.5 + (unit - 700)*5.0
print('Bill  amount  :  ' , cost)

#  Find  outputs
while  True:
	print('Hello') # Hello ----- unitl cond becomes false it will iterate
print('Bye')           # Bye ----- printed 

#  Find  outputs
while  False:
	print('Hello')
print('Bye')           # Bye




        

