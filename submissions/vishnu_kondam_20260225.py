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
#=================================================================
a=complex(input("enter the first complex number:"))
b=complex(input("enter the second complex number:"))
print(f'sum of a and b :{a}+{b}={a+b}')
print(f'Difference of a and b :{a}-{b}={a-b}')
print(f'product of a and b :{a}*{b}={a*b}')
print(f'diviision of a and b :{a}/{b}={a/b}')
#========================================================
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
#===============================================================
length=eval(input("Enter the length of ractangle:"))
breadth=eval(input("Enter the length of ractangle:"))
print(f'area of rectangle is:{length*breadth}')
print(f'perimeter of rectangle is:{2*(length+breadth)}')
#===================================================================
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
#===========================================================
import math
radius=eval(input("Enter the radius of sphere:"))
print(f'volume of sphere with radius {radius} is:{4/3*(math.pi)*pow(radius,3)}')
#====================================================================
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
#======================================================================
principal_amount=eval(input("Enter the principal amount:"))
time_duration=eval(input("Enter the time_duration:"))
rate_of_interest=eval(input("Enter the rate_of_interest:"))
print(f'simple interest is:{principal_amount*time_duration*rate_of_interest/100}')
print(f'compound interest is:{principal_amount*(1+(rate_of_interest/100)**time_duration)-principal_amount}')
#======================================================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
#=================================================================================
a=eval(input("Enter first input:"))
b=eval(input("Enter second input:"))
print(f'Before swap: a={a},b={b}')
temp=a
a=b
b=temp
print(f'After swap: a={a},b={b}')
#===================================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
#===================================================
a=eval(input("Enter first input:"))
b=eval(input("Enter second input:"))
print(f'Before swap: a={a},b={b}')
a,b=b,a
print(f'After swap: a={a},b={b}')
#=========================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition and two subtractions

x =  25
y =  10
'''
#=======================================================
a=eval(input("Enter first input:"))
b=eval(input("Enter second input:"))
print(f'Before swap: a={a},b={b}')
a=a+b
b=a-b
a=a-b
print(f'After swap: a={a},b={b}')
#==========================================================
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication and division

x =  25
y =  10
'''
#====================================================
a=eval(input("Enter first input:"))
b=eval(input("Enter second input:"))
print(f'Before swap: a={a},b={b}')
a=a*b
b=a//b
a=a//b
print(f'After swap: a={a},b={b}')
#=================================================
# Identify  error
else:                                   #cant use else directly 
		print('else  suite')
print('Outside')
#================================================
# Identify  error
if  9 > 5
	print('Hello')            #No colon
print('Bye')
#============================================
# Identify  error
if  9 > 12:
	print('Hyd')             #No colon in else
else
	print('Sec')
#=============================================
# Identify  error
if  (10,20,15):
print('Hyd')           #no proper indentation
else:
print('Sec')
#==============================
 #Identify  error
if  ():
			print('Hyd')              #if and else and last print should have same indentation
	else:
					print('Sec')
print('Bye')
#=================================================
# Identify  error
if  { }:
{
	print('One')                 #Error:cant have brackets for blocks
	print('Two')
	print('Three')
}
else:
{
	print('Four')             #Error :cant have brackets for blocks
	print('Five')
	print('Six')
}
print('Bye')
#====================================================
# Identify  error
if  ():
	print('One')            
	print('Two')
	print('Three')
else:
if  []:                          # inside if is not indented
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')                # inside if is not indented
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#========================================================
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
num=int(input("enter a num:"))
if num%2==0:
	print(f"The provided num:{num} is Even")
else:
	print(f"The provided num:{num} is Odd")
	#=============================================
	# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')              #One<nextline>Two<nextline>Three<nextline>Bye<nextline>
        print('Two')
        print('Three')
print('Bye')
#======================================
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')            
        print('Sec')                           #Hyd<nextline>Sec<nextline>Cyb<nextline>Bye<nextline>
        print('Cyb')
print('Bye')
#======================================
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')                 #Bye<nextline>
	print('Cyb')
print('Bye')
#======================================
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
	month_number=eval(input("Enter a month number between(1-12)"))
	if(month_number==1):
		print("January")
	elif(month_number==2):
		print("February") 
	elif(month_number==3):
		print("March")
	elif(month_number==4):
		print("April")
	elif(month_number==5):
		print("May")
	elif(month_number==6):
		print("June")
	elif(month_number==7):
		print("July")
	elif(month_number==8):
		print("August")
	elif(month_number==9):
		print("September")
	elif(month_number==10):
		print("October")
	elif(month_number==11):
		print("November")
	elif(month_number==12):
		print("December")
except:
	print("enter a valid number between 1-12")
#=============================================================
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
#======================================================================
num = int(input("Enter a digit: "))

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
                                        print("Invalid")
#======================================
'''
# Write  a  program  to  test  year  is  leap  year  or  not

# 1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

# 2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

# 3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

# 4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

# 5) Hint:  3  conditions
'''
#====================================================================
try:
	year_num=int(input("Enter year:"))
	if(year_num%4==0 and year_num%100!=0 or year_num%400==0):
		print(f'The provided year:{year_num} is Leap Year')
	else:
		print(f'The provided year:{year_num} is not a Leap Year')
except:
	print(" the input be int and year fomrat yyyy")
	#==============================================================
	'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
try:
	num1=int(input("enter num1:"))
	num2=int(input("enter num2:"))
	num3=int(input("enter num3:"))
	if num2<num1>num3:
		print(f"The value {num1} is Largest")
	elif num2>num3:
		print(f"The value {num2} is Largest")
	else:
		print(f"The value {num3} is largest")
except:
	print("Enter valid input:inpus should be integer")
#=====================================================
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
try:
	num=int(input("Enter 1 to convert celcius to faranheit and 2 to convert from faranheit to celcius"))
	if(num==1):
		celcius_value=int(input("enter celcius temperature:"))
		print(f'The faranheit equivalent:{1.8*celcius_value+32}')
	elif(num==2):
		faranheit_value=int(input("enter faranheit temperature:"))
		print(f'The celcius equivalent:{(faranheit_value-32)/1.8}')
except:
	print("inout should be integer")
#=================================================================================
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
try:
	x=int(input("enter first value in (x,y) pair:x= "))
	y=int(input("enter first value in (x,y) pair:y= "))
	if x>0 and y>0:
		print(f"The pair {x,y} belongs to Quadrant-1")
	elif x<0 and y>0:
		print(f"The pair {x,y} belongs to Quadrant-2")
	elif x<0 and y<0:
		print(f"The pair {x,y} belongs to Quadrant-3")
	elif x>0 and y<0:
		print(f"The pair {x,y} belongs to Quadrant-4")
	elif x==0 and y==0:
		print(f"The pair {x,y} is origin")
	elif x==0:
		print(f"The pair {x,y} lies on y axis")
	elif y==0:
		print(f"The pair {x,y} lies on x axis")
except:
	print("values should be integer")
#================================================================
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
#=====--======================--=============--=========================
x=int(input("enter first value x= "))
y=int(input("enter second value y= "))
z=int(input("enter third value z= "))
max=z
min=z
mid=z
if(y>=max):
	max=y
elif x>=max:
	max=x
if(x<=min):
	min=x
elif(y<=min):
	min=y
mid=x+y+z-max-min
print(f'max value is:{max}')
print(f'min value is:{min}')
print(f'mid value is:{mid}')





