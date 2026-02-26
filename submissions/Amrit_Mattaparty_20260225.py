#1
'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j) =  (15 -18j + 20j + 24) /  (25 + 36)=  39 / 61 + 2j / 61
'''
try:
    c1 = complex(input("Enter 1st complex number: "))
    c2 = complex(input("Enter 2nd complex number: "))

    sum  = c1 + c2
    diff = c1 - c2
    prod = c1 * c2
    div  = c1 / c2

    print(f"Sum: {sum}")
    print(f"Difference: {diff}")
    print(f"Product: {prod}")
    print(f"Division: {div}")

except ValueError:
    print("Invalid Input! Please use the format '3+4j' with no spaces.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")




#2
'''
(Home work)
Write a program to determine area and perimeter of rectangle

1) What are the inputs?  ---> length and breadth

2) What are the outputs? ---> area and perimeter

3) What is the area of rectangle? ---> length * breadth

4) What is the perimeter of rectangle ? ---> 2 * (length + breadth)
'''
try:
    l = float(input("Enter length of the rectangle: "))
    b = float(input("Enter breadth of the rectangle: "))
    print(f"Area: {l*b:.2f}")
    print(f"Perimeter: {2*(l+b):.2f}") 
except ValueError:
    print("Error: Please enter a valid numeric value")
except TypeError:
    print("Error: Please ensure length and breadth are positive numbers")



#3
'''
(Home work)
Write a program to determine volume of a sphere

1) What is the input? ---> radius

2) What is the output? ---> volume

3) What is the volume of sphere? --->  4 / 3  * pi *  r ^ 3
'''
import math
try:
    r = float(input("Enter radius of the circle: ")) 
    print(f"Volume: {4/3*math.pi*r**3:.2f}")
except ValueError:
    print("Error: Please enter a valid numeric value.")
except TypeError:
    print("Error: Could not calculate volume. Please check your radius input")



#4
'''
(Home work)
Write a program to determine simple interest and compound interest

1) What are the inputs?  ---> principle , time and rate of interest

2) What are the outputs? ---> Simple interest and compound interest

3) What is simple interest formula?  --->  ptr / 100

4) What is compound interest formula?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
try:
    p = float(input("Enter the principle amount: "))
    t = float(input("Enter the time: ")) 
    r = float(input("Enter the rate of interest: ")) 
    print(f"Simple Interest: {(p*t*r)/100:.2f}") 
    print(f"Compound Interest: {(p*(1 + (r/100))**t) - p:.2f}")
except ValueError:
    print("Error: Please enter a valid numeric value.")
except TypeError:
    print("Error: Unable to process interest. Please verify your amount, time, and rate")



#5
'''
(Home work)
Write a program to swap values of two objects using 3rd object

Let x = 10 and y = Hyd
What are the values of x and y after swap ? --->  x = Hyd and y = 10
'''
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")

print(f"Before swap: x='{x}' y='{y}'")

temp = x
x = y
y = temp

print(f"After swap: x='{x}' y='{y}'")



#6
'''
(Home work)
Write a program to swap values of two objects without using 3rd object

Hint: One addition and two subtractions

x = 25
y =  10
'''
try:
    x = int(input("Enter 1st number (x): "))
    y = int(input("Enter 2nd number (y): "))

    print(f"Before swap: x={x}  y={y}")

    x = x + y  # Addition
    y = x - y  # Subtraction 1
    x = x - y  # Subtraction 2

    print(f"After swap: x={x}  y={y}")
except ValueError:
    print("This method only works with numbers!")



#7
'''
(Home work)
Write a program to swap values of two objects without using 3rd object

Hint: One multiplication and two divisions

x =  25
y =  10
'''
try:
    x = float(input("Enter 1st number (x): "))
    y = float(input("Enter 2nd number (y): "))

    if y == 0:
        print("Error: Cannot divide by zero for this swap method.")
    else:
        print(f"Before swap: x={x}  y={y}")

        x = x * y  #Multiplication
        y = x / y  #Division 1
        x = x / y  #Division 2

        print(f"After swap: x={x}  y={y}")
except ValueError:
    print("Input must be a number!")



#8
# Identify  error
else:
		print('else  suite') #Error as, just a 'if' statement can be stand alone but not else statement 
print('Outside') #Outside



#9
# Identify  error
if  9 > 5 #Error as colon i.e. ':' is missing after if statement 
	print('Hello')
print('Bye') #Bye



#10
# Identify  error
if  9 > 12:
	print('Hyd')
else #Error as colon i.e. ':' is missing after 'else'
	print('Sec')



#11
	# Identify  error
if  (10,20,15): 
print('Hyd') #Error improper indentation
else: 
print('Sec') #Error improper indentation



#12
# Identify  error
if  ():
			print('Hyd')
	else: 
					print('Sec') #Error improper and inconsistet indentation
print('Bye') #Bye



#13
# Identify  error
if  { }:
{ #Error improper usage of delimeter i.e. flower braces are not used to represent a suite in python 
	print('One')
	print('Two')
	print('Three')
}
else:
{ #Error improper usage of delimeter i.e. flower braces are not used to represent a suite in python
	print('Four')
	print('Five')
	print('Six')
}
print('Bye') #Bye



#14
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: #Error as no proper indentation resulting in improper syntax of 'nested if' statement
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
print('Bye') #Bye



#15
# Write a program to determine a number is even or odd with if statement
n = float(input("Enter a number:"))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")



#16
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One') #One
        print('Two') #Two
        print('Three') #Three
print('Bye') #Bye



#17
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') #Hyd
        print('Sec') #Sec
        print('Cyb') #Cyb
print('Bye') #Bye



#18
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye



#19
# Write a program to print month name for input month number by using if and elif (Home  work)
try:
    mn = int(input("Enter month number (1 - 12): "))
    if mn < 1 or mn > 12:
        print("Input should be between 1 and 12")
    elif mn == 1:
        print("January")
    elif mn == 2:
        print("February")
    elif mn == 3:
        print("March")
    elif mn == 4:
        print("April")
    elif mn == 5:
        print("May")
    elif mn == 6:
        print("June")
    elif mn == 7:
        print("July")
    elif mn == 8:
        print("August")
    elif mn == 9:
        print("September")
    elif mn == 10:
        print("October")
    elif mn == 11:
        print("November")
    elif mn == 12:
        print("December")
except ValueError:
    print("Input should be an integer")
except TypeError:
    print("Type Error: Invalid class object type provided")



#20
'''
Write a program to print digit in words with else and if (do not use elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
try:
    digit = int(input("Enter any digit (0 - 9): "))
    if digit < 0 or digit > 9:
        print("Input should be between 0 and 9")
    else:
        if digit == 0:
            print("Zero")
        else:
            if digit == 1:
                print("One")
            else:
                if digit == 2:
                    print("Two")
                else:
                    if digit == 3:
                        print("Three")
                    else:
                        if digit == 4:
                            print("Four")
                        else:
                            if digit == 5:
                                print("Five")
                            else:
                                if digit == 6:
                                    print("Six")
                                else:
                                    if digit == 7:
                                        print("Seven")
                                    else:
                                        if digit == 8:
                                            print("Eight")
                                        else:
                                            if digit == 9:
                                                print("Nine")
except ValueError:
    print("Input should be an integer")
except TypeError:
    print("Type Error occurred")



#21
'''
Write a program to test year is leap year or not

1) What is leap year?  ---> Divisible by 4 but not by 100 (or) divisble by 400

2) Are 2016 , 2020 , 2024 leap years? --->  Yes because leap year for every 4 years

3) Are 1700 , 1800 , 1900 leap years? --->  No because no leap year for every 100 years

4) Are 1600 , 2000 , 2400 leap years?  --->  Yes because leap year for every 400 years

5) Hint: 3 conditions
'''
try:
    yr = int(input("Enter 4-digit year: "))
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")
except ValueError:
    print("Input should be an integer")
except TypeError:
    print("Type Error occurred")



#22
'''
Write a program to determine largest of three numbers with if and else

Hint: Write multiple conditions
'''
try:
    a = float(input("Enter your 1st number: "))
    b = float(input("Enter your 2nd number: "))
    c = float(input("Enter your 3rd number: "))

    if a > b:
        if a > c:
            print(f"{a} is the largest element")
        else:
            print(f"{c} is the largest element")
    else: # b >= a
        if b > c:
            print(f"{b} is the largest element")
        else:
            print(f"{c} is the largest element")
except ValueError:
    print("Input should be a number")



#23
'''
Write a program to convert celsius temperature to farenheit and vice-versa

1) What is the formula to convert celsius to farenheit? --->  1.8 * temp + 32

2) What is the formula to convert farenheit to celsius? --->  (temp - 32) / 1.8
'''
try:
    choice = input("Enter '1' to 'Convert Celsius to Farenheit' and '2' to 'Convert Fahrenheit to Celsius': ")

    if choice == '1':
        temp = float(input("Enter celsius temperature : "))
        res = (1.8 * temp) + 32
        print(f"Fahrenheit Equivalent : {res}")
    else:
        if choice == '2':
            temp = float(input("Enter fahrenheit temperature : "))
            res = (temp - 32) / 1.8
            print(f"celsius equivalent : {res:.2f}")
        else:
            print("Invalid input")

except ValueError:
    print("Input should be an integer")



#24
'''
Write a program to test a point (x , y) lies in 1st quadrant , 2nd quadrant , 3rd quadrant , 4th quadrant , x - axis , y - axis or origin

1) What are the values of x and y in 1st quadrant? ---> Both are +ve

2) What are the values of x and y in 2nd quadrant? ---> 'x' is -ve and 'y' is +ve

3) What are the values of x and y in 3rd quadrant? ---> Both  are -ve

4) What are the values of x and y in 4th quadrant? ---> 'x' is +ve and 'y' is -ve

5) What are the values of x and y on x - axis? ---> 'x' is non-zero and 'y' is 0

6) What are the values of x and y on y - axis? ---> 'x' is 0 and 'y' is non-zero

7) What are the values of x and y if point is origin? ---> Both are zeroes

8) Hint: Use if .. elif
'''
try:
    x = float(input("Enter value of x co-ordinate : "))
    y = float(input("Enter value of y co-ordinate : "))

    if x == 0 and y == 0:
        print("Origin")

    elif x == 0:
        print("y - axis")
    elif y == 0:
        print("x - axis")

    elif x > 0 and y > 0:
        print("1st quadrant")
    elif x < 0 and y > 0:
        print("2nd quadrant")
    elif x < 0 and y < 0:
        print("3rd quadrant")
    elif x > 0 and y < 0:
        print("4th quadrant")

except ValueError:
    print("Input should be a numerical value")



#25
'''
Write a program to determine largest , smallest and middle of three numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10

1) What is the initial value of max?  --->  a

2) Whichever input >  max, assign that input to max

3) What is the initial value of  min?  --->  'a'

4) Whichever input <  min, assign that input to min

5) How to obtain middle number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do not use else in the program
'''
try:
    a = float(input("Enter first input: "))
    b = float(input("Enter second input: "))
    c = float(input("Enter third input: "))
    
    maxv = a
    minv = a

    if b > maxv:
        maxv = b
    if c > maxv:
        maxv = c

    if b < minv:
        minv = b
    if c < minv:
        minv = c

    mid = (a + b + c) - (maxv + minv)

    print(f"Largest input  : {maxv}")
    print(f"Smallest input : {minv}")
    print(f"Middle input   : {mid}")

except ValueError:
    print("Input should be a numerical value")