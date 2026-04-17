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

Program:
import math

a = int(input("Enter 1st side: "))
b = int(input("Enter 2nd side: "))
c = int(input("Enter 3rd side: "))

if a + b > c and b + c > a and c + a > b:

    s = (a + b + c) / 2   #

	
    if a == b == c:
        print("Equilateral Triangle")
        area = (math.sqrt(3) / 4) * (a ** 2)
        print("Area :", area)
        print("Perimeter :", a + b + c)

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Area :", area)
        print("Perimeter :", a + b + c)

    else:
        print("Scalene Triangle")
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Area :", area)
        print("Perimeter :", a + b + c)

else:
    print("Sum of every two sides should be greater than 3rd side")


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


#Program:
import math

a = float(input("Enter a (a != 0): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

disc = b**2 - 4*a*c
print("Discriminant =", disc)

if disc > 0:
    print("Roots are Real and Distinct")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif disc == 0:
    print("Roots are Real and Same")
    root = -b / (2*a)
    print("Root =", root)

else:
    print("Roots are Complex (Imaginary)")
    real_part = -b / (2*a)
    imag_part = math.sqrt(-disc) / (2*a)
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)
    print("Root 1 =", root1)
    print("Root 2 =", root2)


Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle

Program:
import math

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
r = float(input("Enter radius: "))

distance = math.sqrt(x**2 + y**2)

if distance > r:
    print("Point lies Outside the circle")
elif distance < r:
    print("Point lies Inside the circle")
else:
    print("Point lies On the circle")





# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
# Bye




# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: # Error
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')




# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  # Error
		print('Hello')
	case  _:  
		print('Bye')
print('End')




#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:  
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
# Hyd
 Bye




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
print('Bye')

# Book
  Bye



1) What  are  the  outputs  if  input  is  -6 ? ---> # Hyd
		                                               Sec
		                                               Cyb
														Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One, Two, Three, Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India,China, USA , Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd, Sec, Cyb , bYe
5) What  are  the  outputs  if  input  is  -10  ?  --->One, Two, Three, Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd, Sec, Cyb, bye
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





1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> # Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->   # x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->  #y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> # origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> # not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->  #Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> # Y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> # not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> # not a point
10) What  is  the  output  when  input  is  (25,) ?  --->  # not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> # not a point
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
match  units/100:
	case  0:
				cost = units*3.00
	case  1:
				cost = 100*3.00(unit-100)*3.50
	case  ???:
				cost = 
	case  ???:
				cost = 
	case  ???:				
				cost = 
print('Bill  amount  :  ' , cost)




#  Find  outputs
while  True:
	print('Hello')
print('Bye')
# hello (infinite)



#  Find  outputs
while  False:
	print('Hello')

print('Bye')
#Bye
