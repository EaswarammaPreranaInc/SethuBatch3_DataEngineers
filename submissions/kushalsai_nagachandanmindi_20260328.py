#Find outputs (Home work)
def change(b):
    b.append(25)
    b[2] = 17
    b.pop(1) # Note: 'del b[1]' is used in your snippet; both modify the original list
# End of the function
a = [10, 20, 15, 18]
print(a) # [10, 20, 15, 18]
change(a)
print(a) # [10, 17, 18, 25]


#Find outputs (Home work)
def change(b):
    b = [50, 60, 70, 80] # This creates a NEW local 'b', doesn't affect 'a'
    print(b) # [50, 60, 70, 80]
# End of the function
a = [10, 20, 30, 40]
print(a) # [10, 20, 30, 40]
change(a)
print(a) # [10, 20, 30, 40]


#Find outputs (Home work)
def f1(x):
    x = 20 # Local assignment
    print(x) # 20
# End of the function
x = 10
print(x) # 10
f1(x)
print(x) # 10


#Find outputs (Home work)
def f1(b):
    b[2] = 25 # Error as 'tuple' object does not support item assignment
# End of the function
a = (10, 20, 15, 18)
print(a) # (10, 20, 15, 18)
f1(a) # ERROR as Tuples are immutable and cannot be changed.
print(a)


#Find outputs (Home work)
square = lambda x=10: x * x
print(square(5)) # 25
print(square()) # 100


#Find outputs (Home work)
print((lambda x: x * x)(7)) # 49
print(lambda x: x * x(7)) # <function <lambda> at ...> (Returns function object, doesn't execute)
print(lambda x: x * x) # <function <lambda> at ...>
print((lambda x=25: x * x)()) # 625
square = lambda x: x * x
print(square(5)) # 25


#Find outputs (Home work)
add = lambda x, y: x + y
print(type(add)) # <class 'function'>
print(add(10, 20)) # 30
print(add(10.6, 20.8)) # 31.4
print(add('Hyder', 'abad')) # Hyderabad
print(add(True, False)) # 1 (True is 1, False is 0)
print(add(25, 10.8)) # 35.8
print(add(3 + 4j, 5 + 6j)) # (8+10j)
print(add(10, '20')) # Error as unsupported operand type(s) for +: 'int' and 'str'
print(add()) # Error as missing 2 required positional arguments


#Find outputs (Home work)
add = lambda a=1, b=2: a + b
print(add(10, 20)) # 30
print(add()) # 3


#Find outputs (Home work)
print((lambda x, y: x + y)(10, 20)) # 30
print((lambda x, y: x + y)(10.8, 20.6)) # 31.4
print((lambda x, y: x + y)('Hyder', 'abad')) # Hyderabad
print(lambda x, y: x + y ('Hyder', 'abad')) # Error as 'str' object is not callable (trying to call 'abad')


#Find outputs (Home work)
large = lambda x, y: x if x > y else y
print(large(10, 20)) # 20
print(large(10.7, 5.6)) # 10.7
print(large('g', 's')) # s
print(large('Rama', 'Rajesh')) # Rama
print(large(True, False)) # True


#Find outputs (Home work)
power = lambda a=3.5, b=2: a ** b
print(power(2, 3)) # 8
print(power(4.5, 4)) # 410.0625
print(power()) # 12.25
print(power(9)) # 81.0


#Find outputs (Home work)
all_math = lambda a, b: (a + b, a - b, a * b, a / b)
x = all_math(10, 7)
print(type(x)) # <class 'tuple'>
print(x) # (17, 3, 70, 1.4285714285714286)
p, q, r, s = all_math(9, 2)
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5


#Find outputs (Home work)
a = lambda: 'Hyd'
print(a()) # Hyd
print(a) # <function <lambda> at ...>


#Tricky program
#Find outputs
a = lambda: print('Hyd'); print('Sec'); print('Cyb') 
# Error as Lambda functions can only contain a single expression.


#Find outputs (Home work)
s = 'Hyd'
print(lambda s: print(s)) # <function <lambda> at ...>
# print(lambda x: print(x) (s)) # Error as 'NoneType' object is not callable
print((lambda x: print(x))(s)) # Hyd \n None (Prints Hyd, then prints the return value of print which is None)
(lambda x: print(x))(s) # Hyd


#Tricky program
#Find outputs
x = 5
adder1 = lambda y: x + y
x = 10
adder2 = lambda y: x + y
x = 20
adder3 = lambda y: x + y
print(adder1(100)) # 120 (Uses current value of x, which is 20)
x = 30
print(adder2(200)) # 230 (Uses current value of x, which is 30)
x = 40
print(adder3(300)) # 340 (Uses current value of x, which is 40)


#Find outputs (Home work)
a = [lambda x: x * 2, lambda x: x * 3, lambda x: x ** 4]
for fun in a:
    print(fun(5)) # 10, 15, 625


#Find outputs
def f1(): print('Hyd')
def f2(): print('Sec')
a = [f1, f2]
for x in a:
    x() # Hyd, Sec
a = [def f1(): print('Hyd')] # Error as 'def' is a statement, cannot be inside a list.


#Find outputs (Home work)
a = {'power_2': lambda x: x ** 2, 'power_3': lambda x: x ** 3, 'power_4': lambda x: x ** 4}
key = 'power_3'
print(a[key]) # <function <lambda> at ...>
print(a[key](5)) # 125


#Find outputs (Home work)
def f1(x):
    return lambda n: x ** n
lamb = f1(3)
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) # 9
print(lamb(5)) # 243
print(lamb) # <function f1.<locals>.<lambda> at ...>
print(lamb()) # Error as missing 1 required argument 'n'


#Find outputs (Home work)
def eval_quad(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval_quad(3, 4, 5)
print(lam(2)) # 25
print(lam(2.5)) # 33.75
print(lam(4)) # 69


#Nested lambda function (Home work)
add = lambda x=10: lambda y: x + y
a = add()
print(a(20)) # 30
print(add(30)(40)) # 70


#Find outputs (Home work)
add = lambda x: x == 25
print(add(10)) # False
add = lambda x=25: x == 35
print(add()) # False
add = lambda x: x = 25 # Error as Assignment not allowed in lambda.
add = lambda x: x := 25 # Error (Needs parentheses in some versions)


'''
Write a recursive function to determine gcd (or) hcf of two numbers

1) gcd(12 , 15) = gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3

2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
'''
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
m = int(input('Enter any number: '))
n = int(input('Enter any number: '))
print('Gcd: ', gcd(m,n))


'''
Write a recursive function to find sum of the digits of a number

sod(678) = 678 % 10 + sod(678 // 10)
         = 8 + sod(67)
         = 8 + 67 % 10 + sod(67 // 10)
         = 8 + 7 + sod(6)
         = 8 + 7 + 6 % 10 + sod(6 // 10)
         = 8 + 7 + 6 + sod(0)
         = 8 + 7 + 6 + 0
         = 21

1) How many function calls are in sod(678) ? --> 4

2) How many function calls are in sod(n-digit number)? --> n + 1
'''
def sod(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sod(n // 10)
n = int(input('Enter any number: '))
print('Sum of the digits: ', sod(n))


'''
Write a recursive function for fibonacci term
Use the function to generate fibonacci series

1) What is the fibonacci series? --> 0 , 1 , 1 , 2 , 3 , 5 , 8 , ......

2) What is the formula for 10th term? --> 9th term + 8th term
   What is the formula for 3rd term? --> 2nd term + 1st term
   What is the formula for ith term? --> (i - 1)th term + (i - 2) term

3) What are the first two terms? --> 0 and 1
'''
def fib(i):
    if i <= 1:
        return 0
    if i == 2:
        return 1
    return fib(i - 1) + fib(i - 2)
n = int(input('How many terms? '))
print('Fibonacci series:', fib(n))

#How to print first 'n' terms of fibonacci series
[print(fib(i), end=' ') for i in range(1, n + 1)]


'''
Write a recursive power function

1) What is the formula for 4.5 ^ 3? --> 4.5 * 4.5 ^ 2

2) What is the formula for 4.5 ^ -3? --> 1 / 4.5 * 4.5 ^ -2

3) What is 4.5 ^ 0? --> 1
'''
def power(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * power(a, b - 1)
    if b < 0:
        return 1 / power(a, -b)
a = float(input('Enter base: '))
b = int(input('Enter power: '))
result = power(a, b)
print(f"{a:g} ^ {b} = {result:g}")
'''
1) power(4.5 , 3) = 4.5 * 4.5 ^ 2 = 91.125

2) power(4.5 , -3) = 1 / 4.5 * 4.5 ^ -2 = 0.0109739

3) How many function calls are in power(a , b)? --> b > 0 then b+1 calls if not b < 0 |b|+2 calls
'''

'''
Write a recursive function to reverse a number

rev(678) = 678 % 10 * 10 ^ 2 + rev(678 // 10)
         = 800 + rev(67)
         = 800 + 67 % 10 * 10 ^ 1 + rev(67 // 10)
         = 800 + 70 + rev(6)
         = 800 + 70 + 6 % 10 * 10 ^ 0 + rev(6 // 10)
         = 800 + 70 + 6 + rev(0)
         = 800 + 70 + 6 + 0
         = 876

1) How many function calls are in rev(678)? -->  4

2) How many function calls are in rev(n-digit number)? --> n + 1

3) How to obtain length of a number? --> len(str(number))
'''
def rev(n):
    if n < 10:
        return n
    return (n % 10) * (10 ** (len(str(n)) - 1)) + rev(n // 10)
n = int(input('Enter any number: '))
print('Reverse Number: ', rev(n))
'''
rev(946) = 649
'''