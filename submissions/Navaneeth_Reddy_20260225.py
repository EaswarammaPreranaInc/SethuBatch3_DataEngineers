'''
Q1
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
a = eval(input("Enter the 1st Complex Number : "))
b = eval(input("Enter the 2nd Complex Number : "))

s = a+b
d = a - b
p = a*b
di = a/b
print("Sum : " , s)
print("Difference : " , d)
print("Product : ", p)
print("Division : ", di)

'''
Output :
Enter the 1st Complex Number : 8+14j
Enter the 2nd Complex Number : -9+19j
Sum :  (-1+33j)
Difference :  (17-5j)
Product :  (-338+26j)
Division :  (0.43891402714932126-0.6289592760180995j)
'''

'''
Q2
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

a = float(input("Enter the Length of rectangle : "))
b = float(input("Enter the Breadth of rectangle : "))

ar = a*b
pr = 2*(a+b)

print("Area : ", ar)
print("Perimeter : ", pr)


'''
Output :
Enter the Length of rectangle : 5.3
Enter the Breadth of rectangle : 4.9
Area :  25.970000000000002
Perimeter :  20.4
'''

'''
Q3
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math

r = float(input("Enter the radius of sphere : "))
vl= (4/3)*math.pi*r**3
print("Volume of Sphere : ",vl)

'''
Output :
Enter the radius of sphere : 4.8
Volume of Sphere :  463.2466863277364
'''

'''
Q5
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

pri = float(input("Enter the principle : "))
t = float(input("Enter the time : "))
ri = float(input("Enter the rate of interest : "))

sif = (pri*t*ri)/100
cif = pri*(1 + ri/100)**t - pri

print("Simple Interest : ",sif)
print("Compund Interest : ",cif)


'''
Output :
Enter the principle : 1500000
Enter the time : 7
Enter the rate of interest : 5.6
Simple Interest :  587999.9999999999
Compund Interest :  696537.8255118714
'''

'''
Q6
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
print(f"Before Swap : {x = } , {y = }")
temp = x
x = y
y = temp 
print(f"After Swap : {x = } , {y = }")

'''
Output :
Enter 1st input : 'Sec'
Enter 2nd input : 97.8
Before Swap : x = 'Sec' , y = 97.8
After Swap : x = 97.8 , y = 'Sec'
'''

'''
Q7
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before Swap : {x = } , {y = }")
x = x + y
y = x - y
x = x - y
print(f"After Swap : {x = } , {y = }")

'''
Output :
Enter 1st input : 78
Enter 2nd input : 89
Before Swap : x = 78 , y = 89
After Swap : x = 89 , y = 78
'''

'''
Q9
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  25
y =  10
'''


x = float(input("Enter 1st input : "))
y = float(input("Enter 2nd input : "))
print(f"Before Swap : {x = } , {y = }")
x = x * y
y = x / y
x = x / y
print(f"After Swap : {x = } , {y = }")


'''
Output :
Enter 1st input : 78
Enter 2nd input : 23
Before Swap : x = 78.0 , y = 23.0
After Swap : x = 23.0 , y = 78.0
'''

# Identify  error
else:
		print('else  suite')
print('Outside') # Error, because you can not execute else without having 'if' condition

# Identify  error
if  9 > 5
	print('Hello')
print('Bye') # Error, there should be colon(:) after if

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') # Error, there should be colon(:) after else
 
 # Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') # Error, because statements in if and else should follow indentation

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye') # Error, there is no proper indentation in else condition

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
print('Bye') # Error, 

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
print('Bye') # Error, because there is no proper indentation in nested if conditions, where program should be moved right side 


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a =int(input("Enter the number : "))

if a%2 == 0:
    print("Even Number")
else :
    print("Odd Number")

'''
Enter the number : 56
Even Number
'''

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
Output :
One
Two
Three
Bye
'''

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')


'''
Output :
Hyd
Sec
Cyb
Bye
'''
'''
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye
'''

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  
try :
    m = int(input("Enter month number (1-12) : "))

    if m == 1:
        print("January")
    elif m == 2:
        print("Febuary")
    elif m ==3 :
        print("March")
    elif m == 4 :
        print("April")
    elif m == 5:
        print("May")
    elif m == 6:
        print("June")
    elif m == 7:
        print("July")
    elif m == 8:
        print("August")
    elif m == 9:
        print("September")
    elif m == 10:
        print("October")
    elif m == 11:
        print("November")
    elif m == 12:
        print("December")
    else :
        print("Input should be between 1 and 12")
except :
    print("Input should be integer value")

    
'''
Output :
Enter month number (1-12) : 8
August
PS D:\SSSSDP\Homeworks> py pr1.py
Enter month number (1-12) : 13.5
Input should be integer value
'''

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

try :
    num = int(input("Enter a digit (0-9) : "))
    
    if num == 0:
        print("Zero")
    else :
        if num == 1:
            print("One")
        else :
            if num == 2:
                print("Two")
            else :
                if num == 3 :
                    print("Three")
                else :
                    if num == 4 :
                        print("Four")
                    else :
                        if num == 5:
                            print("Five")
                        else :
                            if num == 6:
                                print("Six")
                            else :
                                if num == 7 :
                                    print("Seven")
                                else :
                                    if num == 8:
                                        print("Eight")
                                    else :
                                        if num == 9:
                                            print("Nine")
                                        else :
                                            print("Invalid")
except :
    print("Enter a Valid Number")


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''


try :
    ly = int(input("Enter a year : "))
    
    if (ly % 4 == 0 and ly % 100 != 0):
        print("Leap Year")
    elif(ly % 400 == 0) :
        print("Leap Year")
    else :
        print("Not a leap year")
except :
    print("Enter a valid integer year number")


'''
Output :
Enter a year : 1996
Leap Year
Enter a year : 2029
Not a leap year
'''

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

try :
    a = int(input("Enter the 1st input : "))
    b = int(input("Enter the 2nd input : "))
    c = int(input("Enter the 3rd input : "))

    if (a > b and a > c) :
        print("Largest number is : ", a)
    else :
        if (b > a and b > c) :
            print("Largest number is : ", b)
        else :
            print("Largest number is : ", c)
except :
    print("Enter valid integer number")

    
'''
Enter the 1st input : 58
Enter the 2nd input : 96
Enter the 3rd input : 56
Largest number is :  96
'''

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''


op = int(input("Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : "))

if op == 1 :
    cel = float(input("Enter celsius temperature : "))
    f = 1.8*cel + 32
    print("Farenhit Equivalent : ", f)
else :
    if op == 2 :
        f = float(input("Enter Farenhit temperature : "))
        cel = (f - 32)/1.8
        print("Celsius Equivalent : ",cel)
    else :
        print("Invalid Input")  
                       
                
'''
Output :
Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : 2
Enter Farenhit temperature : 100
Celsius Equivalent :  37.77777777777778
Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : 3
The number should be between only 1 and 2
'''

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

x = float(input("Enter x-coordinate : "))
y = float(input("Enter y-coordinate : "))

if (x > 0 and y > 0) :
    print("1st Quadrant")
elif (x < 0 and y >0):
    print("2nd Quadrant")
elif (x < 0 and y < 0):
    print("3rd Quadrant")
elif (x > 0 and y <0):
    print("4th Quadrant")
elif (x == 0 and y == 0):
    print("It is on Origin")
elif (y == 0 and x != 0) :
    print("Point on x-axis")
elif (x == 0 and y != 0) :
    print("Point on y-axis")


'''
Output :
Enter x-coordinate : -9.6
Enter y-coordinate : 4
2nd Quadrant
'''

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


a = int(input("Enter first input : "))
b = int(input("Enter second input : "))
c = int(input("Enter third input : "))


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

print("Largest Input : ", max)
print("Middle Input : ", mid)
print("Smallest Input : ", min)

'''
Output :
Enter first number: 96
Enter second number: 98
Enter third number: 97
Largest = 98
Middle = 97
Smallest = 96
'''