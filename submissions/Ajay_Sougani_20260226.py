import math;

a = int(input("Enter first side : "))
b = int(input("Enter second side : "))
c = int(input("Enter third side : "))

# finding that sides are qualifying triangle or not
if a+b>c or b+c>a or a+c>b:
    if a==b==c:
        print("This is an equilateral triangle")
        area =  math.sqrt(3) / 4 * a ^ 2
        print("area: ", area);
    elif a==b or b==c or c==a:
        print("this is isoscles triangle")
        perimeter = a+b+c
        print("perimeter: ", perimeter)
    else:
        print("this is scalene triangle")
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c)) 
        print("area: ", area);
else :
    print("given inputs don't form a triangle")


import math;
a = int(input("enter the a value: "));
b = int(input("enter the b value: "));
c = int(input("enter the c value: "));
if a!=0:
    disc =  b ^ 2 - 4*a*c
    print("Discriminant:", disc)
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / 2*a;
        root2 = (-b - math.sqrt(disc)) / 2*a
        print("root1: ", root1, "root2: ", root2)
    elif disc == 0:
        print("Roots are Real and Same")
        root = -b/2;
        print("root1: ", root);
        print("root2: ", root);

    else:
        print("Roots are Complex (Imaginary)")
        real = -b/2*a;  
        img =  math.sqrt(-disc) / 2*a;
        root1 = complex(real, img)
        root2 = complex(real, -img)
        print("root1:", root1, "root2:", root2)
else:
    print("Coefficient 'a' should not be 0 for a quadratic equation.")

import math;
x = float(input("enter the x coordinate: "))
y = float(input("enter the y coordinate: "))
r = float(input("enter the radius: "))
distance =  math.sqrt(x ** 2 + y ** 2)
print("distance from the origin: ", distance)
if r>0:
    if distance > r:
        print(" Outside  the  circle")
    else:
        if distance < r:
            print("Inside  the  circle")
        else:
            print(" On  the  circle")
else:
    print("Radius must be positive")

m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # Bye

i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # Two

m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # End

m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Bye

ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') #Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') # Bye

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

