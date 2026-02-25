a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city <next line>
b = 'Hyd  is  "green"  city'
print(b) # prints Hyd  is  "green"  city <next line>
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  \'green\'  city
# print('Hyd  is  ' green  '  city') # error as word green is not in any quotes to print

import math


try:
    x  = eval(input('Enter 1st integer number :'))
    print(x)
except:
    print('Please Enter a Integer')

try:
    y  = eval(input('Enter 2nd integer number :'))
    print(y)
except:
    print('Please Enter a Integer')

print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y}')
print(f'{x} % {y} = {x % y}')
print(f'max({x},{y}) = {max(x, y)}')
print(f'min({x},{y}) = {min(x, y)}')
print(f'pow({x},{y}) = {math.pow(x, y)}')
print(f'sqrt({x}) = {math.sqrt(x)}')
print(f'gcd({x},{y}) = {math.gcd(x,y)}')
print(f'fact({x}) = {math.factorial(x)}')


i = eval(input('Enter 1st input'))
j = (input('Enter 2nd input'))
print(f'Before Swap : i = {i} \t j = {j} ')
i,j = j,i
print(f'After Swap : i = {i} \t  j = {j}')


a = eval(input('Enter 1st input :'))
b = eval(input('Enter 2nd input :'))
max_int = (a if a>b else b)
print(f'Largest Input : {max_int}')

a = input('Enter 1st input :')
b = input('Enter 2nd input :')
c = input('Enter 3rd input :')
max_element = a if (a>b and a>c)  else (b if b>c else c)
print(f'Largest Input :{max_element}')


a = input('Enter 1st input :')
b = input('Enter 2nd input :')
Result = '>' if a > b else '<'
print(f'{Result}')


a = eval(input('Enter 1st input :'))
Result = 1 if a > 0 else (-1 if a < 0 else 0)
print (f'Result = {Result}')


try:
    a = int(input('Enter any +ve integer :' ))
except:
    print('Please enter a number')
Number = 'Even Number' if a%2 == 0 else 'Odd Number'
print(f'{Number}')