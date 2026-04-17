# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')#Bye

 # Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')#error becoz case  _: at the end of all cases 
	case  2:
		print('Two')
print('Bye')#Bye

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')#Hello
	case  _:  
		print('Bye')
print('End')#End


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')#Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')#Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book')#Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')#Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? --->#Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->#One<nextline>Two<nextline>Three<nextline>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->#India<nextline>China<nextline>Usa<nextline>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->#India<nextline>China<nextline>Usa<nextline>Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->#One<nextline>Two<nextline>Three<nextline>Bye
6) What  are  the  outputs  if  input  is  7  ?  --->#Hyd<nextline>Sec<nextline>Cyb<nextline>Bye

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



1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Quadrant
8) What  is  the  output  when  input  is  ()  ?  --->Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->Not  a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not  a  point

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


'''
 #  Find  outputs
while  True:
	print('Hello')#Hello
print('Bye')#Bye

 #  Find  outputs
while  False:
	print('Hello')
print('Bye')#Bye

# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
#Center  is  origin  and  radius  is  'r'
#1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)
#2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle
#3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle
#4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle"""

from math import sqrt 
try:
    x=int(input("Enter value of x: "))
    y=int(input("Enter value of y: "))
    radius=int(input("Enter radius of the circle : "))
    distance=sqrt(x ** 2 + y ** 2)

    if( distance > radius):
        print("point is  outside the circle")  
    elif(distance < radius):
        print("point is inside the circle")
    else:
        print("point is on circle")
except ValueError:
    print("Enter valid input numbers ")

""""Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
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
	 What  is  root2  if  real  part  is  3  and  imag  part  is  4 ?  ---> 3 - 4j"""
	 
from math import sqrt
try:
    a=int(input("Enter value of a : "))
    if(a==0):
        print("value of a cannot be 0")
    else:
        b=int(input("Enter value of b : "))
        c=int(input("Enter value of c : "))
        discriminant=(b ** 2) -(4*a*c)
        if( discriminant > 0):
                print("roots  are real and distinct")
                root1=(-b + sqrt(discriminant) / 2*a)
                root2=(-b - sqrt(discriminant) / 2*a)
                print(f'root1:{root1=}')
                print(f'root2:{root2=}')
        elif( discriminant == 0):
                print("  Real  and  same")
                root=-b / 2*a
                print(f"root1:{root=}")
                print(f"root2:{root=}")
        else:
                print(" Complex  (or)  Imaginary  roots")
                real=(-b/ (2*a))
                imag=sqrt(-discriminant) / 2*a
                root1=complex(real,imag)
                root2=complex(real,imag)
                print(f"root1={root1=}")
                print(f"root2={root2=}")
except ValueError:
    print("enter  valid numbers")



      

''''
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

Hint:  Use  match  ...  case   but  not  if ... else"""


'''
units = int(input('Enter  units :   '))

match units:
    case 100:
        cost = 100*3.00
    case 200:
        cost = 100 * 3.00 + 100 * 3.50
    case 300:
        cost = 100 * 3.00 + 100 * 3.50 + 100 * 4.00
    case 400:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00
    case 500:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 100 * 4.50
    case 600:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 200 * 4.50
    case 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50
    case _:
        if units > 700:
            extra_units = units - 700
            extra_units_cost = extra_units * 5.00
            cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + extra_units_cost
print('Bill  amount  :  ', cost)
_____________
'''
#Write  a  program  to  determine  three  sides  form  a  triangle  or  not

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

from math import sqrt
a=int(input("Enter 1st side :"))
b=int(input("Enter 2nd side :"))
c=int(input("Enter 3rd side :"))
if(a+b>c and a+c>b and b+c>a): 
    if(a==b and b==c and a==c):
        print("Equilateral triangle")
        area=sqrt(3) / 4 * a ** 2
        print(f"area:{area}")
    else:
        if(a!=b and a!=c ) and (b!=c):
            print("scalene  triangle")
            s=(a + b + c) / 2
            area=sqrt(s * (s - a) * (s - b) * (s - c))
            perimeter=a + b + c
            print(f"area:{area}")
            print(f'perimeter:{perimeter}')
        else:
            if((a==b or b==c) or a==c):
                print("Isoscles triangle")
                perimeter=a+b+c
                print(f'perimeter:{perimeter}')
            else:
                print('')
else:                
    print("it is not a triangle")
