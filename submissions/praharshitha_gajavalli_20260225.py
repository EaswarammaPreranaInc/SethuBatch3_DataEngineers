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

a = complex(input("Enter first complex number: "))
b = complex(input("Enter second complex number: "))
print(f"Sum : {a+b}")
print(f"Difference : {a-b}")
print(f"Product : {a*b}")
print(f"Division : {a/b}")

(Home  work)
'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
print(f"Area : {l*b:.2f}")
print(f"Perimeter: {2*(l+b):.2f}")

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math
r = float(input("Enter radius: "))
print(f"Volume: {4/3*math.pi*r**3:.2f}")

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p = float(input("Enter principle: "))
t = int(input("Enter time: "))
r = float(input("Enter rate of interest: "))
print(f"Simple Interest: {p*t*r/100:.2f}")
print(f"Compound Interest: {p*(1+r/100)**t-p:.2f}")


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f"Before Swap: {x=}   {y=}")
temp = x
x = y
y = temp
print(f"After Swap: {x=}   {y=}")


(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print(f"Before Swap: {x=}   {y=}")
x = x+y
y = x-y
x = x-y
print(f"After Swap: {x=}   {y=}")

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

x = int(input("Enter 1st input: "))
y = int(input("Enter 2nd input: "))
print(f"Before Swap: {x=}   {y=}")
x = x*y
y = x//y
x = x//y
print(f"After Swap: {x=}   {y=}")

# Identify  error
else:
		print('else  suite') #error as there is no if
print('Outside')  

# Identify  error
if  9 > 5  #error as no colon
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12:
	print('Hyd')
else  #error as no colon
	print('Sec')
	
# Identify  error
if  (10,20,15):
print('Hyd') # error - no indentation
else:
print('Sec')# error - no indentation

# Identify  error
if  ():
			print('Hyd')
	else:  # error - indentation
					print('Sec')
print('Bye')

# Identify  error
if  { }:
{ # no indentation
	print('One')
	print('Two')
	print('Three')
}
else:
{        # no indentation
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
if  []:     # no indentation
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

 # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement




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

#outputs
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

#outputs
Hyd
sec
Cyb
 
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#outputs
Bye


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a=int(input('Enter any number : '))
if a%2==0:
    print(F'{a} is Even Number.')
else:
    print(F'{a} is Odd Number.')


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    month=int(input("Enter month number (1-12): "))
    if month==1:
        print("January")
    elif month==2:
        print("February")
    elif month==3:	
        print("March")
    elif month==4:
        print("April")	
    elif month==5:
        print("May")	
    elif month==6:
        print("June")	
    elif month==7:
        print("July")	
    elif month==8:
        print("August")
    elif month==9:
        print("September")	
    elif month==10:
        print("October")
    elif month==11:
        print("November")
    elif month==12:
        print("December")
    elif month>12:
        print("Input should be between 1 and 12")
except ValueError:
    print("Input should be an integer")


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

a = int(input("Enter a digit(0-9): "))

if a == 0 :
    print("Zero")
elif a == 1 :
    print("One")
elif a == 2 :
    print("Two")
elif a == 3 :
    print("Three")
elif a == 4 :
    print("Four")
elif a == 5 :
    print("Five")
elif a == 6 :
    print("Six")
elif a == 7 :
    print("Seven")
elif a == 8 :
    print("Eight")
elif a == 9 :
    print("Nine")
else :
    print("Invalid")


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

year = int(input("Enter 4-digit year: "))
if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"Largest = {largest}")


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

x = int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if x== 1:
    c = float(input('Enter celsius temperature : '))
    f = 1.8 * c + 32
    print(F'Fahrenheit Equivalent:{f}')

elif x== 2:
    f = float(input('Enter fahrenheit temperature : '))
    c = (f - 32) / 1.8
    print(F'Celsius Equivalent:{c:.2f}')

else:
    print('Invalid input')


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
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
if x == 0 and y == 0:
    print('Orgin')
elif x!=0 and y == 0:
    print('x-axis')
elif x == 0 and y!=0:
    print("y-axis")
elif x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")



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

	

	


 
	
