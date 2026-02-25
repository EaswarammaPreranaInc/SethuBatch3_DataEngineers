#1)
x=eval(input("enter 1st complex no :"))
y=eval(input("enter 2nd complex no :"))
print(f"Sum: {x+y}")
print(f"Difference: {x-y}")
print(f"Product: {x*y}")
print(f"Division: ({(x/y)}")

#2)
x=float(input("enter length of rectangle :"))
y=float(input("enter breadth of rectangle :"))
print("Area : ",x*y)
print("Perimeter : ",2*(x+y))

#3)
import math
r=float(input("enter radius : "))
x=4/3*math.pi*r**3
print(f"Volume : ",'%.2f' %x)

#4)
x=float(input("Enter principle :"))
y=float(input("Enter time :"))
z=float(input("Enter rate of interest :"))
a=(x*y*z)/100
b=(x*(1+z/100)**y)-x
print("Simple Interest :",'%.2f' %a)
print("Compound Interest :",'%.2f' %b)

#5)
x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
print(f"Before swap : x='{x}'  y='{y}'")
temp = x
x = y
y = temp
print(f"After  swap : x='{x}'  y='{y}'")

#6)
x = eval(input("Enter 1st input : "))
y = eval(input("Enter 2nd input : "))
print(f"Before swap : x='{x}'  y='{y}'")
x=x+y
y=x-y
x=x-y
print(f"After  swap : x='{x}'  y='{y}'")

#7)
x =int(input("Enter 1st input : "))
y = int(input("Enter 2nd input : "))
print(f"Before swap : x='{x}'  y='{y}'")
x=x*y
y=int(x/y)
x=int(x/y)
print(f"After  swap : x='{x}' y='{y}' ")

#8) Identify  error
else:
 print('else  suite')   # without If statement else statement can't be used
print('Outside')
#9) Identify  error
if  9 > 5
	print('Hello')     #Error bcz if condition does not contains ':' 
print('Bye')   
#10) Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')          # Error bcz else condition does not contains ':'
#11) Identify  error
if  (10,20,15):
print('Hyd')                # Error Bcz improper Indentation 
else:
print('Sec')   
#12)Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')      # Error Bcz improper Indentation
print('Bye')
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
print('Bye')                    # Error bcz braces are not permitted in python

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
print('Bye')                # Error, because there is no proper indentation in nested if conditions, where program should be moved right side 


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a =int(input("Enter the number : "))

if a%2 == 0:
    print("Even Number")
else :
    print("Odd Number")

'''
Enter the number : 56
Even Number
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
Output :
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
Output :
Hyd
Sec
Cyb
Bye
'''
'''
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye
'''

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  
try :
    m = int(input("Enter month number (1-12) : "))

    if m == 1:
        print("January")
    elif m == 2:
        print("Febuary")
    elif m ==3 :
        print("March")
    elif m == 4 :
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
    else :
        print("Input should be between 1 and 12")
except :
    print("Input should be integer value")

    
'''
Output :
Enter month number (1-12) : 8
August
PS D:\SSSSDP\Homeworks> py pr1.py
Enter month number (1-12) : 13.5
Input should be integer value
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

try :
    num = int(input("Enter a digit (0-9) : "))
    
    if num == 0:
        print("Zero")
    else :
        if num == 1:
            print("One")
        else :
            if num == 2:
                print("Two")
            else :
                if num == 3 :
                    print("Three")
                else :
                    if num == 4 :
                        print("Four")
                    else :
                        if num == 5:
                            print("Five")
                        else :
                            if num == 6:
                                print("Six")
                            else :
                                if num == 7 :
                                    print("Seven")
                                else :
                                    if num == 8:
                                        print("Eight")
                                    else :
                                        if num == 9:
                                            print("Nine")
                                        else :
                                            print("Invalid")
except :
    print("Enter a Valid Number")


'''
Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions
'''


try :
    ly = int(input("Enter a year : "))
    
    if (ly % 4 == 0 and ly % 100 != 0):
        print("Leap Year")
    elif(ly % 400 == 0) :
        print("Leap Year")
    else :
        print("Not a leap year")
except :
    print("Enter a valid integer year number")


'''
Output :
Enter a year : 1996
Leap Year
Enter a year : 2029
Not a leap year
'''

'''
Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

Hint:  Write  multiple  conditions
'''

try :
    a = int(input("Enter the 1st input : "))
    b = int(input("Enter the 2nd input : "))
    c = int(input("Enter the 3rd input : "))

    if (a > b and a > c) :
        print("Largest number is : ", a)
    else :
        if (b > a and b > c) :
            print("Largest number is : ", b)
        else :
            print("Largest number is : ", c)
except :
    print("Enter valid integer number")

    
'''
Enter the 1st input : 58
Enter the 2nd input : 96
Enter the 3rd input : 56
Largest number is :  96
'''

'''
Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8
'''


op = int(input("Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : "))

if op == 1 :
    cel = float(input("Enter celsius temperature : "))
    f = 1.8*cel + 32
    print("Farenhit Equivalent : ", f)
else :
    if op == 2 :
        f = float(input("Enter Farenhit temperature : "))
        cel = (f - 32)/1.8
        print("Celsius Equivalent : ",cel)
    else :
        print("Invalid Input")  
                       
                
'''
Output :
Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : 2
Enter Farenhit temperature : 100
Celsius Equivalent :  37.77777777777778
Enter 1 to convert celsius to farenhit or Enter 2 to convert farenhit to celsius : 3
The number should be between only 1 and 2
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

x = float(input("Enter x-coordinate : "))
y = float(input("Enter y-coordinate : "))

if (x > 0 and y > 0) :
    print("1st Quadrant")
elif (x < 0 and y >0):
    print("2nd Quadrant")
elif (x < 0 and y < 0):
    print("3rd Quadrant")
elif (x > 0 and y <0):
    print("4th Quadrant")
elif (x == 0 and y == 0):
    print("It is on Origin")
elif (y == 0 and x != 0) :
    print("Point on x-axis")
elif (x == 0 and y != 0) :
    print("Point on y-axis")


'''
Output :
Enter x-coordinate : -9.6
Enter y-coordinate : 4
2nd Quadrant
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


a = int(input("Enter first input : "))
b = int(input("Enter second input : "))
c = int(input("Enter third input : "))


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

print("Largest Input : ", max)
print("Middle Input : ", mid)
print("Smallest Input : ", min)

'''
Output :
Enter first number: 96
Enter second number: 98
Enter third number: 97
Largest = 98
Middle = 97
Smallest = 96
'''