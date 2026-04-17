a = eval(input("Enter first complex number :    "))
b = eval(input("Enter second complex number :   "))
print(F'Sum: {a+b}')
print(F'Difference: {a-b}')
print(F'Product: {a*b}')
print(F'Division: {a/b}')



l= int(input("Enter length of rectangle:   "))
b = int(input("Enter breadth of rectangle:  "))
print(F'Area: {l*b}')
print(F'Perimeter: {2*(l+b)}')


r = eval(input("Enter radius:   "))
import math
print(F'Volume: {4/3*(math.pi)*(pow(r,3))}')



p = int(input("Enter principle:   "))
t = int(input("Enter time:   "))
r = eval(input("Enter rate of interest:  "))
print(F'Simple Interest: {p*t*r/100}')
import math
print(F'Compound Interest: {p*(math.pow(1+r/100,t))-p}')


x = int(input("Enter the value of x co-ordinate:   "))
y = int(input("Enter the value of y co-ordinate:   "))

if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadrant")
elif x<0 and y<0:
    print("3rd quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x==0 and y==0:
    print("origin")
elif x==0:
    print("lies on y-axis")
elif y==0:
    print("lies on x-axis") 


# Identify  error
else:
		print('else  suite') #There is no if statement
print('Outside')


# Identify  error
if  9 > 5 #Error because invalid syntax : is missing
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12: #Evaluuates false and goes to else block
	print('Hyd')
else #error invalid syntax : is missing
	print('Sec')



# Identify  error
if  (10,20,15):
print('Hyd') #Indentation is missing
else:
print('Sec') #Indentatiion is missing



# Identify  error
if  ():
			print('Hyd')
	else: #error due to invalid indentation
					print('Sec')
print('Bye')



# Identify  error
if  { }:  #Error due to there will be no open braces and closed braces 
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
if  (): #Evaluate false because empty tuple
	print('One')
	print('Two')
	print('Three')
else:
if  []: #Evaluate false because empty list
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: #Evaluate false because empty dictionary
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')





# Find outputs  (Home  work)
if(): #Evaluates false because empty tuple
        print('Hyd')
        print('Sec')
        print('Cyb')
else: #prints else block
        print('One') #One
        print('Two') #Two
        print('Three') #Three
print('Bye') #Bye




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: #Evaluates true because it is dictionary and prints the if block and outside the block
        print('Hyd') #Hyd
        print('Sec') #Sec
        print('Cyb') #Cyb
print('Bye') #Bye




# Find outputs  (Home  work)
if { }: #Evaluates false because it is empty dictionary 
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye




x = int(input("Enter 1st input:  "))
y = eval(input("Enter 2nd input:  "))

print("Before swap: x =", x, ", y =", y)
temp = x
x = y
y = temp
print("After swap: x =", x, ", y =", y)




x =  int(input("Enter  1st input:  "))
y =  int(input("Enter 2nd input:   "))
print("Before swap: x =", x, ", y =", y)

x = x+y
y = x-y
x = x-y
print("After swap: x =", x, ", y =", y)




x = int(input("Enter 1st input:  "))
y = int(input("Enter 2nd input:  "))
print("Before swap: x =", x, ", y =", y)
x = x * y
y = x / y
x = x / y
print("After swap: x =", x, ", y =", y )



a = int(input("Enter first input:  "))
b = int(input("Enter second input: "))
c = int (input("Enter third input: "))
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
mid = (a+b+c) - (max + min) 
print(F'Largest input: {max}')
print(F'Smallest input: {min}')
print(F'Middle input: {mid}')



num = int(input("Enter +ve integer:  "))
if (num % 2 == 0):
    print("It is a even number")
if (num % 2 != 0):
    print("It is a odd number")




month_num = int(input("Enter month number (1-12):  "))

if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
else:
    print("Invalid month number")




year = int(input("Enter 4-digit year:  "))

if (year % 4 == 0 and year % 100 !=  0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")




a = int(input("Enter first number:  "))
b = int(input("Enter second number:  "))
c = int(input("Enter third number:  "))

if (a>b and a>c):
    print("The largest number is a")
else:
    if (b>c and b>a):
    
          print("The largest number is b")
    if (c>a and c>b):     
          print("The largest number is c")        




digit = int(input("Enter a digit(0-9):   "))

if digit == 0:
    print("Zero")
if digit == 1:
    print("One")
if digit == 2:
    print("Two")
if digit == 3:
    print("Three")
if digit == 4:
    print("Four")
if digit == 5:
    print("Five")
if digit == 6:
    print("Six")
if digit == 7:
    print("Seven")
if digit == 8:
    print("Eight")
if digit == 9:
    print("Nine")
else:
    if digit < 0 or digit >9:
        print("Invalid")


























