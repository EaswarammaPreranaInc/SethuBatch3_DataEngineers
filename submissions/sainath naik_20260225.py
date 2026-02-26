1.Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
First  complex  number  --> # 3 + 4j
2nd   complex  number --> # 5 + 6j
What  is  the  sum --> # 8 + 10j
What  is  the  difference --> # (-2-2j)
What  is  the  product --> # (-9+38j)
What  is  the  division --> # (0.6393442622950819+0.03278688524590165j)
  
x = complex(input("Enter first complex number : ")) 
y= complex(input("Enter second complex number : ")) 

sum_result = x + y
difference = x - y
product = x * y
division = x / y

print("First complex number :", x)
print("Second complex number:", y)
print("Sum :", sum_result)
print("Difference :", difference)
print("Product :", product)
print("Division :", division)


2.Write  a  program  to  determine  area  and  perimeter  of  rectangle
1) What  are  the  inputs ?  --->  length  and   breadth  

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

   length = float(input("Enter length of the rectangle : ")) # 4
   breadth = float(input("Enter breadth of rectangle : ")) # 5

   area = length * breadth
   perimetr = perimeter = 2 * (length + breadth)

   print("Length:", length) # 4.0
   print("Breadth:", breadth) # 5.0
   print("Area of rectangle:", area) # 20.0
   print("Perimeter of rectangle:", perimeter) # 18.0


3.Write a program to determine volume of a sphere
 1) What is the input ? ---> radius 
 2) What is the output ? ---> volume
 3) What is the volume of sphere ? ---> 4 / 3 * pi * r ^ 3

  import math 
  radius = float(input("Enter radius of sphere : ")) # 7
  volume = (4/3) * math.pi * radius ** 3
  print("Radius:", radius) # 7.0
  print("Volume of sphere:", volume) # 1436.7550402417319



4.Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

p = float(input("Enter principle  :  ")) #  20000
t = float(input("Enter  time  :  "))  # 12
r = float(input("Enter  rate  of  interest  :  ")) # 2

si = (p * t * r) / 100

ci = p * (1 + r / 100) ** t - p

print("Simple  Interest  :  {:.2f}".format(si)) # 4800.0
print("Compound  Interest  :  {:.2f}".format(ci)) # 5364.84



5. Write  a  program  to  swap  values  of  two   objects   using  3rd  object
Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

x = 10
y = "Hyd"

print("Before swap :  x =", x, " y =", y)  # x = 10, y = "Hyd"
temp = x
x = y
y = temp

print("After swap : x =", x, " y =", y) # x = "Hyd", y = 10




6.Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

# Given values
x = 25
y =  10
print("Before swap : x =", x, " y =", y) # x = 25  y = 10

x = x + y = 35
y  = x - y = 25
 x = x -y = 10
print("After swap : x =", x, " y =", y) # x = 10  y = 25



7.Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x = 25
y = 10
print("Before swap : x =", x, " y =", y) # x = 25  y = 10
x = x * y
y = x / y
x = x / y
print("After swap  : x =", x, " y =", y) # x = 10.0  y = 25.0



8.# Identify  error
else:
		print('else  suite')
print('Outside')  # invalid syntax-->else cannot be used alone

correct code:

if True:
    print('if suite')
else:
    print('else suite')

print('Outside')



9.# Identify  error
if  9 > 5
	print('Hello')
print('Bye') # syntax Error [expected ':']
                  # in python , every if statement must be end with semicolon
correct code:

if 9 > 5:
    print('Hello')

print('Bye') # Hello
                    Bye



10.# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') # syntax Error --> Missing colon (:) after else
correct code:
if  9 > 12:
	print('Hyd')
else:
	print('Sec') # Sec


 
11.# Identify error 
if (10,20,15): 
print('Hyd') 
else: 
print('Sec') # Indentation Error

correct code:

if (10, 20, 15):
    print('Hyd')
else:
    print('Sec') # Hyd



12.# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye') # Indentation Error

correct code:

if ():
    print('Hyd')
else:
    print('Sec')

print('Bye') # Sec
                    Bye
 
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
print('Bye') # invalid syntax [Curly Braces { } Are Invalid in Python Blocks]

correct code: 

if {}:
    print('One')
    print('Two')
    print('Three')
else:
    print('Four')
    print('Five')
    print('Six')

print('Bye') # Four
	    Five
	    Six
	    Bye



13.# Identify  error
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
print('Bye') # IndentationError

correct code:
if ():
    print('One')
    print('Two')
    print('Three')
else:
    if []:
        print('Four')
        print('Five')
        print('Six')
    else:
        if {}:
            print('Seven')
            print('Eight')
            print('Nine')
        else:
            print('Hyd')
            print('Sec')
            print('Cyb')

print('Bye') # Hyd
	     Sec
	      Cyb
	       Bye




14.# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
# code:
num = int(input("Enter a number : "))

if num % 2 == 0:
       print("The number is Even")
else:
       print(The number is Odd")



15.# Find outputs  (Home  work)
 if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') # One 
	     Two
	     Three
	     Bye



16.# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd
	     Sec
	     Cyb
 	     Bye



17.# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye



18.# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
# Read month number
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



19.Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
code:-
# Read input
num = int(input("Enter a digit (0-9): "))

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


 
20.
1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions

code:-
year = int(input("Enter a year: "))

# Check leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")



21.Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
 
code:-
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Find largest using multiple conditions
if a >= b and a >= c:
    print("Largest number is:", a)
else:
    if b >= a and b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)




22.Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

code:-
choice = int(input("Enter 1 for Celsius to Fahrenheit\nEnter 2 for Fahrenheit to Celsius\nEnter your choice: "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = 1.8 * c + 32
    print("Temperature in Fahrenheit:", f)

else:
    if choice == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        c = (f - 32) / 1.8
        print("Temperature in Celsius:", c)
    else:
        print("Invalid choice")




23.Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin
1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve
2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve
3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve
4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve
5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0
6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero
7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes
8) Hint:  Use  if  ..   elif

code:-
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

# Determine position
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
    print("Point is at the Origin")




24.Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10


25.
1) What  is  the  initial  value  of  max  ?  --->  a
2) Whichever  input >  max,  assign  that  input  to  max
3) What  is  the  initial  value  of  min  ?  --->  'a'
4) Whichever  input  <  min,  assign  that  input  to  min
5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c
6) Hint : Do  not  use  else  in  the  program
code:--
a = 10
b = 20
c = 7

# Step 1: Find Maximum
max = a
if b > max:
    max = b
if c > max:
    max = c
# Step 2: Find Minimum
min = a
if b < min:
    min = b
if c < min:
    min = c
# Step 3: Find Middle
mid = (a + b + c) - (max + min)
# Print results
print("Largest  :", max)
print("Smallest :", min)
print("Middle   :", mid)