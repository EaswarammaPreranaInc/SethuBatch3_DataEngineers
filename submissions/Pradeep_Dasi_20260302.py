# Print uppercase alphabets (A-Z)
print("Uppercase Alphabets:")
for i in range(65, 91):   # ASCII values from 65 to 90
    print(chr(i), end=" ")

print("\n")

# Print lowercase alphabets (a-z)
print("Lowercase Alphabets:")
for i in range(97, 123):  # ASCII values from 97 to 122
    print(chr(i), end=" ")


# Input
n = int(input("Enter the value of n: "))

# First two terms
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


import math

# Input
x = int(input("Enter a number: "))

# Function to check perfect square
def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s * s == n

# A number is Fibonacci if one of these is a perfect square:
# 5*x*x + 4  OR  5*x*x - 4
if is_perfect_square(5*x*x + 4) or is_perfect_square(5*x*x - 4):
    print("Found")
else:
    print("Not Found")


# Find outputs (Home work)

for i in range(1, 8):
    print(i)              # 1 2 3 4 5 6 7
    if i % 3 == 0:
        continue
    else:
        print('Sec')      # Sec Sec Sec Sec Sec
    print('Hello')        # Hello Hello Hello Hello Hello
else:
    print('else  suite')  # else  suite

# End of the loop
print('Outside  loop')    # Outside  loop


# Find outputs (Home work)

for i in range(1, 8):
    print(i)              # 1 2 3 4 5 6 7
    if i == 8:
        break
    else:
        print('Sec')      # Sec Sec Sec Sec Sec Sec Sec
    print('Hello')        # Hello Hello Hello Hello Hello Hello Hello
else:
    print('else  suite')  # else  suite

# End of the loop
print('Outside loop')     # Outside loop



# Given list
lst = [10, 20, 15, 12, 18]

x = int(input("Enter element to search: "))

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        break
else:
    print("Not found")



# Given list
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

x = 15
count = 0

for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1

print(x, "is found", count, "times")



#  Walrus   operator (:=)  demo  program
print(a := 25)
print(a = 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
print((a = 6) + 7)


# Walrus operator (:=) demo program

print(a := 25)        # 25
print(a = 25)         # Error
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
print((a = 6) + 7)



# Find outputs (Home work)

a = 0
if a == 0:
    print('Hyd')          # Hyd
else:
    print('Sec')

if b := 0:
    print('Hyd')
else:
    print('Sec : ', b)    # Sec :  0

if c = 0:                 # Error
    print('Hyd')
else:
    print('Sec')




# Program to find average of inputs terminated by Ctrl + Z

total = 0
count = 0

try:
    while True:
        x = eval(input("Enter value: "))
        total = total + x
        count = count + 1
except EOFError:
    pass

if count > 0:
    print("Average =", total / count)
else:
    print("No inputs given")



# del operator demo program

a = 25
print(a)   # 25
del a
print(a)   # Error



# Find outputs (Home work)

a = b = c = 25   # All three variables point to 25
print(a, b, c)   # 25 25 25

del a            # a is deleted
print(b, c)      # 25 25
print(a)         # Error: a is not defined

del b            # b is deleted
print(c)         # 25
print(b)         # Error: b is not defined

del c            # c is deleted
print(c)         # Error: c is not defined




# Can multiple objects be deleted with same del operator?

a, b, c = 25, 10.8, 'Hyd'  
print(a, b, c)        # 25 10.8 Hyd

del a, b, c           # Deletes all three variables

print(a)              # Error: name 'a' is not defined
print(b)              # Error: name 'b' is not defined
print(c)              # Error: name 'c' is not defined



# Find outputs (Home work)

a = [10, 20, 15, 18]  
print(a)             # [10, 20, 15, 18]

del a[2]             # Deletes element at index 2 (15)
print(a)             # [10, 20, 18]

del a                # Deletes the whole list variable
print(a)             # Error: name 'a' is not defined
print(a[0])          # Error: name 'a' is not defined



# Find outputs (Home work)

a = (10, 20, 15, 18)  
print(a)           # (10, 20, 15, 18)
print(a[0])        # 10

del a[2]           # Error: 'tuple' object doesn't support item deletion

del a              # This line will not execute because program already stops at previous error
print(a)           # Error (would happen if previous line succeeded)
print(a[0])        # Error