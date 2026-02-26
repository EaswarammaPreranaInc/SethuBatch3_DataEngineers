
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1)Find  area  if  it  is  an  equilateral  triangle
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

CODE:

import math
a = eval(input('Enter first side: '))
b = eval(input('Enter second side: '))
c = eval(input('Enter third side: '))
if a+b > c and a+c > b and b+c > a:
    pass
else:
    print('not a triangle')
if a == b == c:
    print("Equilateral triangle")
    area_equilateral_triangle = math.sqrt(3) / 4 * a ** 2
    print('Area : ', area_equilateral_triangle)
else:
    if (a == b or a == c or b == c) and (a+b > c and a+c > b and b+c > a):
        print('isosceles  triangle')
        print('perimeter: ', a + b + c)
if a != b != c and (a+b > c and a+c > b and b+c > a):
    print('scalene  triangle')
    s = (a + b + c) / 2
    print('Area : ', math.sqrt(s * (s - a) * (s - b) * (s - c)))
    print('perimeter : ', a + b + c)


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

CODE:

try:
    a = eval(input('Enter value of a : '))
    if a == 0:
        print('a can not be 0')
    else:
        b = eval(input('Enter value of b : '))
        c = eval(input('Enter value of c : '))
        disc = b**2-4*a*c
        import math
        if disc > 0:
            print('Real  and  distinct')
            print('root 1 :', (-b + math.sqrt(disc)) / 2*a)
            print('root 2 : ', (-b - math.sqrt(disc)) / 2*a)
        elif disc == 0:
            print('Real  and  same')
            print('root : ', -b / 2*a)
        elif disc < 0:
            print('Complex  (or)  Imaginary  roots')
            real = -b / 2*a
            imag = math.sqrt(-disc) / 2*a
            root1 = complex(real, imag)
            root2 = complex(real, imag)
            print(root1)
            print(root2)
except:
    print("value should be numbers")


'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

CODE:

try:
    x = eval(input('Enter value of x : '))
    y = eval(input('Enter value of y : '))
    r = eval(input('Enter radius of circle : '))
    import math
    d = math.sqrt(x ** 2 + y ** 2)
    if d > r:
        print('point is Outside  the  circle')
    elif r > d:
        print('point is Inside  the  circle')

    else:
        print(' point is on the circle')


except:
    print('input should be integer, float')

#Find  outputs  (Home  work)
  m = 4
  match  m:
  	case  1:
 		print('One')
 	case  2:
 		print('Two')
 	case  3:
 		print('Three')
 print('Bye') # Bye

# Identify  Error
  i = 2
  match  i:
 	case  1:
 		print('One')
 	case  _:  #error case_ should be end of the match
 		print('None of   the  above')
 	case  2:
 		print('Two')
  print('Bye')

# Find  outputs  (Home  work)
  m = 2
  match  m:
 	case  1:
 		print('One')
 	case  _:        #error
 		print('Hello')
 	case  _:
 		print('Bye')
  print('End')

#  Find  outputs  (Home  work)
  m = 1
  match  m:
 	case  1:
 		print('Hyd') #Hyd
 	case  1:
 		print('Sec')
 	case  1:
 		print('Cyb')
  print('Bye') #Bye

# Find  outputs  (Home  work)
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
  print('Bye') #Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd <next line> Sec <next line> Cyb
2) What  are  the  outputs  if  input  is  15  ?  ---> One <next line> Two <next line> Three
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India <next line> China <next line> Usa
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd <next line> Sec <next line> Cyb
5) What  are  the  outputs  if  input  is  -10  ?  --->One <next line> Two <next line> Three
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd <next line> Sec <next line> Cyb
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
  End  of  match
  print('Bye') #Bye

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
8) What  is  the  output  when  input  is  ()  ?  --->Origin
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not  a  point
10) What  is  the  output  when  input  is  (25,) ?  --->x - axis
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not  a  point
'''
CODE:

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
First  100  units				Rs. 3.00 / unit

Next  100  units				Rs. 3.50 / unit

Next  200  units		         	Rs. 4.00 / unit

Next  300  units				Rs. 4.50 / unit

Above  700  units				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 + 500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''

CODE:

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
print('extra_units ', extra_units)




