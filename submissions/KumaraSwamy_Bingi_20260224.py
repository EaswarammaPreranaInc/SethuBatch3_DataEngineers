#  Find outputs  (Home  work)
a = 'Hyd  is  green  city' 
print(a) #Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) #Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) #Hyd  is  'green'  city
print('Hyd  is  ' green  '  city') #Error



#program 1:
import math
a = int(input('Enter 1st number: ')) #Enter 1st number: 10
b = int(input('Enter 2nd number: ')) #Enter 2nd number: 7
print('Sum of 2 numbers is: ',f'{a}+{b} = {a+b}') #Sum of 2 numbers is:  17
print('Difference of 2 numbers is: ', f'{a}-{b} = {a-b}') #Difference of 2 numbers is: 3
print('Product of 2 numbers is: ', f'{a}*{b} = {a*b}') #Product of 2 numbers is:  70
print('Quotient of 2 numbers is: ', f'{a}/{b} = {a/b}') #Quotient of 2 numbers is:  1.4285714285714286
print('Remainder of 2 numbers is: ', f'{a}%{b} = {a%b}') #Remainder of 2 numbers is:  3
print('larger number is: ', f'max({a},{b}) = {max(a,b)}') #larger number is:  10
print('Smaller number is: ', f'min({a},{b}) = {min(a,b)}') #Smaller number is: 7
print('squaroot of 1st number is: ', f'sqrt({a}) = {a**0.5}') #square root of 1st number is: 3.1622776601683795
print('power of 1st number to 2nd number is: ', f'{a}**{b} = {a**b}') #power of 1st number to 2nd number is: 100000000
print('gcd of 2 numbers is: ', f'gcd({a},{b}) = {math.gcd(a,b)}') #gcd of 2 numbers is:  1
print('factorial of 1st number is: ',   f'factorial({a}) = {math.factorial(a)}') #factorial of 1st number is:  3628800



#program 2:

x = int(input('Enter 1st number: ')) #Enter 1st number: 10
y = int(input('Enter 2nd number: ')) #Enter 2nd number

x,y = y,x

print(x,y) #Hyd 25



#program 3:

a = eval(input('Enter 1st input: '))
b = eval(input('Enter 2nd input: '))

larger = a if a > b else b

print('Larger input is:', larger)


# program 4:

a = eval(input('Enter 1st input: '))
b = eval(input('Enter 2nd input: '))
c = eval(input('Enter 3rd input: '))

largest = a if (a > b and a > c) else (b if b > c else c)

print('Largest input is:', largest)


#program 5:

a = eval(input('Enter 1st input: '))
b = eval(input('Enter 2nd input: '))

result = '>' if a > b else ('<' if a < b else '=')

print(result)


#program 6:

a = eval(input('Enter input: '))

result = 1 if a > 0 else (-1 if a < 0 else 0)

print(result)


#program 7:

n = int(input('Enter a number: '))

print('Divisible by 2 even number' if n % 2 == 0 else 'Not divisible by 2 odd number')





