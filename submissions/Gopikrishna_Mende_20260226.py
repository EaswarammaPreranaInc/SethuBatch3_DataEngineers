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
	What  is  the  value  of  's'  ?  --->  	(a…
'''
import math
a=int(input('Enter 1st side:'))
b=int(input('Enter 2nd side:'))
c=int(input('Enter 3rd side:'))
if (a+b)>c and (a+c)>b and (b+c)>a:
    if a==b==c:
        print("Equailateral Triangle")
        area=math.sqrt(3)/4*a**2
        print(f"{area=:.2f}")
    elif a==b or a==c or b==c:
        print("Isoscles Triangle")
        print('Perimeter=',a+b+c)
    else:
         print("Scalene Triangle")
         s=(a+b+c)/2
         area=math.sqrt(s*(s-a)*(s-b)*(s-c))
         print(f"{area=:.2f}")
         print("Perimeter=",a+b+c)
else:
    print("Not a triangle")


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
	 What  is  r
…

'''
import math
a=int(input('Enter value of a:'))
b=int(input('Enter value of b:'))
c=int(input('Enter value of c:'))
if a!=0:
    d= b**2-4*a*c
    if d>0:
        e=math.sqrt(d)
        print("Roots are real")
        root1=(-b+e)/(2*a)
        root2=(-b-e)/(2*a)
        print(f"{root1=:.2f}")
        print(f"{root2=:.2f}")
    elif d==0:
        print("Roots are Real and same")
        r=-b/(2*a)
        print(f"{r=}")
    else:
         print("Roots are imaginary")
         real=f"{-b/(2*a)}"
         imag=f"{(math.sqrt(-d)/(2*a))}j"
         print("Root1=",(real),"+",imag)
         print("Root2=",(real),"-",imag)
else:
    print("Value of 'a' should not be 0")



'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math
x=int(input('Enter value of x:'))
y=int(input('Enter value of y:'))
r=(float(input('Enter radius of circle:')))
d=math.sqrt(x**2+y**2)
if d>r:
    print("Point is outside the circle")
elif d==r:
        print("Point is on circle")
       
else:
    print("Point is Inside the circle")


#(Home  work)
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
	case  _:  #Error 
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
print('Bye')#Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Hyd
						     Sec
						     Cyb
						     Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> One
						       Two
						       Three
						       Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India china Usa
4) What  are  the  outputs  if  input  is  0  ?  --->Hyd
						     Sec
						     Cyb
						     Bye

5) What  are  the  outputs  if  input  is  -10  ?  --->One
						       Two
						       Three
						       Bye
6) What  are  the  outputs  if  input  is  7  ?  --->Hyd
						     Sec
						     Cyb
						     Bye
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
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x-axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y-axis
4) What  is  the  output  when  input  is  (0 , 0) ?  --->origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->Not a point
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->Not a point
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->Not a point
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

Hint: Use  match  ...  case   but  not  if ... else
'''


a = int(input('Enter units : '))

match a:
    
    case a if a <= 100:
      cost = a * 3.00
    case a if a <= 200:
       cost = (100 * 3.00) + (a - 100) * 3.50
    case a if a <= 400:
      cost = (100 * 3.00) + (100 * 3.50) + (a - 200) * 4.00
    case a if a <= 700:
        cost = (100 * 3.00) +(100 * 3.50) +(200 * 4.00) +(a - 400) * 4.50
    case a:
        cost = (100 * 3.00) + (100 * 3.50) +(200 * 4.00) +(300 * 4.50) +(a - 700) * 5.00
print('Bill amount :', cost)



 #  Find  outputs
while  True:
	print('Hello')
print('Bye') #Hello .......
 #  Find  outputs
while  False:
	print('Hello')
print('Bye') #Bye