#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b)  # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) #Hyd  is  'green'  city
print('Hyd  is  ' green  '  city')  
---------------------------------------------------

import math
a = eval(input('Enter 1st integer number :  '))
b = eval(input('Enter 2nd integer number :  ')) 
print(F'{a}+{b}={a+b}')
print(F'{a}-{b}={a-b}')
print(F'{a}*{b}={a*b}')
print(F'{a}/{b}={a/b}')
print(F'{a}%{b}={a%b}')
print(F'max({a},{b})={max(a,b)}')
print(F'min({a},{b})={min(a,b)}')
print(F'sqrt{a}={math.sqrt(a)}')
print(F'pow({a},{b})={pow(a,b)}')
print(F'gcd({a},{b})={math.gcd(a,b)}')
print(F'fact{a}={math.factorial(a)}')

--------------------------------------------------

a = eval(input('Enter 1st input :  '))
b = eval(input('Enter 2nd input :  ')) 

c = a if a>b else b
print(F'Largest Input : {c}')

--------------------------------------------------

a = eval(input('Enter 1st input :  '))
b = eval(input('Enter 2nd input :  ')) 
c = eval(input('Enter 3rd input :  '))

d = a if a>b and a>c else b if b>a and b>c else c
print(F'Largest Input : {d}')

--------------------------------------------------

a = eval(input('Enter 1st input :  '))
b = eval(input('Enter 2nd input :  ')) 

c = '>' if a>b else '<' if b>a else '='
print(F'Result : {c}')

--------------------------------------------------

a = eval(input('Enter any number :  '))

b = '1' if a>0 else '-1' if a<0 else '0'
print(F'Result : {b}')

--------------------------------------------------

a = eval(input('Enter any +ve integer :  '))

b = 'Even Number' if a%2==0 else 'Odd Number'
print(b)

