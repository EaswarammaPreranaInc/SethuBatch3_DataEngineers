import math

a = float(input('Enter 1st side : '))
b = float(input('Enter 2nd side : '))
c = float(input('Enter 3rd side : '))

# Step 1: Check triangle qualification
if a + b > c and a + c > b and b + c > a:
    
    # Step 2: Check type of triangle (nested if)
    if a == b and b == c:
        print('Equilateral triangle')
        area = (math.sqrt(3) / 4) * (a ** 2)
        print(f'Area: {area:.2f}')
    
    elif a == b or b == c or a == c:
        print('Isosceles triangle')
        perimeter = a + b + c
        print(f'Perimeter: {perimeter}')
    
    else:
        print('Scalene triangle')
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print(f'Area: {area:.2f}')
        print(f'Perimeter: {perimeter}')

else:
    print('Not a triangle')

input('Press any key to continue')


import math

a = float(input('Enter 1st side : '))
b = float(input('Enter 2nd side : '))
c = float(input('Enter 3rd side : '))

# Step 1: Check triangle qualification
if a + b > c and a + c > b and b + c > a:
    
    # Step 2: Check type of triangle (nested if)
    if a == b and b == c:
        print('Equilateral triangle')
        area = (math.sqrt(3) / 4) * (a ** 2)
        print(f'Area: {area:.2f}')
    
    elif a == b or b == c or a == c:
        print('Isosceles triangle')
        perimeter = a + b + c
        print(f'Perimeter: {perimeter}')
    
    else:
        print('Scalene triangle')
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print(f'Area: {area:.2f}')
        print(f'Perimeter: {perimeter}')

else:
    print('Not a triangle')

input('Press any key to continue')


import math

while True:
    try:
        x = float(input("Enter value of x: "))
        y = float(input("Enter value of y: "))
        r = float(input("Enter radius of circle: "))

        if r < 0:
            print("Radius can not be negative")
            input("Press any key to continue")
            continue

        distance = math.sqrt(x*x + y*y)

        if distance > r:
            print("\nPoint is outside the circle")
        elif distance < r:
            print("\nPoint is inside the circle")
        else:
            print("\nPoint is on the circle")

        input("\nPress any key to continue\n")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")


# Find  outputs  (Home  work)
m = 4
match  m:
	case  1:
		print('One')
	case  2:
		print('Two')
	case  3:
		print('Three')
print('Bye') #Bye


# Identify  Error
i = 2
match  i:
	case  1:
		print('One')
	case  _: 
		print('None of   the  above')
	case  2:
		print('Two')
print('Bye') # error



# Find  outputs  (Home  work)
m = 2
match  m:
	case  1:
		print('One')
	case  _:  
		print('Hello')
	case  _:  
		print('Bye')
print('End') #error


#  Find  outputs  (Home  work)
m = 1
match  m:
	case  1:
		print('Hyd') #Hyd
	case  1:
		print('Sec')
	case  1:
		print('Cyb')
print('Bye') #Bye


# Find  outputs  (Home  work)
ch = 'B'
match  ch:
	case   'A':
		print('Apple')
	case  'B':
		print('Book') #Book
	case  'C':
		print('Cafe')
	case  _:
		print('None of  the  above')
print('Bye') #Bye


'''
1) What  are  the  outputs  if  input  is  -6 ? --->
2) What  are  the  outputs  if  input  is  15  ?  --->
3) What  are  the  outputs  if  input  is  10.8  ?  --->
4) What  are  the  outputs  if  input  is  0  ?  --->
5) What  are  the  outputs  if  input  is  -10  ?  --->
6) What  are  the  outputs  if  input  is  7  ?  --->
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:
		print('Hyd')#Hyd
		print('Sec')#Sec
		print('Cyb')#cyb #Bye
	case  -10 | 15:
		print('One') #One
		print('Two') #Two
		print('Three') #Three #Bye
	case  _:
		print('India')# India
		print('China')# China
		print('Usa') #Usa
# End  of  match
print('Bye') #Bye



answer
units = int(input('Enter units : '))
match units:
    
    case u if u <= 100:
        cost = u * 3.00

    case u if u <= 200:
        cost = (100 * 3.00) + ((u - 100) * 3.50)

    case u if u <= 400:
        cost = (100 * 3.00) + (100 * 3.50) + ((u - 200) * 4.00)

    case u if u <= 700:
        cost = (100 * 3.00) + (100 * 3.50) + (200 * 4.00) + ((u - 400) * 4.50)

    case u if u > 700:
        cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 + (u - 700) * 5.00
print('Bill amount :', cost)


#  Find  outputs
while  True:
print('Hello')# Hello hello hello.....
print('Bye') 


#  Find  outputs
while  False:
print('Hello') 
print('Bye') #Bye
