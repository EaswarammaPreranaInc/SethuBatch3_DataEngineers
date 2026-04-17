'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''


c1 = 3 + 4j 
c2 = 5 + 4j

sum = c1 + c2
sub = c1 - c2
mul = c1 * c2
div = c1 / c2

print(f"sum: {sum}")
print(f"subtract: {sub}")
print(f"multiple: {mul}")
print(f"division: {div}")


output 


Sum: (8+10j)
Difference: (-2-2j)
Product: (-9+38j)
Division: (0.639344262295082+0.03278688524590164j)





'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

length = float(input("enter a lenght")

breadth = float(input("enter a breadth")

area formula 
length * breadth 

area = length * breadth 

 perimeter formula 2 * (length + breadth)

perimeter = 2 * (length + breadth)

print (f"area of rectangle is : {area} ")
print (f"perimeter of rectangle is : {perimeter}")


output
enter a lenght = 4
enter a breadth = 5
area : 20.00
perimeter : 18.00





'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''




import math

radius = float(input("Enter radius of sphere: "))

volume = (4/3) * math.pi * (radius ** 3)

print(f"Volume of sphere is: {volume:.2f}")



output
Enter radius of sphere:3
Volume of sphere is: 113.10







'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''


principal = float (input("enter principal amount: "))
rate = float (input("enter rate of interest:"))
time = float(input ("enter time in years: "))

simple_interest = (principal * rate * time )/100

compound_interest = principal *(1+rate/100)**time-principle

print(f"simple interest = {simple_interest:.2f}")
print(f"compound interest = {compound_interest:.2f") 



output
enter principal amount:10000
enter rate of interest:5
enter time in years:2

Simple Interest = 1000.00
Compound Interest = 1025.00





'''
(Home  work)
 Write  a  program  to  swap  values  of  two   objects   using  3rd  object

 Let  x = 10  and  y = Hyd
 What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''


x = 10
y = "Hyd"

print("before swap:")
print(f"x = {x}")
print(f"y = {y}")

temp = x                                      #temp=x---->x=y--->y=temp
x = y
y = temp

print("ofter swap:")
print(f"x= {x}")
print(f"y = {y}")



output

Before Swap:
x = 10
y = Hyd

After Swap:
x = Hyd
y = 10




'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''


x = 25
y = 10

print("before swap:")
print(f"x = {x}")
print(f"y = {y}")


x = x + y
y = x - y
x = x - y


print ("ofter swap:")
print (f"x = {x}" )
print(f"y = {y}")

output

Before Swap:
x = 25
y = 10

After Swap:
x = 10
y = 25





'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

x = 25
y = 10

print("Before Swap:")
print(f"x = {x}")
print(f"y = {y}")

# Swapping without 3rd variable
x = x * y
y = x / y
x = x / y

print("\nAfter Swap:")
print(f"x = {x}")
print(f"y = {y}")



output

Before Swap:
x = 25
y = 10

After Swap:
x = 10.0
y = 25.0





# Identify  error
else:
		print('else  suite')
print('Outside')


#error else must be attached to an if block



# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

#error Missing colon : after if condition



# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

#error Missing colon : after else





# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

#IndentationError



# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

#No Syntax Error
#No Indentation Error





# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

output
Python does NOT use { } for blocks






# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


ouput
No error in syntax






# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')


output

One
Two
Three
Bye



# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)



month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")




output
Enter month number 6
june




'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''



year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

output
Enter a year:2016
2016 is a Leap Year




'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a > b and a > c:
    print(f"{a} is the largest")
else:
    if b > c:
        print(f"{b} is the largest")
    else:
        print(f"{c} is the largest") 

output

10
20
15
20 is the largest






'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''


x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

if x == 0 and y == 0:
    print("Point lies at Origin")

elif x == 0:
    print("Point lies on Y-axis")

elif y == 0:
    print("Point lies on X-axis")

elif x > 0 and y > 0:
    print("Point lies in 1st Quadrant")

elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")

elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")

else:
    print("Point lies in 4th Quadrant")

output
x = 5
y = 3
Point lies in 1st Quadrant


x = -4
y = 6
Point lies in 2nd Quadrant

x = 0
y = 0
Point lies at Origin




'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''


a = 10
b = 20
c = 7

# Step 1: Assume
max_val = a
min_val = a

# Step 2: Find max
if b > max_val:
    max_val = b

if c > max_val:
    max_val = c

# Step 3: Find min
if b < min_val:
    min_val = b

if c < min_val:
    min_val = c

# Step 4: Find middle
mid = (a + b + c) - (max_val + min_val)

print(f"Max = {max_val}")
print(f"Min = {min_val}")
print(f"Mid = {mid}")

output

Max = 20
Min = 7
Mid = 10




