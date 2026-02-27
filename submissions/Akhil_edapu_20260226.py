

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
a = int(input("Enter 1st number :"))
b= int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))

if (a+b >c and b+c>a and c+a >b):
    if( a==b==c):
        print("Equilertal triangle")
        print(f'Area = {math.sqrt(3)/4*a*a}')
    elif(a==b or b==c or c==a):
        print("Isosceles triangle")
        print(f'Perimeter : {a+b+c}')
    else:
        print("Scalene triangle")
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f'Area:{area}')

else:
    print("It\'s not a triangle")



        


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

a = float(input("Enter 1st number :"))
if a == 0:
    print("Value cannot be 0")
    exit()
b= float(input("Enter 2nd number :"))
c = float(input("Enter 3rd number :"))
disc = b**2-4a*c
if disc > 0:
    print("Roots are real and distinct ")
    root1 = (-b+math.sqrt(disc))/(2*a)
    root2 = (-b-math.sqrt(disc))/(2*a)
    print(f'Root1 : {root1}')
    print(f'Root2 : {root2}')
elif disc <0:
    print("Roots are imaginary or complex")
    real = -b/2*a
    imag = math.sqrt(-disc)/(2*a)
    print("Root1 : {real}+{imag}")
    print("Root2 : {real}+{imag}")
    
else:
    print("Roots are real and equal")
    root = -b/2*a
    











'''
Write  a  program   to  determine  a  point (x , y)  lies  inside , outside  or  on  the  circle.
Center  is  origin  and  radius  is  'r'

1) What  is  the  distance  between  origin  and  point (x , y) ?  --->  sqrt(x ^ 2 + y ^ 2)

2) Where  is  the  point  if  distance >  raidus ?  --->  Outside  the  circle

3) Where  is  the  point  if  distance < raidus ?  --->  Inside  the  circle

4) Where  is  the  point  if  distance  and  raidus   are  same ?  ---> On  the  circle
'''

a = int(input("Enter 1st number :"))
b= int(input("Enter 2nd number :"))
r = int(input("Enter 3rd number :"))

d = math.sqrt(a**2+b**2)
if d > r:
    print("Outside the circle")
elif(d<r):
    print("Inside the circle")
else:
    prnt("on the circle")
    





# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') #priinted on screen there is no 4 to match 




# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two') # printed om screen
print('Bye') #printed



# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') # printed on screen there is no match of 2 




#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') # this is printed on screen
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') #printed




# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') # this printed on screen
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #printed



'''
1) What  are  the  outputs  if  input  is  -6 ? ---> # hyd sec cyb bye is printed
2) What  are  the  outputs  if  input  is  15  ?  ---> # one two three bye is printed
3) What  are  the  outputs  if  input  is  10.8  ?  ---> Nothing
4) What  are  the  outputs  if  input  is  0  ?  ---> hyd sec cyb bye is printed
5) What  are  the  outputs  if  input  is  -10  ?  ---> one two three byeis printed
6) What  are  the  outputs  if  input  is  7  ?  ---> hyd sec cyb bye is printed 
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
1) What  is  the  output  when  input  is  (-10 , -20) ?  ---> # tuple (-10,-20) is printed
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> # tuple (10,0) is printed
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> # tuple (-0,-20) is printed
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> # tuple (0,0) is printed
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  ---> # tuple (10,20,30) is printed
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> # List [10,20] is printed
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> #List [0,-25] is printed
8) What  is  the  output  when  input  is  ()  ?  --->  # empty set 
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> #set {10,20} is printed
10) What  is  the  output  when  input  is  (25,) ?  ---> #tuple (25) is printed
11) What  is  the  output  when  input  is  {10 : 20} ?  ---> #dict {10:20} printed
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
	case  :
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
while  True: #Every time True is 1 so it keep repeating the while loop
	print('Hello')
print('Bye') # the bye is never exceuted




#  Find  outputs
while  False: # False is 0 so the while loop terminted 
	print('Hello')
print('Bye') # print is exceuted print 'bye' on screen


