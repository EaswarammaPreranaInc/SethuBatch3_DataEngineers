# ============================================================
# 1) Print Uppercase and Lowercase Alphabets
# ============================================================

# Uppercase A-Z
for i in range(65, 91):
    print(chr(i), end=" ")
print()

# Lowercase a-z
for i in range(97, 123):
    print(chr(i), end=" ")
print()

# Output:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# a b c d e f g h i j k l m n o p q r s t u v w x y z


# ============================================================
# 2) Print first n terms of Fibonacci series
# ============================================================

n = 6
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# Output:
# 0 1 1 2 3 5


# ============================================================
# 3) Search for x in Fibonacci series (without generating series)
# ============================================================

import math

x = 21

def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s * s == n

if isPerfectSquare(5*x*x + 4) or isPerfectSquare(5*x*x - 4):
    print("Found")
else:
    print("Not found")

# If x = 10  -> Not found
# If x = 21  -> Found


# ============================================================
# 4) Find Outputs (continue example)
# ============================================================

for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print("Sec")
    print("Hello")
else:
    print("else suite")

print("Outside loop")

# Output:
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# 7
# Sec
# Hello
# else suite
# Outside loop


# ============================================================
# 5) Find Outputs (break condition)
# ============================================================

for i in range(1, 8):
    print(i)
    if i == 8:
        break
    else:
        print("Sec")
    print("Hello")
else:
    print("else suite")

print("Outside loop")

# Output:
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# Sec
# Hello
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# Sec
# Hello
# 7
# Sec
# Hello
# else suite
# Outside loop


# ============================================================
# 6) Search element in list (no duplicates)
# ============================================================

lst = [10, 20, 15, 12, 18]
x = 15

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        break
else:
    print("Not found")

# If x = 15 -> Found at index 2
# If x = 19 -> Not found


# ============================================================
# 7) Search element and count occurrences
# ============================================================

lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = 15
count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print("15 is found at index", i)
        count += 1

if count > 0:
    print("15 is found", count, "times")
else:
    print("Not found")

# Output:
# 15 is found at index 2
# 15 is found at index 5
# 15 is found at index 8
# 15 is found 3 times


# ============================================================
# 8) Walrus Operator Demo
# ============================================================

print(a := 25)      # 25
print(a)            # 25
print(a := 6 + 7)   # 13
print(a)            # 13
print((a := 6) + 7) # 13
print(a)            # 6

# print(a = 25)     # SyntaxError
# print((a = 6)+7)  # SyntaxError


# ============================================================
# 9) if conditions with == , := , =
# ============================================================

a = 0
if a == 0:
    print("Hyd")
else:
    print("Sec")

if b := 0:
    print("Hyd")
else:
    print("Sec :", b)

# if c = 0:   # SyntaxError


# Output:
# Hyd
# Sec : 0


# ============================================================
# 10) Average of inputs terminated with Ctrl+Z
# ============================================================

total = 0
count = 0

try:
    while True:
        x = eval(input())
        total += x
        count += 1
except EOFError:
    pass

if count > 0:
    print("Average =", total / count)

# Example:
# 25
# 10.8
# True
# Ctrl+Z
# Average = 12.266666666666667


# ============================================================
# 11) del operator demo
# ============================================================

a = 25
print(a)      # 25
del a
# print(a)    # NameError


# ============================================================
# 12) del with multiple variables
# ============================================================

a = b = c = 25
print(a, b, c)   # 25 25 25
del a
print(b, c)      # 25 25
# print(a)       # NameError


# ============================================================
# 13) del multiple objects together
# ============================================================

a, b, c = 25, 10.8, "Hyd"
print(a, b, c)   # 25 10.8 Hyd
del a, b, c
# print(a)       # NameError


# ============================================================
# 14) del with list
# ============================================================

a = [10, 20, 15, 18]
print(a)       # [10, 20, 15, 18]
del a[2]
print(a)       # [10, 20, 18]
del a
# print(a)     # NameError


# ============================================================
# 15) del with tuple
# ============================================================

a = (10, 20, 15, 18)
print(a)       # (10, 20, 15, 18)
print(a[0])    # 10
# del a[2]     # TypeError
del a
# print(a)     # NameError
print(a[0])    # type error