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
#============================================================
import math
try:
    a=float(input("Enter 1st side:"))
    b=float(input("Enter 2nd side:"))
    c=float(input("Enter 3rd side:"))
    s=(a+b+c)/2
    if (a+b)>c and (b+c)>a and(c+a)>b and a!=0 and b!=0 and c!=0:
        if(a==b and b==c):
            print("Equilateral triangle")
            print(f"{math.sqrt(s * (s - a) * (s - b) * (s - c))}")
        elif(a==b or b==c or c==a):
            print("isoceles triangle")
            print(f"perimeter:{a+b+c}")
        elif(a!=b and b!=c and c!=a):
            print("scalene triangle")
            print(f"Area:{math.sqrt(s * (s - a) * (s - b) * (s - c))}")
            print(f"perimeter:{a+b+c}")
    else:
        print("not a triangle")
except:
    print("input should be numbers")
#=================================================================================
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
#=============================================================================================
import math
try:
    a=float(input("Enter value of a: "))
    b=float(input("Enter value of b: "))
    c=float(input("Enter value of c: "))
    if(a!=0):
        disc=b**2-4*a*c
        if(disc>0):
            print("roots are Real and distinct")
            print(f"Root 1:{(-b + math.sqrt(disc)) / (2*a)}")
            print(f"Root 2:{(-b - math.sqrt(disc)) / (2*a)}")
        elif(disc==0):
            print("roots are Real and equal")
            print(f"Root 1:{(-b + math.sqrt(disc)) / (2*a)}")
            print(f"Root 2:{(-b - math.sqrt(disc)) / (2*a)}")
        elif(disc<0):
            print("roots are imaginary or complex")
            print(f"Root 1:{(-b)/ (2*a)}+{(math.sqrt(abs(disc)))/(2*a)}j")
            print(f"Root 2:{(-b)/ (2*a)}-{(math.sqrt(abs(disc)))/(2*a)}j")
    else:
        print("a value cannot be zero")
except:
     print("values should be numbers")    
# #===========================================================================================
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
#==================================================================================================
import math
radius=float(input("enter the radius of circle:"))
a=float(input("Enter value of a: "))
b=float(input("Enter value of b: "))
distance=math.sqrt(a**2+b**2)
if(radius!=0):
    if(distance>radius):
        print("point is outside the circle")
    elif(distance<radius):
        print("point is inside the circle")
    else:
        print("point is on the circle")
else:
    print("radius should be greater than 0")
#==========================================================
Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')              #Bye
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')
#========================================================
Identify  Error
i = 2
match  i:
	case  1:
		print('One')                 #Error
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
#========================================================
Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:                   #Error
		print('Hello')
	case  _:  
		print('Bye')
print('End')
#=======================================================
#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')               #Hyd<nextline>Bye
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')
#==================================================
# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':                                 #Book<nextline>Bye
		print('Book')
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye')
#========================================================
'''
1) What  are  the  outputs  if  input  is  -6 ? ---># Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->One<nextline>Two<nextline>Three<nextline>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India<nextline>China<nextline>Usa<nextline>Bye
4) What  are  the  outputs  if  input  is  0  ?  ---># Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->One<nextline>Two<nextline>Three<nextline>Bye
6) What  are  the  outputs  if  input  is  7  ?  ---># Hyd<nextline>Sec<nextline>Cyb<nextline>Bye
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
#==========================================================================================
'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->X-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant#any ordered sequence of length-2
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Y-axis
8) What  is  the  output  when  input  is  ()  ?  --->Not a point
9) What  is  the  output  when  input  is  {10 , 20} ?  --->Not a point
10) What  is  the  output  when  input  is  (25,) ?  --->Not a point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->Not a point
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
#========================================================================================
#  Find  outputs
while  True:
	print('Hello')  #infinite times:Hello
print('Bye')
#  Find  outputs
while  False:
	print('Hello')           #Bye      
print('Bye')
#==============================================================
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
	case units if units<=100:
				print(f"cost = {units*3.00}")
	case  units if units>100 and units<=200:
				print(f"cost = { 100*3.00+(units-100)*3.50}")
	case  units if units>100 and units<=400:
				print(f"cost = {100*3.0+100*3.50+(units-200)*4.00}")
	case units if  units>400 and units<700:
				print(f"cost = {100 * 3.00 + 100 * 3.50 + 200 * 4.00+(units-400)*4.50}")
	case  units if units >700 and units<1400:				
				print(f"cost =  {100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  300 * 4.50 +(units-700)*5.00}")
