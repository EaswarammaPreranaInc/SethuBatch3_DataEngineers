from math import *
a= int(input('Enter 1st side :  '))
b= int(input('Enter 2nd side :  '))
c= int(input('Enter 3rd side :  '))

if (a==b==c):
    print('Equilateral Triangle')
    area = sqrt(3) / 4 * a ** 2
    print(F'Area : {area:.2f}')
    
        
else:
    if(a==b!=c) or (a!=b==c) or (b!=a==c) :
     print('Isoceles Triangle')
     perimeter = a + b + c
     print(F'Perimeter : {perimeter:.2f}')
     
    else:
        if (a+b<c) or (c+b<a) or (a+c<a):
            print ('Not a Triangle')
    
        else:
            if (a!=b) and (b!=c) and (c!=a):
                print('Scalene Triangle')
                s = (a + b + c) / 2
                area = sqrt(s * (s - a) * (s - b) * (s - c))
                print(F'Area : {area:.2f}')
                perimeter = a + b + c
                print(F'Perimeter : {perimeter:.2f}')


---------------------------------------------------------

import math
a= int(input('Enter value of a :  '))
if(a==0):
    print('value of a can not be 0')
else:
    b= int(input('Enter value of b :  '))
    c= int(input('Enter value of c :  '))
    
    disc =  b**2 - 4*a*c
    if(disc>0):
            print('Roots are Real and distinct')
            x = (-b + math.sqrt(disc)) / (2*a)
            y = (-b - math.sqrt(disc)) / (2*a)
            print(f'Root 1: {x:.2f} \n Root 2: {y:.2f}')
            
    if (disc==0):
            print('Roots are Real and same')
            x =   -b / (2*a)
            print(f'Root 1: {x:.2f} \n Root 2: {x:.2f}')
                
    if (disc<0):
            print('Roots are Complex (or) Imaginary  roots')
            R =  -b / (2*a)
            I = math.sqrt(-disc) / (2*a)
            print(f'Root 1: {R} + {I}j \n Root 2: {R} - {I}j')

---------------------------------------------------------

from math import *
x= int(input('Enter value of x :  '))
y= int(input('Enter value of y :  '))
r= float(input('Enter radius of circle :  '))

d= sqrt(x**2 + y**2)

if d>r:
    print('Poin is Outside  the  circle')
elif d<r:
    print('Poin is Inside  the  circle')
elif d==r:
    print('Poin is On  the  circle')


---------------------------------------------------------

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye')				#Bye


---------------------------------------------------------

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')				# Error


---------------------------------------------------------

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')				#error

---------------------------------------------------------

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')   #Hyd <nl> Bye

---------------------------------------------------------

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
print('Bye')			# Book <nl> Bye


---------------------------------------------------------
'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # Hyd <nl> Sec <nl> Cyb <nl> Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> # One <nl> Two <nl> Three <nl> Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->  # India <nl> China <nl> Usa <nl> Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> # Hyd <nl> Sec <nl> Cyb <nl> Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->  # One <nl> Two <nl> Three <nl> Bye
6) What  are  the  outputs  if  input  is  7  ?  --->  # Hyd <nl> Sec <nl> Cyb <nl> Bye
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

---------------------------------------------------------
'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->  Quadrant
8) What  is  the  output  when  input  is  ()  ?  ---> origin
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Quadrant
10) What  is  the  output  when  input  is  (25,) ?  ---> x axis
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

---------------------------------------------------------
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
u = int(input('Enter  units :   '))  
match 1200:
	case u if u<=100:
		cost = u*3
	case u if 100<u and u<=200:
		cost = 100*3 + (u-100)*3.5
	case u if 200<u and u<=400:
		cost = 100*3 + 100 * 3.50 + (u-200)*4
	case u if 400<u and u<=700:
		cost = 100*3 + 100 * 3.50 + 200*4 + (u-300)*4.50
	case u if 700<u:
		cost = 100*3 + 100*3.50 + 200*4 + 300*4.50 + (u-700)*5
print('Bill  amount  :  ' , cost)
---------------------------------------------------------

#  Find  outputs
while  True:
	print('Hello')  #Hello <nl> Bye
print('Bye')

---------------------------------------------------------

#  Find  outputs
while  False:
	print('Hello')
print('Bye')  #  Bye