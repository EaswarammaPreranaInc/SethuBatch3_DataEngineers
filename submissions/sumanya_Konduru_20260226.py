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
import math

a = float(input('Enter 1st input : '))
b = float(input('Enter 2nd input : '))
c = float(input('Enter 3rd input : '))

try:
    if a + b >c and a + c > b and b + c > a :
    if (a == b == c):
        print('Equilateral Triangle')
        Area = (math.sqrt(3))/4*a**2
        print(f'Area : {(Area):.2f}')
    elif (a == b or b == c or c == a):
        print('Isoscles triangle')
        p = a + b + c
        print(f'Perimeter : {p}')
    else : 
        print('Scalene triangle')
        s = (a+b+c)/2 
        print(f'Area : {math.sqrt(s*(s-a)*(s-b)*(s-c))}')
        print(f'Area : {area:.2f}')
        print(f'Perimeter : {2*s}')
else : 
    print('Not a triangle')
except:
    print('Input should be a number')

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
import math
a = float(input('Enter value of a : '))
if a == 0 : 
    print('value of a can not be 0')
    exit()
b = float(input('Enter value of b : '))
c = float(input('Enter value of c : '))

disc = b**2 - 4*a*c 
if disc > 0 :
    print('real and distinct')
    root1 = (-b + math.sqrt(disc))/2*a
    root2 = (-b - math.sqrt(disc))/2*a
    print(f'Root1 : {root1:.2f}')
    print(f'Root2 : {root2:.2f}')
elif disc < 0:
    print('Roots are imaginary or complex')
    real = -b / (2*a)
    imag = math.sqrt(-disc)/(2*a)
    print(f'Root1 : {real} + {imag}')
    print(f'Root2 : {real} + {imag}')
else:
    print('Roots are real and equal')
    root = -b / (2*a)
    print(f'Root 1 : {root}')
    print(f'Root 2 : {root}')
'''
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
'''
import math
x = float(input('Enter value of x : '))
y = float(input('Enter value of y : '))
r = float(input('Enter radius of circle : '))

d = math.sqrt(x**2+y**2)
if d > r :
    print('Point is outside of the circle')
elif d < r :
    print('Point is inside of the circle')
else:
    print('Point is on the circle')
'''

# Find  outputs  (Home  work)
m = 4
match  m:
	case 1:
	    print('One')
	case 2:
	    print('Two')
	case 3:
	    print('Three')
print('Bye') # Bye 

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # Error due to case _ of the match 

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # Error due to case_ of the match 

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') '''
             Hyd
             Bye
             '''

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
print('Bye') '''
             Book 
             Bye 
             '''

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # Hyd <next line> Sec <nextline> Cyb 
2) What  are  the  outputs  if  input  is  15  ?  ---> # One <next line> Two <next line> Three  
3) What  are  the  outputs  if  input  is  10.8  ?  ---> # India <next line> China <next line> Usa 
4) What  are  the  outputs  if  input  is  0  ?  ---> # Hyd <next line> Sec <nextline> Cyb 
5) What  are  the  outputs  if  input  is  -10  ?  ---> # One <next line> Two <next line> Three 
6) What  are  the  outputs  if  input  is  7  ?  ---> # Hyd <next line> Sec <nextline> Cyb 
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
print('Bye') # Bye 

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---># Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> # x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> # y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> # Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---># Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> # Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---># y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> # Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> # Not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> # Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # Not a point
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

#  Find  outputs
while  True:
	print('Hello')
print('Bye') # Hello in Infinity loop  


'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)		    	Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(units >= 700)		Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0: # units  between  0  and  99
		cost = units * 3.00
	case  1: # units  between  100 and  199
		cost =  100 * 3.00 + (units - 100) * 3.50
	case  2|3: # units between 200 and 399
	    cost = (100 * 3.00 +100 * 3.50 + (units - 200) * 4.00)
	case  4|5|6:
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 +(units - 400) * 4.50
	case  _:				
		cost = 100 * 3.00 + 100 * 3.50 + 200 * 4+300 * 4.50 +(units - 700) * 5
print('Bill  amount  :  ' , cost)

#  Find  outputs
while  False:
	print('Hello') # nothing is printed
print('Bye') # Bye 
 