'''
Q1
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

try :
    a = float(input("Enter 1st side : "))
    b = float(input("Enter 2nd side : "))
    c = float(input("Enter 3rd side : "))
    
    if (a + b > c) and (b + c > a) and (c + a > b):
        
        if a == b == c :
            print("Equilateral Triangle")
            
            area = (math.sqrt(3)/4)*(a**2)
            print("Area : ", area)
            
        else :
            if a == b or b==c or a==b:
                print("Isoceles Triangle")
                
                pt = a + b + c
                print("Perimeter of Triangle : ", pt)
                
            else :
                print("Scalene Triangle")
                
                s = (a + b + c)/2
                
                ar =  math.sqrt(s*(s -a)*(s - b)*(s - c))
                
                pt = a + b + c
                print("Area : ", ar)
                print("Perimeter  : ", pt)
    
    else :
        print("It is not Triangle")

except :
    print("Input should be Valid Int or Float")

    
'''
Output :
Enter 1st side : 8
Enter 2nd side : 9.5
Enter 3rd side : 9.5
Isoceles Triangle
Perimeter of Triangle :  27.0
PS D:\SSSSDP\Homeworks> py pr1.py
Enter 1st side : 9.5
Enter 2nd side : 5
Enter 3rd side : 23.5
It is not Triangle
'''

'''
Q2
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

try :
    a = float(input("Enter value of a : "))
    b = float(input("Enter value of b : "))
    c = float(input("Enter value of c : "))
    
    if a != 0:
        
        disc = (b**2) - (4*a*c)
        
        if disc == 0 :
            print("Real and Equal Roots")
            
            r1 = (-b)/(2*a)
            print("Root 1 : ", r1)
            print("Root 2 : ", r1)
            
        elif disc > 0 :
            print("Real and Distinct Roots")
            r1 = (-b + math.sqrt(disc))/(2*a)
            r2 = (-b - math.sqrt(disc))/(2*a)
            print("Root 1 : ",r1)
            print("Root 2 : ",r2)
            
        else : 
            print("Roots are imaginary or complex")
            
            rp = -b/(2*a)
            ip = (math.sqrt(-disc))/(2*a)
            
            r1 = complex(rp , ip)
            r2 = complex(rp , -ip)
            
            print("Root 1 : ",r1)
            print("Root 2 : ",r2)
    else :
        print("Value of a can not be zero")

except :
    print("Enter valid Input")


'''
Output :
Enter value of a : 3
Enter value of b : 10
Enter value of c : 3
Real and Distinct Roots
Root 1 :  -0.3333333333333333
Root 2 :  -3.0
'''

'''
Q3
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

import math

try :
    
    x = float(input("Enter x-cordinate value : "))
    y = float(input("Enter y-cordinate value : "))
    r = float(input("Enter the radius of circle : "))
    
    dis = math.sqrt((x**2) + (y**2))
    
    if dis == r :
        print("On the circle")
    
    elif dis > r:
        print("Outside the Circle")
    
    else :
        print(" Inside the circle")
        
except :
    print("Enter valid input")


'''
Output :
Enter x-cordinate value : 3
Enter y-cordinate value : 4
Enter the radius of circle : 5
On the circle
PS D:\SSSSDP\Homeworks> py pr1.py
Enter x-cordinate value : -5
Enter y-cordinate value : 4
Enter the radius of circle : 3
Outside the Circle
'''       

# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') # Bye, as there is no case number matches m , so prints Bye


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # Error, because anonymous case should be at end, not at middle of valid cases

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # Error, because anonymous case should be at end, not between cases

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') # Hyd
             # Bye
             

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
print('Bye') # Book
             # Bye
             

'''
1) What  are  the  outputs  if  input  is  -6 ? --->
2) What  are  the  outputs  if  input  is  15  ?  --->
3) What  are  the  outputs  if  input  is  10.8  ?  --->
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->
6) What  are  the  outputs  if  input  is  7  ?  --->
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
1. Hyd
   Sec
   Cyb
   Bye
2. One
   Two
   Bye
3. Bye
4. Hyd
   Sec
   Cyb
   Bye
5. One
   Two
   Bye
6. Hyd
   Sec
   Cyb
   Bye
'''

'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->
2) What  is  the  output  when  input  is  (10 , 0) ?  --->
3) What  is  the  output  when  input  is  (0 , -20) ?  --->
4) What  is  the  output  when  input  is  (0 , 0) ?  --->
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->
6) What  is  the  output  when  input  is  [10 , 20]  ?  --->
7) What  is  the  output  when  input  is  [0 , -25]  ?  --->
8) What  is  the  output  when  input  is  ()  ?  --->
9) What  is  the  output  when  input  is  {10 , 20} ?  --->
10) What  is  the  output  when  input  is  (25,) ?  --->
11) What  is  the  output  when  input  is  {10 : 20} ?  --->
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
Output :
1. Quadrant
2. x - axis
3. y - axis
4. Origin
5. Not a point
6. Quadrant
7. y - axis
8 .Not a point
9. Not a point
10. Not a point
11. Not a point
'''
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
	case u if u <= 100 :
				cost = u*3.00
	case  u if u <= 200:
				cost =  (100*300) + (u - 100)*3.50
	case  u if u <= 400:
				cost = (100*300) + (100*3.50) + (u -200)*4.00 
	case  u if u <= 700:
				cost = (100*300) + (100*3.50) + (200*4.00) + (u - 400)*4.50
	case  u :				
				cost = (100*300) + (100*3.50) + (200*4.00) + (300*4.50) + (u - 700)*5.00
print('Bill  amount  :  ' , cost)

#  Find  outputs
while  True:
	print('Hello')
print('Bye') # It prints infinite times, because this while runs infinite times as condition is always True, so loop never stops.

#  Find  outputs
while  False:
	print('Hello')
print('Bye') # Bye, because as while condition is false, it will not print statement inside while loop and it moves outside of loop and prints outer statement 