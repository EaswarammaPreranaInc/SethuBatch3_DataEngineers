#  Find  outputs  (Home  work)
def change(b):
    b.append(25)
    b[2] = 17
    del b[1]
# End of the function
a = [10, 20, 15, 18]
print(a)        # [10, 20, 15, 18]
change(a)
print(a)        # [10, 17, 18, 25]


def change(b):
    b = [50, 60, 70, 80]
    print(b)        # [50, 60, 70, 80]
# End of the function
a = [10, 20, 30, 40]
print(a)            # [10, 20, 30, 40]
change(a)
print(a)            # [10, 20, 30, 40]



def f1(x):
    x = 20
    print(x)        # 20
# End of the function
x = 10
print(x)            # 10
f1(x)
print(x)            # 10


def f1(b):
    b[2] = 25    # Error due to 'tuple' object does not support item assignment
# End of the function
a = (10, 20, 15, 18)
print(a)        # (10, 20, 15, 18)
f1(a)           # Error occurs here
print(a)        # Not executed


# Find  outputs (Home  work)
square = lambda  x = 10  :    x * x
print(square(5))    #25
print(square())     #100



# Find  outputs  (Home  work)
print((lambda x: x * x)(7))          # 49
print(lambda x: x * x(7))            # <function <lambda> at 0x...>  (prints the lambda function object)
print(lambda x: x * x)               # <function <lambda> at 0x...>  (prints the lambda function object)
print((lambda x=25: x * x)())        # 625
square = lambda x: x * x
print(square(5))                     # 25



print(type(add))             # <class 'function'>
print(add(10, 20))           # 30               (int + int)
print(add(10.6, 20.8))       # 31.4             (float + float)
print(add('Hyder', 'abad'))  # 'Hyderabad'      (string concatenation)
print(add(True, False))      # 1                (True=1, False=0)
print(add(25, 10.8))         # 35.8             (int + float)
print(add(3 + 4j, 5 + 6j))   # (8+10j)          (complex + complex
print(add(10, '20'))         # Error: unsupported operand types for +: 'int' and 'str'
print(add())                 # Error: missing 2 required positional arguments
print(add)                   # <function <lambda> at 0x...> (the function object itself)



add = lambda a=1, b=2: a + b
print(add(10, 20))   # 30
print(add())         # 3   (default a=1, b=2)


print((lambda x, y: x + y)(10, 20))        # 30
print((lambda x, y: x + y)(10.8, 20.6))    # 31.4
print((lambda x, y: x + y)('Hyder', 'abad'))  # 'Hyderabad'
print(lambda x, y: x + y('Hyder', 'abad'))    # Error


#  Find  outputs (Home  work)
#How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10, 20))        # 20           (int comparison)
print(large(10.7, 5.6))     # 10.7         (float comparison)
print(large('g', 's'))      # 's'          (string comparison by Unicode)
print(large('Rama', 'Rajesh'))  # 'Rama'   (string comparison by Unicode: 'Rama' > 'Rajesh')
print(large(True, False))   # True         (True=1, False=0)



#Find outputs (Home work)
power = lambda a=3.5, b=2: a ** b
print(power(2, 3))    # 8       → 2 ** 3
print(power(4.5, 4))  # 410.0625 → 4.5 ** 4
print(power())         # 12.25   → default a=3.5, b=2 → 3.5 ** 2
print(power(9))        # 81      → 9 ** 2 (default b=2)


#Find outputs
all = lambda a, b: (a + b, a - b, a * b, a / b)
x = all(10, 7)
print(type(x))      # <class 'tuple'>
print(x)            # (17, 3, 70, 1.4285714285714286)
p, q, r, s = all(9, 2)
print(p)            # 11
print(q)            # 7
print(r)            # 18
print(s)            # 4.5


#Find outputs
a = lambda: 'Hyd'
print(a())      # 'Hyd' calls the lambda function
print(a)        # <function <lambda> at 0x...> it prints the lambda function object


# Tricky  program
# Find  outputs
a  =  lambda  :  print('Hyd');  print('Sec')  ; print('Cyb')
a()     #Sec
        #Cyb
        #Hyd


#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda s: print(s))                   # <function <lambda> at 0x...>
print(lambda x: print(x)(s))                # Error
print((lambda x: print(x))(s))              # Hyd
(lambda x: print(x))(s)                     # Hyd


# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda y: x + y
x = 10
adder2 = lambda y: x + y
x = 20
adder3 = lambda y: x + y
print(adder1(100))   # ?
x = 30
print(adder2(200))   # ?
x = 40
print(adder3(300))   # ?



#Find outputs (Home work)
a = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
for fun in a:
    print(fun(5))      # 25   → 5 ** 2
    print(fun(5))      # 125  → 5 ** 3
    print(fun(5))      # 625  → 5 ** 4


def f1():
    print('Hyd')
def f2():
    print('Sec')
a = [f1, f2]
for x in a:
    x()            # Hyd
                    # Sec
a = [def f1(): print('Hyd'), def f2(): print('Sec')]
print(a)        # Error due to invalid syntax



a = {
    'power_2': lambda x: x ** 2,
    'power_3': lambda x: x ** 3,
    'power_4': lambda x: x ** 4
}
key = 'power_3'
print(a[key])        # <function <lambda> at 0x...>
print(a )     # 125


# Find outputs (Home work)
def f1(x):
    return lambda n: x ** n
# End of the function
lamb = f1(3)
print(type(f1))        # <class 'function'>          f1 is a regular function
print(type(lamb))      # <class 'function'>          lamb is a lambda function
print(lamb(2))         # 9                           3 ** 2
print(lamb(5))         # 243                         3 ** 5
print(lamb)            # <function f1.<locals>.<lambda> at 0x...>  → the lambda function object
print(lamb())          # Error due to missing 1 required positional argument 'n'



# Find  outputs   (Home  work)
def eval(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
lam = eval(3, 4, 5)
print(lam(2))        # 3*2**2 + 4*2 + 5 = 3*4 + 8 + 5 = 12 + 8 + 5 = 25
print(lam(2.5))      # 3*2.5**2 + 4*2.5 + 5 = 3*6.25 + 10 + 5 = 18.75 + 10 + 5 = 33.75
print(lam(4))        # 3*4**2 + 4*4 + 5 = 3*16 + 16 + 5 = 48 + 16 + 5 = 69


#Nested  lambda  function  (Home  work)
add = lambda x=10: lambda y: x + y
a = add()
print(a(20))          # 30       x=10 (default), y=20     10 + 20
print(add(30)(40))    # 70       x=30, y=40               30 + 40



# Find  output  (Home  work)
add = lambda x: x == 25
print(add(10))        # False      10 == 25?  False
add = lambda x=25: x == 35
print(add())          # False      default x=25   25 == 35?   False
add = lambda x: x = 25      # Error due to cannot use assignment (=) inside a lambda
add = lambda x: x := 25     # Error due to cannot use walrus (:=) in lambda in this context


# Recursive function to find GCD
def gcd(m, n):
    if n == 0:            
        return m
    else:
        return gcd(n, m % n)   
m = int(input('Enter any number  : '))
n = int(input('Enter any number  : '))
print('Gcd :', gcd(m, n))


# Recursive function to find sum of digits
def sod(n):
    if n == 0:                 
        return 0
    else:
        return n % 10 + sod(n // 10)   
n = int(input('Enter any number : '))
print('Sum of the digits :', sod(n))



# Recursive function to find ith Fibonacci term
def fib(i):  
    if i == 0:           
        return 0
    if i == 1:           
        return 1
    return fib(i - 1) + fib(i - 2)   
# Input number of terms
n = int(input('How many terms? : '))
print('Fibonacci series:')
for j in range(n):
    print(fib(j), end=' ')



# Recursive function to calculate a^b
def power(a, b):
    if b == 0:                
        return 1
    if b < 0:                 
        return 1 / power(a, -b)
    return a * power(a, b - 1)   
a = float(input('Enter base : '))
b = int(input('Enter power : '))
print(f'{a} ^ {b} =', power(a, b))



# Recursive function to reverse a number
from math import *
def rev(n):
    if n == 0:                   
        return 0
    else:
        digits = int(log10(n)) + 1  
        return (n % 10) * (10 ** digits - 1) // 10 + rev(n // 10)
n = int(input('Enter any number : '))
print('Reverse Number :', rev(n))