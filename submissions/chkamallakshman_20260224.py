a = 'Hyd  is  green  city'
print(a)
b = 'Hyd  is  "green"  city'
print(b)
c = 'Hyd  is  \'green\'  city'
print(c)
print('Hyd  is  ' green  '  city')

1)
import math
num1 = int(input("Enter 1st integer number : "))
num2 = int(input("Enter 2nd integer number : "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"max({num1} , {num2}) = {max(num1, num2)}")
print(f"min({num1} , {num2}) = {min(num1, num2)}")
print(f"{num1} ^ {num2} = {num1 ** num2}")
print(f"sqrt({num1}) = {math.sqrt(num1)}")
print(f"gcd({num1} , {num2}) = {math.gcd(num1, num2)}")
print(f"fact({num1}) = {math.factorial(num1)}")

2)
x=eval(input("enter 1st input:"))
y=eval(input("enter 2nd input:"))
print(f"Before swap: x='{x}' y=\"{y}\"")
x,y=y,x
print(f"After swap: x=\"{x}\" y={y}")

3)
a = eval(input("Enter first input: "))
b = eval(input("Enter second input: "))
largest = a if a > b else b
print("Largest =", largest)

4)
a = eval(input("Enter first input: "))
b = eval(input("Enter second input: "))
c = eval(input("Enter third input: "))
largest = a if (a > b and a > c) else (b if b > c else c)
print("Largest =", largest)

5)
a = eval(input("Enter first input: "))
b = eval(input("Enter second input: "))
result = ">" if a > b else ("<" if a < b else "=")
print(result)

6)
num = int(input("Enter a number: "))
result = 1 if num > 0 else (-1 if num < 0 else 0)
print(result)

7)
num = int(input("Enter a number: "))
result = "Even Number" if num % 2 == 0 else "Odd Number"
print(f"The given number {num} is {result}")



