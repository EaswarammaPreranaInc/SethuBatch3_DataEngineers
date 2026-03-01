 1.#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a)  # Hyd is green city
b = 'Hyd  is  "green"  city'
print(b) # Hyd is "green" city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city
print('Hyd  is  ' green  '  city') # Error --> Invalid syntax

-------------------------------------------------------------------------------------------------------------
2.
import math

# Taking inputs
a = int(input("Enter 1st  integer  number : 10 ")) # 10
b = int(input("Enter 2nd  integer  number :  7")) # 7

# Operations
print(f"{a} + {b} = {a + b}") # 10 + 7 = 17
print(f"{a} - {b} = {a - b}") # 10 - 7 = 3
print(f"{a} * {b} = {a * b}") #  10 * 7 = 70
print(f"{a} / {b} = {a / b}") #  10 / 7 = 1.4285714285714286
print(f"{a} % {b} = {a % b}") # 10 % 7 = 3
print(f"max({a} , {b}) = {max(a, b)}") # max(10,7) = 10
print(f"min({a} , {b}) = {min(a, b)}") # min(10,7) = 7
print(f"{a} ^ {b} = {a ** b}") # 10 ^ 7 = 10000000
print(f"sqrt({a}) = {math.sqrt(a)}") # sqrt(10) = 3.1622776601683795  
print(f"gcd({a} , {b}) = {math.gcd(a, b)}") # gcd(10 , 7) = 1
print(f"fact({a}) = {math.factorial(a)}") # fact(10) = 3628800
-------------------------------------------------------------------------------------------------------------
3.
 # Taking inputs
x = eval(input("Enter  1st  input  :  "))
y = eval(input("Enter  2nd  input  :  "))
print(f"Before  swap  :   x={x!r}        y={y!r}")
# Single statement swap
x, y = y, x
print(f"After   swap  :   x={x!r}        y={y!r}")

o/p:--- Enter  1st  input  :  25
           Enter  2nd  input  :  'Hyd'
           Before  swap  :   x=25        y='Hyd'
           After   swap  :   x='Hyd'     y=25
-------------------------------------------------------------------------------------------------------------
4. # Taking inputs
  a = eval(input("Enter 1st input :  "))
  b = eval(input("Enter 2nd input: "))

   #using ternary operator
 largest = a if a > b else b
 
 print(f"Largest  Input  :  {largest}")

o/p:-- Enter  1st  input  :  10
         Enter  2nd  input  :  20.8
         Largest  Input  :  20.8
-------------------------------------------------------------------------------------------------------------
5.
 # Read three inputs
a = eval(input("Enter first input  : "))
b = eval(input("Enter second input : "))
c = eval(input("Enter third input  : "))

# Nested ternary operator
largest = a if a > b and a > c else (b if b > c else c)

print("Largest value :", largest)

output:---
 Enter 1st input : 'RAMA'
 Enter 2nd input :'RAKESH'
 Enter 3rd input : 'RAJESH'
 Largest value : RAMA
-------------------------------------------------------------------------------------------------------------
6.
# Read two inputs
a = eval(input("Enter first input  : "))
b = eval(input("Enter second input : "))

# Nested ternary operator
result = '>' if a > b else ('<' if a < b else '=')

print(result)

output:---Enter first input : 20
              Enter second input : 30 
	result : <
-------------------------------------------------------------------------------------------------------------
7.
# Read input
a = eval(input("Enter a number : "))

# Nested ternary operator
result = 1 if a > 0 else (-1 if a < 0 else 0)

print(result)

output:--- Enter a number : 75
               result : 1
-------------------------------------------------------------------------------------------------------------
8.
# Read input
n = int(input("Enter a number : "))

# Ternary operator
result = "Even Number" if n % 2 == 0 else "Odd Number"

print(result)

output:--- Enter a number : 24
                result : Even Number

