
print("Uppercase Alphabets:")
for i in range(65, 91):
    print(chr(i), end=" ")

print("\nLowercase Alphabets:")
for i in range(97, 123):
    print(chr(i), end=" ")

print("\n\n=========================================")


n = int(input("Enter n for Fibonacci terms: "))

a = 0
b = 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\n\n=========================================")



import math

x = int(input("Enter number to check Fibonacci: "))

check1 = 5*x*x + 4
check2 = 5*x*x - 4

if int(math.sqrt(check1))**2 == check1 or int(math.sqrt(check2))**2 == check2:
    print("Found in Fibonacci")
else:
    print("Not Found in Fibonacci")

print("\n=========================================")



for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')

print('Outside loop')

print("\n=========================================")



for i in range(1, 8):
    print(i)
    if i == 8:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')

print('Outside loop')

print("\n=========================================")


lst = [10, 20, 15, 12, 18]
x = int(input("Enter number to search in list: "))

found = False

for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not Found")

print("\n=========================================")


lst2 = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = 15

count = 0

for i in range(len(lst2)):
    if lst2[i] == x:
        print(f"{x} is found at index {i}")
        count += 1

print(f"{x} is found {count} times")

print("\n=========================================")



print(a := 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)

print("\n=========================================")



a = 0

if a == 0:
    print('Hyd')
else:
    print('Sec')

if (b := 0):
    print('Hyd')
else:
    print('Sec :', b)

print("\n=========================================")



total = 0
count = 0

try:
    while True:
        val = eval(input("Enter value (Ctrl+Z to stop): "))
        total += val
        count += 1
except EOFError:
    pass

if count > 0:
    print("Average =", total / count)
else:
    print("No inputs given")

print("\n=========================================")



a = 25
print(a)
del a


a, b, c = 25, 10.8, 'Hyd'
print(a, b, c)
del a, b, c


a = [10, 20, 15, 18]
print(a)
del a[2]
print(a)
del a


a = (10, 20, 15, 18)
print(a)
del a