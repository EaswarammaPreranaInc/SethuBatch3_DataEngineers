''
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
a = complex(input("Enter first complex number: ")
b = complex(input("Enter second complex number: ")
print(f'Sum ={a+b}')
print(f'Difference ={a-b}')
print(f'Product ={a*b}')
print(f'Division ={(a/b):'2f}')



'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  ---> area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
area = l*b
perimeter =  2*(l+b)
print('Area: ', area)
print('Perimeter: ', perimeter)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  ---> volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3

import math
r = float(input("Enter radius : "))
volume = 4/3*math.pi*r**3
print("Volume: ",volume)


Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  ---> principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  ---> p * (1  +  r  /  100) ^  t  -  p
p = float(input("Enter Principle: "))
t = float(input("Enter time: "))
r = float(input("Enter rate of interest: "))
SI= (p*t*r)/100
CI =p * (1  +  r  /  100)**t  -  p
print("Simple interest : ", SI)
print("Compound interest: ", CI)


Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->  x = Hyd  and   y = 10
'''
x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f'Before Swap:{x=} \t {y=}')
temp = a
a = b
b = temp
print(f'After Swap:{x=} \t {y=}')

Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10
'''
x = 25
y =  10
s = x+y #35
x = s-x
y = s - x
print(x,y)


# Identify  error
else:
		print('else  suite')
print('Outside')#output:indentation error


# Identify  error
if  9 > 5    #output: " : " is missing
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')#output: " : " is missing


# Identify  error
if  (10,20,15):
print('Hyd')#output:indentation error
else:
print('Sec')


# Identify  error
if  ():
			print('Hyd')#output:indentation error

	else:
					print('Sec')#output:indentation error

print('Bye')



# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')#output:braces are not allowed in conditional statements
}
else:
{
	print('Four')
	print('Five')
	print('Six')#output:braces are not allowed in conditional statements
}
print('Bye')

# Identify  error
if  ():#output:indentation error
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')#output:indentation error
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')##output:indentation error



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

a = int(input("Enter any num: "))
if a % 2 == 0:
  print("Even Number")
else:
  print("Odd Number")

# Find outputs
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
#output:One Two Three Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')#output:Hyd Sec Cyb bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')#output:bye


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
  
   m = int(input("Enter month number(1-12): "))
   if m == 1:
     print("January")
   elif m == 2:
     print("February")
   elif m == 3:
      print("March")
   elif m == 4:
    print("April")
   elif m == 5:
    print("May")
   elif m == 6:
    print("June")
   elif m == 7:
    print("July")
   elif m == 8:
    print("August")
   elif m == 9:
    print("September")
   elif m == 10:
    print("October")
   elif m == 11:
    print("November")
   elif m == 12:
    print("December")
   else:
    print("Number should between 1-12")
except:
 print("Input should be an integer.")
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
try:
   m = int(input("Enter any digit(0-9): "))
   if m == 1:
     print("one")
   else:
    if m == 2:
     print("two")
    else:
     if m == 3:
      print("three")
     else:
      if m == 4:
       print("four")
      else:
       if m == 5:
        print("five")
       else:
        if m == 6:
          print("six")
        else:
          if m == 7:
            print("seven")
          else:
            if m == 8:
              print("eight")
            else:
             if m == 9:
              print("nine")
             else:
              print("Invalid")
except:
 print("Input should be an integer.")


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''
year = int(input("Enter a year to fine leap year or not: "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0 :
    print("Leap year.")
else  :
    print("Not a leap year")

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''
a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
c = float(input("Enter c number: "))
if a > b and b > c:
  print("A",a)
else: 
  if b > a and b > c:
    print("B",a)
  else:
   print("c",c)

'''
Write  a  program  to  convert  Celsius  temperature  to  Fahrenheit  and  vice-versa

1) What  is  the  formula  to  convert  Celsius  to  Fahrenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  Fahrenheit  to  Celsius ?  --->  (temp - 32) / 1.8
'''

a = int(input("Enter 1 to convert Celsius to Fahrenheit and 2 to convert Fahrenheit to Celsius: "))
if a ==1:
  temp= float(input("Enter celsius number: "))
  Fahrenheit = 1.8 * temp + 32
  print("Fahrenheit Equivalent: ", Fahrenheit)
elif a == 2:
  temp= float(input("Enter Fahrenheit number: "))
  Celsius = (temp - 32) / 1.8
  print(" Celsius Equivalent: ", Celsius)
else:
  print("Invalid output")

   

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
x= int(input("Enter value of x co-ordinate: ")
y= int(input("Enter value of x co-ordinate: ")

x= int(input("Enter value of x co-ordinate: "))
y= int(input("Enter value of x co-ordinate: "))

if x > 0 and y > 0:
  print("1st Quadrant") 
elif x < 0 and y > 0:
  print("2nd Quadrant") 
elif x < 0 and y < 0:
  print("3rd Quadrant") 
elif x > 0 and y < 0:
  print("4th Quadrant") 
elif x > 0 and y == 0:
  print(" x  and  y  on  x - axis") 
elif x == 0 and y > 0:
  print(" x  and  y  on  y - axis") 
elif x == 0 and y == 0:
  print("x  and  y point  to the  origin") 







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
a = 10
b = 20
c = 7
max = a
if b > max :
  max = b
if c > max:
  max=c
min = a
if b < min :
  min = b
if c < min:
  min=c
middle = (a + b+c)-(max + min)
print("Largest input: ",max)
print("Smallest input :",min)
print("Middle input: ", middle)








































