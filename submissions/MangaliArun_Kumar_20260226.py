# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One') # Error
	case  2:
		print('Two') # Error
	case  3:
		print('Three') # Error
print('Bye') # Bye

# Identify  Error
i = 2
match  i:
	case  1:
		print('One') # Error
	case  _: # Error bcz anonymous object should be declate at the end
		print('None of   the  above')
	case  2:
		print('Two') # Two
print('Bye') # Bye

# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One') # Error
	case  _:  
		print('Hello') # Error
	case  _:  
		print('Bye') # Error
print('End') # End

#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # Hyd
	case  1:
		print('Sec') 
	case  1:
		print('Cyb')
print('Bye') # Bye

# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple') # Error
	case  'B':
		print('Book') # Book
	case  'C':
		print('Cafe') # Error
	case  _:
		print('None of  the  above') # Error
print('Bye') # Bye

'''
1) What  are  the  outputs  if  input  is  -6 ? ---> Sec Bye
2) What  are  the  outputs  if  input  is  15  ?  ---> Two Bye
3) What  are  the  outputs  if  input  is  10.8  ?  ---> India Bye
4) What  are  the  outputs  if  input  is  0  ?  ---> Cyb Bye
5) What  are  the  outputs  if  input  is  -10  ?  ---> One Bye
6) What  are  the  outputs  if  input  is  7  ?  ---> Hyd bye
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> Not a point
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> error
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> not a point
8) What  is  the  output  when  input  is  ()  ?  ---> Error
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Quadrant
10) What  is  the  output  when  input  is  (25,) ?  ---> x axis
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> Error
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
		
#  Find  outputs
while  True:
	print('Hello') # Hello infinate times
print('Bye') # Bye

#  Find  outputs
while  False:
	print('Hello') # nothing
print('Bye') # Bye

# Write  a  program  to  determine  three  sides  form  a  triangle  or  not
import math
x = int(input("Enter 1st side : "))
y = int(input("Enter 2nd side : "))
z = int(input("Enter 3rd side : "))
if x==y:
    if y==z :
        print("Equilateral Triangle")
        area = (math.sqrt(3))/4*x**2
        print("area : ",area)
    if y!=z:
        print("Isoscles Triangle")
        perimeter = x+y+z
        print("perimeter : ",perimeter)
else:
    print("scalene Triangle")
    s = (x+y+z)/2
    area = math.sqrt(s*(s-x)*(s-y)*(s-z))
    print("area : ",area)
    perimeter = x+y+z
    print("perimeter : ",perimeter)



# Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
# Center  is  origin  and  radius  is  'r'
x = int(input("Enter value of x : "))
y = int(input("Enter value of y : "))
r = int(input("Enter radius of circle : "))
dist = math.sqrt(x**2+y**2)
if dist > r:
    print("Outside the circle")
if dist < r:
    print("Inside the circle")
if dist == r :
    print("On the circle")
	

# Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0
import math
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))
if a != 0:
     disc = b**2-4*a*c

     if disc > 0:
        print("roots are distinct")
        root1 = (-b+math.sqrt(disc))/(2*a)
        root2 = (-b-math.sqrt(disc))/(2*a)
        print("root1 : ",root1)
        print("root2 : ",root2)

     elif disc == 0:
          print("roots are real and same")
          r = -b/(2*a)
          print("root1 : ",r)
     else :
          print("roots are imaginary or complex")
          real = -b/(2*a)
          imag = math.sqrt(-disc)/(2*a)
          print("root1 : ",complex(real,imag))
          print("root1 : ",complex(real,imag))
else :
   print("not a quadratic equation")

# Write  a  program  to  determine  bill  amount  and  input  is  units
units = int(input("Enter units :"))
match units :
    case u if u <= 100:
        cost = u*3.00
    case u if u <=200:
        cost = 100*3.00+(u-100)*3.50
    case u if u <= 400:
        cost = 100*3.00+100*3.50+(u-200)*4.00
    case u if u <= 700:
        cost = 100*3.00+100*3.50+200*4+(u-400)*4.5
    case _ :
        cost = 100*3.00+100*3.50+200*4+300*4.5+(units-700)*5
print("Bill amount :",cost)