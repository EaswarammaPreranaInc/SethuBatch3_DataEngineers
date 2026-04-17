#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green"city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd is 'green' city
print('Hyd  is  ' green  '  city') # Error
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results

Let  inputs  be  10  and  7,
What  is  the  sum ?  --->  17 
What  is  the  difference ?  --->  3
What  is  the  product ?  --->  70
What  is  the  quotient ?  --->  1.42
What  is  the  remainder ?  ---> 3
What  is  the  largest  number ?  --->  10
What  is  the  smallest  number ?  --->  7
What  is  the  sqrt  of  1st  input ?  --->  3.16
What  is  the  result  of  power ?  --->  10000000
What  is  the  gcd  of  2  numbers ?  --->  1
What  is  the  factorial   of  1st  input ?  --->  10!

import math
a = eval(input("Enter first integer : "))
b = eval(input(Enter second integer : "))

add =a+b
print(F'{a}+{b} = {add}')
sub =a-b
print(F'{a}-{b} = {sub}')
product =a*b
print(F'{a}*{b} = {product}')
quotient = a/b
print(F'{a}/{b} = {quotient:.2}')
rem =a%b
print(F'{a}%{b} = {rem}')
max_val = max(a,b)
print(F'max(a , b) = {max_val}')
min val = min(a,b)
print(F'min(a , b) = {min_val}')
sqr = math.sqrt(a)
print(F'sqrt{a} = {sqr}')
power = math.pow(a,b)
print(F'{a}^{b} = {power}')
gcd = math.gcd(a,b)
print(F'gcd{a , b} = {gcd}')
fact = math.factorial(a)
print(F'factorial ({a}) = {fact}')


program -2

a =eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))

print(F'Before snap : values of a and b are {a , b}')
a,b = b,a
print(F'After snap : values of a and b are {a , b}')


program -3
 
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))

print(F'{a} is the largest among both inputs ') if a>b else print(F'{b}
is the largest among both inputs')



program -4


a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))
c = eval(input("Enter the value of c :"))

print(F'{a} is the largest among three inputs ') if a>b & a>c else print(F'{b}
is the largest among three inputs ') if b>a&b>c else print(F'{c} is the largest among three inputs ')


program -5
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))
result + '>> if a > b else '," if a < b else '='
print (result)

program -6

a = eval(input(Enter the value of a:"))
print("+1") if a>0 else print("-1)if a<0 else print("0")


program-7

a = eval(input("Enter the value of a :"))
print(F'{a} is even')if a%2==0 else print(F'{a} is odd')


