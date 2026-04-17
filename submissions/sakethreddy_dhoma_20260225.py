# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
a=complex(input("Enter First  complex  number:"))
b=complex(input("Enter Second  complex  number:"))
print("Sum :", a + b)
print("Difference :", a - b)
print("Product :", a * b)
print("Division :", a / b)

# Write  a  program  to  determine  area  and  perimeter  of  rectangle
a = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
print("Area : ", a * b)
print("Perimeter : ", 2 * (a + b))

# Write  a  program  to  determine  volume  of  a  sphere
from math import pi
a = float(input("Enter radius : "))
print("Volume : ", 4 / 3 * pi * a ** 3)

# Write  a  program  to  determine  simple  interest  and  compound  interest
a = int(input("Enter principle : "))
b = float(input("Enter time : "))
c = float(input("Enter rate of Interest : "))
print("Simple Interest : ", a * b * c / 100)
print("Compund Interest : ", a * (1  +  c  /  100) **  b  -  a)

# Write  a  program  to  swap  values  of  two   objects   using  3rd  object
x = int(input("Enter 1st input : "))
y = input("Enter 2nd input : ")
print(f"Before swap :  x='{x}'    y='{y}'")
temp = x
x = y
y = temp
print(f"After  swap :  x='{x}'    y='{y}'")

# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before swap :  x='{x}'    y='{y}'")
x = x + y 
y = x - y
x = x - y
print(f"After  swap :  x='{x}'    y='{y}'")

# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before swap :  x='{x}'    y='{y}'")
x = x * y 
y = x / y
x = x / y
print(f"After  swap :  x='{x}'    y='{y}'")

# Identify  error
else:
		print('else  suite')
print('Outside')  # without implenting if else cannot be done

# Identify  error
if  9 > 5
	print('Hello')
print('Bye') # after condition ":" missing

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') # after condition2 ":" missing
	
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') # tab needs to be before statemets in python

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye') # irregular tab and spaces

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
print('Bye') # there is no need of "{}"

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
print('Bye') # no tabs after the condition and before statements

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a=int(input("Enter an Integer : "))
if a % 2 == 0:
	print("Even number")
else:
	print("odd number")
	
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') # One <nextline> Two <nextline> Three <nextline> Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd <nextline> Sec <nextline> Cyd <nextline> Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
a = int(input("Enter month number (1-12): "))
if a == 1:
    print("January")
elif a == 2:
    print("February")
elif a == 3:
    print("March")
elif a == 4:
    print("April")
elif a == 5:
    print("May")
elif a == 6:
    print("June")
elif a == 7:
    print("July")
elif a == 8:
    print("August")
elif a == 9:
    print("September")
elif a == 10:
    print("October")
elif a == 11:
    print("November")
elif a == 12:
    print("December")
else:
    print("Enter valid month number between (1 - 12)")

# Write a program to print digit in words with else and if (do not use elif)
a = int(input("Enter a digit (0–9): "))
if a == 0:
    print("Zero")
else:
    if a == 1:
        print("One")
    else:
        if a == 2:
            print("Two")
        else:
            if a == 3:
                print("Three")
            else:
                if a == 4:
                    print("Four")
                else:
                    if a == 5:
                        print("Five")
                    else:
                        if a == 6:
                            print("Six")
                        else:
                            if a == 7:
                                print("Seven")
                            else:
                                if a == 8:
                                    print("Eight")
                                else:
                                    if a == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")

# Write  a  program  to  test  year  is  leap  year  or  not
int(input("Enter 4-digit year : "))
year = int(input("Enter 4-digit year : "))
if year % 400 == 0:
    print("Leap year")
else:
    if year % 100 == 0:
        print("Not a Leap year")
    else:
        if year % 4 == 0:
            print("Leap year")
        else:
            print("Not a Leap year")

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))
if a > b and a > c:
    print("Largest number :", a)
else:
    if b > c:
        print("Largest number :", b)
    else:
        print("Largest number :", c)

#Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
print("Enter 1 to convert Celsius to Fahrenheit")
print("Enter 2 to convert Fahrenheit to Celsius")
choice = int(input("Enter your choice : "))
if choice == 1:
    c = float(input("Enter celsius temperature : "))
    f = 1.8 * c + 32
    print("Fahrenheit Equivalent :", f)
else:
    if choice == 2:
        f = float(input("Enter fahrenheit temperature : "))
        c = (f - 32) / 1.8
        print("Celsius equivalent :", round(c, 2))
    else:
        print("Invalid choice")

#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
x = float(input("Enter value of x : "))
y = float(input("Enter value of y : "))
if x == 0 and y == 0:
    print("Point is at Origin")
elif x > 0 and y > 0:
    print("Point lies in 1st Quadrant")
elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")
elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")
elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")
elif y == 0 and x != 0:
    print("Point lies on X-axis")
elif x == 0 and y != 0:
    print("Point lies on Y-axis")

#Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
max_val = a
min_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid_val = (a + b + c) - (max_val + min_val)
print("Largest input  :", max_val)
print("Smallest input :", min_val)
print("Middle input   :", mid_val)