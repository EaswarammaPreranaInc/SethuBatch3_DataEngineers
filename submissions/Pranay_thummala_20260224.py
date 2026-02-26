#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) # Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  "green"  city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  'green'  city
#print('Hyd  is  ' green  '  city') # Error

# Program to perform operations on two numbers
import math
a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))
sum_ = a + b
diff = a - b
prod = a * b
quot = a / b
rem = a % b
largest = max(a, b)
smallest = min(a, b)
power = a ** b
sqrt_a = math.sqrt(a)
gcd_val = math.gcd(a, b)
fact_a = math.factorial(a)
print(f"{a} + {b} = {sum_}")
print(f"{a} - {b} = {diff}")
print(f"{a} * {b} = {prod}")
print(f"{a} / {b} = {quot}")
print(f"{a} % {b} = {rem}")
print(f"max({a} {b}) = {largest}")
print(f"min({a} {b}) = {smallest}")
print(f"{a} ^ {b} = {power}")
print(f"sqrt({a}) = {sqrt_a}")
print(f"gcd({a} , {b}) = {gcd_val}")
print(f"fact({a}) = {fact_a}")

# Swap two objects in a single statement (without 3rd object)
x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")
print(f"Before swap :  x='{x}'    y=\"{y}\"")
x, y = y, x
print(f"After  swap :  x=\"{x}\"    y='{y}'")

# Program to find largest of two inputs
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
largest = a if a > b else b
print(f"Largest Input : {largest}")

# Program to find largest of three inputs
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))
largest = a if (a > b and a > c) else (b if b > c else c)
print(f"Largest Input : {largest}")

# Program to print comparison symbol using nested ternary operator
a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
result = '>' if a > b else ('<' if a < b else '=')
print(f"Result : {result}")

# Program to print 1 (positive), -1 (negative), 0 (zero)
n = eval(input("Enter any number : "))
result = 1 if n > 0 else (-1 if n < 0 else 0)
print(f"Result : {result}")

# Program to check whether a number is Even or Odd
n = int(input("Enter any +ve integer : "))
result = "Even number" if n % 2 == 0 else "Odd number"
print(result)