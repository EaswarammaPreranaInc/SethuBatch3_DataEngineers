Problem-1
a= eval(input("enter first complex number :"))
b =  eval(input("enter second complex number :"))
print(F'{a}+{b} = {a+b}')
print(F'{a}-{b} = {a-b}')
print(F'{a}*{b} = {a*b}')
print(F'{a}/{b} = {a/b:.2}')

Problem-2
length = int(input("enter the length of rectangle : "))
breadth = int(input("enter the breadth of rectangle : "))

area = length*breadth
perimeter = 2*(length+breadth)

result = (F'Area of the triangle = {area} \n'F'Perimeter of the triangle = {perimeter}')

print(result)

Problem-3
import math
radius = int(input("Enter the radius of sphere : "))

Volume = 4/3 * math.pi * math.pow(radius,3)  

print(F'Volume of the sphere = {Volume:.2f}')


Problem-4

principle = float(input("enter the principle : "))
rate_of_interest =  float(input("enter the interest : "))
time =  float(input("enter the time period: "))

simple_interest = principle*rate_of_interest*time/100

compound_interest = principle*(1+rate_of_interest/100)**time-principle

result = print(F'The simple interest is {simple_interest} \n' F'The compound interest is {compound_interest}'  )

Problem-5
try : 
    a=eval(input("enter a value : "))
    b=eval(input("enter a value : "))
    temp=a
    a=b
    b=temp
    print(a,b)

except :
    print("if it is a string then enter in quotes  ")




Problem-6
x = int(input("Enter the value x : "))
y=int(input("Enter the value of y: "))

x=x+y
y=x-y
x=x-y
print(x,y)

Problem-7

x = int(input("Enter the value x : "))
y=int(input("Enter the value of y: "))

x=x*y
y=x//y
x=x//y
print(x,y)


# else:
#         print('else  suite')
# print('Outside') Error else without if

if  9 > 5
    print('Hello')
print('Bye') # Error no colon after if statement 

if  9 > 12:
    print('Hyd')
else
    print('Sec') # Error no colon after else

if  (10,20,15):
print('Hyd')
else:
print('Sec') # Error indentation

if  ():
            print('Hyd')
    else:
                    print('Sec')
print('Bye') # Error indentation 

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
print('Bye') # syntax error

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
print('Bye') # Empty tuple, no correct nesting and indentation errors







Problem-8

try:
    a=int(input("Enter integer value of a :"))
    if a%2==0:
        print(F'{a} is even')
except NameError:
    print("Enter only integer values")

if ():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') #One
Two
Three
Bye







if {10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd
Sec
Cyb
Bye

if { }:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Bye

Problem-9

try:
    a = int(input("Enter a number in between 1-12: "))

    if a == 1:
        print("January")
    elif a == 2:
        print("February")
    elif a == 3:
        print("March")
    elif a == 4:
        print("April")
    elif a == 5:
        print("May")
    elif a == 6:
        print("June")
    elif a == 7:
        print("July")
    elif a == 8:
        print("August")
    elif a == 9:
        print("September")
    elif a == 10:
        print("October")
    elif a == 11:
        print("November")
    elif a == 12:
        print("December")
    else:
        print("Number should be in range of 1-12")

except ValueError:
    print("Please enter a valid number")







Problem-10

n = int(input("Enter a digit (0–9): "))

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

Problem-11

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

Problem-12

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print("Largest =", a)
    else:
        print("Largest =", c)
else:
    if b > c:
        print("Largest =", b)
    else:
        print("Largest =", c)

Problem -13

temp = float(input("Enter temperature: "))
choice = input("Enter C for Celsius or F for Fahrenheit: ")

if choice == 'C':
    f = 1.8 * temp + 32
    print("Fahrenheit =", f)
else:
    c = (temp - 32) / 1.8
    print("Celsius =", c)

Problem -14

temp = float(input("Enter temperature: "))
choice = input("Enter C for Celsius or F for Fahrenheit: ")

if choice == 'C':
    f = 1.8 * temp + 32
    print("Fahrenheit =", f)
else:
    c = (temp - 32) / 1.8
    print("Celsius =", c)

Problem-15

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

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

print("Largest =", max)
print("Smallest =", min)
print("Middle =", mid)


