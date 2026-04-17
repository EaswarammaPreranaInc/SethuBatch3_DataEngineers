# Find outputs (Home work)

a = 'Hyd  is  green  city'
print(a)  # Hyd  is  green  city

b = 'Hyd  is  "green"  city'
print(b)  # Hyd  is  "green"  city

c = 'Hyd  is  \'green\'  city'
print(c)  # Hyd  is  'green'  city

# print('Hyd  is  ' green  '  city')  




import math
a = 10
b = 7
print(f"What is the sum ?  --->  {a + b}")                # 17
print(f"What is the difference ?  --->  {a - b}")         # 3
print(f"What is the product ?  --->  {a * b}")            # 70
print(f"What is the quotient ?  --->  {round(a / b, 2)}") # 1.43
print(f"What is the remainder ?  --->  {a % b}")          # 3
print(f"What is the largest number ?  --->  {a if a > b else b}")   # 10
print(f"What is the smallest number ?  --->  {a if a < b else b}")  # 7
print(f"What is the sqrt of 1st input ?  --->  {round(math.sqrt(a),2)}")  # 3.16
print(f"What is the result of power ?  --->  {a ** b}")   # 10000000
print(f"What is the gcd of 2 numbers ?  --->  {math.gcd(a,b)}")  # 1
print(f"What is the factorial of 1st input ?  --->  {math.factorial(a)}")  # 3628800


x = 25
y = 'Hyd'
x, y = y, x   # Swapping references
print(x, y)  # Hyd 25



a = 10
b = 20
largest = a if a > b else b
print(largest)  # 20

a = 35.8
b = 27.9
largest = a if a > b else b
print(largest)  # 35.8

a = 'RAMA'
b = 'RAJESH'
largest = a if a > b else b
print(largest)  # RAMA

a = [10 , 20 , 15 , 18 , 19 , 28]
b = [10 , 20 , 25 , 17]
largest = a if a > b else b
print(largest)  # [10 , 20 , 25 , 17]




a = 10
b = 20
c = 15
largest = a if (a > b and a > c) else (b if b > c else c)
print(largest)  # 20

a = 35.8
b = 42.8
c = 27.9
largest = a if (a > b and a > c) else (b if b > c else c)
print(largest)  # 42.8

a = 'RAMA'
b = 'RAKESH'
c = 'RAJESH'
largest = a if (a > b and a > c) else (b if b > c else c)
print(largest)  # RAMA

a = [10 , 20 , 15 , 18]
b = [10 , 20 , 32 , 19]
c = [10 , 20 , 25 , 17]
largest = a if (a > b and a > c) else (b if b > c else c)
print(largest)  # [10 , 20 , 32 , 19]




a = 10
b = 20
print(">" if a > b else "<" if a < b else "=")  # <

a = 70
b = 60
print(">" if a > b else "<" if a < b else "=")  # >

a = 25
b = 25
print(">" if a > b else "<" if a < b else "=")  # =




num = -25
print(1 if num > 0 else -1 if num < 0 else 0)  # -1

num = 75
print(1 if num > 0 else -1 if num < 0 else 0)  # 1

num = 0
print(1 if num > 0 else -1 if num < 0 else 0)  # 0



num = 10
print("Even" if num % 2 == 0 else "Odd")  # Even

num = 7
print("Even" if num % 2 == 0 else "Odd")  # Odd