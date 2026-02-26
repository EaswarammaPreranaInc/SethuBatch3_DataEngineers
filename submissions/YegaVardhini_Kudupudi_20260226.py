'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2
p
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
a=float(input ('Enter 1st side : ') ) 
b=float(input ('Enter 2nd side : ') ) 
c=float(input ('Enter 3rd side : ') ) 
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
            print('Equilateral Triangle ')
            print ('Area : ',math.sqrt(3) /4*a**2)
    elif a==b or a==c or b==c:
        print('Isosceles Triangle')
        print('Perimeter : ',a+b+c)
            
    else:
        print('Scalene Triangle ')
        s=(a+b+c)/2
        print('Area : ',math.sqrt(s*(s-a)*(s-b)*(s-c)))
        print('Perimeter :', a+b+c)
            
else:
    print('Not a Triangle')

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
a=eval(input ('Enter value of a : ')) 
b=eval(input ('Enter value of b : ')) 
c=eval(input ('Enter value of c : ')) 
disc = b**2-(4*a*c)
if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Nature: Real and Distinct")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

elif disc == 0:
        root = -b / (2*a)
        print("Nature: Real and Same")
        print(f"Root: {root}")

else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Nature: Complex (Imaginary)")
        print(f"Root 1: {real_part} + {imag_part}j")
        print(f"Root 2: {real_part} - {imag_part}j")

'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''


import math
x=float(input("Enter value of x : "))
y=float(input("Enter value of y : "))
r=float(input("Enter radius of circle : "))
distance = math.sqrt(x**2 + y**2)
print(f"Distance from origin: {distance:.2f}")
print(f"Radius: {r}")
try:
    if distance > r:
        print("Point is Outside the circle")
    elif distance < r:
        print("Point is Inside the circle")
    else:
        print("Point is On the circle")
except:
    print("Enter numerical values")


# Find  outputs  (Home  work)
m = 4
match  m: #False
	case  1:
		print('One') # ignored
	case  2:
		print('Two')# ignored
	case  3:
		print('Three') # ignored
print('Bye') # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: # SyntaxError coz this case makes the match unreachable to other present cases
		print('None of   the  above')
	case  2:
		print('Two') # Two
print('Bye') # Bye

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  # SyntaxError coz this case makes the match unreachable to other present cases
		print('Hello')
	case  _:  
		print('Bye') #Bye
print('End') # End

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec') # ignored as duplicates
	case  1:
		print('Cyb') # ignored as duplicates
print('Bye') # Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') # Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') # Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd
                                                     Sec
                                                     Cyb
                                                     Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One
                                                       Two
                                                       Three
                                                       Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India 
                                                         China
                                                         Usa 
                                                         Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd
                                                      Sec
                                                      Cyb
                                                      Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One
                                                        Two
                                                        Three
                                                        Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd
                                                      Sec
                                                      Cyd
                                                      Bye
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
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not  a point
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
units = int(input('Enter  units :   '))

match units:
    case u if u <= 100:
        cost = u * 3.0
    case u if u <= 200:
        cost = (100 * 3.0) + (u - 100) * 3.5
    case u if u <= 400:
        cost = (100 * 3.0) + (100 * 3.5) + (u - 200) * 4.0
    case u if u <= 700:
        cost = (100 * 3.0) + (100 * 3.5) + (200 * 4.0) + (u - 400) * 4.5
    case u:
        cost = (100 * 3.0) + (100 * 3.5) + (200 * 4.0) + (300 * 4.5) + (u - 700) * 5.0
print('Bill  amount  :  ' , cost)


#  Find  outputs
while  True:
	print('Hello') # Hello -- multiple no. of times
print('Bye') # Bye


#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye