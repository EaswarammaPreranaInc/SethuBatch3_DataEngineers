
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
    a = float(input('Enter 1st side : '))
    b = float(input('Enter 2nd side : '))
    c = float(input('Enter 3rd side : '))
    s = (a+b+c)/2
    if a + b > c and b + c > a and c + a > b:
        if a != b and b != c and c != a :
            print('Scalene tringle ')
            print(f'Area : {math.sqrt(s*(s-a)*(s-b)*(s-c))}')
            print(f'Perimeter : {a+b+c}')
    
    if a + b > c and b + c > a and c + a > b:
        if (a == b or b == c  or c == a) and (a == b != c  or b==c != a or c==a != b):
            print('Isoscles triangle')
            print(f'Perimeter : {a+b+c}')
    
    if  a + b > c and b + c > a and c + a > b:
        if a == b == c :
            print('Equilateral Triangle ')
            print(f'Area : {math.sqrt(3) / 4 * a**2}') 
    
    else:
        print('Not a Triangle ')
except:
    print('Input should be in integers')
        


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
a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))
c = int(input('Enter value of c : '))

disc = b**2 - 4*a*c
print(f'{disc=}')

if a != 0 :
    if disc > 0 :
        print('Real and Distinct ')
        print(f'Root 1 : {(-b + math.sqrt(disc)) / 2*a }')
        print(f'Root 2 : {(-b - math.sqrt(disc)) / 2*a}')
    elif disc == 0 : 
        print('Real and  Same ')
        print(f'Root : {-b / 2*a}')
    else:
        print('Roots are Complex (or) Imaginary roots ')
        print(f'Root 1 : {complex(-b / 2*a )}')
        print(f'Root 2 : {complex(math.sqrt(-disc) / 2*a )}')
else :
    print("Coefficient 'a' cannot be zero for a quadratic equation. ")


'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

try:
    x = float(input('Enter value of x : '))
    y = float(input('Enter value of y : '))
    r = float(input('Enter Radius of circle : '))
    
    distance = math.sqrt(x**2 + y**2)
    
    if distance > r :
        print('Point is outside the circle ')
    elif distance == r:
        print('Point is on the circle ')
    else:
        print('Point is inside the circle ')
except:
    print('please enter integer only ')


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') #Bye


# Identify  Error
i = 2 
match  i:
	case  1:
		print('One')
	case  _:  #Error 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')


# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  #Error nameless object should always be last after all class 
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
print('Bye') #Hyd <next line> Bye


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
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <nexline> Sec <nextline> Cyb <nextline> Bye <nextline>
2) What  are  the  outputs  if  input  is  15  ?  ---> One <nexline> Two <nextline> Three <nextline> Bye <nextline>
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India <nexline> China <nextline> Usa <nextline> Bye <nextline>
4) What  are  the  outputs  if  input  is  0  ?  ---> Hyd <nexline> Sec <nextline> Cyb <nextline> Bye <nextline>
5) What  are  the  outputs  if  input  is  -10  ?  ---> One <nexline> Two <nextline> Three <nextline> Bye <nextline>
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd <nexline> Sec <nextline> Cyb <nextline> Bye <nextline>
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Qudrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis 
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis 
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y - axis 
8) What  is  the  output  when  input  is  ()  ?  ---> Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not a point
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
match  units:
	case  100:
				cost = 100*3.00 
	case  200:
				cost = 100*3.00 + 100*3.00 
	case  300:
				cost = 100*3.00 + 200*4.00
	case  400:
				cost = 100*3.00 + 300*4.50
	case  700:				
				cost = 100*3.00 + 700*5.00
    case _:
                print('please enter valid amount between (100)')
print('Bill  amount  :  ' , cost)


#  Find  outputs
#while  True:
	print('Hello')
print('Bye') #hello will be printed multiple time until the codition is true 


#  Find  outputs
while  False:
	print('Hello')
print('Bye') #Bye