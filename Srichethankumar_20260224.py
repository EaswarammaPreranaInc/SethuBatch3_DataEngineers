import math


a = int(input("Enter 1st integer number : "))
b = int(input("Enter 2nd integer number : "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")

print(f"max({a} , {b}) = {max(a, b)}")
print(f"min({a} , {b}) = {min(a, b)}")

print(f"{a} ^ {b} = {a ** b}")
print(f"sqrt({a}) = {math.sqrt(a)}")
print(f"gcd({a} , {b}) = {math.gcd(a, b)}")
print(f"fact({a}) = {math.factorial(a)}")