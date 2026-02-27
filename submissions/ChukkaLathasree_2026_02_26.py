
import math
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if (a + b > c):
    if (a + c > b):
        if (b + c > a):
            print("The given sides form a triangle")

            if a == b:
                if b == c:
                    print("It is an Equilateral Triangle")
                    area = (math.sqrt(3) / 4) * a ** 2
                    print("Area =", area)
                else:
                    print("It is an Isosceles Triangle")
                    perimeter = a + b + c
                    print("Perimeter =", perimeter)
            
            else:
                if a == c or b == c:
                    print("It is an Isosceles Triangle")
                    perimeter = a + b + c
                    print("Perimeter =", perimeter)
                else:
                    print("It is a Scalene Triangle")
                    s = (a + b + c) / 2
                    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    perimeter = a + b + c
                    print("Area =", area)
                    print("Perimeter =", perimeter)
        else:
            print("Not a triangle")
    else:
        print("Not a triangle")5
else:
    print("Not a triangle")


import math
a = float(input("Enter value of a != 0 "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))
if a != 0 :
    disc = b ** 2 - 4 * a * c
    print("discriminant =", disc)

    if disc > 0:
     print("Roots are real and Distinct")
     root1 = (-b + math.sqrt(disc)) / (2*a)
     root1 = (-b - math.sqrt(disc)) / (2*a)
     print("root1 =", root)
     print("root1 =", root)
    else:
     print("Iroots are complex (Imaginary)")
     real_part = -b / (2*a)
     image_part = math.sqrt(-disc) / (2*a)
     print("root1 =", real_part, "+", imag_part, "j")
     print("root2 =", real_part, "-", imag_part, "j")
else:
 print("Coefficient 'a' should not be zero")


import math
x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))
r = float(input("Enter radius of circle: "))
distance = math.sqrt(x**2 + y**2)
print("Distance from origin =", distance)
if r > 0:
    if distance > r:
        print("Point is Outside the circle")
    else:
        if distance < r:
            print("Point is Inside the circle")
        else:
            print("Point is On the circle")
else:
    print("Radius must be positive")


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')---> 'Bye'

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')--> case _ should not lie in between the prgm, 'Bye'


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')---> Error

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')--->'Hyd'
                'Bye'


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
print('Bye')---> 'Book'

'''


1) What  are  the  outputs  if  input  is  -6 ? --->False
2) What  are  the  outputs  if  input  is  15  ?  --->True
3) What  are  the  outputs  if  input  is  10.8  ?  --->False
4) What  are  the  outputs  if  input  is  0  ?  --->True
5) What  are  the  outputs  if  input  is  -10  ?  --->False
6) What  are  the  outputs  if  input  is  7  ?  --->True
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->False
2) What  is  the  output  when  input  is  (10 , 0) ?  --->True
3) What  is  the  output  when  input  is  (0 , -20) ?  --->False
4) What  is  the  output  when  input  is  (0 , 0) ?  --->True
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->True
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->True
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->False
8) What  is  the  output  when  input  is  ()  ?  --->False
9) What  is  the  output  when  input  is  {10 , 20} ?  --->True
10) What  is  the  output  when  input  is  (25,) ?  --->True
11) What  is  the  output  when  input  is  {10 : 20} ?  --->True
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
match  1200:
	case  100:
				cost = 3.00
	case  100:
				cost = 3.50 
	case  200:
				cost = 4.00
	case  300:
				cost = 4.50
	case  700:				
				cost = 5.00
print('Bill  amount  :  5300' , cost)

# Program using match-case

print("1 -> 100 * 3.00")
print("2 -> 100 * 3.50")
print("3 -> 200 * 4.00")
print("4 -> 300 * 4.50")
print("5 -> 500 * 5.00")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        result = 100 * 3.00
        print("Result =", result)
    case 2:
        result = 100 * 3.50
        print("Result =", result)
    case 3:
        result = 200 * 4.00
        print("Result =", result)
    case 4:
        result = 300 * 4.50
        print("Result =", result)
    case 5:
        result = 500 * 5.00
        print("Result =", result)
    case _:
        print("Invalid Choice")

#  Find  outputs
while  True:
	print('Hello')---> 'True'
print('Bye')-->'Bye'

#  Find  outputs
while  False:
	print('Hello')--->False
print('Bye')--->'Bye'

