'''
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
'''



import math
try:
    a = int(input("Enter 1st side:"))
    b = int(input("Enter 2nd side:"))
    c = int(input("Enter 3rd side:"))

    if a + b > c and a + c > b and b + c > a:

        if a == b == c:
            # Equilateral triangle
            area = math.sqrt(3)/4*a**2
            print("Equilateral Triangle")
            print(f"Area : {area}")

        elif a == b or b == c or a == c:
            # Isosceles triangle
            perimeter = a + b + c
            print("Isosceles Triangle")
            print(f"Perimeter : {perimeter}")

        else:
            # Scalene triangle
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter = a + b + c
            print("Scalene Triangle")
            print(f"Area : {area}")
            print(f"Perimeter : {perimeter}")

    else:
        print("Not a triangle")

except ValueError:
    print("Enter integer input only")


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
try:
    a = float(input("Enter the value of a :"))
    b = float(input("Enter the value of b :"))
    c = float(input("Enter the value of c :"))

    if a==0:
        print("value of a should not be 0")
    else :
        disc = b*b-4*a*c
        print(f"Discriminant = {disc}")

        if disc > 0:
            root1=  (-b +math.sqrt(disc)) / 2*a
            root2=  (-b -math.sqrt(disc)) / 2*a
            print("Roots are real and distinct")
            print("Root 1 :", root1)
            print("Root 2 :", root2)
        elif disc ==0:
            root = -b / 2*a
            print("Roots are real and same")
            print(F"Root is {root}")
        else:

                root1 = -b / 2*a
                root2= math.sqrt(-disc) / 2*a
                print("Roots are complex or imaginary")
                print("Root 1 :", root1)
                print("Root 2 :", root2)

except ValueError:
    print("Enter valid numeric input")


'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math
try:
      x = float(input("Enter the value of x : "))
      y = float(input("Enter the value of y : "))
      radius=float(input("Enter the radius : "))

      distance = math.sqrt(x ** 2 + y ** 2)
      if distance==radius:
            print("Point is on the circle")
      elif distance>radius:
            print("Point is outside the circle")
      else:
            print("Point is inside the circle")

except:
      print("Enter a valid input")


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # output is Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:  #Error we cannot give _ in middle of execution of program.
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
print('End') # Error due to more wildcard(_) than one.

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') #"Hyd" <next line> Bye

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
print('Bye') #Book <next line> Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> 'Hyd''Sec''Cyb''Bye'
2) What  are  the  outputs  if  input  is  15  ?  ---> 'One''Two''Three''Bye'
3) What  are  the  outputs  if  input  is  10.8  ?  --->'India''China''Usa''Bye'
4) What  are  the  outputs  if  input  is  0  ?  ---> 'Hyd''Sec''Cyb''Bye'
5) What  are  the  outputs  if  input  is  -10  ?  --->'One''Two''Three''Bye'
6) What  are  the  outputs  if  input  is  7  ?  ---> 'Hyd''Sec''Cyb''Bye'
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Not a point
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> Not a point
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Error
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> Not a point
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not a point
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
match  units:
	case u if u <= 100:
		bill = u * 3.00

    case u if u <= 200:
        bill = 100 * 3.00 + (u - 100) * 3.50

    case u if u <= 400:
        bill = 100 * 3.00 + 100 * 3.50 + (u - 200) * 4.00

    case u if u <= 700:
        bill = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            (u - 400) * 4.50
        )

    case _:
        bill = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            300 * 4.50 +
            (units - 700) * 5.00
        )

print(f"Bill Amount = Rs. {bill}")

#  Find  outputs
while  True:
	print('Hello') 
print('Bye') #Hello <next line> Bye

#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye



