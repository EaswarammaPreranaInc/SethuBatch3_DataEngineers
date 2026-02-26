'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
'''
import math

a = float(input())
b = float(input())
c = float(input())
if a == 0:
        print("Not a quadratic equation")
else:
    d = b**2 - 4*a*c     
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
        
    print("root1:", r1)
    print("root2:", r2)
##############################################################################################################
'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'


1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''
code:
import math
x=float(input())
y=float(input())
radius=float(input())
res=x**2+y**2
distance=math.sqrt(res)
if distance>radius:
    print("outside the circle")
elif distance<radius:
    print("inside the circle")
else:
    print("on the circle")

##############################################################################################################
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
#output:Bye
##############################################################################################################
# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #error here Because _ matches everything.
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye')
##############################################################################################################
# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End')
#output:Error 
##############################################################################################################
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
#output:Hyd
	Bye
##############################################################################################################
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
#output:Book
       Bye
##############################################################################################################
 '''
1) What  are  the  outputs  if  input  is  -6 ? --->Hyd <newline>Sec<newline>Cyb<newline>Bye
2) What  are  the  outputs  if  input  is  15  ?  --->one<newline>Two<newline>Three<newline>Bye
3) What  are  the  outputs  if  input  is  10.8  ?  --->India<newline>China<newline>Usa<newline>Bye
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd <newline>Sec<newline>Cyb<newline>Bye
5) What  are  the  outputs  if  input  is  -10  ?  --->one<newline>Two<newline>Three<newline>Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd <newline>Sec<newline>Cyb<newline>Bye
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
##############################################################################################################
 '''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  --->x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  --->y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->y - axis
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
		print('Not a point')
##############################################################################################################
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
##############################################################################################################
 #  Find  outputs
while  True:
	print('Hello')
print('Bye')
#output:Hello in infinity loop
##############################################################################################################
 #  Find  outputs
while  False:
	print('Hello')# nothing is printed
print('Bye')