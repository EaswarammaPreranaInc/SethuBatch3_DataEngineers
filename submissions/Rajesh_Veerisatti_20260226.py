#  Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math

a = int(input("Enter 1st side : "))
b = int(input("Enter 2nd side : "))
c = int(input("Enter 3rd side : "))


if a + b > c and b + c > a and a + c > b:

    

    
    if a == b and b == c:
        area = (math.sqrt(3) / 4) * a**2
        print("Equilateral triangle")
        print("Area :", area)

    
    elif a == b or b == c or c == a:
        perimeter = a + b + c
        print("Isosceles triangle")
        print("Perimeter :", perimeter)

   
    else:
        perimeter = a + b + c
        s = perimeter / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Scalene triangle")
        print("Perimeter :", perimeter)
        print("Area :", area)

else:
    print("Not a triangle")


#  Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

import math

a = float(input("Enter value of a : "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c : "))

if a == 0:
    print("Not a quadratic equation")
else:
    disc = b**2 - 4*a*c
    print("Discriminant :", disc)

    # Case 1: Real and Distinct
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Roots are Real and Distinct")
        print("Root1 :", root1)
        print("Root2 :", root2)

    # Case 2: Real and Same
    elif disc == 0:
        root = -b / (2*a)
        print("Roots are Real and equal")
        print("Root1 :", root)
        print("Root2 :", root)

    # Case 3: Complex Roots
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(-disc) / (2*a)
        print("Roots are imaginary or complex")
        print("Root1 :", complex(real_part, imag_part))
        print("Root2 :", complex(real_part, -imag_part))


# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.Center  is  origin  and  radius  is  'r'

import math

x = float(input("Enter x coordinate : "))
y = float(input("Enter y coordinate : "))
r = float(input("Enter radius : "))


distance = math.sqrt(x**2 + y**2)

print("Distance from origin :", distance)

if distance > r:
    print("Point is Outside the circle")

elif distance < r:
    print("Point is Inside the circle")

else:
    print("Point is On the circle")

# Write  a  program  to  determine  bill  amount  and  input  is  units 
units = int(input("Enter units : "))

match True:

    
    case _ if units > 700:
        cost = (100 * 3.00) +(100 * 3.50) +(200 * 4.00) +(300 * 4.50) +((units - 700) * 5.00)

    
    case _ if units > 400:
        cost = (100 * 3.00) +(100 * 3.50) +(200 * 4.00) + ((units - 400) * 4.50)

    
    case _ if units > 200:
        cost = (100 * 3.00) +(100 * 3.50) + ((units - 200) * 4.00)

   
    case _ if units > 100:
        cost = (100 * 3.00) + ((units - 100) * 3.50)

    
    case _:
        cost = units * 3.00

print("Bill amount :", cost)