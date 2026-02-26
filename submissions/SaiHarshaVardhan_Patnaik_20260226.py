# Program to determine three sides form triange or not
from math import *

a = int(input("Enter first side value: "))
b = int(input("Enter second side value: "))
c = int(input("Enter third side value: "))

# check triangle first
if (a+b>c) and (b+c>a) and (c+a>b):
    print("It is Triangle.")

    s = (a+b+c)/2
    d = sqrt(s*(s-a)*(s-b)*(s-c))   

    if a==b==c:
        print("Equilateral Triangle")
        print("Area:", (sqrt(3)/4)*(a**2))

    elif a==b or b==c or c==a:
        print("Isosceles Triangle")
        print("Perimeter:", a+b+c)

    else:
        print("Scalene Triangle")
        print("Area:", d)
        print("Perimeter:", a+b+c)

else:
    print("Not a Triangle.")
    
'''
Output:
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first side value: 3
Enter second side value: 4
Enter third side value: 5
It is Triangle.
Scalene Triangle
Area: 6.0
Perimeter: 12
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first side value: 7
Enter second side value: 8
Enter third side value: 7
It is Triangle.
Isosceles Triangle
Perimeter: 22
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first side value: 7
Enter second side value: 7
Enter third side value: 7
It is Triangle.
Equilateral Triangle
Area: 21.217622392718745
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first side value: 7
Enter second side value: 8
Enter third side value: 16
Not a Triangle.

'''
            
#Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
from math import *

a = float(input("Enter first input: "))
b = float(input("Enter second input: "))
c = float(input("Enter third input: "))

if a != 0:
    print("It is a Quadratic equation.")

    # correct discriminant
    d = (b**2) - (4*a*c)

    if d > 0:
        print("There are two real roots:",
              f"{(-b + sqrt(d)) / (2*a)}",
              "and",
              f"{(-b - sqrt(d)) / (2*a)}")

    elif d == 0:
        print("Root is:", f"{-b / (2*a)}")

    else:
        print("Complex or imaginary roots:")

        e = -b / (2*a)          # real part
        f = sqrt(-d) / (2*a)    # imaginary part

        print(f"root1: {e} + {f}j")
        print(f"root2: {e} - {f}j")

else:
    print("It is not a Quadratic equation.")

'''
Output:
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first input: 5
Enter second input: 6
Enter third input: 5
It is a Quadratic equation.
Complex or imaginary roots:
root1: -0.6 + 0.8j
root2: -0.6 - 0.8j
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first input: 5
Enter second input: 10
Enter third input: 5
It is a Quadratic equation.
Root is: -1.0
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first input: 3
Enter second input: 10
Enter third input: 3
It is a Quadratic equation.
There are two real roots: -0.3333333333333333 and -3.0
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter first input: 0
Enter second input: 0
Enter third input: 0
It is not a Quadratic equation.
'''

#Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle. Center  is  origin  and  radius  is  'r'
from math import *
x=int(input("Enter vlaue of x:"))
y=int(input("Enter value of y:"))
r=int(input("Enter radius of circle :"))
d= sqrt(x**2 + y**2)
if d>r:
    print("Point is outside the circle")
elif d<r:
    print("Point is insideside the circle")
else:
    print("Point is on the circle")

'''
Output:
Enter vlaue of x:3
Enter value of y:4
Enter radius of circle :5
Point is on the circle
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
print('Bye')

#Output: Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: #Error
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
		print('Hyd')
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye')

#Output:Hyd
        #Bye

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
Output:
Enter any  number :  -6
Hyd
Sec
Cyb
Bye
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter any  number :  15
One
Two
Three
Bye
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter any  number :  10.8
India
China
Usa
Bye
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter any  number :  0
Hyd
Sec
Cyb
Bye
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter any  number :  -10
One
Two
Three
Bye
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter any  number :  7
Hyd
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
Output:
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (-10,-20)
Quadrant
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (10,0)
x - axis
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (0,-20)
y - axis
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (0,0)
Origin
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (10,20,30)
Not  a  point
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  [10,20]
Quadrant
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  [0,-25]
y - axis
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  ()
Not  a  point
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  {10,20}
Not  a  point
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  (25,)
Not  a  point
PS C:\Users\hp\AppData\Local\Programs\Microsoft VS Code> & C:\Users\hp\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/hp/OneDrive/Desktop/Data Engineering/26Homework.py"
Enter  any  point  in  the  form  of  (x , y) :  {10:20}
Not  a  point
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
units = int(input('Enter units: '))  

match units:
    case _ if units <= 100:
        cost = units * 3.00
    case _ if units <= 200:
        cost = (100 * 3.00) + (units - 100) * 3.50
    case _ if units <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + (units - 200) * 4.00
    case _ if units <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (units - 400) * 4.50
    case _:  # Default case catches everything above 700
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + (300 * 4.50) + (units - 700) * 5.00

print('Bill amount: Rs.', cost)

'''
Output:
Enter units: 100
Bill amount: Rs. 300.0
'''

#  Find  outputs
while  True:
	print('Hello')
print('Bye')

'''
Output:
Hello
Hello
Hello
.....
.....
.....
.....
Hello
'''