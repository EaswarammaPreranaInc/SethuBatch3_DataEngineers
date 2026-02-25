Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

# Define the complex numbers
c1 = 3 + 4j
c2 = 5 + 6j

sum_result = c1 + c2
difference_result = c1 - c2
product_result = c1 * c2
division_result = c1 / c2

# Display results
print("First complex number:", c1)
print("Second complex number:", c2)
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Division:", division_result)

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''

Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

# Input
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)

# output

Enter length of rectangle: 4
Enter breadth of rectangle: 5
Area of rectangle: 20.0
Perimeter of rectangle: 18.0


Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math

radius = float(input("Enter radius of sphere: "))
volume = (4/3) * math.pi * radius**3
print("Volume of sphere:", volume)

# output

Enter radius of sphere: 3.5
Volume of sphere: 179.59


Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

# Input
p = float(input("Enter principal amount: "))
t = float(input("Enter time (in years): "))
r = float(input("Enter rate of interest: "))

# Simple Interest
si = (p * t * r) / 100

# Compound Interest
ci = p * (1 + r / 100) ** t - p

print("Simple Interest:", si)
print("Compound Interest:", ci)

# output

Enter principal amount: 1000
Enter time (in years): 3
Enter rate of interest: 7.5
Simple Interest: 2250.00
Compound Interest: 2422.97


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

# Initial values
x = 10
y = "Hyd"

print("Before swapping:")
print("x =", x)
print("y =", y)

# Swapping using third variable
temp = x
x = y
y = temp

print("\nAfter swapping:")
print("x =", x)
print("y =", y)

# output

Before swapping:
x = 10
y = Hyd

After swapping:
x = Hyd
y = 10


Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10

#  program

x = 25
y = 10

print("Before swapping:")
print("x =", x)
print("y =", y)

# Swapping without third variable
x = x + y
y = x - y
x = x - y

print("\nAfter swapping:")
print("x =", x)
print("y =", y)

# output

Before swapping:
x = 25
y = 10

After swapping:
x = 10
y = 25

using one multiplication and two division

# program
x = 25
y = 10

print("Before swapping:")
print("x =", x)
print("y =", y)

# Swapping without third variable
x = x * y
y = x / y
x = x / y

print("\nAfter swapping:")
print("x =", x)
print("y =", y)

# output

Before swapping:
x = 25
y = 10

After swapping:
x = 10.0
y = 25.0



# Identify  error
else:
		print('else  suite')
print('Outside')
# else without corresponding if
 #Reason: else must follow an if block.


# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# Error : missing : (colon) after if condition


# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

#Error: missing : (colon) after if condition

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# Error: Indentation error ( no indentation inside if and else)

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')


print('Bye')

# Error because wrong indentation of else and else must align with if


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

# Error: {}block syntax invalid {} cannot be used for code blocks

 
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

# Error: identation Error


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

# program

number = int(input("Enter a number: "))

# Check even or odd
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")



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
# Empty tuple is False
# output
One
Two
Three
Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

# non-Empty dictionary is true

# output

Hyd
Sec
Cyb
Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# empty dictionary is false

# output 

Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

# Input
month = int(input("Enter month number (1-12): "))

# Check month name
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
    print("Input should be 1and 12")

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
'''

# Input
num = int(input("Enter a digit (0-9): "))

# Check digit and print in words
if num == 0:
    print("Zero")
else:
    if num == 1:
        print("One")
    else:
        if num == 2:
            print("Two")
        else:
            if num == 3:
                print("Three")
            else:
                if num == 4:
                    print("Four")
                else:
                    if num == 5:
                        print("Five")
                    else:
                        if num == 6:
                            print("Six")
                        else:
                            if num == 7:
                                print("Seven")
                            else:
                                if num == 8:
                                    print("Eight")
                                else:
                                    if num == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")

# output
Enter a digit (0-9): 4
Four


Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
'''

# Input
year = int(input("Enter a year: "))

# Check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# output

Enter a year: 1992
1992 is a Leap Year

Enter a year: 2026
2026 is non a Leap Year


Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
'''

# Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Determine the largest number
if a >= b and a >= c:
    largest = a
else:
    if b >= a and b >= c:
        largest = b
    else:
        largest = c
print("The largest number is:", largest)

# output

Enter first number: 10
Enter second number: 25
Enter third number: 15
The largest number is: 25



Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
'''

# Input temperature and choice
temp = float(input("Enter the temperature: "))
choice = input("Convert to (F)ahrenheit or (C)elsius? ").upper()

# Conversion
if choice == "F":
    result = 1.8 * temp + 32
    print(f"{temp}°C = {result}°F")
else:
    if choice == "C":
        result = (temp - 32) / 1.8
        print(f"{temp}°F = {result}°C")
    else:
        print("Invalid choice! Enter F or C.")

 # 0utput

Enter the temperature: 25
Convert to (F)ahrenheit or (C)elsius? F
25.0°C = 77.0°F

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
'''

x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

# Check position
if x == 0 and y == 0:
    print("The point is at the Origin")
else:
    if x == 0:
        print("The point lies on the Y-axis")
    else:
        if y == 0:
            print("The point lies on the X-axis")
        else:
            if x > 0 and y > 0:
                print("The point lies in the 1st Quadrant")
            else:
                if x < 0 and y > 0:
                    print("The point lies in the 2nd Quadrant")
                else:
                    if x < 0 and y < 0:
                        print("The point lies in the 3rd Quadrant")
                    else:
                        print("The point lies in the 4th Quadrant")

# output

Enter x-coordinate: -10
Enter y-coordinate: 20
The point lies in the 2st Quadrant


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
# program

# Input three numbers
a = 10
b = 20
c = 7

# Find largest
if a >= b and a >= c:
    largest = a
else:
    if b >= a and b >= c:
        largest = b
    else:
        largest = c

# Find smallest

if a <= b and a <= c:
    smallest = a
else:
    if b <= a and b <= c:
        smallest = b
    else:
        smallest = c

middle = (a + b + c) - (largest + smallest)

print("Largest:", largest)
print("Smallest:", smallest)
print("Middle:", middle)

# output

Enter first input : 10
Enter second input : 20
Enter third input : 7
Largest input : 20
Smallest input : 7
Middle input : 10







