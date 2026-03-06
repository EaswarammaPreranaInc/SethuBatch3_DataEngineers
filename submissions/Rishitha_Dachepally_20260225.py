'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

1) First  complex  number   --->  3 + 4j

2) 2nd   complex  number   --->  5 + 6j

3) What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j

4) What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j

5) What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j

6) What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j) =  (15 -18j + 20j + 24) /  (25 + 36) =  39 / 61 + 2j / 61
'''

x = complex(input('Enter 1st complex number : '))  # Enter 1st complex number : 3+4j
y = complex(input('Enter 2nd complex number : '))  # Enter 2nd complex number : 5+6j

print(f"Sum : {x + y}")  # Sum : (8+10j)
print(f"Difference : {x - y}")  # Difference : (-2-2j)
print(f"Product : {x * y}")  # Product : (-9+38j)
print(f"Division : {x / y}")  # Division : (0.6393442622950819+0.03278688524590165j)

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

x = float(input('Enter length of rectangle : '))  # Enter length of rectangle : 4
y = float(input('Enter breadth of rectangle : '))  # Enter breadth of rectangle : 5

area = x * y  # 4 * 5 = 20
perimeter = 2 * (x + y)  # 2 * (4 + 5) = 18

print(f"Area : {area:.2f}")  # Area : 20.00
print(f"Perimeter : {perimeter:.2f}")  # Perimeter : 18.00

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math

r = float(input('Enter radius : '))  # Enter radius : 3.5
Volume = 4 / 3 * math.pi * (r ** 3)  # 179.59

print(f"Volume : {Volume:.2f}")  # Volume : 179.59

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p = float(input('Enter principle : '))  # Enter principle : 10000
t = float(input('Enter time : '))  # Enter time : 3
r = float(input('Enter rate of interest : '))  # Enter rate of interest : 7.5

simple_interest = p*t*r / 100  # 2250.0
compound_interest = p * (1 + r / 100) ** t - p  # 2422.97

print(f"Simple Interest : {simple_interest:.2f}")  # Simple Interest : 2250.00
print(f"Compound Interest : {compound_interest:.2f}")  # Compound Interest : 2422.97

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd

What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = input('Enter 1st input : ')  # Enter 1st input : 25
y = input('Enter 2nd input : ')  # Enter 2nd input : Hyd

print(f"Before swap : {x = }    {y = }")  # Before swap : x='25' y='Hyd'

z = x
x = y
y = z

print(f"After swap : {x = }    {y = }")  # After swap : x='Hyd' y='25'

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = int(input('Enter 1st input : '))  # Enter 1st input : 25
y = int(input('Enter 2nd input : '))  # Enter 2nd input : 10

print(f"Before swap : {x = }    {y = }")  # Before swap : x=25 y=10

x = x + y
y = x - y
x = x - y

print(f"After swap : {x = }    {y = }")  # After swap : x=10 y=25

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

x = int(input('Enter 1st input : '))  # Enter 1st input : 25
y = int(input('Enter 2nd input : '))  # Enter 2nd input : 10

print(f"Before swap : {x = }    {y = }")  # Before swap : x=25 y=10

x = x * y
y = x // y
x = x // y

print(f"After swap : {x = }    {y = }")  # After swap : x=10 y=25

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# else:
#         print('else  suite')
# print('Outside')
# Error because 'else' cannot be used without a matching 'if' statement

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if 9 > 5
#     print('Hello')
# print('Bye')
# Error because ':' is missing at the end of the if statement

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if  9 > 12:
#     print('Hyd')
# else
#     print('Sec')
# Error because ':' is missing after else

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if (10,20,15):
# print('Hyd')
# else:
# print('Sec')
# Error because print statements must be indented inside the if and else blocks

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if ():
#             print('Hyd')
#     else:
#                     print('Sec')
# print('Bye')
# Error because 'else' must align with 'if' (wrong indentation)

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if {}:
# {  
#     print('One')
#     print('Two')
#     print('Three')
# }
# else:
# {
#     print('Four')
#     print('Five')
#     print('Six')
# }
# print('Bye')
# Error because Python does not use '{ }' for block structure

# -----------------------------------------------------------------------------------------

'''
Identify  error
'''

# if ():
#     print('One')
#     print('Two')
#     print('Three')
# else:
# if []:
#     print('Four')
#     print('Five')
#     print('Six')
# else:
# if {}:
#     print('Seven')
#     print('Eight')
#     print('Nine')
# else:
#     print('Hyd')
#     print('Sec')
#     print('Cyb')
# print('Bye')
# Error because indentation is incorrect and else blocks are mismatched

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''

x = int(input('Enter any number : '))  # Enter any number : 5

if x % 2 == 0:
    print('Even number')
else:
    print('Odd number')  # Odd number

# -----------------------------------------------------------------------------------------

'''
Find outputs
'''

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')    # One
        print('Two')    # Two
        print('Three')  # Three
print('Bye')            # Bye

# -----------------------------------------------------------------------------------------

'''
Find  outputs
'''

if {10:20, 30:40}:
        print('Hyd')   # Hyd
        print('Sec')   # Sec
        print('Cyb')   # Cyb
print('Bye')           # Bye

# -----------------------------------------------------------------------------------------

'''
Find outputs
'''

if {}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')   # Bye

# -----------------------------------------------------------------------------------------

'''
Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
'''

mnth = int(input('Enter month (1 - 12) : '))  # Enter month (1 - 12) : 3

if mnth == 1:
    print('January')
elif mnth == 2:
    print('February')
elif mnth == 3:
    print('March')  # March
elif mnth == 4:
    print('April')
elif mnth == 5:
    print('May')
elif mnth == 6:
    print('June')
elif mnth == 7:
    print('July')
elif mnth == 8:
    print('August')
elif mnth == 9:
    print('September')
elif mnth == 10:
    print('October')
elif mnth == 11:
    print('November')
elif mnth == 12:
    print('December')
else:
    print('Invalid month number')

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

d = int(input('Enter  any  digit  (0 - 9):  '))  # Enter  any  digit  (0 - 9):  4

if d == 0:
    print('Zero')
else:
    if d == 1:
        print('One')
    else:
        if d == 2:
            print('Two')
        else:
            if d == 3:
                print('Three')
            else:
                if d == 4:
                    print('Four')  # Four
                else:
                    if d == 5:
                        print('Five')
                    else:
                        if d == 6:
                            print('Six')
                        else:
                            if d == 7:
                                print('Seven')
                            else:
                                if d == 8:
                                    print('Eight')
                                else:
                                    if d == 9:
                                        print('Nine')
                                    else:
                                        print('Invalid')

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes

3) Are  1700 , 1800 , 1900  leap  years ? --->  No

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes

5) Hint:  3  conditions
'''

year = int(input('Enter  4-digit  year  :  '))  # Enter  4-digit  year  :  2026

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Leap year')
else:
    print('Not a leap year')  # Not a leap year

# Example 2
# Enter  4-digit  year  :  1992
# Leap year

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = float(input('Enter first number : '))   # Enter first number : 10
b = float(input('Enter second number : '))  # Enter second number : 20
c = float(input('Enter third number : '))   # Enter third number : 7

if a >= b and a >= c:
    print('Largest : ', a)
elif b >= a and b >= c:
    print('Largest : ', b)   # Largest :  20.0
else:
    print('Largest : ', c)

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

choice = int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius  :  '))  
# Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius  :  1

if choice == 1:
    c = float(input('Enter  celsius  temperature  :  '))  # Enter  celsius  temperature  :  30
    print('Fahrenheit  Equivalent  :  ', 1.8 * c + 32)  # Fahrenheit  Equivalent  :  86.0
elif choice == 2:
    f = float(input('Enter  fahrenheit  temperature  :  '))  # Enter  fahrenheit  temperature  :  100
    print('celsius  equivalent  :  ', round((f - 32) / 1.8,2))  # celsius  equivalent  :  37.78
else:
    print('Invalid input')  # Invalid input

# -----------------------------------------------------------------------------------------

'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  at  origin ?  --->  Both  are  0
'''

x = float(input('Enter  value  of  x  co-ordinate  :  '))  # Enter  value  of  x  co-ordinate  :  -10
y = float(input('Enter  value  of  y  co-ordinate  :  '))  # Enter  value  of  y  co-ordinate  :  20

if x == 0 and y == 0:
    print('Origin')
elif x == 0:
    print('y - axis')
elif y == 0:
    print('x - axis')
elif x > 0 and y > 0:
    print('1st quadrant')
elif x < 0 and y > 0:
    print('2nd quadrant')  # 2nd quadrant
elif x < 0 and y < 0:
    print('3rd quadrant')
else:
    print('4th quadrant')

# -----------------------------------------------------------------------------------------

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

a = float(input('Enter  first  input  :  '))   # Enter  first  input  :  10
b = float(input('Enter  second  input  :  '))  # Enter  second  input  :  20
c = float(input('Enter  third  input  :  '))   # Enter  third  input  :  7

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

print('Largest  input  :  ', max)     # Largest  input  :  20.0
print('Smallest  input  :  ', min)    # Smallest  input  :  7.0
print('Middle  input  :  ', mid)      # Middle  input  :  10.0



