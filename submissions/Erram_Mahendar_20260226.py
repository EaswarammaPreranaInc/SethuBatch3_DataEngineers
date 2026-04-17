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


import math
a = float (input("enter 1st side of an triangle :"))
b = float (input("enter 1st side of an triangle :"))
c = float (input("enter 1st side of an triangle :"))
d = int (input("enter 1 if you want to get area or 2 if you want to get perimeter"))

if a+b>c and b+c > a and c+a > b:
	if d == 1:
		if a == b== c : 
			print(f'area of equilateral triangle : {math.sqrt(3) /4 * (a ** 2):.2f}')
		elif ((a==b and  b!=c) or ( a==c and a!=b) or (b==c and a!=b)):
			s= (a+b+c)/2
			print(f'area of an isoceles triangle : {math.sqrt(s * (s - a) * (s - b) * (s - c)) }')
		
		elif a!=b and b!=c and c!=a:
			s= (a+b+c)/2
			print(f'area of an scalen triangle : {math.sqrt(s * (s - a) * (s - b) * (s - c)) }')

elif d ==2:
	print(f'perimeter of the given triangle of sides {a}, {b}, {c} is {a + b+ c}')

else:
	print('f given sides are not valid try with another')

**************************************************************************


Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle



import math
x = float(input('enter x value:'))
y = float(input('enter y value:'))
r = float(input('enyter radius:'))
dist =math.sqrt( x**2 + y**2)

if (dist>r):
	print(f'Outside  the  circle')
elif (dist<r):
	print(f'inside  the  circle')
elif (dist==r):
	print(f'On  the  circle')

**************************************************************************


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


units = int(input('Enter  units :   '))  
match  units:
	case  units<=100:
				cost = units * 3.00
	case  ???:
				cost =  
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)



************************************************



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



************************************************


m = 4
match m:
    case 1:
        print('One')
    case 2:
        print('Two')
    case 3:
        print('Three')
print('Bye')      # Bye


i = 2
match i:
    case 1:
        print('One')
    case _:
        print('None of the above')
    case 2:
        print('Two')   # SyntaxError (default case '_' must be last)
print('Bye')

m = 2
match m:
    case 1:
        print('One')
    case _:
        print('Hello')
    case _:
        print('Bye')   # SyntaxError (multiple '_' not allowed)
print('End')


m = 1
match m:
    case 1:
        print('Hyd')   # Hyd
    case 1:
        print('Sec')
    case 1:
        print('Cyb')
print('Bye')           # Bye


ch = 'B'
match ch:
    case 'A':
        print('Apple')
    case 'B':
        print('Book')   # Book
    case 'C':
        print('Cafe')
    case _:
        print('None of the above')
print('Bye')            # Bye


match x:
    case 7 | -6 | 0:
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:
        print('One')
        print('Two')
        print('Three')
    case _:
        print('India')
        print('China')
        print('Usa')
print('Bye')


tpl = (-10 , -20)
match tpl:
    case (0 , 0):
        print('Origin')
    case (0 , y):
        print('y - axis')
    case (x , 0):
        print('x - axis')
    case (x , y):
        print('Quadrant')   # Quadrant
    case _:
        print('Not a point')


************************************************


import math

a = 1
b = -5
c = 6

disc = b**2 - 4*a*c   # discriminant

print(f'Discriminant value = {disc}')

if disc > 0:
    r1 = (-b + math.sqrt(disc)) / (2*a)
    r2 = (-b - math.sqrt(disc)) / (2*a)
    print('Roots are Real and Distinct')
    print(f'Root1 = {r1}')
    print(f'Root2 = {r2}')

elif disc == 0:
    r = -b / (2*a)
    print('Roots are Real and Same')
    print(f'Root = {r}')

else:
    real = -b / (2*a)
    imag = math.sqrt(-disc) / (2*a)
    print('Roots are Complex (Imaginary)')
    print(f'Root1 = {real} + {imag}j')
    print(f'Root2 = {real} - {imag}j')


*****************************************************

units = 1200   # suppose input is 1200

match units:
    
    case u if u <= 100:
        cost = u * 3.00

    case u if u <= 200:
        cost = (100 * 3.00) + (u - 100) * 3.50

    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (u - 200) * 4.00

    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (u - 400) * 4.50

    case _:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (units - 700) * 5.00

print('Bill amount : ', cost)


*************************************************

while True:
    print('Hello')    # Hello (prints continuously, infinite times)
print('Bye')          # (never printed)


while False:
    print('Hello')    # (never printed)
print('Bye')          # Bye




















