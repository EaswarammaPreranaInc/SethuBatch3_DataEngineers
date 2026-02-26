Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61
# program:
a=eval(input('Enter first complex number :'))
b=eval(input('Enter second complex number :'))
print('sum :',(a+b))
print('Difference :',(a-b))
print('Product :',(a*b))
print('Division :',(a/b))


(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

Promgram:

a=float(input('Enter leanth of rectangle :'))
b=float(input('Enter breadth of rectangle :'))
print('Area :', (a*b))
print('Perimeter :', 2*(a+b))

(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3


Program:
import math
r=float(input('Enter radius :' ))
print('Volume :', (4/3*math.pi*r**3))




Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

Program :

p=float(input('Enter Priciple : ', ))
t=float(input('Enter time : ', ))
r=float(input('Enter rate of intrest : ', ))
print('Simple intrest :' , (p*t*r/100))
print('Compound intrest : ', (p*(1+r/100)**t-p))


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10


Program:
x=(input('Enter 1st input  : '))
y=(input('Enter 2nd input  : '))
print(f"Before swap : x='{x}' \t y='{y}' ")
temp = x
x = y
y = temp
print(f"After swap  : x='{x}' \t y='{y}'")



Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10

# Program:

x=int(input('Enter first number : '))
y=int(input('Enter second number : '))
print(f"Before swap : x='{x}' \t y='{y}' ")
x,y=x+y-x,x+y-y
print(f"After swap : x='{x}' \t y='{y}' ")


Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
Program:

x=int(input('Enter first number : '))
y=int(input('Enter second number : '))
print(f"Before swap : x='{x}' \t y='{y}' ")
x,y=(x*y)/x,(x*y)/y
print(f"After swap : x='{x}' \t y='{y}' ")





# Identify Erorr

else:
		print('else  suite')
print('Outside')
# else without if 



# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# : is missing for if 



# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

# : is missing for else



# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# indantation Error


# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# Indantation error


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
print('Bye')  # Braces should not be there








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
print('Bye')  # invalid syntax after else i.e if







# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

# Program:
a=int(input('Enter a number  :  '))
if a%2==0:
	print('Even')
else:
	print('Odd')


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

# One
  Two
  Three
  Bye




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

# Hyd
  Sec
  Cyb
  Bye





# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # Bye




# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

# Program

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
    print("Invalid month number! Please enter a number from 1 to 12.")


#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
# Program
n = int(input("Enter a digit (0-9): "))

if n == 0:
    print("Zero")
else:
    if n == 1:
        print("One")
    else:
        if n == 2:
            print("Two")
        else:
            if n == 3:
                print("Three")
            else:
                if n == 4:
                    print("Four")
                else:
                    if n == 5:
                        print("Five")
                    else:
                        if n == 6:
                            print("Six")
                        else:
                            if n == 7:
                                print("Seven")
                            else:
                                if n == 8:
                                    print("Eight")
                                else:
                                    if n == 9:
                                        print("Nine")
                                    else:
                                        print("Invalid")





Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions

Program:
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")



#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
Program:
a = int(input("Enter first number  : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number  : "))

if a >= b:
    if a >= c:
        print(f"Largest number is {a}")
    else:
        print(f"Largest number is {c}")
else:
    if b >= c:
        print(f"Largest number is {b}")
    else:
        print(f"Largest number is {c}")


Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

Program:

ch = input("Enter C for Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

temp = float(input("Enter temperature: "))

if ch == 'C':
    f = 1.8 * temp + 32
    print("Temperature in Fahrenheit =", f)
else:
    c = (temp - 32) / 1.8
    print("Temperature in Celsius =", c)


#Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif


Program :
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

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
elif x == 0 and y == 0:
    print("Point is Origin")
else:
    print("Invalid input")
	

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

Program:

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
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
print("Max =", max_val)
print("Min =", min_val)
print("Mid =", mid_val)
