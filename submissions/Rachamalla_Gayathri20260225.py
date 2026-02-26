
(Home  work)
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
###code:
a=eval(input("enter first comolex"))
b=eval(input("enter secind comolex"))
print(f" a+b",a+b)
print(f" a-b",a-b)
print(f"a*b",a*b)
print(f"a/b",a/b)
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
##code:
length=int(input("enter length of rectangle:"))
breadth=int(input("enter breadth of rectangle:"))
Area=length*breadth
perimeter=2*(length+breadth)
print("area:",Area)
print("perimeter:",perimeter)
Write  a  program  to  determine  volume  of  a  sphere
##code:
radius=float(input("enter the radius"))
volume=4/3*(3.14)(radius)*3
print("volume:",volume)

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest
##code:
p=int(input("Enter principle:"))
t=int(input("enter time:"))
r=float(input("enter rate of intrest:"))
simple_interest=(p*t*r)/100
compound_interest=p*(1+r/100)**t-p
print("simple intrest:",simple_interest)
print("compound intrest:",compound_interest)

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
##code:
x=10
y='Hyd'
print("Before swap", x,y)
temp=x
x=y
y=temp
print("after swap",x,y)
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
##code:
x = 10
y = 20
print("before_swap", x,y)
x = x + y   # one addition
y = x - y   # first subtraction
x = x - y   # second subtraction

print("x =", x)
print("y =", y)
print("after swap",x,y)
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
x = 10
y = 20
print("before_swap", x,y)
x = x * y   # one addition
y = x //y   # first subtraction
x = x //y   # second subtraction

print("x =", x)
print("y =", y)
print("after swap",x,y)
 # Identify  error
else:
		print('else  suite') #error
print('Outside')
# Identify  error
if  9 > 5
	print('Hello')#Hello
print('Bye')#Bye
# Identify  error
if  9 > 12:
	print('Hyd')
else:
	print('Sec')#Sec
# Identify  error
if  (10,20,15):
print('Hyd')#Hyd
else:
print('Sec')#Sec
# Identify  error
if  ():
   print('Hyd')
else:
	print('Sec')
print('Bye')
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
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n=int(input("enter a number:))
if n%2==0:
    print("number is even")
else:
   print("the number is odd")

 # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')# one two Three Bye
print('Bye')
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd Sec Cyb Bye
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye
 # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
month=int(input("enter month number(1-12): "))

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

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
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
                                        print("Invalid digit")

Write  a  program  to  test  year  is  leap  year  or  not
#code:
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years


5) Hint:  3  conditions
'''

Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''#code:
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)


Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Middle
middle = a + b + c - largest - smallest

print("Largest:", largest)
print("Smallest:", smallest)
print("Middle:", middle)

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