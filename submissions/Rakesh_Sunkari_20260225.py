'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
							   
'''
#program:

import math
a=complex(input("Enter first complex number:" ))
b=complex(input("Enter second complex number:"))

print("Addition=", a+b)

print("subtraction=", a-b)

print("Product=", a*b)

print('Dision=', a/b)




'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle
'''
#program:

lenght = eval(input("enter the length of a rectangle:"))
breadth = eval(input("entegr the breadth of a rectangle:"))
print("area=", lenght * breadth)
print("perimeter=", 2*(lenght + breadth))



'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

'''

#program:

import math
r=eval(input("Enter radius = "))
b=(4/3)* math.pi *r**3
print("volume of sphere is:",b)




'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
'''
#program:

import math
a=float(input("Enter principle: "))
b=float(input("Enter time: "))
c=float(input('Enter rate of Interest: '))
simple_interest=(a*b*c)/100
compound_interest=a*(1+c/100)**b-a
print("simple interest= ",simple_interest)
print("compound interest= ",compound_interest)






'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
#program:

x='Hyd'
y=10
print(f"before swap: x={x},y={y}")
temp= x
x=y
y=temp
print(f"after the swap: x={x},y={y}")



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
#program:

x=25
y=10
print(f"before swap: x={x},y={y}")
x=x+y
y=x-y
x=x-y
print(f"after the swap: x={x},y={y}")



'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
#program:

x=25
y=10
print(f"before swap: x={x},y={y}")
x=x*y
y=x/y
x=x/y
print(f"after the swap: x={x},y={y}")





 # Identify  error
else:
		print('else  suite')
print('Outside')




 # Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# no colon




# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')

# no colon for else


 # Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')

# the print statement should have the space after the if and else are executed



 # Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')


# indentation error




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

# indentation error






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
# indentation error







 # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
#program:

a=int(input("enter even or odd number: "))

if a%2==0:	
	print("a is even")
else:		
	print("a is odd number")




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

output:
# Hyd
# Sec
# Cyb
# Bye



 # Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

output:
# {10 : 20 , 30 : 40}
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

output:
Hyd 
Sec
Cyb
Bye


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

#program:

month=int(input("Enter the month number between 1 -12:"))

if month==1:
	print("January")
elif month==2:
	print("February")
elif month==3:
	print("March")
elif month==4:
	print("April")
elif month==5:
	print("May")
elif month==6:
	print('June')
elif month==7:
	print('July')
elif month==8:
	print('August')
elif month==9:
	print('September')
elif month==10:
	print("October")
elif month==11:
	print("November")
elif month==12:
	print("December")
else:
	print("month should be from 1-12")




'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
#program:

a=int(input("enter any number (0-9) to print word: "))

if a==0:
	print("zero")
else:
	if a==1:
		print("one")
	else:
		if a==2:
			print("two")
		else:
			if a==3:
				print("three")
			else:
				if a==4:
					print("four")
				else:
					if a==5:
						print("five")
					else:
						if a==6:
							print("six")
						else:
							if a==7:
								print("seven")
							else:
								if a==8:
									print("eight")
								else:
									if a==9:
										print("nine")
									else:
										print("Error")



'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
#program:

import math
a=int(input("enter any year to check if it is a leap year:"))
if a%4==0:
	print("a is leap year")
elif a%400==0:
	print(f" a='{a}' is leap year")
else:
	print(f"a='{a}' is not a leap year")


'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
#program:

a=10
b=20
c=30

if a>b and a>c:
	
	print("largest number is: ", a)
else:
	if b>c:
		print("largest number is:", b)
	else:
			print("largest number is :", c)


'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''
#program:

print("1.Celcius to Farenheit")
print('2. Farenheit to Celcius')

choice =int(input("enter your choice (1 or 2):"))
if choice==1:
	a=float(input("enter temperature in celcius: "))
	b= (1.8* a+32)
	print("Temperature in Celcius:",b)
elif choice==2:
	c=float(input("enter temperature in farenheit: "))
	d= (c-32)/1.8
	print("Temperature in farenheit:",d)
else:
	print("error")





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
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10

#program:
a=10
b=20
c=7

if a>b and a>c:
	print(a)
	print("max is", a)
else:
	if b>c:
		print("max is:",b)
	else:
		print(c)


if a<b and a<c:
	print(a)
	print("min is", a)
else:
	if b<c:
		print("min is:",b)
	else:
		print(c)

f=(a+b+c)-(b+c)
print("mid is : ",f)



	
1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  assign  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  assign  that  input  to  min

5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c

6) Hint : Do  not  use  else  in  the  program
'''
