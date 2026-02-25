First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61			


######


a = eval (input('Enter 1st complex no : '))
b = eval (input('Enter 2nd complex no : '))
print(f'Sum of {a} + {b} = {a + b}')
print(f'difference of {a} - {b} = {a -b}')
print(f'Producrt of {a} * {b} = {a * b}')
print(f'div of {a} / {b} = {a / b}')


*********

Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

####

l = int(input('Enter the length : '))
b = int(input('Enter the breadth : '))
print(f'area of {l} * {b} = {l*b}')
print(f'perimeter of {l=}  {b=} = {2*(l+b)}')

*********

Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

###

import math
r = eval(input('Enter the radius : ')
print(f' volume : {4/3 * math.pi * r**3}') 

**********************

Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p



p = eval (input('Enter principle: '))
t = eval (input('Enter time: '))
r = eval (input('Enter rate of int: '))
print(f'simple interest : {p * t * r / 100}')
print(f'compound interest : {p * (1 + r/100) **t -p}')


**************************


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

######

x = eval(input('enter value 1 : '))
y = eval(input('enter value 2 : '))
print(f'Before Swap : {x=}     {y=}')
z = x
x = y 
y = z
print(f'after Swap : {x=}      {y=}')

**************************


Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

######

x = eval(input('enter value 1 : '))
y = eval(input('enter value 2 : '))
print(f'Before Swap : {x=}     {y=}')
x=x+y
y=x-y
x=x-y
print(f'after Swap : {x=}      {y=}')

*********

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10


x = eval(input('enter value 1 : '))
y = eval(input('enter value 2 : '))
print(f'Before Swap : {x=}     {y=}')
x=x*y
y=x/y
x=x/y
print(f'after Swap : {x=}      {y=}')



**************************

# Identify  error

else:
		print('else  suite')

print('Outside')

# No if statement


 # Identify  error
if  9 > 5
	print('Hello')
print('Bye')

# No :'' after if condition


 # Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

# No ':' after else condition

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# No space or Tab after ':'

# #indentation error

if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

#indentation error
#also condition is false

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

#{} curly braces are invalid block
# indentation is missing

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


#indentation error
#nested if inside else should be indented correctly



***************************


Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement


#
a=int(input('entre a number :' ))
if a % 2 == 0:
    print(f'the number is even')
else:
    print(f' the number is odd')


********************

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')




#
one
sec
cyb
Bye

**********************

if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')


##

Hyd
sec
cyb
Bye

********************

f { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#
Bye


**************************

Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

a=eval(input('Enter month number: ' ))
if a>12 or a<1:
	print(f'enter no between 1 to 12')
elif a == 1:
	print(f' month {a} is Jan')
elif a == 2:
	print(f' month {a} is Feb')
elif a == 3:
	print(f' month {a} is Mar')
elif a == 4:
	print(f' month {a} is Apr')
elif a == 5:
	print(f' month {a} is May')
elif a == 6:
	print(f' month {a} is jun')
elif a == 7:
	print(f' month {a} is Jul')
elif a == 8:
	print(f' month {a} is Aug')
elif a == 9:
	print(f' month {a} is Sep')
elif a == 10:
	print(f' month {a} is Oct')
elif a == 11:
	print(f' month {a} is Nov')
elif a == 12:
	print(f' month {a} is Dec')



**************************

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

a = int(input("Enter any digit (0 -9): "))

if a == 0:
    print("0 - Zero")
else:
    if a == 1:
        print("1 - One")
    else:
        if a == 2:
            print("2 - Two")
        else:
            if a == 3:
                print("3 - Three")
            else:
                if a == 4:
                    print("4 - Four")
                else:
                    if a == 5:
                        print("5 - Five")
                    else:
                        if a == 6:
                            print("6 - Six")
                        else:
                            if a == 7:
                                print("7 - Seven")
                            else:
                                if a == 8:
                                    print("8 - Eight")
                                else:
                                    if a == 9:
                                        print("9 - Nine")
                                    else:
                                        print("10 - Invalid")



************************


Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions



year = int(input("Enter 4-digit year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")



************************

Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print(f"{a} is largest")
else:
    if b > a and b > c:
        print(f"{b} is largest")
    else:
        print(f"{c} is largest")



************************************


Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

choice = int(input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : "))

if choice == 1:
    c = float(input("Enter celsius temperature : "))
    f = 1.8 * c + 32
    print(f"fahrenheit equivalent : {round(f,2)}")

else:
    if choice == 2:
        f = float(input("Enter fahrenheit temperature : "))
        c = (f - 32) / 1.8
        print(f"celsius equivalent : {round(c,2)}")
    else:
        print("Invalid input")


************************************


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


#############

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

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


**************************
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


###############

a = float(input("Enter first input : "))
b = float(input("Enter second input : "))
c = float(input("Enter third input : "))

# Initial values
max = a
min = a

# Find maximum
if b > max:
    max = b

if c > max:
    max = c

# Find minimum
if b < min:
    min = b

if c < min:
    min = c

# Find middle
mid = (a + b + c) - (max + min)

print(f"Largest input  : {max}")
print(f"Smallest input : {min}")
print(f"Middle input   : {mid}")































