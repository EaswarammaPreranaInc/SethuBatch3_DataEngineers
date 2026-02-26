#Programming Homework #1
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
'''
Sample Output:

Enter first complex number: 3 + 4j

Enter second complex number: 5 + 6j

Sum : (8 + 10j)

Difference : (-2-2j)

Product: (- 9 + 38j)

Division : (0.6393442622950819+0.03278688524590165j)
Press any key to continue...
'''

try:
    a = complex(input('Enter the first complex number:'))
    b = complex(input('Enter the second complex number:'))

    add = a + b
    sub = a - b
    mul = a * b
    div = a / b

    print(f'Sum: {add}')
    print(f'Difference: {sub}')
    print(f'Product: {mul}')
    print(f'Division: {div}')
except:
    print('The input should be a number.')



#Programming Homework #2
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
'''
Sample Output:
Enter length of rectangle :4

Enter breadth of rectangle : 5

Area :

20.00

Perimeter :

18.00
Press any key to continue...
'''

try:
    l = float(input('Enter the length of the rectangle:'))
    b = float(input('Enter the breadth of the rectangle:'))

    print(f'Area: \n {l * b}')
    print(f'Perimeter: \n {2*(l+b)}')
except:
    print('The length and breadth should either be an int or a float number.')



#Programming Homework #3
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
'''
Sample Output:

Enter radius : 3.5

Volume : 179.59
Press any key to continue...
'''
import math

try:
    r = float(input('Enter the radius of the sphere:'))

    print(f'Volume: {4/3 * math.pi * r ** 3:.2f}')
except:
    print('The radius should either be an int or a float number.')


#Programming Homework #4
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
'''
Sample Output:

Enter principle : 10000

Enter time : 3

Enter rate of interest : 7.5

Simple Interest : 2250.00

Compound Interest : 2422.97
Press any key to continue...
'''

try:
    p = float(input('Enter the principle amount:'))
    t = float(input('Enter the time in years:'))
    r = float(input('Enter the rate of interest without the "%":'))

    print(f'Simple Interest: {p * t * r / 100:.2f}')
    print(f'Compound Interest: {p * (1 + r / 100) ** t - p:.2f}')
except:
    print('The Principle Amount, Time (in years), Rate of Interest(without the "%") should have either int or float values only.')


#Programming Homework #5
'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
'''
Sample Output:

Enter 1st input : 25

Enter 2nd input : Hyd

Before swap : x='25' y= 'Hyd'

After swap : x= 'Hyd' y='25'
Press any key to continue...
'''

x = eval(input('Enter the first input:'))
y = eval(input('Enter the second input:'))

print(f'Before Swap: {x=} {y=}')

temp = x
x = y
y = temp

print(f'After Swap: {x=} {y=}')



#Programming Homework #6
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y = 10
'''

try:
    x = float(input('Enter the first number:'))
    y = float(input('Enter the second number:'))

    print(f'Before Swap: {x=} {y=})')

    x = x + y
    y = x - y
    x = x - y

    print(f'After Swap: {x=} {y=}')
except:
    print('The values of the inputs need to be either be int or float.')


#Programming Homework #7
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

try:
    x = float(input('Enter the first number:'))
    y = float(input('Enter the second number:'))

    print(f'Before Swap: {x=} {y=})')

    x = x * y
    y = x / y
    x = x / y

    print(f'After Swap: {x=} {y=}')
except:
    print('The values of the inputs need to be either be int or float.')



#Programming Homework #8
'''
Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''
x = float(input('Enter the number:'))

if x % 2 == 0:
    print('The given number is Even.')
else:
    print('The given number is Odd.')



#Programming Homework #9
'''
Write a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
'''
'''
Sample Output 1:

Enter the month number(1 - 12): 6

June
Press any key to continue...


Sample Output 2:

Enter the month number(1 - 12): 13

Input should be between 1 and 12
Press any key to continue...


Sample Output 3:

Enter the month number(1 - 12): 5.0

Input should be an integer
Press any key to continue...
'''
try:
    m = int(input('Enter the month number(1 - 12):'))


    if m == 1:
        print('January')
    elif m == 2:
        print('February')
    elif m == 3:
        print('March')
    elif m == 4:
        print('April')
    elif m == 5:
        print('May')
    elif m == 6:
        print('June')
    elif m == 7:
        print('July')
    elif m == 8:
        print('August')
    elif m == 9:
        print('September')
    elif m == 10:
        print('October')
    elif m == 11:
        print('November')
    elif m == 12:
        print('December')
    else:
        print('The input number should be between 1 and 12 only.')
except:
    print('The input number should be an integer.')



#Programming Homework #10
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
'''
Sample Output:

Enter any digit (0 -9):4

Four
Press any key to continue...
'''
try:
    n = int(input('Enter a digit between 1 to 9:'))

    if n == 1:
        print('One')

    else:
        if n == 2:
            print('Two')

        else:
            if n == 3:
                print('Three')

            else:
                if n == 4:
                    print('Four')

                else:
                    if n == 5:
                        print('Five')

                    else:
                        if n == 6:
                            print('Six')

                        else:
                            if n == 7:
                                print('Seven')

                            else:
                                if n == 8:
                                    print('Eight')

                                else:
                                    if n == 9:
                                        print('Nine')

                                    else:
                                        print('The input integer should be between 1 and 9 only.')
except:
    print('The input should be an integer number.')



#Programming Homework #11
'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
'''
Sample Output 1:

Enter 4-digit year: 2026

Not a leap year
Press any key to continue...


Sample Output 2:

Enter 4-digit year : 1992

Leap year
Press any key to continue...
'''

try:
    y = int(input('Enter a year(in four digits):'))
            
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f'{y} is a Leap year.')
            else:
                print(f'{y} is not a Leap year.')
        else:
            print(f'{y} is a Leap year.')
    else:
        print(f'{y} is not a Leap year.')
except:
    print('Please enter a valid four digit integer input.')



#Programming Homework #12
'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write multiple conditions
'''
a = float(input('Enter the first number:'))
b = float(input('Enter the second number:'))
c = float(input('Enter the third number:'))

if a > b and a > c:
    print(f'The largest number is {a}.')
elif b > c:
    print(f'The largest number is {b}.')
else:
    print(f'The largest number is {c}.')



#Programming Homework #13
'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
'''
Sample Output 1:

Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 3

Invalid input
Press any key to continue...


Sample Output 2:

Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 1

Enter celsius temperature : 30

Fahrenheit Equivalent: 86.0
Press any key to continue...


Sample Output 3:

Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius :

Enter fahrenheit temperature: 100

2

celsius equivalent: 37.78
Press any key to continue...
'''
try:
    T = input('Enter "C" to convert Celsius to Fahrenheit, "F" to convert Fahrenheit to Celsius:')

    if T == 'C':
        CT = float(input('Enter the Celsius Temperature:'))
        print(f'Fahrenheit Equivalent: {1.8 * CT + 32:.2f}')
    elif T == 'F':
        FT = float(input('Enter the Fahrenheit Temperature:'))
        print(f'Celsius Equivalent: {(FT - 32) / 1.8:.2f}')
    else:
        print('Enter a valid input C or F.')
except:
    print('The inputs must either be an integer number or a float number.')


#Programming Homework #14
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
'''
Sample Output:

Enter value of X co-ordinate : -10

Enter value of y co-ordinate : 20 2nd quadrant

Press any key to continue...
'''

try:
    x = int(input('Enter the value of X Co-ordinate:'))
    y = int(input('Enter the value of Y Co-ordinate:'))

    if x > 0 and y > 0:
        print(f'{x} and {y} are in the 1st Quadrant.')
    elif x < 0 and y > 0:
        print(f'{x} and {y} are in the 2nd Quadrant.')
    elif x < 0 and y < 0:
        print(f'{x} and {y} are in the 3rd Quadrant.')
    elif x > 0 and y < 0:
        print(f'{x} and {y} are in the 4th Quadrant.')
    elif x != 0 and y == 0:
        print(f'{x} and {y} are on the x-axis.')
    elif x == 0 and y != 0:
        print(f'{x} and {y} are on the y-axis.')
    else:
        print(f'{x} and {y} are at origin.')
except:
    print('The value of x and y must be an integer.')


#Programming Homework #15
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
'''
Sample Output:

Enter first input : 10

Enter second input : 20

Enter third input : 7

Largest input: 20.0

Smallest input : 7.0

Middle input : 10.0
Press any key to continue...
'''
try:
    a = float(input('Enter the first input:'))
    b = float(input('Enter the second input:'))
    c = float(input('Enter the third input:'))

    maxx = a
    minx = a

    if b > maxx:
        maxx = b
    if c > maxx:
        maxx = c

    if b < minx:
        minx = b
    if c < minx:
        minx = c

    midx = (a + b + c) - (maxx + minx)

    print(f'The Largest value is {maxx}.')
    print(f'The Smallest value is {minx}.')
    print(f'The Middle value is {midx}.')
except:
    print('The inputs should either be an integer number or a float number.')


#Identify Errors Homework #1
else:
		print('else  suite') # syntax error because else cannot be used without if
print('Outside')

#2
if  9 > 5
	print('Hello') # syntax error because ':' is mandatory after if
print('Bye')

#3
if  9 > 12:
	print('Hyd')
else
	print('Sec') # syntax error because ':' is mandatory after else

#3
if  (10,20,15):
print('Hyd')
else:
print('Sec') # indentation error, <space> or <tab> on the line after if an else are mandatory

#4
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye') # indentation error, if and else should be in the same column

#5
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
print('Bye') # indentation error, the line after if and else must contain at least one <space> or <tab>
# commas are mandatory in a set

#6
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
print('Bye') # indentation error, if statement after else needs to be on a different column after else

#Outputs Homework #1
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') # One <next line> Two <next line> Three <next line> Bye

#Outputs Homework #2
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd <next line> Sec <next line> Cyb <next line> Bye

#Outputs Homework #3
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Hyd <next line> Sec <next line> Cyb <next line> Bye




