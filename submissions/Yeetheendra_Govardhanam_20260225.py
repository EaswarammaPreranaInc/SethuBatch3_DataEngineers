#Topic1
'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)												=  (15 -18j + 20j + 24) /  (25 + 36)											=  39 / 61 + 2j / 61										   
'''
"""
x = complex(input("Enter first complex number : "))
y = complex(input("Enter second Complex number : "))

print(F"Sum : {(x)+(y)}")
print(F"Difference : {(x)-(y)}")
print(F"Product: {(x)*(y)}")
print(F"Division : {(x)/(y)}")
"""

#Topic2
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
"""
x = int(input("Enter length of rectangle : "))
y = int(input("Enter breadth of rectangle : "))

print(F"Area: {(x)*(y)}")
print(F"Perimeter: {2*(x+y)}")
"""

#Topic3
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
"""
import math
r = eval(input("Enter radius : "))

print(F"Volume: {(4/3) * (math.pi) * (math.pow(r, 3)):.2f}")
"""

#Topic4
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
"""
x = eval(input("Enter principle : "))
y = eval(input("Enter time : "))
z = eval(input("Enter rate of interest : "))
print(F"Simple Interest : {(x*y*z)/(100):.2f}")
print(F"Compound Interest :  {(x * ((1+z/100)** y)) - x:.2f}")
"""

#Topic5
'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
"""
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")
print(f"Before swap : {x=}\t {y=}")
temp = x 
x = y
y = temp
print(f"After swap : {x=}\t {y=}")
"""

#Topic6
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
"""
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before swap : {x=}\t {y=}")
x = x+y 
y = x-y
x = x-y
print(f"After swap : {x=}\t {y=}")
"""

#Topic7
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

"""
x = int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before swap : {x=}\t {y=}")
x = x*y 
y = int(x/y)
x = int(x/y)
print(f"After swap : {x=}\t {y=}")
"""

#Topic8
"""
    #Topic8.1
# Identify  error
#else:
#        print('else  suite') #error there us no "if block"
#print('Outside') 

    #Topic8.2
# Identify  error
#if  9 > 5
#	print('Hello') #error ":" is missing
#print('Bye') #Bye

    #Topic8.3
# Identify  error
#if  9 > 12:
#	print('Hyd')
#else
#	print('Sec') #error ":" is missing
    
    #Topic8.4
# Identify  error
#if  (10,20,15):
#print('Hyd') #error Indentation(tab space) is missing 
#else:
#print('Sec')

    #Topic8.5
# Identify  error
#if  ():
#			print('Hyd')
#    else: #error it is inside the "if block" 
#					print('Sec')
#print('Bye')

    #Topic8.6
# Identify  error
#if  { }:
#{    #error we should not use {} is should used for srt and dict
#	print('One')
#	print('Two')
#	print('Three')
#}
#else:
#{
#	print('Four')
#	print('Five')
#	print('Six')
#}
#print('Bye')
    #Topic8.7
# Identify  error
#if  ():
#	print('One')
#	print('Two')
#	print('Three')
#else: #error Indentation(tab space) is missing
#  if  []:
#  print('Four')
#  print('Five')
#  print('Six')
#   else:
#  if  {}:
#  print('Seven')
#  print('Eight')
#  print('Nine')
# else:
#   print('Hyd')
#   print('Sec')
#   Print('Cyb')
#print('Bye')

    #Topic8.8
# Find outputs  (Home  work)
if(): #it is false so ignored
        print('Hyd')
        print('Sec')
        print('Cyb')
else: # full suite is printed
        print('One') #One
        print('Two') #Two
        print('Three')#Three
print('Bye') #Bye

    #Topic8.9
 # Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') #Hyd
        print('Sec') #Sec
        print('Cyb') #Cyb
print('Bye') #Bye

    #Topic8.10
 # Find outputs  (Home  work)
if { }: #it is ignored as it is false
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#only Bye is printed

"""

#Topic9
"""
 Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
Eo = abs(int(input("Enter +ve intger : ")))
if (Eo%2 ==0):
    print("Even Number")
else:
    print("Odd Number")
"""

#Topic10 (check images)
"""
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
    M = int(input("Enter month number (1 - 12) : "))
    if (M==1):
        print("January")
    elif (M==2):
        print("February")
    elif (M==3):
        print("March")
    elif (M==4):
        print("April")
    elif (M==5):
        print("May")
    elif (M==6):
        print("June")
    elif (M==7):
        print("July")
    elif (M==8):
        print("August")
    elif (M==9):
        print("September")
    elif (M==10):
        print("October")
    elif (M==11):
        print("November")
    elif (M==12):
        print("December")
    else:
        print("Input should be between 1 and 12")
except:
    print("Input should be an integer")
"""    
    
#Topic11
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
"""
try:
    N = int(input("Enter any digit (0 - 9): "))
    if(N==0):
        print("Zero")
    else:
        if(N==1):
            print("One")
        else:
            if(N==2):
                print("Two")
            else:
                if(N==3):
                    print("Three")
                else:
                    if(N==4):
                        print("Four")
                    else:
                        if(N==5):
                            print("Five")
                        else:
                            if(N==6):
                                print("Six")
                            else:
                                if(N==7):
                                    print("Seven")
                                else:
                                    if(N==8):
                                        print("Eight")
                                    else:
                                        if(N==9):
                                            print("Nine")
                                        else:
                                            if(N>=10):
                                                print("Invalid")
except:
    print("Input should be an integer")
"""
                                  
#Topic12(check images)
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
"""
try:
    L = int(input("Enter 4-digit year : "))
    if(L%4 == 0 and L%100 != 0 or L%400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

except:
    print("Input should be an integer")
"""
    
#Topic13
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
"""
a, b, c = (eval(i) for i in input("Enter three Value (space-saparated) : ").split())
if(a>b):
    print(a)
elif(a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)
"""

#Topic14 (check images)
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

"""
I = int(input("Enter 1 to convert celsium to farenheit and 2 to convert fahrenhit to celsius : "))
if(I==1):
    f = eval(input("Enter celsius temperature : "))
    c = (1.8 * f) +32
    print(F"fahrenheit Equivalent : {c:.1f}")

elif(I==2):
    c = eval(input("Enter fahrenheit temperature : "))
    fa = (c - 32) / 1.8
    print(F"celsius equivalent : {fa:.2f}")
else:
    print("Invaild input")
"""

#Topic15 (check images)
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
"""
x = int(input("Enter value of x co-ordinate :  "))
y = int(input("Enter value of y co-ordinate :  "))
if(x >0 and y >0):
    print("1st  quadrant")
elif(x <0 and y >0):
    print("2nd  quadrant")
elif( x <0 and y <0):
    print("3rd  quadrant")
elif(x > 0 and y <0):
    print("4th  quadrant")
elif(x ==0 and y !=0):
    print("y-axis")
elif(x != 0 and y ==0):
    print("x-axis")
else:
    print("Origin")
"""

#Topic16 (check images)
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

"""
a = eval(input("Enter first input : "))
b = eval(input("Enter second input : "))
c = eval(input("Enter third input : "))
l = a
s = a

if(b>a and b>c):
    l = b
    if(c>b and c>a):
        l = c
        
if(b<a and b<c):
    s = b
    if(c<b and c<a):
        s = c

m = (a+b+c) - (l+s)

print(f"Largest input : {l}")
print(f"Smallest input : {s}")
print(f"Middle input : {m}")
"""