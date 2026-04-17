#  Find outputs  (Home  work)
a = 'Hyd  is  green  city'
print(a) #  Hyd  is  green  city
b = 'Hyd  is  "green"  city'
print(b) # Hyd  is  “green “ city
c = 'Hyd  is  \'green\'  city'
print(c) # Hyd  is  ‘green ‘ city
print('Hyd  is  ' green  '  city') # Error 

program -1
import math
a = eval(input("Enter first integer : "))
b = eval(input("Enter second integer : "))

add = a+b
print(F'{a}+{b} = {add}')
sub = a-b
print(F'{a}-{b} = {sub}')
product = a*b
print(F'{a}*{b} = {product}')
quotient = a/b
print(F'{a}/{b} = {quotient:.2}')
rem = a%b
print(F'{a}%{b} = {rem}')
max_val = max(a,b)
print(F'max(10 , 7) = {max_val}')
min_val = min(a,b)
print(F'min{a , b} = {min_val}')
sqr = math.sqrt(a)
print(F'sqrt{a} = {sqr}')
power = math.pow(a,b)
print(F'{a}^{b} = {power}')
gcd = math.gcd(a,b)
print(F'gcd{a , b} = {gcd}')
fact = math.factorial(a)
print(F'factorial ({a}) = {fact}')

program -2
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))

print(F'Before snap : values of a and b are {a , b}')
a,b = b,a
print(F'After snap : values of a and b are {a , b}')

Program - 3
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))

print(F'{a} is the largest among both inputs ') if a>b else print(F'{b} is the largest among both inputs')





Program - 4
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))
c = eval(input("Enter the value of c :"))

print(F'{a} is the largest among three inputs ') if a>b & a>c else print(F'{b} is the largest among three inputs ') if b>a&b>c else print(F'{c} is the largest among three inputs ')

Program – 5 
a = eval(input("Enter the value of a :"))
b = eval(input("Enter the value of b :"))
result = '>' if a > b else '<' if a < b else '='
print(result)

Program - 6
a = eval(input("Enter the value of a :"))
print("+1") if a>0 else print("-1") if a<0 else print("0") 

Program-7

a = eval(input("Enter the value of a :"))
print(F'{a} is even')if a%2==0 else print(F'{a} is odd')



