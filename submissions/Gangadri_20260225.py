# 1 . Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
# output : 											         =  39 / 61 + 2j / 61

# Input complex numbers
a = 3 + 4j
b = 5 + 6j

# Operations
sum_result = a + b
diff_result = a - b
prod_result = a * b
div_result = a / b

# Output results
print("First Complex Number  =", a)
print("Second Complex Number =", b)

print("\nSum =", sum_result)
print("Difference =", diff_result)
print("Product =", prod_result)
print("Division =", div_result)


# 2 . (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)


# output : 

# Input values
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

# Calculations
area = length * breadth
perimeter = 2 * (length + breadth)

# Output results
print("Area of Rectangle =", area)
print("Perimeter of Rectangle =", perimeter)


# 3 . (Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

# output : 

import math   # To use value of pi

# Input
r = float(input("Enter radius of sphere: "))

# Formula
volume = (4/3) * math.pi * (r ** 3)

# Output
print("Volume of Sphere =", volume)



# 4 .(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

# output : 

# Input values
p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
r = float(input("Enter rate of interest: "))

# Simple Interest
si = (p * t * r) / 100

# Compound Interest
ci = p * (1 + r/100) ** t - p

# Output results
print("Simple Interest =", si)
print("Compound Interest =", ci)


# 5 . (Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

# output : 

# Initial values
x = 10
y = "Hyd"

print("Before swap:")
print("x =", x)
print("y =", y)

# Using third variable
temp = x
x = y
y = temp

print("\nAfter swap:")
print("x =", x)
print("y =", y)


# 6 . (Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10

output : 

# Initial values
x = 25
y = 10

print("Before swap:")
print("x =", x)
print("y =", y)

# Swapping using addition and subtraction
x = x + y      # Step 1
y = x - y      # Step 2
x = x - y      # Step 3

print("\nAfter swap:")
print("x =", x)
print("y =", y)


# 7 . (Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10


# output : 

# Initial values
x = 25
y = 10

print("Before swap:")
print("x =", x)
print("y =", y)

# Swapping using multiplication and division
x = x * y      # Step 1
y = x / y      # Step 2
x = x / y      # Step 3

print("\nAfter swap:")
print("x =", x)
print("y =", y)


# 8 . # Identify  error
else:
		print('else  suite')
print('Outside')

# output : 
if True:
    print("if suite")
else:
    print("else suite")

print("Outside")

# 9 . # Identify  error
if  9 > 5
	print('Hello')
print('Bye')

# output : 
if 9 > 5:
    print('Hello')

print('Bye')

# 10 . # Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

# output : 
if 9 > 12:
    print('Hyd')
else:
    print('Sec')


# 11 . # Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# output : 

if (10, 20, 15):
    print('Hyd')
else:
    print('Sec')


# 11 . # Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# output : if ():
    print('Hyd')
else:
    print('Sec')

print('Bye')


# 12 . # Identify  error
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

# output : 
if {}:
    print('One')
    print('Two')
    print('Three')
else:
    print('Four')
    print('Five')
    print('Six')

print('Bye')


# 13 . # Identify  error
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

# output : 
if ():
    print('One')
    print('Two')
    print('Three')

elif []:
    print('Four')
    print('Five')
    print('Six')

elif {}:
    print('Seven')
    print('Eight')
    print('Nine')

else:
    print('Hyd')
    print('Sec')
    print('Cyb')

print('Bye')


# 14 .  Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
# output : 
# Input month number
m = int(input("Enter month number (1-12): "))

if m == 1:
    print("January")
elif m == 2:
    print("February")
elif m == 3:
    print("March")
elif m == 4:
    print("April")
elif m == 5:
    print("May")
elif m == 6:
    print("June")
elif m == 7:
    print("July")
elif m == 8:
    print("August")
elif m == 9:
    print("September")
elif m == 10:
    print("October")
elif m == 11:
    print("November")
elif m == 12:
    print("December")
else:
    print("Invalid month number")


# 15 . Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid

# output : d = int(input("Enter a digit (0-9): "))

if d == 0:
    print("Zero")
else:
    if d == 1:
        print("One")
    else:
        if d == 2:
            print("Two")
        else:
            if d == 3:
                print("Three")
            else:
                if d == 4:
                    print("Four")
                else:
                    if d == 5:
                        print("Five")
                    else:
                        if d == 6:
                            print("Six")
                        else:
                            if d == 7:
                                print("Seven")
                            else:
                                if d == 8:
                                    print("Eight")
                                else:
                                    if d == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")


# 16 . Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions

# output :
 # Input year
year = int(input("Enter a year: "))

# Leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")


# 17 . '''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions

# output : 

# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Find largest number
if a > b and a > c:
    print("Largest number =", a)
else:
    if b > c:
        print("Largest number =", b)
    else:
        print("Largest number =", c)


# 18 . Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8


# output : 

# Input temperature and choice
temp = float(input("Enter temperature value: "))
choice = input("Enter C for Celsius or F for Fahrenheit: ")

if choice == 'C' or choice == 'c':
    # Celsius to Fahrenheit
    f = 1.8 * temp + 32
    print("Temperature in Fahrenheit =", f)

else:
    # Fahrenheit to Celsius
    c = (temp - 32) / 1.8
    print("Temperature in Celsius =", c)


# 19 . Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif

# output : 

# Input values
x = float(input("Enter x value: "))
y = float(input("Enter y value: "))

# Check position of point
if x > 0 and y > 0:
    print("Point lies in 1st Quadrant")

elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")

elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")

elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")

elif x != 0 and y == 0:
    print("Point lies on X-axis")

elif x == 0 and y != 0:
    print("Point lies on Y-axis")

else:
    print("Point is at Origin")


# 20 . Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

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


# output : a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Step 1: Assume a is max and min
max = a
min = a

# Step 2: Find max
if b > max:
    max = b
if c > max:
    max = c

# Step 3: Find min
if b < min:
    min = b
if c < min:
    min = c

# Step 4: Find middle number
mid = a + b + c - (max + min)

# Output
print("Largest =", max)
print("Smallest =", min)
print("Middle =", mid)

