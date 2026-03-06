x = int(input("Enter value: "))

a = 0
b = 1

while a <= x:
    print(a, end=" ")
    c = a + b
    a = b
    b = c


    nums = [10, 20, 15, 18]

for n in nums:
    print(n)

    s = "Hyd"

for ch in s:
    print(ch)

for i in range(5):
    print(i)



print("1) Dictionary Outputs")

d = {10: 20, 30: 40, 50: 60}

print("Keys:")
for x in d.keys():
    print(x)

print("\nValues:")
for x in d.values():
    print(x)

print("\nItems:")
for x in d.items():
    print(x)

print("\nDirect iteration (same as keys):")
for x in d:
    print(x)



print("\n2) Unpacking items()")

a = {10: 20, 30: 40, 50: 60}

print("\nCorrect way:")
for x, y in a.items():
    print(x, y, sep='...')

print("\nError examples below (commented to avoid crash)")


print("\n3) Identify Error")



print("\n4) Empty Iterations")

for x in ():
    print(x)

for x in []:
    print(x)

for x in {}:
    print(x)

for x in set():
    print(x)

for x in '':
    print(x)

for x in range(10, 10):
    print(x)

print("\n5) Nested Loop")

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
    print("Hello")
print("Bye")


print("\n6) Element with Index")

a = [25, 10.8, 'Hyd', True]

print("Index based loop:")
for i in range(len(a)):
    print(i, a[i])

print("\nFor-each loop using enumerate:")
for index, value in enumerate(a):
    print(index, value)



print("\n7) Reverse List")

print("Index based reverse:")
for i in range(len(a) - 1, -1, -1):
    print(a[i])

print("\nFor-each reverse (no slice):")
for x in reversed(a):
    print(x)


print("\n8) Add Two Lists")

a = [10, 20, 15, 18]
b = [30, 40, 35, 12, 100]
c = []

for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])


print("\n9) Index 2 to 4")

a = [25, 10.8, 'Hyd', True, 3+4j, None, 'Sec']

for i in range(2, 5):
    print(a[i])



print("\n10) Tricky Program")

a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1
print("a:", a)

b = [10, 20, 15, 18]
for x in b:
    x += 1
print("b:", b)


# 
print("\n11) Full Pyramid")

n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


print("\n12) First 20 Even Numbers")

i = 1
count = 0
while count < 20:
    print(2 * i)
    i += 1
    count += 1


print("\n13) Error Example")

print("\n14) Break Example")

for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        break
    else:
        print("Sec")
    print("Hello")

print("Outside loop")

