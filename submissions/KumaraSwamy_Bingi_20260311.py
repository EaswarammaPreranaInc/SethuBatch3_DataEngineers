a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]

try:
    i = -1
    while (i := a.index(15, i + 1)) >= 0:
        print(i)
except:
    print(f'15 is found {a.count(15)} times')






a = eval(input())
b = eval(input())

try:
    pos = -1
    for x in a:
        pos = b.index(x, pos + 1)
    print(True)
except ValueError:
    print(False)










# copy()  method  demo program  (Home  work)

a = [10 , 20 , 15 , 18]

b = a.copy()
print(b)          # [10, 20, 15, 18]
print(a is b)     # False
print(a == b)     # True

c = a[:]
print(c)          # [10, 20, 15, 18]
print(a is c)     # False
print(a == c)     # True

d = a
print(d)          # [10, 20, 15, 18]
print(a is d)     # True
print(a == d)     # True




