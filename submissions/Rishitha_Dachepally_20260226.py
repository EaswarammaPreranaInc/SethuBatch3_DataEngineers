# Write  a  program  to  determine  three  sides  form  a  triangle  or  not

# 1) Find  area  if  it  is  an  equilateral  triangle
    # What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    # What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

# 2) Find  perimeter  if  it  is  an  isosceles  triangle
    # What  is  an  isosceles  triangle ?  ---> Any  two  sides  are  same
    # What   is  the  perimeter  of  isosceles  triangle ?  ---> a + b + c

# 3) Find  both  if  it  is  scalene  triangle
    # What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    # What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	# What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
    # What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

# 4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

# 5) Hint: Use  nested  if

import math

a = float(input("Enter  1st  side  :  "))
b = float(input("Enter  2nd  side  :  "))
c = float(input("Enter  3rd  side  :  "))

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print("Equilateral  triangle")  # Equilateral  triangle
        area = (math.sqrt(3) / 4) * a * a
        print(f"Area  :  {area:.2f}")  # Area  :  21.22  (if sides are 7,7,7)

    elif a == b or b == c or a == c:
        print("Isosceles  triangle")  # Isosceles  triangle
        perimeter = a + b + c
        print(f"Perimeter  :  {perimeter}")  # Perimeter  :  22.0  (if sides are 7,8,7)

    else:
        print("Scalene  triangle")  # Scalene  triangle
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print(f"Area  :  {area:.2f}")  # Area  :  6.00  (if sides are 3,4,5)
        print(f"Perimeter  :  {perimeter}")  # Perimeter  :  12.0  (if sides are 3,4,5)

else:
    print("Not  a  triangle")  # Not  a  triangle  (if sides are 7,8,16)

# -----------------------------------------------------------------------------

# Write  a  program  to  determine  roots  of  a  quadratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

# 1) What  is  the  value  of  discriminant ?  ---> b ^ 2 - 4ac

# 2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     # What  is  the  formula  for  root1  ?  --->   (-b + sqrt(disc)) / 2a
     # What  is  the  formula  for  root2 ?  --->  (-b - sqrt(disc)) / 2a

# 3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     # What  is  the  formula  for  root  ?  --->  -b / 2a

# 4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     # What  is  the  formula  for  real  part ?  --->  -b / 2a
	 # What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 # What  is  root1  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 + 4j
	 # What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j

import math

a = float(input("Enter  value  of  a : "))
if a == 0:
    print("Value  of  a  can  not  be  0") # Value  of  a  can  not  be  0

else:
    b = float(input("Enter  value  of  b : "))
    c = float(input("Enter  value  of  c : "))

    disc = b**2 - 4*a*c

    if disc > 0:
        print("Roots  are  real  and  distinct") # Roots  are  real  and  distinct
        r1 = (-b + math.sqrt(disc)) / (2*a)
        r2 = (-b - math.sqrt(disc)) / (2*a)
        print(f"Root 1 : {r1:.2f}") # Root 1 : -0.33  (if a=3,b=10,c=3)
        print(f"Root 2 : {r2:.2f}") # Root 2 : -3.00  (if a=3,b=10,c=3)

    elif disc == 0:
        print("Roots  are  real  and  equal") # Roots  are  real  and  equal
        r = -b / (2*a)
        print(f"Root 1 : {r:.1f}") # Root 1 : -1.0  (if a=5,b=10,c=5)
        print(f"Root 2 : {r:.1f}") # Root 2 : -1.0  (if a=5,b=10,c=5)

    else:
        print("Roots  are  imaginary  (or)  complex") # Roots  are  imaginary  (or)  complex
        real = -b / (2*a)
        imag = math.sqrt(-disc) / (2*a)
        r1 = complex(real, imag)
        r2 = complex(real, -imag)
        print(f"Root 1 : {r1:.1f}") # Root 1 : -0.6+0.8j  (if a=5,b=6,c=5)
        print(f"Root 2 : {r2:.1f}") # Root 2 : -0.6-0.8j  (if a=5,b=6,c=5)

# -----------------------------------------------------------------------------

# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

# 1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

# 2) Where  is  the  point  if  distance >  radius ?  --->  Outside  the  circle

# 3) Where  is  the  point  if  distance < radius ?  --->  Inside  the  circle

# 4) Where  is  the  point  if  distance  and  radius   are  same ?  ---> On  the  circle

import math

x = float(input("Enter  value  of  x : "))
y = float(input("Enter  value  of  y : "))
r = float(input("Enter  radius  of  circle  : "))

distance = math.sqrt(x**2 + y**2)

if distance > r:
    print("Point  is  outside  the  circle") # Point  is  outside  the  circle

elif distance < r:
    print("Point  is  inside  the  circle") # Point  is  inside  the  circle

else:
    print("Point  is  on  the  circle") # Point  is  on  the  circle

# -----------------------------------------------------------------------------

# Find  outputs  (Home  work)

m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # Bye

# -----------------------------------------------------------------------------

# Identify  Error

i = 2
match  i:
	case  1:
		print('One')
	case  _:
		print('None of   the  above')
	case  2: # Error because wildcard case '_' must be the last case in match statement
		print('Two')
print('Bye')

# -----------------------------------------------------------------------------

# Find  outputs  (Home  work)

m = 2
match  m:
	case  1:
		print('One')
	case  _:
		print('Hello')
	case  _: # Error because multiple wildcard '_' cases are not allowed
		print('Bye')
print('End')

# -----------------------------------------------------------------------------

#  Find  outputs  (Home  work)

m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Bye

# -----------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------

# What are the outputs if input is -6 ? ---> Hyd Sec Cyb Bye

# What are the outputs if input is 15 ? ---> One Two Three Bye

# What are the outputs if input is 10.8 ? ---> India China Usa Bye

# What are the outputs if input is 0 ? ---> Hyd Sec Cyb Bye

# What are the outputs if input is -10 ? ---> One Two Three Bye

# What are the outputs if input is 7 ? ---> Hyd Sec Cyb Bye

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

# -----------------------------------------------------------------------------

# What is the output when input is (-10 , -20) ? ---> Quadrant

# What is the output when input is (10 , 0) ? ---> x - axis

# What is the output when input is (0 , -20) ? ---> y - axis

# What is the output when input is (0 , 0) ? ---> Origin

# What is the output when input is (10 , 20 , 30) ? ---> Not a point

# What is the output when input is [10 , 20] ? ---> Quadrant

# What is the output when input is [0 , -25] ? ---> y - axis

# What is the output when input is () ? ---> Not a point

# What is the output when input is {10 , 20} ? ---> Not a point

# What is the output when input is (25,) ? ---> Not a point

# What is the output when input is {10 : 20} ? ---> Not a point

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

# -----------------------------------------------------------------------------

# Write  a  program  to  determine  bill  amount  and  input  is  units

# Units                                                      Cost
# ------------------------------------------------------------
# First  100  units					Rs. 3.00 / unit

# Next  100  units				Rs. 3.50 / unit

# Next  200  units		    	Rs. 4.00 / unit

# Next  300  units				Rs. 4.50 / unit

# Above  700  units				Rs. 5.00 / unit
# ------------------------------------------------------------

# Let  units  be  1200
# What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

# Hint:  Use  match  ...  case   but  not  if ... else

# units = int(input('Enter  units :   '))
# match  ???:
# 	case  ??:
# 			cost =
# 	case  ???:
# 			cost =
# 	case  ???:
# 			cost =
# 	case  ???:
# 			cost =
# 	case  ???:
# 			cost =
# print('Bill  amount  :  ' , cost)

units = int(input('Enter  units :   '))

match units:
    
    case u if u <= 100:
        cost = u * 3.00

    case u if u <= 200:
        cost = 100 * 3.00 + (u - 100) * 3.50

    case u if u <= 400:
        cost = (100 * 3.00 +
                100 * 3.50 +
                (u - 200) * 4.00)

    case u if u <= 700:
        cost = (100 * 3.00 +
                100 * 3.50 +
                200 * 4.00 +
                (u - 400) * 4.50)

    case u:
        cost = (100 * 3.00 +
                100 * 3.50 +
                200 * 4.00 +
                300 * 4.50 +
                (u - 700) * 5.00)

print('Bill  amount  :  ', cost) # Bill  amount  :  5300.0  (if units = 1200)

# -----------------------------------------------------------------------------

#  Find  outputs

while  True:
	print('Hello')
print('Bye')
# Infinite loop because condition is always True

# -----------------------------------------------------------------------------

#  Find  outputs

while  False:
	print('Hello')
print('Bye') # Bye

