# Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61	

a = complex(input("Enter the 1st complex number :"))
b = complex(input("Enter the 2st complex number :"))
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("division:",a/b)

# Write  a  program  to  determine  area  and  perimeter  of  rectangle
1) What  are  the  inputs ?  --->  length  and   breadth
2) What  are  the  outputs  ?  ---> area  and  perimeter
3) What  is  the  area  of  rectangle  ?  ---> length * breadth
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

length = float(input("Enter length of rectangle:"))
breadth = float(input("Enter breadth of rectangle:"))
print("Area of rectangle :",length*breadth)
print("Perimeter  of  rectangle:",2*(length+breadth))

(Home  work)
# Write  a  program  to  determine  volume  of  a  sphere
1) What  is  the  input ?  ---> radius
2) What  is  the  output ?  ---> volume
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

r = float(input("Enter radius :"))
pi = 3.14159
print("Volume:",4 / 3  * pi *  r ** 3)

#(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest
1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest
2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest
3) What  is  simple interest  formula ?  --->  ptr / 100
4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

p = float(input("Enter principle :"))
t = float(input("Enter time:"))
r = float(input("Enter rate  of  interest :"))
print(" simple interest :",p*t*r / 100)
print(" compound  interest  formula:",p * (1  +  r  /  100) ** t  -  p)

Write  a  program  to  swap  values  of  two   objects   using  3rd  object
Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

x = int(input("Enter 1st input :"))
y = input("Enter 2nd input :")
print("before swap : x ='{}'  y = '{}' ".format(x,y))
temp = x
x = y
y = temp
print("after swap :  x ='{}'  y = '{}' ".format(x,y))

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
x = 25
y =  10

x = int(input("Enter 1st input :"))
y = int(input("Enter 2nd input :"))
print("before swap : x ='{}'  y = '{}' ".format(x,y))
x = x+y
y = x-y
x = x-y
print("after swap :  x ='{}'  y = '{}' ".format(x,y))

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  25
y =  10

x = int(input("Enter 1st input :"))
y = int(input("Enter 2nd input :"))
print("before swap : x ='{}'  y = '{}' ".format(x,y))
x = x*y
y = x/y
x = x/y
print("after swap :  x ='{}'  y = '{}' ".format(x,y))


# Identify  error
else:
		print('else  suite')
print('Outside')
# Syntax error

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# Syntax error

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
# Syntax error

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
# Hyd

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
# Sec Bye

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
# Syntax Error

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
# Syntax Error


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

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
# One Two Three Bye 

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
print('Bye')
# Syntax Error

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

num = int(input("Enter month number (1-12): "))
if num == 1:
    print("January")
elif num == 2:
    print("February")
elif num == 3:
    print("March")
elif num == 4:
    print("April")
elif num == 5:
    print("May")
elif num == 6:
    print("June")
elif num == 7:
    print("July")
elif num == 8:
    print("August")
elif num == 9:
    print("September")
elif num == 10:
    print("October")
elif num == 11:
    print("November")
elif num == 12:
    print("December")
else:
    print("Invalid month number")

# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid

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

# Write  a  program  to  test  year  is  leap  year  or  not
1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400
2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs
3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years
4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years
5) Hint:  3  conditions

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
Hint:  Write  multiple  conditions

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
else:
    if b >= a and b >= c:
        print("Largest =", b)
    else:
        print("Largest =", c)

# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

choice = input("Type C to convert Celsius or F to convert Fahrenheit: ")
if choice == "C":
    c = float(input("Enter temperature in Celsius: "))
    print("Fahrenheit =", 1.8 * c + 32)
elif choice == "F":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Celsius =", (f - 32) / 1.8)
else:
    print("Invalid choice")

# Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin
1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve
2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve
3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve
4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve
5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0
6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero
7) What  are  the  values  of  x and  y  if  point  is  origin ?  --->  Both  are  zeroes
8) Hint:  Use  if  ..   elif

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))
if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x != 0 and y == 0:
    print("On X-axis")
elif x == 0 and y != 0:
    print("On Y-axis")
else:
    print("Origin")

# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
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

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
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
print("Maximum =", max)
print("Minimum =", min)
print("Middle =", mid)