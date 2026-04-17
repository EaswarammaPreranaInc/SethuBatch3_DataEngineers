# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers


# Program:

# Taking complex inputs
c1 = complex(input("Enter first complex number (e.g. 3+4j) : "))
c2 = complex(input("Enter second complex number (e.g. 5+6j) : "))

# Operations
sum_result = c1 + c2
diff_result = c1 - c2
prod_result = c1 * c2
div_result = c1 / c2

# Display results
print("Sum        :", sum_result)
print("Difference :", diff_result)
print("Product    :", prod_result)
print("Division   :", div_result)

#Output:

Enter first complex number (e.g. 3+4j) : 3+4j
Enter second complex number (e.g. 5+6j) : 5+6j

Sum        : (8+10j)
Difference : (-2-2j)
Product    : (-9+38j)
Division   : (0.639344262295082+0.03278688524590164j)

# Write  a  program  to  determine  area  and  perimeter  of  rectangle

# Program:

# Inputs
length = float(input("Enter length of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))

# Calculations
area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of rectangle :", area)
print("Perimeter of rectangle :", perimeter)


# Output:

Enter length of rectangle : 10
Enter breadth of rectangle : 5
Area of rectangle : 50.0
Perimeter of rectangle : 30.0

# Write a program to determine volume of a sphere

import math

# Input
radius = float(input("Enter radius of sphere : "))

# Calculation
volume = (4/3) * math.pi * (radius ** 3)

print("Volume of sphere :", volume)



# Outputs

Enter radius of sphere : 7
Volume of sphere : 1436.7550402417319

# Write a program to determine simple interest and compound interest

#Program

p = float(input("Enter principle amount : "))
t = float(input("Enter time (in years) : "))
r = float(input("Enter rate of interest : "))

# Simple Interest
si = (p * t * r) / 100

# Compound Interest
ci = p * (1 + r / 100) ** t - p

print("Simple Interest :", si)
print("Compound Interest :", ci)

#Output:

Enter principle amount : 10000
Enter time (in years) : 2
Enter rate of interest : 5

Simple Interest : 1000.0
Compound Interest : 1025.0

# Write a program to swap values of two objects using 3rd object


# Program

x = 10
y = "Hyd"

print("Before Swap :")
print("x =", x)
print("y =", y)

# Swapping using third variable
temp = x
x = y
y = temp

print("\nAfter Swap :")
print("x =", x)
print("y =", y)

# Output

Before Swap :
x = 10
y = Hyd

After Swap :
x = Hyd
y = 10

#Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

# Using one addition and two subtractions

x = 25
y = 10

print("Before Swap :")
print("x =", x)
print("y =", y)

# Swapping
x = x + y
y = x - y
x = x - y

print("\nAfter Swap :")
print("x =", x)
print("y =", y)

Output:

Before Swap :
x = 25
y = 10

After Swap :
x = 10
y = 25

#Write a program to swap values of two objects without using 3rd object

# Using one multiplication and two divisions

x = 25
y = 10

print("Before Swap :")
print("x =", x)
print("y =", y)

# Swapping
x = x * y
y = x / y
x = x / y

print("\nAfter Swap :")
print("x =", int(x))
print("y =", int(y))

#Output:

Before Swap :
x = 25
y = 10

After Swap :
x = 10
y = 25

# Identify  error
else:
		print('else  suite')
print('Outside')

#Error: else without corresponding if
#Reason: else must follow an if block.


# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
#Error:Missing : (Colon) After if Condition
# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

#Error:Missing : (Colon) After else Condition


# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

#Error: Indentation error (no indentation inside if and else)

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# Error Beacues Wrong indentation of else And else must align with if

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

# Error : { } block syntax invalid in Python and Curly braces {} cannot be used for code blocks


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

'''
 Indentation Error / Invalid Syntax

After else: you must properly indent the next if block.

Python expects an indented block after else: but here if []: is written at the same indentation level.
'''
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

# Program:

num = int(input("Enter any integer : "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Output:

Enter any integer : 15
Odd number

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
#otput:
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
#Non-empty dictionary is True

#Output
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

#Empty dictionary is False

#Output

Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

# Program

month = input("Enter month number (1-12) : ")

if month.isdigit():   # checking input is integer
    month = int(month)

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
        print("Input should be between 1 and 12")
else:
    print("Input should be an integer")

#Output:

Enter month number (1-12) : 5
May

#output:

Enter month number (1-12) : 13

Input should be between 1 and 12

#Output:

Enter month number (1-12) : 5.0

Input should be an integer

# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

# Program:

num = int(input("Enter a digit (0-9) : "))

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

#Output:

Enter a digit (0-9) : 4
Four

# Write a program to test year is leap year or not

# Program

year = int(input("Enter 4-digits  year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

# Ouput:

Enter 4-digits  year  : 2024
2024 is a Leap Year

# Output:

Enter 4-digits  year  : 2026
2026 is Not a Leap Year


# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

# Program:

a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))

if a >= b and a >= c:
    print("Largest number is :", a)
else:
    if b >= a and b >= c:
        print("Largest number is :", b)
    else:
        print("Largest number is :", c)

# Output

Enter first number  : 15
Enter second number : 25
Enter third number  : 20
Largest number is : 25

#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

choice = input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius : ")

temp = float(input("Enter temperature : "))

if choice == 'C' or choice == 'c':
    fahrenheit = 1.8 * temp + 32
    print("Temperature in Fahrenheit :", fahrenheit)

elif choice == 'F' or choice == 'f':
    celsius = (temp - 32) / 1.8
    print("Temperature in Celsius :", celsius)

else:
    print("Invalid input")

#Output:

Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius : 1
Enter temperature : 25
Temperature in Fahrenheit : 77.0

#Output:

Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius : 2
Enter temperature : 77
Temperature in Celsius : 25.0

#Output:

Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius : 3
Invalid input

# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin

# Program:

x = float(input("Enter value of x : "))
y = float(input("Enter value of y : "))

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

#Output:

Enter value of x : -5
Enter value of y : 4
Point lies in 2nd Quadrant

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

# Program:

a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))

max = a
min = a

if b > max:
    max = b
if c > max:
    max = c

if b < min:
    min = b
if c < min:
    min = c

mid = (a + b + c) - (max + min)

print("Largest input:", max)
print("Smallest input:", min)
print("Middle input :", mid)

#Output:

Enter first number  : 10
Enter second number : 20
Enter third number  : 7

Largest input: 20.0
Smallest input: 7.0
Middle input : 10.0 



