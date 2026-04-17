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
a=complex(input('Enter first number:'))
b=complex(input('Enter first number:'))
print(F'Sum: {a+b}')
print(F'Difference: {a-b}')
print(F'Product: {a*b}')
print(F'Division: {a/b}')

'''



'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''


'''
l=float(input('Enter length of rectangle:'))
b=float(input('Enter breadth of rectangle:'))
print(F'Area: {l*b}')
print(F'Perimeter: {2*(l+b)}')

'''


'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''


'''

from math import pi
r=float(input('Enter radius:'))
print(F'Volume: {(4/3)*pi*r**3}')

'''



'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''



'''
p=float(input('Enter principle:'))
t=float(input('Enter time:'))
r=float(input('Enter rate of interest:'))
print(F'Simple interest: {(p*t*r)/100}')
print(F'Compound interest: {(p*(1+r/100)**t)-p}')
'''


'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''


'''
x=input('Enter 1st input:')
y=input('Enter 2nd input:')
print(F'Before swap:{x=}\t{y=}')
temp=x
x=y
y=temp
print(F'After swap:{x=}\t{y=}')
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''


'''
x=float(input('Enter 1st input:'))
y=float(input('Enter 2nd input:'))
print(F'Before swap:{x=}\t{y=}')
x=x+y
y=x-y
x=x-y
print(F'After swap:{x=}\t{y=}')
'''


'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''

'''
x=float(input('Enter 1st input:'))
y=float(input('Enter 2nd input:'))
print(F'Before swap:{x=}\t{y=}')
x=x*y
y=x/y
x=x/y
print(F'After swap:{x=}\t{y=}')
'''

# Identify  error
else:
		print('else  suite')   #else cant be used without if
print('Outside')


# Identify  error
if  9 > 5   #no : after condition
	print('Hello')
print('Bye')

# Identify  error
if  9 > 12:
	print('Hyd')
else     #no : after else
	print('Sec')

# Identify  error  
#after : there is no space or indentation (statements must be written after spaces or indent)
if  (10,20,15):
print('Hyd')
else:
print('Sec')



# Identify  error   
#if and else must be in the same coulumn or indent
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')


# Identify  error
#suite must not be written in {}
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

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: #no indent
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: #no indent
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

'''
a=int(input('enter a number:'))
if(a%2==0):
    print(F'{a} is even')
else:
    print(F'{a} is odd')
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
Hyd
Sec
Cyb
Bye

'''

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

'''
try:
    a=int(input('enter month number(1-12):'))
    if(a==1):
         print('January')
    elif(a==2):
         print('February')
    elif(a==3):
         print('March')
    elif(a==4):
         print('April')
    elif(a==5):
         print('May')
    elif(a==6):
         print('June')
    elif(a==7):
         print('July')
    elif(a==8):
         print('August')
    elif(a==9):
         print('September')
    elif(a==10):
         print('October')
    elif(a==11):
         print('November')
    elif(a==12):
         print('December')
    else:
         print('Input should be between 1 and 12')

except ValueError:
    print('Input should be an integer')

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

'''
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


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

'''
if(a%4==0 and a%100!=0 or a%400==0):
    print('Leap year')
else:
    print('Not a leap year')
'''

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

'''
a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
if(a>b and a>c):
    print(f'{a} is largest')

else:
    if(b>c):
        print(f'{b} is largest')
    else:
        print(f'{c} is largest')
'''

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''


'''
a=int(input('enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius:'))
if(a==1):
    b=int(input("enter celsius temperature:"))
    print(f'Farenheit equivalent {1.8*b+32}')
elif(a==2):
    c=int(input("enter farenheit temperature:"))
    print(f'celsius equivalent {(c-32)/1.8}')
else:
    print('invalid input')
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


'''
x=int(input('enter value of x co-ordinate:'))
y=int(input('enter value of y co-ordinate:'))
if(x>0 and y>0):
    print('1st quadrant')
elif(x<0 and y>0):
    print('2nd quadrant')
elif(x<0 and y<0):
    print('3rd quadrant')
elif(x>0 and y<0):
    print('4th quadrant')
elif(x!=0 and y==0):
    print('x axis')
elif(x==0 and y!=0):
    print('y axis')
elif(x==y==0):
    print('origin')
else:
    print('enter valid input')
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

'''
x=float(input('Enter first input:'))
y=float(input('Enter second input:'))
z=float(input('Enter third input:'))
max=x
if(y>max):
    max=y
if(z>max):
    max=z
min=x
print(f'Largest input:{max}')
if(y<min):
    min=y
if(z<min):
    min=z
print(f'Smallest input:{min}')
print(f'Middle input:{(x+y+z)-(max+min)} ')
'''