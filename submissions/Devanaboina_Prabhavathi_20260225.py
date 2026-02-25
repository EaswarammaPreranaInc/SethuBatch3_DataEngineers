# Read complex numbers from user
a = complex(input("Enter first complex number: "))
b = complex(input("Enter second complex number: "))

# Operations
sum_result = a + b
diff_result = a - b
prod_result = a * b
div_result = a / b

# Output
print("\nSum :", sum_result)
print("Difference :", diff_result)
print("Product :", prod_result)
print("Division :", div_result)
input("\nPress any key to continue")

# Step 1: Inputs
length = float(input("Enter length of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))

# Step 2: Formulas
area = length * breadth
perimeter = 2 * (length + breadth)

# Step 3: Outputs (format same as question)
print("\nArea : {:.2f}".format(area))
print("Perimeter : {:.2f}".format(perimeter))

# Step 4: Hold screen
input("\nPress any key to continue")


import math

# Step 1: Input
radius = float(input("Enter radius : "))

# Step 2: Formula
volume = (4 / 3) * math.pi * radius ** 3

# Step 3: Output (same format as question)
print("\nVolume : {:.2f}".format(volume))

# Step 4: Hold screen
input("\nPress any key to continue")

# Step 1: Inputs
p = float(input("Enter principle : "))
t = float(input("Enter time : "))
r = float(input("Enter rate of interest : "))

# Step 2: Formulas
si = p * t * r / 100
ci = p * (1 + r / 100) ** t - p

# Step 3: Outputs (same format)
print("\nSimple Interest : {:.2f}".format(si))
print("Compound Interest : {:.2f}".format(ci))

# Step 4: Hold screen
input("\nPress any key to continue")


# Step 1: Inputs
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")

# Step 2: Before swap
print("\nBefore swap :")
print("\nx='{}'".format(x))
print("\ny='{}'".format(y))

# Step 3: Swap using 3rd variable
temp = x
x = y
y = temp

# Step 4: After swap
print("\nAfter swap :")
print("\nx='{}'".format(x))
print("\ny='{}'".format(y))

# Step 5: Hold screen
input("\nPress any key to continue")

# Inputs
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))

# Before swap
print("\nBefore swap :")
print("\nx=", x)
print("\ny=", y)

# Swap without 3rd variable ( + and - )
x = x + y
y = x - y
x = x - y

# After swap
print("\nAfter swap :")
print("\nx=", x)
print("\ny=", y)

input("\nPress any key to continue")


# Inputs
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))

# Before swap
print("\nBefore swap :")
print("\nx=", x)
print("\ny=", y)

# Swap without 3rd variable ( * and / )
x = x * y
y = x / y
x = x / y

# After swap
print("\nAfter swap :")
print("\nx=", int(x))
print("\ny=", int(y))

input("\nPress any key to continue")

else:
    print('else suite')# SyntaxError: 'else' cannot appear without a matching 'if' statement
print('Outside')# This line is fine, but the program fails before reaching here

# Identify error
if 9 > 5
    print('Hello')# SyntaxError: Missing colon ':' after the if condition
print('Bye')# This line is correct, but the program stops due to the syntax error above


# Identify error
if 9 > 12:
    print('Hyd')
else
    print('Sec')# SyntaxError: Missing colon ':' after the else statement

# Identify error
if (10, 20, 15):
print('Hyd')# IndentationError: Expected an indented block after the if statement
else:
print('Sec')# IndentationError: Expected an indented block after the else statement


# Identify error
if ():
    print('Hyd')
  else:    # IndentationError: 'else' must be aligned with the matching 'if'
      print('Sec')
print('Bye') # This line is correct, but the program fails due to wrong indentation above



# Identify error
if {}:
{             # SyntaxError: Curly braces '{}' cannot be used to define code blocks in Python
    print('One')
    print('Two')
    print('Three')
}
else:
{         # SyntaxError: Python uses indentation, not curly braces, to define blocks
    print('Four')
    print('Five')
    print('Six')
}
print('Bye')    # This line is correct, but the program fails due to invalid block syntax above


# Identify error
if ():
    print('One')
    print('Two')
    print('Three')
else:
if []:   # IndentationError: Nested if must be properly indented inside the else block
    print('Four')
    print('Five')
    print('Six')
else:
if {}:   # IndentationError: Nested if must be indented to show it belongs to the previous else
    print('Seven')
    print('Eight')
    print('Nine')
else:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')  # This line is fine, but the program fails due to incorrect indentation above


# Input
n = int(input("Enter a number : "))

# Check even or odd using if statement
if n % 2 == 0:
    print(n, "is Even")
else:
    print(n, "is Odd")

# Hold screen
input("\nPress any key to continue")


if():
        print('Hyd')
        print('Sec')
        print('Cyb') #False
else:
        print('One')#one
        print('Two') #Two
        print('Three') #Three
        print('Bye') # Bye

if {10 : 20 , 30 : 40}: #True
        print('Hyd') #Hyd
        print('Sec') #Sec
        print('Cyb') #Cyb
        print('Bye') #Bye

if { }: # False
    print('Hyd')
    print('Sec')
    print('Cyb')
   print('Bye') #Bye


# Read input as string first
m = input("Enter month number (1 -12): ")

# Check integer or not
if not m.isdigit():
    print("Input should be an integer")
else:
    m = int(m)

    # Check range
    if m < 1 or m > 12:
        print("Input should be between 1 and 12")
    else:
        # Month mapping using if-elif
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

# Hold screen
input("\nPress any key to continue")


# Read input as string first
s = input("Enter any digit (0 -9): ")

# Check integer or not
if not s.isdigit():
    print("Invalid")
else:
    n = int(s)

    # Check range 0 to 9
    if n < 0 or n > 9:
        print("Invalid")
    else:
        # No elif: only if statements
        if n == 0:
            print("Zero")
        if n == 1:
            print("One")
        if n == 2:
            print("Two")
        if n == 3:
            print("Three")
        if n == 4:
            print("Four")
        if n == 5:
            print("Five")
        if n == 6:
            print("Six")
        if n == 7:
            print("Seven")
        if n == 8:
            print("Eight")
        if n == 9:
            print("Nine")

# Hold screen
input("\nPress any key to continue")

year = int(input("Enter a year: ")) 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
print(f"{year} is a leap year. ")
else: 
print(f"{year} is not a leap year

22-->Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
Hint:  Write  multiple  conditions
'''
a=float(input('Enter 1st input:'))
b=float(input('Enter 2nd input:'))
c=float(input('Enter 3rd input:'))
if (a>b and a>c):
    print(F'{a}')
else:
    if b>c:
        print(F'{b}')
    else:
        print(F'{c}')

'''
23-->Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 1
Enter celsius temperature : 30
Fahrenheit Equivalent: 86.0
Press any key to continue...
-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 2
Enter celsius temperature : 100
Fahrenheit Equivalent: 37.78
Press any key to continue...
-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 3
Invalid input
Press any key to continue...
'''
x = int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if x== 1:
    c = float(input('Enter celsius temperature : '))
    f = 1.8 * c + 32
    print(F'Fahrenheit Equivalent:{f}')

else:
    if x== 2:
        f = float(input('Enter fahrenheit temperature : '))
        c = (f - 32) / 1.8
        print(F'Celsius Equivalent:{c:.2f}')
    else:
        print('Invalid input')

'''
24-->Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve
2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve
3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve
4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve
5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0
6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero
7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes
8) Hint:  Use  if  ..   elif

-->Sample Output:
Enter value of X co-ordinate : -10
Enter value of y co-ordinate : 20 
2nd quadrant
Press any key to continue...
'''
x=float(input('Enter value of x co-ordinate:'))
y=float(input('Enter value of y co-ordinate:'))
if x > 0 and y > 0:
    print('1st quadrant')
elif x < 0 and y > 0:
    print('2nd quadrant')
elif x < 0 and y < 0:
    print('3rd quadrant')
elif x > 0 and y < 0:
    print('4th quadrant')
elif x != 0 and y == 0:
    print('On X-axis')
elif x == 0 and y != 0:
    print('On Y-axis')
else:
    print('Origin')

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

-->Sample Output 15:
Enter first input : 10
Enter second input : 20
Enter third input : 7
Largest input: 20.0
Smallest input : 7.0
Middle input : 10.0
Press any key to continue...
'''
a=float(input('Enter first input :'))
b=float(input('Enter second input :'))
c=float(input('Enter third input :'))
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
print('Largest input:', max)
if b < min:
    min = b
if c < min:
    min = c
print('Smallest input:', min)
mid = (a + b + c) - (max + min)
print('Middle input:', mid)
