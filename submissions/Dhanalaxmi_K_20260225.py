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

a=complex(input("Enter the first complex number:"))
b=complex(input("Enter the second complex number:"))
print(f'Sum: {a+b}')
print(f'Difference: {a-b}')
print(f'Product: {a*b}')
print(f'Division: {a/b}')

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l=float(input("Enter the length of rectangle:"))
b=float(input("Enter the breadth of rectangle:"))
area=l*b
perimeter=2*(l+b)
print(f'area: {area}')
print(f'perimeter: {perimeter}')


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r=float(input("Enter radius: "))
volume=4/3*(math.pi)*r**3
print(f'Volume : {volume:.2f}')

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
p=float(input("Enter principle : "))
t=float(input("Enter time : "))
r=float(input("Enter rate of interest : "))
si= p*t*r/100
ci= p*(1+r/100)**t-p
print(f'Simple Intrest : {si:.2f}')
print(f'Compound Intrest : {ci:.2f}')

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
x=(input("Enter 1st input :  "))
y=(input("Enter 2nd input :  "))
print(f'Before Swap : {x=} {y=}')
temp=x
x=y
y=temp
print(f'After Swap : {x=} {y=}')


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
x=int(input('Enter 1st input:'))
y=int(input('Enter 2nd input:'))
print(F'Before swap: {x=}\t {y=}')
x=x+y
y=x-y
x=x-y
print(F'After swap: {x=} \t {y=}')

'''x=int(input("Enter the first input:"))
y=int(input("Enter the second input:"))
print(f'Before Swap : {x} , {y}')
x=x+y 
y=x-y 
x=x-y
print(f'After Swap : {x} , {y}')'''
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x=int(input("Enter the first input:"))
y=int(input("Enter the second input:"))
print(f'Before Swap : {x} , {y}')
x=x*y 
y=x//y 
x=x//y
print(f'After Swap : {x} , {y}')

# Identify  error 
'''else:
		print('else  suite')
print('Outside')'''
#answer-no if condition and statment are given and without if condition else statement cannot be printed

# Identify  error
'''if  9 > 5
	print('Hello')
print('Bye')'''
#answer-syntax error- missing colon for if 


# Identify  error
'''if  9 > 12:
	print('Hyd')
else
	print('Sec')'''
#answer- syntax error- missing colon for else 


# Identify  error
'''if  (10,20,15):
print('Hyd')
else:
print('Sec')'''
#answer-Identation error after colon there should be space or tab space


# Identify  error
'''if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')'''

#answer-syntax error- if and else should be in same column

# Identify  error
'''if  { }:
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
print('Bye')'''
#answer-syntax error - {} are not used in conditional statements

# Identify  error
'''if  ():
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
print('Bye')'''
#answer-indentation error between if and else 


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a=int(input("Enter the a number:"))
if(a%2==0):
    print(f'{a} is an Even number')
if(a%2!=0):
      print(f'{a} is an odd number')

# Find outputs  (Home  work)
'''if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')'''
'''One
	Two
	Three
	Bye'''


# Find  outputs  (Home  work)
'''if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')'''
'''Hyd
   Sec
   Cyb
   Bye'''


# Find outputs  (Home  work)
'''if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')'''
#Bye


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
month=int(input("Enter the month number (1-12): "))
if(month==1):
     print("January")
elif(month==2):
     print("February")
elif(month==3):
     print("March")
elif(month==4):
     print("April")
elif(month==5):
     print("May")
elif(month==6):
     print("June")
elif(month==7):
     print("July")
elif(month==8):
     print("August")
elif(month==9):
     print("September")    
elif(month==10):
     print("October")
elif(month==11):
     print("November")
elif(month==12):
     print("December")
else:
     print("Input should be an integer ")


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
n=int(input('Enter any digit(0-9):'))
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
                                        print("Invalid digit")
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
n=int(input("Enter the year:"))
if(n%4==0):
    print(f'{n} is a Leap year')
elif(n%400==0):
    print(f'{n} is a Leap year')
elif(n%100==0):
    print(f'{n} is not a Leap year')
else:
    print('Not a Leap year')



'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the value of 3rd number: "))
if(a>b and a>c):
     print(f'{a} is largest')
else:
      if(b>a and b>c):
     		print(f'{b} is the largest')
      else:
            print(f'{c} is largest')
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
x = int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if x== 1:
    c = float(input('Enter celsius temperature : '))
    f = 1.8 * c + 32
    print(F'Fahrenheit Equivalent:{f}')

else:
    if x== 2:
        f = float(input('Enter fahrenheit temperature : '))
        c = (f - 32) / 1.8
        print(F'Celsius Equivalent:{c:.2f}')
    else:
        print('Invalid input')
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
x = float(input("Enter value of X co-ordinate: "))
y = float(input("Enter value of Y co-ordinate: "))
if(x>0 and y>0):
    print("1st Quadrant")
elif(x<0 and y>0):
    print("2nd Quadrant")
elif(x<0 and y<0):
    print("3rd Quadrant")
elif(x>0 and y<0):
    print("4th Quadrant")
elif(x!=0 and y==0):
    print("x-axis")
elif(x==0 and y!=0):
    print("y-axis")
else:
    print("Origin")
    
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
a=float(input('Enter first input :'))
b=float(input('Enter second input :'))
c=float(input('Enter third input :'))
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
print('Largest input:', max)
if b < min:
    min = b
if c < min:
    min = c
print('Smallest input:', min)
mid = (a + b + c) - (max + min)
print('Middle input:', mid)
