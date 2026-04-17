import math
# Inputs
a = int(input("Enter 1st  integer  number :  "))
b = int(input("Enter 2nd  integer  number :  "))

# Operations
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")

print(f"max({a} , {b}) = {max(a,b)}")
print(f"min({a} , {b}) = {min(a,b)}")

print(f"{a} ^ {b} = {a ** b}")
print(f"sqrt({a}) = {math.sqrt(a)}")
print(f"gcd({a} , {b}) = {math.gcd(a,b)}")
print(f"fact({a}) = {math.factorial(a)}")





# Swapping two refferences

x = input("Enter  1st  input :  ")
y = input("Enter  2nd  input :" "")

print(f"Before swap :{x!r}  y={y!r}")

x, y = y, x
print(f"After swap :x={x!r}  y={y!r}")


# Program to find largest of Three inputs using ternary operator

a = eval(input("Enter first input  :  "))
b = eval(input("Enter second input :  "))
c = eval(input("Enter third input :  "))

largest = a if a > b else b and b if b > c else c

print(f"Largest = {largest!r}")


# Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,'<'  if  1st  input  <  2nd  input  and'='  if  inputs  are  same


a = eval(input("Enter first input  :  "))
b = eval(input("Enter second input :  "))

Result = ">" if a>b else "<" and "<" if a<b else "="
print("Result  :  ", Result)

# Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

a=int(input("Enter any integer: "))
result = 1 if a>0 else -1 and -1 if a<0 else 0
print("result: ",result)


#   Write  a  program  to  test  input  is  even  number  or  odd  number
a=int(input("Enter +ve number: "))

result = 'Enter +ve number only' if a<0 else ('Even Number'  if a%2==0 else 'Odd Number')
print("result: ",result)