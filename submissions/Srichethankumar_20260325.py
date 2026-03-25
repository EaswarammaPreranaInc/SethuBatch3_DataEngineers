a = complex(input("enter the first complex numbr :"))
b = complex(input("enter the first complex numbr :"))
sum = a+b
difference = a-b
product = a*b
division = a/b
print(f"sum :{sum}")
print(f"difference :{difference}")
print(f"product:{product}")
print(f"division :{division}")


l = int(input("enter the length :"))
b = int(input("enter the breadth:"))

perimeter = 2*(l+b)
area = l*b
print(f"perimeter : {perimeter}")
print(f"area : {area}")

import math
r = eval(int("enter the radius:"))
volume = 4/3*math.pi*r**3
print(f"volume : {volume:.2f}")



p = float(input("Enter principle : "))
t = float(input("Enter time : "))
r = float(input("Enter rate of interest : "))
SimpleIntrest = (p * t * r) / 100
CompundIntrest = p * (1 + r / 100) ** t - p
print(f"Simple Interest : {SimpleIntrest:.2f}")
print(f"Compound Interest : {CompundIntrest:.2f}")


x =eval(input("enter the 1st input : "))
y= eval(input("enter the 2nd input :"))
print("Before swap:")
print("x =", x)
print("y =", y)
temp = x
x = y
y = temp
print("After swap:")
print("x =", x)
print("y =", y)


x =eval(input("enter the 1st input : "))
y= eval(input("enter the 2nd input :"))
print("Before swap:")
print("x =", x)
print("y =", y)
x = x + y   
y = x - y   
x = x - y   
print("After swap:")
print("x =", x)
print("y =", y)

x =eval(input("enter the 1st input : "))
y= eval(input("enter the 2nd input :"))
print("Before swap:")
print("x =", x)
print("y =", y)
x = x * y   
y = x / y   
x = x / y   
print("After swap:")
print("x =", x)
print("y =", y)



num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")




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




month = int(input("Enter month number (1 - 12): "))
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
    print("Input should be between 1 and 12")





num = int(input("Enter any digit (0 - 9): "))
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



year = int(input("Enter 4-digit year : "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")







a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
else:
    if b >= a and b >= c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)





choice = int(input("Enter 1 to convert celsius to farenheit and 2 to convert fahrenheit to celsius : "))

if choice == 1:
    c = float(input("Enter celsius temperature : "))
    f = 1.8 * c + 32
    print(f"farenheit equivalent : {f:.2f}")

if choice == 2:
    f = float(input("Enter fahrenheit temperature : "))
    c = (f - 32) / 1.8
    print(f"farenheit equivalent : {c:.2f}")






x = float(input("Enter value of x co-ordinate : "))
y = float(input("Enter value of y co-ordinate : "))

if x > 0 and y > 0:
    print("1st quadrant")
elif x < 0 and y > 0:
    print("2nd quadrant")
elif x < 0 and y < 0:
    print("3rd quadrant")
elif x > 0 and y < 0:
    print("4th quadrant")
elif x != 0 and y == 0:
    print("On x-axis")
elif x == 0 and y != 0:
    print("On y-axis")
else:
    print("Origin")





a = float(input("Enter first input : "))
b = float(input("Enter second input : "))
c = float(input("Enter third input : "))
max_val = a
min_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
mid_val = (a + b + c) - (max_val + min_val)
print("Largest input : ", max_val)
print("Smallest input : ", min_val)
print("Middle input : ", mid_val)


