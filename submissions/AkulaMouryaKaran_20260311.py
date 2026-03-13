a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]

try:
    i = -1
    while True:
        print(i := a.index(15, i + 1))
except:
    print(f'15 is found at {a.count(15)} times ')

##########################################################

a = list(eval(input('Enter first list: ')))
b = list(eval(input('Enter second list: ')))

try:
    start = 0
    for x in a:
        start = b.index(x, start) + 1
    print(True)
except:
    print(False)

#########################################################

a = [10, 20, 15, 18]

b = a.copy()
print(b)
print(a is b)
print(a == b)

c = a[:]
print(c)
print(a is c)
print(a == c)

d = a
print(d)
print(a is d)
print(a == d)
