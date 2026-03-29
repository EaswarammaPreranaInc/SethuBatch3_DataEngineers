# 1
Hyd
<function <lambda> at ...>

# 2
Sec
Cyb
Hyd

# 3
<function <lambda> at ...>
<function <lambda> at ...>
Hyd
Hyd

# 4
120
230
340

# 5
10
15
625

# 6
Hyd
Sec
SyntaxError

# 7
<function <lambda> at ...>
125

# 8
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at ...>
TypeError

# 9
25
33.75
69

# 10
30
70

# 11
False
False
SyntaxError
SyntaxError

# gcd
def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

m = int(input())
n = int(input())
print(gcd(m, n))

# sod
def sod(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sod(n // 10)

n = int(input())
print(sod(n))

# fib
def fib(i):
    if i == 1:
        return 0
    if i == 2:
        return 1
    return fib(i-1) + fib(i-2)

n = int(input())
for i in range(1, n+1):
    print(fib(i), end=" ")

# power
def power(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / power(a, -b)
    return a * power(a, b-1)

a = float(input())
b = int(input())
print(power(a, b))

# reverse
from math import *

def rev(n):
    if n == 0:
        return 0
    else:
        return (n % 10) * (10 ** int(log10(n))) + rev(n // 10)

n = int(input())
print(rev(n))