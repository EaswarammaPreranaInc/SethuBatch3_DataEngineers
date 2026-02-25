Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61			

a=complex(input("Enter 1st integer number: "))
b=complex(input("Enter 2nd integer number: "))
c=(a+b)
print("Sum:",c)(Home  work)


Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
c=(a-b)
print(f"Difference:",c)
c=(a*b)
print(f"Product:",c)
c=(a/b)
print(f"Division:",c)

a=float(input("Enter Length of Rectangle:"))
b=float(input("Enter Breadth of Rectangle:"))
Area=a*b
print("Area:",Area)
Perimeter=2*(a+b)
print("Perimeter:",Perimeter)

Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

import math
a=float(input("Enter Radius:"))
volume=4/3*math.pi*a**3
print('volume',volume)

Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

a=float(input("Enter Principle:"))
b=float(input("Enter Time :"))
c=float(input("Enter Rate of Interest:"))
simple_interest=(a*b*c)/100
print("simple interest",simple_interest)
compound_interest= a * (1  + c/  100) ** b  -  a
print("compound interest",compound_interest)

Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

x=eval(input("Enter 1st input:"))
y=eval(input("Enter 2nd input :")) 
print("Before Swapping:")
print("x=",x)
print("y=",y)
print("After Swapping:")
temp = x
x = y
y = temp
print("x =", x)
print("y =", y)

Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

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

Hyd
Sec
Cyb
Bye

if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    month = int(input("Enter month number (1 - 12): "))

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

except ValueError:
    print("Input should be an integer")

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid

digit = int(input("Enter any digit (0-9): "))


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
                                    else:
                                        print("Invalid")
                                        
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions

year = int(input("Enter 4-digit year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print( "Leap Year")
else:
    print(" Not a Leap Year")

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

x= float(input("Enter value of x coordinate: "))
y = float(input("Enter value of y coordinate: "))

if x > 0 and y > 0:
    print("1st Quadrant")

elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")

elif x > 0 and y < 0:
    print("4th Quadrant")

elif x != 0 and y == 0:
    print("Point lies on X-axis")

elif x == 0 and y != 0:
    print("Point lies on Y-axis")

else:
    print("Point is at the Origin")

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
 

c=int(input("Enter Third Input:"))

max_num = a
min_num = a


if b > max_num:
    max_num = b
if c > max_num:
    max_num = c


if b < min_num:
    min_num = b
if c < min_num:
    min_num = c


mid_num = (a + b + c) - (max_num + min_num)


print("Largest Input:", max_num)
print("Smallest Input:", min_num)
print("Middle Input:", mid_num)





