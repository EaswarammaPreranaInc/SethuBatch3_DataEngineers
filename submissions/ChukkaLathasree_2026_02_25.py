a = eval(input('Enter 1st complex number: '))
b = eval(input('Enter 2nd complex number: '))
print(f'sum: {a + b}')
print(f'diff: {a - b}')
print(f'product: {a * b}')
print(f' division: {a / b}')



length = float(input('Enter length of rectangle: '))
breadth = float(input('Enter breadth of rectangle: '))
area = length * breadth
perimeter = 2 *(length + breadth)
print("area :", area )
print("perimeter :", perimeter )

import math
radius = float(input('Enter volume of a sphere: '))
volume = float(input('Enter volume of a sphere: '))
volume = (4/3)* math.pi * (radius**3)
print("volume of sphere: ", radius)
print("radius of sphere: ", volume )

principle = float(input('Enter principle amount: '))
time = float(input('Enter time (in years): '))
rate  = float(input('Enter rate of intrest: '))
simple_intrest = principle*time* rate / 100
compound_intrest = principle*(1 + rate   / 100)** time-principle
print("simple_intrest: ", simple_intrest )
print("compound_intrest: ", compound_intrest )

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f'before swap: {x=}   {y=}')
z = x , y = y,x
print(f'after swap: {x=}   {y=}')

x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f'before swap: {x=}   {y=}')
x = x*y
y = x/y
y = x/y
print(f'after swap: {x=}   {y=}')


x = input("Enter 1st input: ")
y = input("Enter 2nd input: ")
print(f'before swap: {x=}   {y=}')
x = x+y
y = x-y
y = x-y
print(f'after swap: {x=}   {y=}')

# Identify  error
else:
		print('else  suite')
print('Outside')---> # there is no if condition else does not there in prgm

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')---> more space indentation error

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')---> for else colon is  manadatory.

# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')---> # after if cond there should be a space or tab key

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')---> # more space indentation error

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
print('Bye')---> Empty dict error

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
print('Bye')---> # Empty set error

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')----> # 'One'
                    'Two'
                    'Three'
                     'Bye'
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')---> 'Hyd'
                 'Sec'
                 'Cyb'
                 'Bye'

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') ---> 'Hyd'
                 'Sec'
                 'Cyb'
                 'Bye' 
