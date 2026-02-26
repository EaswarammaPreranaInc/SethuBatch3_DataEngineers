'''
1-->Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) = -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)=  (15 -18j + 20j + 24) /  (25 + 36)=  39 / 61 + 2j / 61

-->Sample Output 1:
Enter first complex number: 3 + 4j
Enter second complex number: 5 + 6j
Sum : (8 + 10j)
Difference : (-2-2j)
Product: (- 9 + 38j)
Division : (0.6393442622950819+0.03278688524590165j)
Press any key to continue...
'''

#Answer
a=complex(input('Enter first complex number:'))
b=complex(input('Enter second complex number:'))
print(F'Sum:{a+b}')
print(F'Difference:{a-b}')
print(F'Product:{a*b}')
print(F'Division:{a/b}')

'''
2-->Write  a  program  to  determine  area  and  perimeter  of  rectangle
1) What  are  the  inputs ?  --->  length  and   breadth
2) What  are  the  outputs  ?  ---> area  and  perimeter
3) What  is  the  area  of  rectangle  ?  ---> length * breadth
4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)

-->Sample Output 2:
Enter length of rectangle :4
Enter breadth of rectangle : 5
Area :20.00
Perimeter :18.00
Press any key to continue...
'''

#Answer
l=float(input('Enter length of rectangle:'))
b=float(input('Enter breadth of rectangle:'))
print(F'Area:{l*b}')
print(F'Perimeter:{2*(l+b)}')

'''
3-->Write  a  program  to  determine  volume  of  a  sphere
1) What  is  the  input ?  ---> radius
2) What  is  the  output ?  ---> volume
3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

-->Sample Output 3:
Enter radius : 3.5
Volume : 179.59
Press any key to continue...
'''
#Answer
import math
r=float(input('Enter radius:'))
print(F'Volume:{4/3*math.pi*r**3:.2f}')

'''
4-->Write  a  program  to  determine  simple  interest  and  compound  interest
1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest
2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest
3) What  is  simple  interest  formula ?  --->  ptr / 100
4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p

-->Sample Output 4:
Enter principle : 10000
Enter time : 3
Enter rate of interest : 7.5
Simple Interest : 2250.00
Compound Interest : 2422.97
Press any key to continue...
'''
#Answer
p=float(input('Enter principle:'))
t=float(input('Enter time:'))
r=float(input('Enter rate of interest:'))
SI=(p*t*r / 100)
CI=(p * (1  +  r  /  100) ** t  -  p)
print(F'Simple Interest:{SI}')
print(F'Compound Interest:{CI:.2f}')

'''
5-->Write  a  program  to  swap  values  of  two   objects   using  3rd  object
Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10

-->Sample Output 5:
Enter 1st input : 25
Enter 2nd input : Hyd
Before swap : x='25' y= 'Hyd'
After swap : x= 'Hyd' y='25'
Press any key to continue...
'''
#Answer
x=eval(input('Enter 1st input:'))
y=eval(input('Enter 2nd input:'))
print(F'Before swap: {x=}\t {y=}')
temp=x
x=y
y=temp
print(F'After swap: {x=} \t {y=}')

'''
6-->Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
x = 25 y =  10
'''
#Answer
x=int(input('Enter 1st input:'))
y=int(input('Enter 2nd input:'))
print(F'Before swap: {x=}\t {y=}')
x=x+y
y=x-y
x=x-y
print(F'After swap: {x=} \t {y=}')

'''
7-->Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
x =  25 y =  10
'''
#Answer
x=int(input('Enter 1st input:'))
y=int(input('Enter 2nd input:'))
print(F'Before swap: {x=}\t {y=}')
x=x*y
y=x//y
x=x//y
print(F'After swap: {x=} \t {y=}')

#8-->Identify  error
else:
		print('else  suite')
print('Outside') #ERROR because else can't be used without if

#9-->Identify  error
if  9 > 5
	print('Hello')
print('Bye') # ERROR because after condition : is mandatory

#10-->Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') # ERROR because after else : is mandatory

#11-->Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec') # ERROR because after : there should be spacebar or tab key (mandatory)

#12-->Identify  error
if  ():
			print('Hyd') # ERROR indentation error
	else:
					print('Sec') # ERROR indentation error
print('Bye')

#13-->Identify  error
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
print('Bye') # ERROR statements should not be in { } braces

#14-->Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else: # ERROR instead of else: if we can use elif
if  []: #  ERROR indentation error
	print('Four')
	print('Five')
	print('Six')
else: # ERROR instead of else: if we can use elif
if  {}: # ERROR indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

'''
15-->Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''
a=int(input('Enter and +ve number:'))
if a%2==0:
    print('Even number')
if a%2!=0:
    print('Odd number')

#16-->Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
#answer--> One<nextline>Two<nextline>Three<nextline>Bye

#17-->Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#answer-->Hyd<nextline>Sec<nextline>Cyb<nextline>Bye

#18-->Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#answer-->Bye

'''
#19-->Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

-->Sample Output 6:
Enter month number (1 -12): 6
June
Press any key to continue...
-->Sample Output:
Enter month number (1 -12): 13
Input should be between 1 and 12
Press any key to continue
'''
try:
    a=int(input('Enter month number(1-12):'))
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
    print('Input should be integer')

'''
20-->Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid

-->Sample Output 7:
Enter any digit (0 -9):4
Four
Press any key to continue...
'''

n=int(input('Enter any digit(0-9):'))
if n == 0:
    print('Zero')
else:
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
                                        print("Invalid digit")
                                        
'''
21-->Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400
2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs
3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years
4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years
5) Hint:  3  conditions

-->Sample Output 9:
Enter 4-digit year: 2026
Not a leap year
Press any key to continue..

-->Sample Output 10:
Enter 4-digit year : 1992
Leap year
Press any key to continue...
'''
y=int(input('Enter 4-digit year :'))
if y % 4 == 0:
    print('Leap year')
elif y % 400 == 0:
    print('Leap year')
elif y % 100 == 0:
    print('Not a Leap year')
else:
    print('Not a Leap year')

'''
22-->Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
Hint:  Write  multiple  conditions
'''
a=float(input('Enter 1st input:'))
b=float(input('Enter 2nd input:'))
c=float(input('Enter 3rd input:'))
if (a>b and a>c):
    print(F'{a}')
else:
    if b>c:
        print(F'{b}')
    else:
        print(F'{c}')

'''
23-->Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32
2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8

-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 1
Enter celsius temperature : 30
Fahrenheit Equivalent: 86.0
Press any key to continue...
-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 2
Enter celsius temperature : 100
Fahrenheit Equivalent: 37.78
Press any key to continue...
-->Sample Output:
Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : 3
Invalid input
Press any key to continue...
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
24-->Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,4th  quadrant , x - axis , y - axis   or  origin
1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve
2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve
3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve
4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve
5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0
6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero
7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes
8) Hint:  Use  if  ..   elif

-->Sample Output:
Enter value of X co-ordinate : -10
Enter value of y co-ordinate : 20 
2nd quadrant
Press any key to continue...
'''
x=float(input('Enter value of x co-ordinate:'))
y=float(input('Enter value of y co-ordinate:'))
if x > 0 and y > 0:
    print('1st quadrant')
elif x < 0 and y > 0:
    print('2nd quadrant')
elif x < 0 and y < 0:
    print('3rd quadrant')
elif x > 0 and y < 0:
    print('4th quadrant')
elif x != 0 and y == 0:
    print('On X-axis')
elif x == 0 and y != 0:
    print('On Y-axis')
else:
    print('Origin')
'''
25-->Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
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

-->Sample Output 15:
Enter first input : 10
Enter second input : 20
Enter third input : 7
Largest input: 20.0
Smallest input : 7.0
Middle input : 10.0
Press any key to continue...
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



        
