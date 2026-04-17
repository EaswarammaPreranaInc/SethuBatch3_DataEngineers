1. # Identify  error
else:
		print('else  suite')
print('Outside')
#output:- Invalid Syntax(else should be followed by if or elif statements)

2. # Identify  error
if  9 > 5
	print('Hello')
print('Bye')
#output:-missing (:) after if statment

3. # Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
#output:-missing (:) after else statment

4.# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
#output:-Indentation error

5. Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
#output:-Indentation error

6.# Identify  error
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
#output:- Syntax error used "{}" for if & else conditions

7. # Identify  error
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
#output:-Indentation error(after else conditions)


8. # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
#output:-empty tuple() = false
                       One
                       Two
                       Three
                       Bye

9.# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#output:-Non empty dict- true
                       Hyd
                       Sec
                       Cyb
                       Bye

10.# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
#output:-empty dict{} -false
         Bye

11.'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers	   
'''
c1=eval(input("Enter First complex number: "))
c2=eval(input("Enter second complex number: "))
sum_result = c1 + c2
print("\nSum =", sum_result)
diff_result = c1 - c2
print("Difference =", diff_result)
prod_result = c1 * c2
print("Product =", prod_result)
div_result = c1 / c2
print("Division =", div_result)

'''
output:-Enter First complex number: 3+4j
Enter second complex number: 5+6j

Sum = (8+10j)
Difference = (-2-2j)
Product = (-9+38j)
Division = (0.6393442622950819+0.03278688524590165j)
'''
12'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle
'''
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area of rectangle =", area)
print("Perimeter of rectangle =", perimeter)

'''
output:-Enter length: 4
Enter breadth: 5
Area of rectangle = 20.0
Perimeter of rectangle = 18.0
'''

13'''
Write  a  program  to  determine  volume  of  a  sphere
'''
import math
radius = float(input("Enter radius: "))
volume = (4/3) * math.pi * (radius ** 3)
print("Volume of sphere =", volume)

'''
output:-Enter radius: 3.5
Volume of sphere = 179.594
'''
14'''
Write  a  program  to  determine  simple  interest  and  compound  interest
'''

p = float(input("Enter Principal amount: "))
t = float(input("Enter Time (in years): "))
r = float(input("Enter Rate of Interest: "))
si = (p * t * r) / 100
ci = p * (1 + r / 100) ** t - p
print("Simple Interest =", si)
print("Compound Interest =", ci)

'''
output:-Enter Principal amount: 10000
Enter Time (in years): 3
Enter Rate of Interest: 7.5
Simple Interest = 2250.0
Compound Interest = 2422.968749999998
'''

15'''
Write  a  program  to  swap  values  of  two   objects   using  3rd  object
'''
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")
print("Before swap : x =", x, " y =", y)
temp = x
x = y
y = temp
print("After swap  : x =", x, " y =", y)

'''
output:-Enter 1st input : 25
Enter 2nd input : Hyd
Before swap : x = 25  y = Hyd
After swap  : x = Hyd  y = 25
'''

16.'''
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  addition  and  two  subtractions
'''
x = 25
y = 10
print("Before swap:")
print("x =", x)
print("y =", y)
x = x + y
y = x - y
x = x - y
print("\nAfter swap:")
print("x =", x)
print("y =", y)

'''
output:-Before swap:
x = 25
y = 10

After swap:
x = 10
y = 25
'''
17.'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object
Hint: One  multiplication  and  two  divisions
'''
x = 25
y = 10
print("Before swap:")
print("x =", x)
print("y =", y)
x = x * y
y = x / y
x = x / y
print("\nAfter swap:")
print("x =", x)
print("y =", y)

output:-Before swap:
x = 25
y = 10

After swap:
x = 10.0
y = 25.0
'''
18.# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

num = eval(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
'''
output:-Enter a number: 24
The number is Even
'''
19.# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 

month = int(input("Enter month number (1-12): "))
if month == 1:
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
else:
    print("Invalid month number")

20.'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

num = int(input("Enter a digit (0-9): "))

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


21.'''
Write  a  program  to  test  year  is  leap  year  or  not
 Hint:  3  conditions
'''
year = eval(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

22.'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else
Hint:  Write  multiple  conditions
'''
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))
if a > b and a > c:
    print("Largest number is:", a)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)

'''
output:-
Enter first number: 25
Enter second number: 60
Enter third number: 80
Largest number is: 80
'''

23.'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa
'''
choice = int(input("Enter 1 for Celsius to Fahrenheit\nEnter 2 for Fahrenheit to Celsius\n"))
temp = float(input("Enter temperature: "))
if choice == 1:
    fahrenheit = 1.8 * temp + 32
    print("Temperature in Fahrenheit =", fahrenheit)
else:
    if choice == 2:
        celsius = (temp - 32) / 1.8
        print("Temperature in Celsius =", celsius)
    else:
        print("Invalid Choice")

24.'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin
 Hint:  Use  if  ..   elif
'''
x = eval(input("Enter value of x: "))
y = eval(input("Enter value of y: "))
if x > 0 and y > 0:
    print("Point lies in First Quadrant")
elif x < 0 and y > 0:
    print("Point lies in Second Quadrant")
elif x < 0 and y < 0:
    print("Point lies in Third Quadrant")
elif x > 0 and y < 0:
    print("Point lies in Fourth Quadrant")
elif x != 0 and y == 0:
    print("Point lies on X-axis")
elif x == 0 and y != 0:
    print("Point lies on Y-axis")
else:
    print("Point is at the Origin")

25.'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers
a = 10
b = 20
c = 7
max = 20
min = 7
mid =   (10 + 20 + 7) - (20 + 7) = 10
 Hint : Do  not  use  else  in  the  program
'''
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))
max = a
if b > max:
    max = b
if c > max:
    max = c
min = a
if b < min:
    min = b
if c < min:
    min = c
mid = (a + b + c) - (max + min)
print("Largest =", max)
print("Smallest =", min)
print("Middle =", mid)

'''
output:-Enter first number: 20
Enter second number: 10
Enter third number: 7
Largest = 20
Smallest = 7
Middle = 10

'''










































