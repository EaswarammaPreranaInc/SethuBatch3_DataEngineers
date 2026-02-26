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
def complexOperations(x,y):
	rl=y.real
	img =y.imag
	print(F'Sum : ({x+y})')
	print(F'Difference : ({(x-y)})')
	print(F'Product : ({x*y})')
	print(F'Division : ({(x*(rl-img))/(y*(rl-img))})'). # simply x/y

a=complex(input('enter 1st complex number'))
b=complex(input('enter 2nd complex number'))
complexOperations(a,b)

(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''

def rectange(l, b):
	print(F'Area : {(l*b):.2f}')
	print(F'Perimeter : {2*(l+b):.2f}')

l=eval(input('enter length of rectangle'))
b=eval(input('enter breadth of rectangle'))
rectange(l, b)



'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''

import math
r=eval(input('enter radius'))
print(F'Volume : {(4/3)*(math.pi)*(math.pow(r,3)):.2f}')

 '''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''

import math
p=float(input('Enter principle :'))
t=float(input('Enter time :'))
r=float(input('Enter rate of Interest :'))

print(F'Simple Interest : {((p*t*r)/100):.2f}')
print(F'Compound Interest : {(p*(math.pow((1+(r/100)),t))-p):.2f}')


 '''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object


Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
def swap(x,y):
	temp=x;
	x=y;
	y=temp;
	print(F'After swap: {x=}	{y=}')
a=input("Enter 1st input :")
b=input("Enter 2nd input :")
print(F'Before swap: {a=}	{b=}')
swap(a,b)

 ''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''

def swapp(x,y):
	x=x+y
	y=x-y;
	x=x-y;
	print(F'After swap: {x=}	{y=}')
a=int(input("Enter 1st input :"))
b=int(input("Enter 2nd input :"))
print(F'Before swap: {a=}	{b=}')
swapp(a,b)


 '''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
def swappp(x,y):
	x=x*y
	y=int(x/y);
	x=int(x/y);
	print(F'After swap: {x=}	{y=}')
a=int(input("Enter 1st input :"))
b=int(input("Enter 2nd input :"))
print(F'Before swap: {a=}	{b=}')
swappp(a,b)

 # Identify  error
else:    # No if with else 
	print('else  suite')
print('Outside')

 # Identify  error
if  9 > 5 # colon is missing syntax error
	print('Hello')
print('Bye')
 # Identify  error
if  9 > 12:
	print('Hyd')
else     # colon is missing syntax error
	print('Sec')

 # Identify  error
if  (10,20,15):  # indentation error
print('Hyd')
 else:
print('Sec')
# Identify  error
if  (): # if and else are not at same indentation to error
			print('Hyd')
	else:
					print('Sec')
print('Bye')
# Identify  error
if  { }:  
{           # Braces not allowed, only indentation is valid in python, braces meant for sets and dictionary
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
if  []: 	# Indentation error 
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

#correct version
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

 # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

def EvenOrOdd(a):
	if(a%2==0):
		print("Even")
	else:
		print("Odd")		



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

#One
#Two
#Three
#Bye

 # Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#Hyd
#Sec
#Cyb
#Bye


 # Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

def monthName(n):
	if n==1:
		print('January')
	elif n==2:
		print('February')
	elif n==3:
		print('March')
	elif n==4:
		print('April')
	elif n==5:
		print('May')
	elif n==6:
		print('June')
	elif n==7:
		print('July')
	elif n==8:
		print('August')
	elif n==9:
		print('September')
	elif n==10:
		print('October')
	elif n==11:
		print('November')
	elif n==12:
		print('December')
	else:
		print('Enter number from 1 to 12 only')
n=int(input('enter number in range of 1 t0 13'))
monthName(n)



'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
def numToWord(n)->str:
	if(n==0):
		return 'Zero'
	else:
		if(n==1):
			return 'One'
		else:
			if(n==2):
				return 'Two'
			else:
				if(n==3):
					return 'Three'
				else:
					if(n==4):
						return 'Four'
					else:
						if(n==5):
							return 'Five'
						else:
							if(n==6):
								return 'Six'
							else:
								if(n==7):
									return 'Seven'
								else:
									if(n==8):
										return 'Eight'
									else:
									    if(n==9):
										    return 'Nine'
									    else:
										    return "Invalid"


n=int(input('enter number in range of 0 t0 9'))
print(numToWord(n))

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''

def isLeap(year)-> bool:
	if((year %400 ==0) or ((year % 100 !=0) and (year % 4 ==0))):
		return True
	return False

year = int(input("Enter 4-digit year : "))
if(isLeap(year)):
	print('Leap Year')
else:
	print('Not Leap Year')

 '''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

a=float(input("Enter 1st input :"))
b=float(input("Enter 2nd input :"))
c=float(input("Enter 3rd input :"))
if( a>b and a>c):
	print(F'{a} is largest')
else:
	if(b>c):
		print(F'{b} is largest')
	else:
		print(F'{c} is largest')


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''

def CelOrFahren(n):
	if(n==1):
	    f = float(input("Enter fahrenheit temperature :"))
	    print(F'Celsius equivalent : {((f-32)/1.8):.2f}')
	if(n==2):
	    c = float(input("Enter celsius temperature :"))
	    print(F'Fahrenheit equivalent : {(1.8*c+32):.1f}')
	else:
		print("Invalid input")

n=int(to be input('Enter 1 to convert celsius to fahrenheit and 2 to convert fahrenheit to celsius :'))
C.elOrFahren(n)
        

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

def Quad(x,y):
    if( x== 0 and y==0)
	    print( 'Origin')
	elif ( x== 0)
	     print('X- axis')
	elif( y== 0)
	     print('Y-axis')
	elif( x > 0 and y >0):
	    print('1st Quadrant')
	elif( x>0 and y<0):
	    print('2nd Quadrant')
	elif( x<0 and y<0):
	    print('3rd  Quadrant')
	else:
		print("4th Quadrant")

x=float(input('Enter value of x co-ordinate :'))
y=float(input('Enter value of y co-ordinate :'))
Quad(x,y)


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

def threeNumbers(x,y,z)->(float,float,float):
	max,min,mid=a,a,a
	if(b>max):
	    max=b
	else( max<c):
		max =c
	if(min>b):
	    min=b
	else( min>c):
	    min =c
	return (max,min, (a+b+c -(max+min)))    
        


a=float(input("Enter 1st input :"))
b=float(input("Enter 2nd input :"))
c=float(input("Enter 3rd input :"))
x,y,z=threeNumbers(a,b,c)
print(F'Largest input : {x:.1f} \nSmallest input : {y:.1f} \nMiddle input : {z:.1f}')
        



