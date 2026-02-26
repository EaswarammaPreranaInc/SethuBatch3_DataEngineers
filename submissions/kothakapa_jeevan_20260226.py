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
a = float(input('Enter first value : '))
b = float(input('Enter second value : '))
c = float(input('enter third value : '))
if (a+b)>c and (b+c)>a and (c+a)>b:
    if a == b == c:
        print('Equilateral triangle')
        print(f'Area :{"%.2f" %(math.sqrt(3) / 4 * a ** 2)}') 
    elif a == b or b == c or c ==a:
        print('Isosceles  triangle')
        print(f'Perimeter : {a + b + c}')
    elif a!=b and b!=c and c!=a :
        print('Scalene Triangle')
        s = (a+b+c)/2
        print(f'Area  of  scalene  triangle : {math.sqrt(s * (s - a) * (s - b) * (s - c))}')
        print(f'Value of s:{a+b+c/2}')
        print(f'perimeter  of  scalene  triangle :{ a + b + c} ')
else :
    print(f'Not a triangle')
    


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
a=float(input('Enter the a value : '))
b=float(input('Enter the b value : '))
c=float(input('Enter the c value : '))
disc = b ** 2 -4*a*c
if disc > 0:
    print('Real and Distinct')
    print(f'Root1 : {-b + math.sqrt(disc)/2*a}')
    print(f'Root2 : {-b - math.sqrt(disc)/2*a}')

elif disc == 0:
    print(f'Real  and  same : {-b / 2*a}')
   
elif disc < 0:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-disc) / (2*a)
    print(f'Complex  (or)  Imaginary  roots')
    print(f'root1 : {real_part} + {'%.2f' %imag_part}j')
    print(f'root2 : {real_part} - {'%.2f' %imag_part}j')




'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math
x=eval(input('enter a value : '))
y=eval(input('enter a value : '))
r=eval(input('enter a radius : '))

distance = math.sqrt(x**2+y**2)
radius = r
if distance > radius :
    print('Outside the circle')
elif distance < radius :
    print(f'Inside the circle')
elif distance==radius:
    print(f'Point is on the circle')




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


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _:  ---> syntax error
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') 



# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:   ---> Syntax error ( because anonymus object must be in the last only otherwise remaining statements not reached)
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
answer : Hyd
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
Answer : Book
         Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? ---> 
							Hyd
							Sec
							Cyb
2) What  are  the  outputs  if  input  is  15  ?  --->
							One
							Two
							Three
3) What  are  the  outputs  if  input  is  10.8  ?  --->
							India
							China
							Usa
4) What  are  the  outputs  if  input  is  0  ?  --->
							Hyd
							Sec
							Cyb
5) What  are  the  outputs  if  input  is  -10  ?  --->
							One
							Two
							Three
6) What  are  the  outputs  if  input  is  7  ?  --->
							Hyd
							Sec
							Cyb
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
print('Bye')


'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->  Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> not a point
10) What  is  the  output  when  input  is  (25,) ?  ---> not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> not a point
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




#  Find  outputs
while  True:
	print('Hello') --> Hello
print('Bye')

#  Find  outputs
while  False:
	print('Hello')
print('Bye') ---> Bye
















