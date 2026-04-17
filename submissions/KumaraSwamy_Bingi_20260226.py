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

#program:

x=int(input("Enter the first side:"))
y=int(input("Enter the second side:"))
z=int(input("Enter the third side:"))

if x+y>z and y+z>x and z+x>y:
    if x==y and y==z:
        area=(3**0.5/4)*x**2
        print("equilateral triangle")
        print(area)
    elif x==y or y==z or z==x:
        perimeter=x+y+z
        print("isosceles triangle")
        print(perimeter)
    else:
        s=(x+y+z)/2
        area=(s*(s-x)*(s-y)*(s-z))**0.5
        perimeter=x+y+z
        print("scalene triangle is:")
        print(area)
        print(perimeter)

else:    
    print("not a triangle")












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

#program:
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
discriminant = b ** 2 - 4 * a * c

try:

    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print("Roots are real and distinct.")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("Roots are real and same.")
        print("Root:", root)
    elif discriminant < 0:
        real_part = -b / (2 * a)
        imag_part = (abs(discriminant) ** 0.5) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        print("Roots are complex (or) imaginary.")
        print("Root 1:", root1)
        print("Root 2:", root2)

except ZeroDivisionError:
    print("a cannot be zero.")













'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

#program:

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
r = float(input("Enter the radius of the circle: "))
distance = (x ** 2 + y ** 2) ** 0.5
if distance > r:
    print("The point is outside the circle.")
elif distance < r:
    print("The point is inside the circle.")
else:
    print("The point is on the circle.")










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

#output: Bye because there is no case for 4, so it will skip the match statement and directly print Bye.













# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:                                #Error due to _ should be in the last case
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')














# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:                        # Error due to case _ should be only one time in match case at the end of the match case
		print('Hello')
	case  _:  
		print('Bye')
print('End')















#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:					# only this case will execute 
		print('Hyd')      
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')            # this is also executed because it is outside the match case


'''

output:

Hyd
Bye


'''














# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')                  #executed
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')                            #executed

'''

output:
Book
Bye

'''















'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd, Sec, Cyb and Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One, Two, Three and Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India, China, Usa and Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd, Sec, Cyb and Bye
5) What  are  the  outputs  if  input  is -10 ? ---> One, Two, Three and Bye
6) What   are   the   outputs   if   input   is   -7 ? ---> India, China, Usa and Bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->    y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->  Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->   Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->   Not  a  point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->   Not  a  point
8) What  is  the  output  when  input  is  ()  ?  --->  Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->    Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->   Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->   Not  a  point
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
units = int(input('Enter units : '))

match units:
    case x if 0 <= x <= 100:
        cost = x * 3.00

    case x if 101 <= x <= 200:
        cost = 100 * 3.00 + (x - 100) * 3.50

    case x if 201 <= x <= 400:
        cost = 100 * 3.00 + 100 * 3.50 + (x - 200) * 4.00

    case x if 401 <= x <= 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + (x - 400) * 4.50

    case _:
        cost = (
            100 * 3.00 +
            100 * 3.50 +
            200 * 4.00 +
            300 * 4.50 +
            (units - 700) * 5.00
        )

print('Bill amount :', cost)


