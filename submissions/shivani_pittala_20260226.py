


#program to determine three sides of a triangle form a triangle or not

import math

# Input three sides
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The sides form a triangle.")

    
    if a == b and b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area =", round(area, 2))

    else:
        if a == b or b == c or a == c:
            print("It is an Isosceles Triangle.")
            perimeter = a + b + c
            print("Perimeter =", perimeter)
        else:
            print("It is a Scalene Triangle.")
            perimeter = a + b + c
            s = perimeter / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Perimeter =", perimeter)
            print("Area =", round(area, 2))
else:
    print("The sides do not form a triangle.")








#program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0


import math

a = int(input('Enter value of a(a!=): '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))


if a == 0:
    print("This is not a quadratic equation (a must not be 0).")
else:
    # Calculate discriminant
    disc = b**2 - 4*a*c
    print("\nDiscriminant =", disc)

    # Nested if for root types
    if disc > 0:
        print("Roots are Real and Distinct.")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Root1 =", round(root1, 2))
        print("Root2 =", round(root2, 2))

    else:
        if disc == 0:
            print("Roots are Real and Same.")
            root = -b / (2*a)
            print("Root =", round(root, 2))
        else:
            print("Roots are Complex (Imaginary).")
            real_part = -b / (2*a)
            imag_part = math.sqrt(-disc) / (2*a)
            root1 = complex(real_part, imag_part)
            root2 = complex(real_part, -imag_part)
            print("Root1 =", root1)
            print("Root2 =", root2)




#program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.

import math

# Input values
x = eval(input("Enter value of x : "))
y = eval(input("Enter value of y : "))
r = eval(input("Enter radius of circle: "))

# Calculate distance from origin
distance = math.sqrt(x**2 + y**2)
print("Distance from origin =", round(distance, 2))

# Nested if to check position
if distance > r:
    print("The point lies Outside the circle.")
else:
    if distance < r:
        print("The point lies Inside the circle.")
    else:
        print("The point lies On the circle.")




#finding outputs
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
 #output: Bye




















































