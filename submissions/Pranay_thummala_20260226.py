# Write  a  program  to  determine  three  sides  form  a  triangle  or  not

# 1) Find  area  if  it  is  an  equilateral  triangle
#     What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
#     What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

# 2) Find  perimeter  if  it  is  an  isosceles  triangle
#     What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
#     What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

# 3) Find  both  if  it  is  scalene  triangle
#     What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
#     What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
# 	What  is  the  value  of  's'  ?  --->  	(a + b + c) / 2
#     What   is  the  perimeter  of  scalene  triangle ?  --->  a + b + c

# 4) What  is  the  qualification  of  triangle  ?  --->  Sum  of  every  two  sides  should  be  >  3rd  side

# 5) Hint: Use  nested  if
import math

# Input three sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check qualification of triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a Triangle")
    
    # Equilateral Triangle
    if a == b == c:
        print("It is an Equilateral Triangle")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area of Equilateral Triangle:", area)
    
    else:
        # Isosceles Triangle
        if a == b or b == c or a == c:
            print("It is an Isosceles Triangle")
            perimeter = a + b + c
            print("Perimeter of Isosceles Triangle:", perimeter)
        
        else:
            # Scalene Triangle
            print("It is a Scalene Triangle")
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter = a + b + c
            print("Area of Scalene Triangle:", area)
            print("Perimeter of Scalene Triangle:", perimeter)

else:
    print("The given sides do NOT form a Triangle")



#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import math

# Input coefficients
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Check if a is not zero
if a != 0:
    
    # Calculate discriminant
    D = b**2 - 4*a*c
    
    # Case 1: D > 0 (Real and distinct roots)
    if D > 0:
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print("Roots are real and distinct")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    
    # Case 2: D == 0 (Real and equal roots)
    elif D == 0:
        root = -b / (2*a)
        print("Roots are real and equal")
        print("Root 1 = Root 2 =", root)
    
    # Case 3: D < 0 (Complex roots)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        print("Roots are complex")
        print("Root 1 =", real_part, "+", imaginary_part, "i")
        print("Root 2 =", real_part, "-", imaginary_part, "i")

else:
    print("Coefficient 'a' should not be zero (Not a quadratic equation)")



#Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle. Center  is  origin  and  radius  is  'r'
# Input values

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
r = float(input("Enter radius: "))

# Calculate distance squared from origin
value = x**2 + y**2
radius_square = r**2

# Check position of point
if value < radius_square:
    print("Point lies Inside the Circle")
elif value == radius_square:
    print("Point lies On the Circle")
else:
    print("Point lies Outside the Circle")   




# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')  # Output: Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: # error
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
	case  _:  
		print('Bye')
print('End') # Output: Hello End


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Output: Hyd Bye


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
print('Bye') # Output: Book Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd Sec Cyb Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One Two Three Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India China Usa Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd Sec Cyb Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One Two Three Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd Sec Cyb Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> x - axis Bye
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis Bye
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis Bye
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin Bye
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not  a  point Bye
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Not  a  point Bye
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y - axis Bye
8) What  is  the  output  when  input  is   ()   ?   ---> Not a point Bye
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not  a  point Bye
10) What  is  the  output  when  input  is  (25,) ?  ---> Not  a  point Bye
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Not  a  point Bye
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
First  100  units				Rs. 3.00 / unit

Next  100  units				Rs. 3.50 / unit

Next  200  units		    	        Rs. 4.00 / unit

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


units = int(input('Enter units : '))

match units:
    
    # First 100 units
    case u if u <= 100:
        cost = u * 3.00
    
    # Next 100 units (101–200)
    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50
    
    # Next 200 units (201–400)
    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00
    
    # Next 300 units (401–700)
    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50
    
    # Above 700 units
    case u if u > 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + \
               (300 * 4.50) + (u - 700) * 5.00

print('Bill amount :', cost)


#  Find  outputs
while  True:
	print('Hello')
print('Bye') # Output: Hello Hello Hello .... (infinite loop, 'Bye' will never be printed)



#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Output: Bye (The loop will not execute, so only 'Bye' will be printed)