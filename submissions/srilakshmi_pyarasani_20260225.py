1) Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
												=  (15 -18j + 20j + 24) /  (25 + 36)
												=  39 / 61 + 2j / 61
#Program
num1 = complex(input("Enter first complex number : "))
num2 = complex(input("Enter second complex number : "))

print(F'sum : {num1 + num2}')
print(F'Difference: {num1 - num2}')
print(F'Product: {num1 * num2}')
print(F'Division:{num1 / num2}')


2) Write  a  program  to  determine  area  and  perimeter  of  rectangle

	1) What  are  the  inputs ?  --->  length  and   breadth

	2) What  are  the  outputs  ?  ---> area  and  perimeter

	3) What  is  the  area  of  rectangle  ?  ---> length * breadth

	4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
#Program
l = float(input("Enter length of rectangle : "))
b = float(input("Enter breadth of rectangle : "))
area = l*b
perimeter = 2*(l+b)
print(F'Area:{area}')
print(F'Perimeter:{perimeter}')

3) Write  a  program  to  determine  volume  of  a  sphere

	1) What  is  the  input ?  ---> radius

	2) What  is  the  output ?  ---> volume

	3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
#Program
import math
r = float(input("Enter radius : "))

Vol= 4/3*math.pi*r**3
print(F'Volume:{Vol}')

4) Write  a  program  to  determine  simple  interest  and  compound  interest

	1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

	2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

	3) What  is  simple  interest  formula ?  --->  ptr / 100

	4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
#Program
p = float(input("Enter principle : "))
t = float(input("Enter time : "))
r = float(input("Enter rate of interest : "))

si = p*t*r/100
ci = p*(1+r/100)**t-p
print(F'Simple Interest:{si}')
print(F'Compund Interest:{ci}')

5) Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
#Program
a=input('Enter 1st input: ')
b=input('Enter 2nd input : ')
print(f'Before swap: x=\'{a}\'  y=\'{b}\'')
temp=a 
a=b
b=temp 
print(f'After swap: x=\'{a}\' y=\'{b}\'')


6) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
#Program
a=int(input('Enter 1st input: '))
b=int(input('Enter 2nd input : '))
print(F'Before swap: x={a}  y={b}')
a=a+b
b=a-b
a=a-b
print(F'After swap: x={a} y={b}')

7) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
#Program
a=int(input('Enter 1st input: '))
b=int(input('Enter 2nd input : '))
print(F'Before swap: x={a}  y={b}')
a=a*b
b=a/b
a=a/b
print(F'After swap: x={a} y={b}')

8) Identify  error
else:
		print('else  suite')# There is no if condition
print('Outside')

9) Identify  error
if  9 > 5# There is no semi colon':'
	print('Hello')
print('Bye')

10) Identify  error
if  9 > 12:
	print('Hyd')
else # 5# There is no semi colon':'
	print('Sec')

11) Identify  error
if  (10,20,15):
print('Hyd')# Indentation Error
else:
print('Sec')

12) Identify  error
if  ():
			print('Hyd')
	else:#Indentation Error
					print('Sec')
print('Bye')

13) Identify  error
if  { }:#Error because of '{}'
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

14) Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:#Error because []
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:# Error because of {}
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

15) Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
#Program
num = int(input("Enter any +ve integer:"))
if num % 2 == 0:
    print(f'Even Number Number ')
else:
    print(f'Odd Number ')

16) outputs  
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
# Output:
	One
	Two
	Three
	Bye

17) outputs  
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#Output:
	Hyd
	Sec
	Cyb
	Bye

18) outputs  
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#Output:
	Bye
	

19) Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  
#Program

try:
    a=int(input('Enter month number(1-12): '))
    if a==1:
        print('January')
    elif a==2:
        print('February')
    elif a==3:
        print('March')
    elif a==4:
        print('April')
    elif a==5:
        print('May')
    elif a==6:
        print('June')
    elif a==7:
        print('July')
    elif a==8:
        print('August')
    elif a==9:
        print('September')
    elif a==10:
        print('October')
    elif a==11:
        print('November')
    elif a==12:
        print('December')
    else:
        print('Input should be between 1 and 12')
except:
    print('Input should be an integer')


20) Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
#Program


21) Write  a  program  to  test  year  is  leap  year  or  not

	1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

	2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

	3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

	4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

	5) Hint:  3  conditions
#Program
y=int(input('Enter 4-digit year: '))
if(y%4==0 and y%100!=0) or (y%400==0):
    print('Leap year')
else:
    print('Not a Leap year')

22) Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
#Program
a=eval(input('Enter 1st number: '))
b=eval(input('Enter 2nd number: '))
c=eval(input('Enter 3rd number: '))
if a>b and a>c:
    print('Larger input: ',a)
elif b>c:
    print('Larger input: ',b)
else:
    print('Larger input: ',c)



23) Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

	1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

	2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
#Program
a=int(input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius : '))
if a==1:
    c=float(input('Enter celsius tempature: '))
    f=(1.8*c)+32
    print(f'Celsius equivalent: {f:.1f}')
elif a==2:
    f=float(input('Enter fahrenheit tempature: '))
    c=(f-32)/1.8
    print(f'Fahrenheit equivalent: {c:.2f}')


24) Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

	1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

	2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

	3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

	4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

	5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

	6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

	7) What  are  the  values  of  x and  y  if  point  is  origin ?  --->  Both  are  zeroes
	
	8) Hint:  Use  if  ..   elif
#Program
x=int(input('Enter value of x co-ordinate : '))
y=int(input('Enter value of y co-ordinate : '))
if x>0 and y>0:
    print('1st quadrant')
elif x>0 and y<0:
    print('4th quadrant')
elif x<0 and y>0:
    print('2nd quadrant')
elif x<0 and y<0:
    print('3rd quadrant')


25) Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

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
#Program
a=int(input('Enter 1st input: ')) 
b=int(input('Enter 2nd input : ')) 
print(f'Before swap: x={a}  y={b}') 
a=a+b
 b=a-b
 a=a-b print(f'After swap: x={a} y={b}')

a=int(input('Enter 1st input : '))
b=int(input('Enter 2nd input : '))
c=int(input('Enter 3rd input : '))
max=a
if b>max:
    max=b
if c>max:
    max=c
    
min=a
if b<min:
    min=b
if c<min:
    min=c
    
middle=(a+b+c)-(max+min)
print('Largest input: ',max)
print('Smallest input : ',min)
print('middle input : ', middle)

