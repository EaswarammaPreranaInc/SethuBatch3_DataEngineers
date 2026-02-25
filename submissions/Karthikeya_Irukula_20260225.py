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
X = eval(input("Enter first complex number:"))
Y = eval(input("2nd complex number:"))
Sum = X+Y
print(F'Sum = {Sum}')
difference = X - Y
print(f'difference = {difference}')
product = X*Y
print(f'product = {product}')
division = X / Y
print(f'division = {division}')

'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)'''

length = eval(input("Enter length of rectangle:"))
breadth = eval(input("Enter breadth of rectangle:"))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f'area = {area}')
print(f'perimeter = {perimeter}')

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
radius = float(input("Enter the radius:"))
Volume = (4/3) * math.pi *radius ** 3
print(f'Volume_of_sphere = {Volume}')

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
principle = float(input("Enter principle: "))
time = float(input("Enter time:"))
rate_of_interest = float(input("Enter rate of interest: "))
Simple_Interest = (principle*time*rate_of_interest) / 100
print(f'Simple Interest = {Simple_Interest}')
Compound_Interest = principle * (1 + rate_of_interest / 100) ** time - principle
print(f'compound interest: {Compound_Interest}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
print(f"Before swap: ")
print(f"x = {x}")
print(f"y= {y}")
temp = x 
x = y 
y = temp 
print(f"After swap:")
print(f"x = {x}")
print(f"y= {y}")

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
print(f"Before swap: ")
print(f"x = {x}")
print(f"y= {y}")

x = x + y 
y = x - y 
x = x - y

print(f"After swap:")
print(f"x = {x}")
print(f"y= {y}")

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = eval(input("Enter 1st input: "))
y = eval(input("Enter 2nd input: "))
print(f"Before swap: ")
print(f"x = {x}")
print(f"y= {y}")

x = x * y 
y = x / y 
x = x / y

print(f"After swap:")
print(f"x = {x}")
print(f"y= {y}")



# Identify  error
else:
		print('else  suite') # Indentation extra spaces.
print('Outside')

# Identify  error
if  9 > 5 # Missing : colon
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12:
	print('Hyd')
else # missing colon :
	print('Sec')
	
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') #indentation error tab or spaces.

# Identify  error
if  ():
			print('Hyd')
	else: # Extra spaces before else block.
					print('Sec') # Extra spaces or indentation is wrong.
print('Bye') 


# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}               # Error due to brackets
else:
{               # Error due to brackets
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: #Error due to square brackets instead of paranthesis ()
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: #Error due to flower brackets instead of paranthesis ()
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a = eval(input("Enter a number: "))
if a%2==0:
	print("Even number")
else:
	print("Odd number")


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

''' 
 One
 Two
 Three
 Bye '''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') #Hyd
        print('Sec') #Sec
        print('Cyb') #Cyb
print('Bye') #Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

Month_number = eval(input("Enter month number(1-12): "))
if Month_number == 1:
	print(f"{Month_number} is January")
elif Month_number == 2:
	print(f"{Month_number} is February")
elif Month_number ==3:
	print(f" {Month_number} is March")
elif Month_number ==4:
	print(f" {Month_number} is April")
elif Month_number ==5:
	print(f"{Month_number} is May")
elif Month_number ==6:
	print(f"{Month_number} is June")
elif Month_number ==7:
	print(f"{Month_number} is July")
elif Month_number ==8:
	print(f"{Month_number} is August")
elif Month_number ==9:
	print(f"{Month_number} is September")
elif Month_number ==10:
	print(f"{Month_number} is October")
elif Month_number ==11:
	print(f"{Month_number} is November")
elif Month_number ==12:
	print(f"{Month_number} is December")
else:
	print("Enter numbers between 1 - 12")

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

x = eval(input("Enter any digit (0 -9): "))
if x==0:
	print(f"{x} is Zero")
if x==1:
	print(f"{x} is One")
if x == 2:
    print(f"{x} is Two")
if x==3:
	print(f"{x} is Three")
if x==4:
	print(f"{x} is Four")
if x==5:
	print(f"{x} is Five")
if x==6:
	print(f" {x} is Six")
if x==7:
	print(f"{x} is Seven")
if x==8:
	print(f"{x} is Eight")
if x==9:
	print(f"{x} is Nine")
else:
	print("Enter numbers between 0 - 9")
					
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

year = int(input("Enter 4 digit year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print(f"{year} is a Leap year")
else:
	print(f"{year} is not a leap year")


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

x = eval(input("Enter a 1st digit: "))
y = eval(input("Enter a 2nd digit: "))
z = eval(input("Enter a 3rd digit: "))
if x > y and x > z:
	print(f"{x} is largest number")
else:
	if y > x and y > z:
		print(f"{y} is largest number")
	else:
		print(f"{z} is largest number")
		
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

print("Temperature Conversion Program")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    c = eval(input("Enter temperature in Celsius: "))
    f = 1.8 * c + 32
    print("Temperature in Fahrenheit is:", f)

else:
    f = eval(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) / 1.8
    print("Temperature in Celsius is:", c)

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

x = eval(input("Enter a value of X quadrant: "))
y = eval(input("Enter a value of y quadrant: "))

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

a = eval(input("Enter 1st value:"))
b = eval(input("Enter 2nd value:"))
c = eval(input("Enter 3rd value:"))

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
print(f"{max_val} is max_val")
print(f"{min_val} is min_val")
print(f"{mid_val} is mid_val")




