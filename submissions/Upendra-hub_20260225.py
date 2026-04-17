# First complex number
c1 = 3 + 4j

# Second complex number
c2 = 5 + 6j

print("Sum =", c1 + c2)  # Sum = (8+10j)

print("Difference =", c1 - c2)   # Difference = (-2-2j)

print("Product =", c1 * c2)   # Product = (-9+38j)

print("Division =", c1 / c2)   # Division = (0.639344262295082+0.03278688524590164j)


length = 10
breadth = 5

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area =", area)  # Area = 50

print("Perimeter =", perimeter)  # Perimeter = 30


import math

radius = 7
volume = (4/3) * math.pi * radius**3

print("Volume of Sphere =", volume)   # Volume of Sphere = 1436.755040241732



p = 10000
r = 5
t = 2

si = p * t * r / 100
ci = p * (1 + r/100) ** t - p

print("Simple Interest =", si)   # Simple Interest = 1000.0

print("Compound Interest =", ci)   # Compound Interest = 1025.0



p = 10000
r = 5
t = 2

si = p * t * r / 100
ci = p * (1 + r/100) ** t - p

print("Simple Interest =", si)    # Simple Interest = 1000.0

print("Compound Interest =", ci)    # Compound Interest = 1025.0



x = 10
y = "Hyd"

temp = x
x = y
y = temp

print("x =", x)   # x = Hyd

print("y =", y)   # y = 10


x = 25
y = 10

x = x + y
y = x - y
x = x - y

print("x =", x)    # x = 10

print("y =", y)    # y = 25



x = 25
y = 10

x = x * y
y = x / y
x = x / y

print("x =", x)    # x = 10.0

print("y =", y)    # y = 25.0



else:
	print('else  suite')
print('Outside')	# Error else without if

if  9 > 5
	print('Hello')
print('Bye')	# Error : is missing after if condition


if  9 > 12:
	print('Hyd')
else
	print('Sec')	# Error : is missing after else condition


if  (10,20,15):
print('Hyd')
else:
print('Sec')	#Error indentation is missing with condition statements and block statements

if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')	#Error indentation is missing before else condition



# Identify  error
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
print('Bye')		#Error becoz { } is a empty set so it is false and {}blocks are not used in python only just indentations are mandatory




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
print('Bye')		#Error becoz improper indentation SyntaxError



# print the number is even or odd
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')		# prints One Two Three Bye becoz if condition false due to ( ) empty condition which is false



# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')		#Hyd
			#Sec
			#Cyb
			#Bye




# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')		#Bye becoz empty dictionary which is false



#identifying month name with a number using if else conditions

month = int(input("Enter month number: "))

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
    print("Invalid month")



n = int(input("Enter digit: "))

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




#finding leap year
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("Largest =", c)


choice = input("Type C for Celsius to Fahrenheit, F for Fahrenheit to Celsius: ")
temp = float(input("Enter temperature: "))

if choice == 'C':
    print("Fahrenheit =", 1.8 * temp + 32)
else:
    print("Celsius =", (temp - 32) / 1.8)



x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x != 0 and y == 0:
    print("On X-axis")
elif x == 0 and y != 0:
    print("On Y-axis")
else:
    print("Origin")



a = 10
b = 20
c = 7

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

print("Max =", max)
print("Min =", min)
print("Mid =", mid)