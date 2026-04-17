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
Code:
a = complex(input("Enter first complex number : "))
b = complex(input("Enter second complex number : "))
print("Sum  :  ",a+b)
print("Difference  :  ",a-b)
print("Product  :  ",a*b)
print("Divison  :  ",a/b)

Output:
Enter first complex number : 3+4j
Enter second complex number : 5+6j
Sum  :   (8+10j)
Difference  :   (-2-2j)
Product  :   (-9+38j)
Divison  :   (0.6393442622950819+0.03278688524590165j)

'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
Code:
length = int(input("Enter length of the rectangle : "))
breadth = int(input("Enter breadth of the rectangle : "))
area = length * breadth
peri = 2 *( length + breadth)
print(F"Area  :  {area:.2f}")
print(F"Perimeter  :  {peri:.2f}")

Output:
Enter length of the rectangle : 4
Enter breadth of the rectangle : 5
Area  :  20.00
Perimeter  :  18.00

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
Code :
import math
r = float(input("Enter radius  :  "))
vol = (4 * math.pi * pow(r,3))/3
print(F'Volume :  {vol:.2f}')

Output:
Enter radius  :  3.5
Volume :  179.59

'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
Code:
p = eval(input("Enter principle  :  "))
t = eval(input("Enter time  :  "))
r = eval(input("Enter rate of interest  :  "))
s_i = (p*t*r)/100
c_i = (p * pow((1+r/100),t)-p)
print(F"Simple Interest :  {s_i:.2f}")
print(F"Compound Interest :  {c_i:.2f}")

Output:
Enter principle  :  10000
Enter time  :  3
Enter rate of interest  :  7.5
Simple Interest :  2250.00
Compound Interest :  2422.97

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
Code:
x = input("Enter 1st input :  ")
y = input("Enter 2nd input :  ")
print(F"Before swap :  {x=}		{y=}")
temp=x
x=y
y=temp
print(F"After swap :  {x=}		{y=}")

Output:
Enter 1st input :  25
Enter 2nd input :  Hyd
Before swap :  x='25'		y='Hyd'
After swap :  x='Hyd'		y='25'

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
Code:
x = int(input("Enter 1st input :  "))
y = int(input("Enter 2nd input :  "))
print(F"Before swap :  {x=}		{y=}")
x=x+y
y=x-y
x=x-y
print(F"After swap :  {x=}		{y=}")

Output:
Enter 1st input :  25
Enter 2nd input :  10
Before swap :  x=25		y=10
After swap :  x=10		y=25

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
Code:
x = int(input("Enter 1st input :  "))
y = int(input("Enter 2nd input :  "))
print(F"Before swap :  {x=}		{y=}")
x=x*y
y=x//y
x=x//y
print(F"After swap :  {x=}		{y=}")

Output:
Enter 1st input :  25
Enter 2nd input :  10
Before swap :  x=25		y=10
After swap :  x=10		y=25

# Identify  error
else:
		print('else  suite')
print('Outside')

# Else block should be written after the if block but here the if block is not present

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

# After the if condition colon(:) should be there

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
# Here the else statement does not have a colon(:) at the end

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# Here the indentation is not there the print statements in if and else block are not indended

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# Here the if and else block should be in same line and there should be indentation between them

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

# Here the {} brackets should not be there for if and else block

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

# Here in the else block the nested if else block should have indentation in them

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
Code:
x = int(input("Enter a integer :  "))
if x%2==0:
    print("Even Number")
else:
    print("Odd Number")

Output:
Enter a integer :  24
Even Number

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

Output:
One
Two
Three
Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

Output:
Hyd
Sec
Cyb
Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

Output:
Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
   m = int(input("Enter month number (1-12): "))
   if m==1:
       print("January")
   elif m==2:
       print("Febraury")
   elif m==3:
       print("March")
   elif m==4:
       print("April")
   elif m==5:
       print("May")
   elif m==6:
       print("June")
   elif m==7:
       print("July")
   elif m==8:
       print("August")
   elif m==9:
       print("September")
   elif m==10:
       print("October")
   elif m==11:
       print("November")
   elif m==12:
       print("December")
   else:
       print("Input should be between 1 and 12")
except:
   print("Input should be an integer")

Output:
Enter month number (1-12): 6
June
Enter month number (1-12): 13
Input should be between 1 and 12
Enter month number (1-12): 5.0
Input should be an integer

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
Code:
n = int(input("Enter any digit (0-9) : "))
if n==0:
   print(F'{n} - Zero')
elif n==1:
   print(F'{n} - One')
elif n==2:
   print(F'{n} - Two')
elif n==3:
   print(F'{n} - Three')
elif n==4:
   print(F'{n} - Four')
elif n==5:
   print(F'{n} - Five')
elif n==6:
   print(F'{n} - Six')
elif n==7:
   print(F'{n} - Seven')
elif n==8:
   print(F'{n} - Eight')
elif n==9:
   print(F'{n} - Nine')
else:
   print(F'{n} - Invalid')

Output:
Enter any digit (0-9) : 2
2 - Two

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
Code:

y = int(input("Enter 4-digit year: "))
if y%4==0 and y%10!=0:
    print("Leap year")
else:
    print("Not a leap year")

Output:
Enter 4-digit year: 2026
Not a leap year
Enter 4-digit year: 1992
Leap year

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
Code:
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
z = int(input("Enter 3rd number : "))
if x>y :
   if x>z:
       print("Largest element : ",x)
   else:
       print("Largest element : ",z)
else:
   if y>z:
       print("Largest element : ",y)
   else:
       print("Largest element : ",z)
Output:
Enter 1st number : 10
Enter 2nd number : 20
Enter 3rd number : 15
Largest element :  20

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
n = int(input("Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : "))
if n==1:
   temp = int(input("Enter fahrenheit temperature : "))
   res = (temp -32)/1.8
   print(F'Celsius equivalent : {res:.2f}')
elif n==2:
   temp = int(input("Enter celsius temperature : "))
   res = (1.8 * temp + 32)
   print(F'Fahrenheit equivalent : {res:.2f}')
else:
   print("Invalid input")
Output:
Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : 1
Enter fahrenheit temperature : 100
Celsius equivalent : 37.78

Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : 2
Enter celsius temperature : 30
Fahrenheit equivalent : 86.00

Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : 3
Invalid input

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
Code:
x = int(input("Enter value of x co-ordinate : "))
y = int(input("Enter value of y co-ordinate : "))
if x==0 and y==0:
   print("Origin")
elif x>0 and y>0:
   print("1st quadrant")
elif x<0 and y>0:
   print("2nd quadrant")
elif x<0 and y<0:
   print("3rd quadrant")
elif x>0 and y<0:
   print("4th quadrant")
elif x!=0 and y==0:
   print("X-axis")
elif x==0 and y!=0:
   print("Y-axis")
else :
   print("Invalid input")


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
Code:
a = int(input("Enter first input : "))
b = int(input("Enter second input : "))
c = int(input("Enter third input : "))
max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid = (a + b + c) - (max_val + min_val)
print("a =", a)
print("b =", b)
print("c =", c)
print("Largest =", max_val)
print("Smallest =", min_val)
print("Middle =", mid)

Output:
Enter first input :  = 10
Enter second input : = 20
Enter third input : = 7
Largest = 20
Smallest = 7
Middle = 10
 
