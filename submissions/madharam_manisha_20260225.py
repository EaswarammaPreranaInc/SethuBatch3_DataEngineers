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
a = complex(input("enter a 1st value : "))
b = complex(input("enter a 2st value : "))
print(f"Sum ({a} , {b}) = {a+b}")
print(f"Difference ({a} , {b}) = {a-b}")
print(f"Product ({a} , {b}) = {a*b}")
print(f"Division ({a} , {b}) = {a/b}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l = float(input("enter a length of a rectangle : "))
b = float(input("enter a breadth of a rectangle : "))
print(f"area of a rectangle = {l*b}")
print(f"perimeter of rectangle = {2*(l+b)}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math 
r = float(input("enter a radius of a sphere : "))
result = 4/3 * math.pi * r**3
print(f"Volume : {result}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

p = float(input("enter a principle : "))
t = float(input("enter a time : "))
r = float(input("enter a rate of interest : "))
result_si = (p*t*r)/100
result_ci = p * ( 1 + r / 100 ) ** t - p
print(f"Simple Interest : {result_si}")
print(f"Compound Interest : {result_ci}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''

a = input("enter a 1st input : ")
b = input("enter a 2nd input : ")
print(f"before swap : {a=} , {b=}")
temp=a
a=b
b=temp
print(f"After swap : {a=} , {b=}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

a = int(input("enter a 1st input : "))
b = int(input("enter a 2nd input : "))
print(f"before swap : {a=} , {b=}")
a= a+b # 25+10 =35
b = a-b # 35-10 = 25 
a = a-b # 35-25 =10
print(f"After swap : {a=},{b=}")
#=======================================================================================================================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

a = int(input("enter a 1st input : "))
b = int(input("enter a 2nd input : "))
print(f"before swap : {a=} , {b=}")
a = a * b
b = a/b
a = a/b
print(f"After swap : {a=},{b=}")
#=======================================================================================================================================================
# Identify  error

else:
	print('else  suite') # if statement is not their syntax error
print('Outside')
#=======================================================================================================================================================
# Identify  error
if  9 > 5       # colon is missing syntax error
	print('Hello')
print('Bye')
#=======================================================================================================================================================
# Identify  error
if  9 > 12:
	print('Hyd')
else                # colon is missing syntax error
	print('Sec')
#=======================================================================================================================================================
# Identify  error
if  (10,20,15):
print('Hyd') # indentation error
else:
print('Sec') # indentation error
#=======================================================================================================================================================
# Identify  error
if  ():
			print('Hyd')
	else:               # indentation error if and else will be in same column
					print('Sec')
print('Bye')
#=======================================================================================================================================================
# Identify  error
if  { }: # curly braces not required syntax error
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
#=======================================================================================================================================================
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # indentation error 
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: # indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#=======================================================================================================================================================
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

n1 =  int(input("enter a number : "))
if n1 % 2 == 0 :
    print("Even number")
else : 
    print("odd number")

#=======================================================================================================================================================
# Find outputs  (Home  work)

if():
        print('Hyd') 
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') # One <nextline> Two <nextline> Three <nextline> Bye
#=======================================================================================================================================================
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') 
        print('Sec')
        print('Cyb')
print('Bye') # Hyd <nextline> Sec <nextline> Cyb <nextline> Bye
#=======================================================================================================================================================
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye
#=======================================================================================================================================================
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

n = input("enter a month number (1-12) : ")
if n == "1":
    print("January")
elif n =='2':
    print("febuary")
elif n =='3':
    print("march")
elif n == '4':
    print("april")
elif n == '5':
    print("may")
elif n == '6':
    print("june")
elif n == '7':
    print("july")
elif n == '8':
    print("august")
elif n == '9':
    print("september")
elif n == "10":
    print("october")
elif n == "11":
    print("november")
elif n == "12":
    print("december")
else:
    print("invalid input month number should be in 1-12")
#=======================================================================================================================================================
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

n = input("enter a input number : ")
if n == "0":
    print("zero")
else:
    if n=="1":
        print("one")
    else:
        if n=="2":
            print("two")
        else:
            if n == "3":
                print("three")
            else:
                if n=="4":
                    print("four")
                else:
                    if n=="5":
                        print("five")
                    else:
                        if n=="6":
                            print("six")
                        else:
                            if n=="7":
                                print("seven")
                            else:
                                if n=="8":
                                    print("eight")
                                else:
                                    if n=="9":
                                        print("nine")
                                    else:
                                        print("invalid input")
#=======================================================================================================================================================                                        
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

a = int(input("enter a year : "))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print("leap year")
else:
    print("not a leap year")
#=======================================================================================================================================================    
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a = float(input("enter a 1st value : "))
b = float(input("enter a 2st value : "))
c = float(input("enter a 3st value : "))
if a>b and a>c :
    print(a)
elif b>c :
    print(b)
else:
    print(c)
#=======================================================================================================================================================    
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

a = int(input("enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : "))
temp = int(input("enter a fahrenheit temperature : "))
result_1 = 1.8 * temp + 32
result_2 = (temp - 32)/1.8
if a == 1 :
    print(f"celsius to fahrenheit {result_1}")
elif a == 2 :
    print(f"fahrenheit to celsius {result_2}")
else : 
    print("invalid input")
#=======================================================================================================================================================   
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

x = float(input("enter a x-axis : "))
y = float(input("enter a y-axis : "))
if x > 0 and y >0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0 :
    print("3rd quadrant")
elif x > 0 and y < 0:
    print("4th quadrant")
elif x != 0 and y == 0 :
    print("x - axis")
elif x == 0 and y != 0 :
    print("y - axis")
elif x==0 and y == 0 : 
    print("origin") 
else :
    print("invalid input")
#=======================================================================================================================================================    
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
a = float(input("enter a 1st value : "))
b = float(input("enter a 2st value : "))
c = float(input("enter a 3st value : "))
max = a
if b > max : 
    max = b
if c> max :
    max = c
print(f"largest number : {max}")
min = a
if b < min :
    min = b
if c < min :
    min = c
print(f"smallest number : {min}")
mid = (a+b+c) - (max+min)
print(f"middle number : {mid}")

