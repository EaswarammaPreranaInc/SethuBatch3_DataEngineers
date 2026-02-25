"""Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input
import math
a = eval(input("Enter the Values"))
b = eval(input("Enter the Values"))
print(f' {a} + {b} = {a + b}')
print(f' {a} - {b} = {a - b}')
print(f' {a} * {b} = {a * b}')
print(f' {a} / {b} = {a / b}')
print(f' {a} % {b} = {a % b}')
print(f'Max({a},{b}) = ' , max(a,b))
print(f'Min({a},{b}) = ' , min(a,b))
print(f'{a} ^ {b} =' , pow(a,b))
print(f'sqrt({a}) = ', math.sqrt(a))
print(f"gcd ({a}, {b}))= ", math.gcd(a,b))
print(f'fact({a}) = ', math.factorial(a))

a = eval(input("Enter the Values"))
b = input("Enter the Values")
print("Before Swap : x = ", a)
a , b = b , a
print("After  Swap : x = " , a)

#Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function
a = eval(input("Enter the Values"))
b = eval(input("Enter the Values"))

print(f'Largest Number :',a if a > b else b)


a = eval(input("Enter the Values"))
b = eval(input("Enter the Values"))
c = eval(input("Enter the Values"))

print(f'Largest Number :',a if a > b else b if a > c else c)

a = eval(input("Enter the Values"))
b = eval(input("Enter the Values"))

print(f'Result :','>' if a > b else '<' if a < b else '=')

a = eval(input("Enter the Values"))


print(f'Result :','+' if a > 0 else '-' if a < 0 else '0')"""


a = eval(input("Enter the Values"))


print('Even Number' if a%2 == 0 else 'Odd Number' )