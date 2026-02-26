import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("The given sides form a triangle.")
    if a == b == c:
        print("It is an Equilateral Triangle.")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area:", area)
    else:
        if a == b or b == c or a == c:
            print("It is an Isosceles Triangle.")
            perimeter = a + b + c
            print("Perimeter:", perimeter)
        else:
            print("It is a Scalene Triangle.")
            perimeter = a + b + c
            s = perimeter / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Perimeter:", perimeter)
            print("Area:", area)
else:
    print("The given sides do NOT form a triangle.")


import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
if a != 0:
    disc = b**2 - 4*a*c
    print("Discriminant:", disc)
    if disc > 0:
        print("Roots are Real and Distinct")
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        print("Root 1:", root1)
        print("Root 2:", root2)
    else:
        if disc == 0:
            print("Roots are Real and Same")
            root = -b / (2*a)
            print("Root 1:", root)
            print("Root 2:", root)
        else:
            print("Roots are Complex (Imaginary)")
            real_part = -b / (2*a)
            imag_part = math.sqrt(-disc) / (2*a)
            root1 = complex(real_part, imag_part)
            root2 = complex(real_part, -imag_part)
            print("Root 1:", root1)
            print("Root 2:", root2)
else:
    print("Coefficient 'a' should not be 0 for a quadratic equation.")


import math

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
r = float(input("Enter radius: "))
distance = math.sqrt(x**2 + y**2)
print("Distance from origin:", distance)
if r > 0:
    if distance > r:
        print("Point is Outside the Circle.")
    else:
        if distance < r:
            print("Point is Inside the Circle.")
        else:
            print("Point is On the Circle.")
else:
    print("Radius must be positive.")
	

m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')   # Bye


m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')   # Hello
	case  _:  
		print('Bye')
print('End')   # End

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
print('Bye')   # Bye


units = int(input('Enter  units :   '))  
match units:
	case u if u <= 100:
		cost = u * 3.00
	case u if u <= 200:
		cost = 100*3.00 + (u-100)*3.50
	case u if u <= 400:
		cost = 100*3.00 + 100*3.50 + (u-200)*4.00
	case u if u <= 700:
		cost = 100*3.00 + 100*3.50 + 200*4.00 + (u-400)*4.50
	case _:
		cost = 100*3.00 + 100*3.50 + 200*4.00 + 300*4.50 + (units-700)*5.00

print('Bill  amount  :  ' , cost)	#Bill amount :  5300.0


while  True:
	print('Hello')
print('Bye')


while  False:
	print('Hello')

print('Bye')		#Bye
