# -----------------------------------------
# Find outputs

a = 10
b = 7
x = lambda a, b: a + b, a - b, a * b, a / b

print(type(x))
print(x)

for y in x:
    print(y)

print(x[0](9, 2))
print(x[1])
print(x())

# -------- OUTPUT --------
<class 'tuple'>
(<function <lambda> at 0x...>, 3, 70, 1.4285714285714286)

<function <lambda> at 0x...>
3
70
1.4285714285714286

11
3
TypeError: 'tuple' object is not callable


# -----------------------------------------
# Find outputs

a = lambda: print('Hyd'); print('Sec'); print('Cyb')
print(a())

# -------- OUTPUT --------
Sec
Cyb
Hyd
None


# -----------------------------------------
# Find outputs

a = lambda: 'Hyd'; print('Sec'); print('Cyb')
print(a())

# -------- OUTPUT --------
Sec
Cyb
Hyd


# -----------------------------------------
# Find outputs

a = lambda: print('Hyd'), print('Sec'), print('Cyb')

print(type(a))
print(a)

for x in a:
    print(x)

a()
print(a[0]())

# -------- OUTPUT --------
<class 'tuple'>
(<function <lambda> at 0x...>, None, None)

<function <lambda> at 0x...>
None
None

TypeError: 'tuple' object is not callable

Hyd
None