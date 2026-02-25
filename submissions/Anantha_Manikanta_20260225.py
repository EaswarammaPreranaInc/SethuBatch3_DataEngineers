'''
1) Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
'''
a = complex(input("Enter first complex number : "))
b = complex(input("Enter second complex number: "))
sum_result = a + b
diff_result = a - b
prod_result = a * b
div_result = a / b
print(f"Sum        :  {sum_result}")
print(f"Difference :  {diff_result}")
print(f"Product    :  {prod_result}")
print(f"Division   :  {div_result}")

'''
2)Write  a  program  to  determine  area  and  perimeter  of  rectangle
'''
length = float(input("Enter  length  of  rectangle  :  "))
breadth = float(input("Enter  breadth  of  rectangle  :  "))
area = length * breadth
perimeter = 2 * (length + breadth)
print(f"Area  :  {area:.2f}")
print(f"Perimeter  :  {perimeter:.2f}")

'''
3)Write  a  program  to  determine  volume  of  a  sphere
'''
import math
radius = float(input("Enter  radius  :  "))
volume = (4/3) * math.pi * radius**3
print(f"Volume  :  {volume:.2f}")

'''
4)Write  a  program  to  determine  simple  interest  and  compound  interest
'''

principal = float(input("Enter  principle  :  "))
time = float(input("Enter  time  :  "))
rate = float(input("Enter  rate  of  interest  :  "))
si = (principal * time * rate) / 100
ci = principal * (1 + rate/100) ** time - principal
print(f"Simple  Interest  :  {si:.2f}")
print(f"Compound  Interest  :  {ci:.2f}")

'''
5)Write  a  program  to  swap  values  of  two   objects   using  3rd  object
'''

# Read inputs
x = input("Enter  1st  input  :  ")
y = input("Enter  2nd  input  :  ")
print(f"Before  swap  :  x='{x}'\ty='{y}'")
temp = x
x = y
y = temp
print(f"After  swap  :  x='{x}'\ty='{y}'")

'''
6) Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions
'''
x = int(input("Enter  1st  number  :  "))
y = int(input("Enter  2nd  number  :  "))
print(f"Before  swap  :  x={x}   y={y}")
x = x + y
y = x - y
x = x - y
print(f"After   swap  :  x={x}   y={y}")

'''
7)Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  division
'''

x = int(input("Enter  1st  number  :  "))
y = int(input("Enter  2nd  number  :  "))
print(f"Before  swap  :  x={x}   y={y}")
x = x * y
y = x / y
x = x / y
print(f"After   swap  :  x={int(x)}   y={int(y)}")

'''
8)# Identify  error
else:
		print('else  suite')  # We cant write else suite if there is no If suite
print('Outside')

'''
'''
9) # Identify  error
if  9 > 5
	print('Hello')  # : is missing after writing if suite
print('Bye')
'''
'''
10) # Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')  # : Is missing in else suite
'''
'''
11) # Identify  error
if  (10,20,15):
print('Hyd')     # Indentation is missing in both if and else suites
else:
print('Sec')
'''
'''
12) # Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')   # If and else suites should be properly indented

'''
'''
13) # Identify  error
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
print('Bye')  # Curly braces are not required in python and throws errors if we use them and they are only for sets and dictionaries

'''
'''
14) # Identify  error
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
print('Bye')               # In both statements after else the if's should be properly indented after else and not straight to else statement
'''
'''
15) # Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
'''
A = int(input("Enter the number:"))
if A % 2 == 0:
    print("Even number")
else:
    print("Odd number")

'''
16) # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')  # Hyd <next line> Sec <next line> Cyb <next line> Bye

'''
'''
17) # Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')  # Hyd <next line> Sec <next line> Cyb <next line> Bye
'''
'''
18) # Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # Bye
'''
'''
19)  Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
'''
try:
    month = int(input("Enter  month  number  (1 - 12): "))

    if month < 1 or month > 12:
        print("Input  should  be  between  1  and  12")
    elif month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
except ValueError:
    print("Input  should  be  an  integer")
'''
20) Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
'''
try:
    n = int(input("Enter  a  digit  (0 - 9): "))

    if n == 0:
        print("Zero")
    else:
        if n == 1:
            print("One")
        else:
            if n == 2:
                print("Two")
            else:
                if n == 3:
                    print("Three")
                else:
                    if n == 4:
                        print("Four")
                    else:
                        if n == 5:
                            print("Five")
                        else:
                            if n == 6:
                                print("Six")
                            else:
                                if n == 7:
                                    print("Seven")
                                else:
                                    if n == 8:
                                        print("Eight")
                                    else:
                                        if n == 9:
                                            print("Nine")
                                        else:
                                            print("Invalid")
'''
21) Write  a  program  to  test  year  is  leap  year  or  not
'''
year = int(input("Enter  4-digit  year  :  "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap  year")
else:
    print("Not  a  leap  year")
'''
22)Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
'''
a = float(input("Enter  1st  number  :  "))
b = float(input("Enter  2nd  number  :  "))
c = float(input("Enter  3rd  number  :  "))
if a > b and a > c:
    print("Largest  number  : ", a)
else:
    if b > a and b > c:
        print("Largest  number  : ", b)
    else:
        print("Largest  number  : ", c)
'''
23)Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
'''
A = int(input("Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius  :  "))
if A == 1:
    c = float(input("Enter  celsius  temperature  :  "))
    f = 1.8 * c + 32
    print("Fahrenheit  Equivalent  :  ", f)
elif A == 2:
    f = float(input("Enter  fahrenheit  temperature  :  "))
    c =  (f - 32) / 1.8
    print("celsius  equivalent  :  ", round(c, 2))
else:
    print("Invalid  input")
'''
24) Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin
'''
x = float(input("Enter  value  of  x  co-ordinate  :  "))
y = float(input("Enter  value  of  y  co-ordinate  :  "))
if x > 0 and y > 0:
    print("1st  quadrant")
elif x < 0 and y > 0:
    print("2nd  quadrant")
elif x < 0 and y < 0:
    print("3rd  quadrant")
elif x > 0 and y < 0:
    print("4th  quadrant")
elif x != 0 and y == 0:
    print("x-axis")
elif x == 0 and y != 0:
    print("y-axis")
else:
    print("Origin")
'''
25) Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
'''
a = int(input("Enter  1st  number  :  "))
b = int(input("Enter  2nd  number  :  "))
c = int(input("Enter  3rd  number  :  "))
max = a
min = a
if b > max:
    max = b
if c > max:
    max = c
if b < min:
    min = b
if c < min:
    min = c
mid = (a + b + c) - (max + min)
print("Largest  : ", max)
print("Smallest : ", min)
print("Middle   : ", mid)