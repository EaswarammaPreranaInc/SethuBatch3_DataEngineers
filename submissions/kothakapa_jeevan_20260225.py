'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
a=eval(input('enter the first complex number : ')
b=eval(input('enter the second complex number : ')
print(f'Sum : (a+b)}')
print(f'Difference : {(a-b)}')
print(f'Product : {(a*b)}')
print(f'Division : {(a/b)}')

Write  a  program  to  determine  area  and  perimeter  of  rectangle
l = float(input('Enter Length of rectangle : '))
b = float(input('Enter Breadth of rectangle : '))
print(f'Area : {l*b}')
print(f'Perimeter : {2*(l+b)}')
print()


(Home  work)
Write  a  program  to  determine  volume  of  a  sphere
r = input('enter radius' )
v = input('enter volume' )
print(f' Volume of Sphere :{ (4 / 3  * pi* r ^ 3)}') 


Write  a  program  to  determine  simple  interest  and  compound  interest
import math
r = float(input('Enter radius : '))
print(f'Volume : {'%.2f' %((4/3)*math.pi*r**3)}')


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

a=eval(input('Enter the first value : '))
b=eval(input('Enter the second value : '))
print(f' Before swap :{a=}\t{b=}')
temp=a
a=b
b=temp
print(f'After swap : {a=}\t{b} ')


# 1. Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
'''
First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61										   
'''
try:
    a = complex(eval(input('Enter first complex number : ')))
    b = complex(eval(input('Enter second complex number : ')))
    print(f'sum : {a+b}')
    print(f'Difference : {a-b}')
    print(f'Product : {a*b}')
    print(f'Division : {a/b}')
    print()
except:
    print('Input should be complex  number')


 (Home  work) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
'''
Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''


a = int(input('Enter 1st input : '))
b = int(input('Enter 2nd input : '))
print(f'Before Swap : {a=} \t {b=}')
a = a+b
b = a-b
a = a-b
print(f'After Swap : {a=} \t {b=}')



Identify  error
if  (10,20,15):
print('Hyd')    # Error Indentation error
else:
print('Sec')    # Error Indentation error



Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')  # Indentation error


 Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')  # {} are used in concept of set and dict
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')



Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:                # Indentation Error
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





Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a = int(input('Enter 1st number : '))
if a%2==0:
    print('Even Number')
else:
    print('Odd Number')

 Find outputs  (Home  work)
if():
        print('Hyd')  
        print('Sec')
        print('Cyb')
else:
        print('One')   # One
        print('Two')   # Two
        print('Three') # Three
print('Bye')           # Bye


Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')  # Hyd
        print('Sec')  # Sec
        print('Cyb')  # Cyb
print('Bye')          # Bye


 Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')          # Bye


 Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

# 1st Type

import calendar
try:
    month = int(input('Enter Month number (1 - 12): '))
    print(calendar.month_name[month])
    if month == 0:
        print(1/month)
except IndexError:
    print('Input should be between 1 and 12')
except ValueError:
    print('Input should be an integer')
except ZeroDivisionError:
    print('Input should be an +ve integer and above 0')


# 2nd Type

months = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}
month = int(input('Enter Month number (1 - 12): '))
if month <= 0 or month > 12:
    print('Input should be between 1 and 12')
elif month in months:
    print(months[month])



 Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
'''
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
digits = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}
digit = int(input('Enter any digit (0 - 9): '))
if digit in digits:
    print(digits[digit])
else:
    print('Invalid')


 Write  a  program  to  test  year  is  leap  year  or  not
'''
1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
num = int(input('Enter 4-digit year : '))
if num%4==0 and num%100!=0 or num%400==0:
    print('Leap Year')
else:
    print('Not a Leap Year')


Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
'''
Hint:  Write  multiple  conditions
'''
a = int(input('Enter 1st input : '))
b = int(input('Enter 2nd input : '))
c = int(input('Enter 3rd input : '))
if a > b and a > c:
    print(f'Largest Input : {a}')
elif b > c:
    print(f'Largest Input : {b}')
else:
    print(f'Largest Input : {c}')


 Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
'''
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
n = int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if n == 1:
    c = float(input('Enter celsius temperature : '))
    print(f'fahrenheit Equivalent : {(1.8*c)+32}')
elif n == 2:
    f = float(input('Enter fahrenheit temperature : '))
    print(f'celsius Equivalent : {'%.2f' %((f-32)/1.8)}')
else:
    print('Invalid input')


 Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
'''
1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''


x = int(input('Enter value of x co-ordinate : '))
y = int(input('Enter value of y co-ordinate : '))
if x > 0 and y > 0:
    print('1st quadrant')
elif x < 0 and y > 0:
    print('2nd quadrant')
elif x < 0 and y < 0:
    print('3rd quadrant')
elif x > 0 and y < 0:
    print('4th quadrant')
elif x != 0 and y==0:
    print('x - axis')
elif x == 0 and y != 0:
    print('y - axis')
else:
    print('origin')



 Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
'''
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
a = float(input('Enter first input : '))
b = float(input('Enter second input : '))
c = float(input('Enter third input : '))
if a > b and a > c:
    maxx = a
elif b > c and b > a:
    maxx = b
elif c > a and c > b:
    maxx = c
if a < b and a < c:
    minn = a
elif b < c and b < a:
    minn = b
elif c < a and c < b:
    minn = c
print(f'Largest input : {maxx}')
print(f'smallest input : {minn}')
print(f'Middle input : {(a+b+c)-(maxx+minn)}')





