try:
    length = int(input('Enter length of rectangle :'))
    breadth = int(input('Enter breadth of rectangle :'))
except:
    print('Please Enter the correct value')

print(f'Area:{length*breadth}')
print(f'Perimeter:{2*(length+breadth)}')



from math import pi
try:
    radius = int(input('Enter the radius :'))
    volume = int(input('Enter the volume :'))
except:
        print('Please Enter the correct value')
print(f'the  volume  of  sphere : {4/3*pi*radius**3}')

try:
    principle = int(input('Enter the principle :'))
    time = int(input('Enter the time :'))
    rate_of_interest = int(input('Enter the rate_of_interest :'))
except:
    print('Please Enter the correct value')
print(f'Simple Interest : {principle*time*rate_of_interest/100}')
print(f'Compound Interest : {principle*(1 + rate_of_interest/100)**time-principle}')


x = input('Enter 1st input :')
y = input('Enter 2nd input :')
print(f'Before Swap : {x=} \t {y=}')
temp = x
x = y
y = temp
print(f'After Swap : {x=} \t {y=}')

x = eval(input('Enter 1st input :'))#25
y = eval(input('Enter 2nd input :'))#10
print(f'Before Swap : {x=} \t {y=}')
y = x+y # 35
x = y-x # 10
y = y-x # 25
print(f'After Swap : {x=} \t {y=}')


x = eval(input('Enter 1st input :'))#25
y = eval(input('Enter 2nd input :'))#10
print(f'Before Swap : {x=} \t {y=}')
y = x*y # 250
x = y/x # 10
y = y/x # 25
print(f'After Swap : {x=} \t {y=}')


# # Identify  error
# else:
# 		print('else  suite') # there is no if statement
# print('Outside')

# # Identify  error
# if  9 > 5 # there is no colon here
# 	print('Hello')
# print('Bye')


# # Identify  error
# if  9 > 12:
# 	print('Hyd')
# else  # no colon here
# 	print('Sec')
       

#        # Identify  error
# if  (10,20,15):
# print('Hyd') # indentation error as it is not following a tab space after colon
# else:
# print('Sec') # indentation error as it is not following a tab space after colon


# # Identify  error
# if  ():
# 			print('Hyd')
# 	else: # Else indentation is not same as if identation
# 					print('Sec')
# print('Bye')  


# # Identify  error
# if  { }:
# { # there are open braces which are unecessary
# 	print('One')
# 	print('Two')
# 	print('Three')
# } # there are open braces which are unecessary
# else:
# { # there are open braces which are unecessary
# 	print('Four')
# 	print('Five')
# 	print('Six')
# }
# print('Bye')

# there are open braces  which are unecessary


# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:    # identation error
# if  []:  # identation error
# 	print('Four')
# 	print('Five')
# 	print('Six')
# else:   # identation error
# if  {}: # identation error
	print('Seven')
	print('Eight')
	print('Nine')
# else:   # identation error 
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye')
# #


x = int(input('Enter input :'))
if x%2 == 0:
    print('Even Number')
if x%2 != 0:
    print('Odd Number')
    


# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:   # prints else statements as if statment is false as it has empty int
        print('One')
        print('Two')
        print('Three')
print('Bye')



# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: # No error as there is no empty objects in the if statements
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')



try:
    x = int(input('Enter month number (1 - 12) :'))
    if x <= 1 or x >= 12:
        print('Input should be between 1 and 12')
    elif x == 1:
        print('January')
    elif x == 2:
        print('Febraury')
    elif x == 3:
        print('March')
    elif x == 4:
        print('April')
    elif x == 5:
        print('May')
    elif x == 6:
        print('June')
    elif x == 7:
        print('July')
    elif x == 8:
        print('August')
    elif x == 9:
        print('September')
    elif x == 10:
        print('October')
    elif x == 11:
        print('November')
    elif x == 12:
        print('December')
except ValueError:
    print('Input should be integer')



try:
    digit = int(input("Enter a digit (0 - 9): "))
    
    if digit == 0:
        print("Zero")
    else:
        if digit == 1:
            print("One")
        else:
            if digit == 2:
                print("Two")
            else:
                if digit == 3:
                    print("Three")
                else:
                    if digit == 4:
                        print("Four")
                    else:
                        if digit == 5:
                            print("Five")
                        else:
                            if digit == 6:
                                print("Six")
                            else:
                                if digit == 7:
                                    print("Seven")
                                else:
                                    if digit == 8:
                                        print("Eight")
                                    else:
                                        if digit == 9:
                                            print("Nine")
                                        else:
                                            print("Invalid")
except ValueError:
    print('Please enter a Integer')
                                        




try:
    Year = int(input("Enter a 4-digit Year: "))
    if Year%4 == 0 and Year%100 != 0 and Year%400 != 0 :
        print('Leap Year')
    elif Year == 0:
        print('Please enter a 4-digit number')
    else:
        print('Not a Leap Year')
except ValueError:
    print('Please enter a Apropriate year')



x = int(input('Enter a Number :'))
y = int(input('Enter a Number :'))
z = int(input('Enter a Number :'))

if x > y and x > z:
    print(f'{x} is the greatest number')
else:
    if y > z:
        print(f'{y} is the greatest number')
    else:
        print(f'{z} is the greatest number')
        

x = int(input('Enter 1 or 2 :'))
if x!= 1 and x != 2:
    print('Please enter 1 or 2')
else:
    if x == 1:
        temp = int(input('Enter fahranheit temperature : '))
        print(f'Celsius equivalent : {(temp - 32) / 1.8}')
    elif x == 2:
        temp = int(input('Enter celsius temperature: '))
        print(f'Fahranheit equivalent : {1.8 * temp + 32}')
    
        

x = int(input('Enter a Value of x co-ordinate :'))
y = int(input('Enter a Value of y co-ordinate :'))
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x == 0 and y == 0:
    print("Point lies at Origin")

elif x == 0 and y != 0:
    print("Point lies on Y-axis")

elif y == 0 and x != 0:
    print("Point lies on X-axis")

elif x > 0 and y > 0:
    print("Point lies in 1st Quadrant")

elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")

elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")

elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")

    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Step 1: Assume a is max and min
max = a
min = a

# Step 2: Find maximum
if b > max:
    max = b
if c > max:
    max = c

# Step 3: Find minimum
if b < min:
    min = b
if c < min:
    min = c

# Step 4: Find middle
mid = a + b + c - (max + min)

print("Largest =", max)
print("Smallest =", min)
print("Middle =", mid)