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
a=complex(input('enter first complex number:'))
b=complex(input('enter first complex number:'))
sum:a+b
Difference:a-b
product:a*b
Division:a/b
print(f'{'sum'}:{a+b}')
print(f'{'Difference'}:{a-b}')
print(f'{'product'}:{a*b}')
print(f'{'Divison'}:{a/b}')

"""
#OUT PUT

enter first complex number:3+4j
enter first complex number:5+6j
sum:(8+10j)
Difference:(-2-2j)
product:(-9+38j)
Divison:(0.6393442622950819+0.03278688524590165j)

"""
'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
a=float(input('Enter length of rectangle:'))
b=float(input('Enter length of rectangle:'))
Area : a*b
Perimeter : 2*(a+b)
print(f'{'Area :'}{a*b}')
print(f'{'Perimeter :'}{2*(a+b)}')

"""
OUTPUT

Enter length of rectangle:4
Enter length of rectangle:5
Area :20.0
Perimeter :18.0
"""
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
radius=eval(input("Enter radius :"))
pi=22/7
volume=(4/3)*pi*radius**3
print('volume :',volume)
"""
OUT PUT
Enter radius :3.5
volume : 179.66666666666663

"""
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
p=eval(input('Enter principle :'))
t=eval(input('Enter time :'))
r=eval(input('Enter rate of interest :'))
simple_Interst =p*t*r/100
compound_Interest=p*((1+r/100)**t)-p
print('simple Interest :',simple_Interst)
print('Compund interest:',compound_Interest)
"""
OUT PUT
Enter principle :10000
Enter time :3
Enter rate of interest :7.5
simple Interest : 2250.0
Compund interest: 2422.968749999998
"""

'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
print("befor swap   x=10  y='Hyd'")
x=10
y='Hyd'
temp1='Hyd'
temp2=10
x,y=y,x
print("after  swap "   'x=',x,  'y=',y)

"""
OUT PUT
befor swap   x=10  y='Hyd'
after  swap
x= Hyd
y= 10


"""
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
X = 25
Y =  10
temp=X+Y
Y=temp-X
X=temp-Y
print('X=',X)
print('Y=',Y)
"""
OUTPUT
X= 25
Y= 10

"""
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
X = 25
Y =  10
temp=X*Y
X=temp//X
Y=temp//Y
print('X=',X)
print('Y=',Y)
"""
OUT PUT
X= 10
Y= 25
"""

# Identify  error
else:
		print('else  suite')#ERROR due to indentation 
print('Outside')#Outside

# Identify  error
if  9 > 5
	print('Hello')#Hello
print('Bye')#Bye

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')#error due to no":" after else

# Identify  error
if  (10,20,15):
print('Hyd')#error due to no indentation after if statement
else:
print('Sec')#error due to no indentation after else statement

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')#error due to  indentation is to long after else statement
print('Bye')#Bye

# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}#error due to there are no {}
else:
{
	print('Four')
	print('Five')
	print('Six')
}#error due to there are no {} 
print('Bye')#Bye

# Identify  error
if  ():
	print('One')#One
	print('Two')#Two
	print('Three')#Three
else:
if  []:
	print('Four')#Four
	print('Five')#Five
	print('Six')#Six
else:
if  {}:
	print('Seven')#Seven
	print('Eight')#Eight
	print('Nine')#Nine
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#Bye

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n=int(input('enter the numder-'))
if(n%2==0):
	print("even")
else:
	print("odd")

# Find outputs  (Home  work)
if():
        print('Hyd')#Hyd
        print('Sec')#Sec
        print('Cyb')#Cyd
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')#Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')#Hyd
        print('Sec')#Sec
        print('Cyb')#Cyd
print('Bye')#Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')#Hyd
	print('Sec')Sec
	print('Cyb')#Cyd
print('Bye')#Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

a=int(input('Enter month numder (1-12):'))
try:
    if (a==1):
        print(" January")
    elif(a==2):
        print(" February")
    elif(a==3):
        print(" March")
    elif(a==4):
        print(" April ")
    elif(a==5):
        print(" may")
    elif(a==6):
        print(" June")
    elif(a==7):
        print(" July")
    elif(a==8):
        print(" August")
    elif(a==9):
        print(" September")
    elif(a==10):
        print(" October")
    elif(a==11):
        print(" November")
    elif(a==12):
        print(" December")
    else:
        print("Input should Between 1 to 12")
except:
    print(" Input should be an integer ")
"""
OUT PUT
Enter month numder (1-12):6
 June
Enter month numder (1-12):13
Input should Between 1 to 12
Enter month numder (1-12):5.0
Input should be an integer
"""
# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)

a=int(input('Enter any digit (0-9):'))
try:
    if (a==0):
        print(" zero")
    elif(a==1):
        print(" One")
    elif(a==2):
        print(" Two")
    elif(a==3):
        print(" Three")
    elif(a==4):
        print(" Four")
    elif(a==5):
        print(" Five")
    elif(a==6):
        print(" Six")
    elif(a==7):
        print(" Seven")
    elif(a==8):
        print(" Eight")
    elif(a==9):
        print("Nine")
    else:
        print("Invalid")
except:
    print(" Input should be an integer ")
"""
OUT PUT
Enter month numder (0-9):4
 Four
"""

'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years
'''

a=int(input('Enter 4 -digit year:'))
if (a%4==0):
	print("Leap year")
else:
	print("Not a leap year")

"""
OUT PUT
Enter 4 -digit year:1992
Leap year
Enter 4 -digit year:2026
Not a leap year
"""


















