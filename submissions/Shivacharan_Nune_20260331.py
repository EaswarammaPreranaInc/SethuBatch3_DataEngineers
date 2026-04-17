# --------------------------------------------------
# Find outputs
x = 5
adder1 = lambda y, x=x: x + y
x = 10
adder2 = lambda y, x=x: x + y
x = 20
print(adder1(100))      # 105
print(adder2(200))      # 210
print(adder1(300, 400)) # 700


# --------------------------------------------------
# Nested lambda function
add = lambda x=10: lambda y: x + y
a = add()
print(a(20))        # 30
print(add(30)(40))  # 70


# --------------------------------------------------
# Find outputs
a = ((10,'Rama',1000.0),(20,'Sita',2000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(5,'Amar',1300.0))

b = sorted(a)
print(b)  
# [(5,'Amar',1300.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(20,'Sita',2000.0)]

c = sorted(a, reverse=True)
print(c)  
# [(20,'Sita',2000.0),(18,'Kiran',2800.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0)]

d = sorted(a, key=lambda x: x[1])
print(d)  
# [(5,'Amar',1300.0),(18,'Kiran',2800.0),(15,'Rajesh',500.0),(10,'Rama',1000.0),(20,'Sita',2000.0)]

e = sorted(a, key=lambda x: x[2])
print(e)  
# [(15,'Rajesh',500.0),(10,'Rama',1000.0),(5,'Amar',1300.0),(20,'Sita',2000.0),(18,'Kiran',2800.0)]

f = sorted(a, key=lambda x: x[0])
print(f)  
# [(5,'Amar',1300.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(20,'Sita',2000.0)]

g = sorted(a, key=lambda x: x[1], reverse=True)
print(g)  
# [(20,'Sita',2000.0),(10,'Rama',1000.0),(15,'Rajesh',500.0),(18,'Kiran',2800.0),(5,'Amar',1300.0)]

print(sorted(a, key=x[1]))  # ERROR


# --------------------------------------------------
# Find outputs
a = [{'Make':'Ford','Model':'Focus','Year':2013},
     {'Make':'Tesla','Model':'X','Year':1999},
     {'Make':'Mercedes','Model':'C350E','Year':2008}]

b = sorted(a, key=lambda x: x['Year'])
print(b)
# [{'Make':'Tesla','Model':'X','Year':1999},
#  {'Make':'Mercedes','Model':'C350E','Year':2008},
#  {'Make':'Ford','Model':'Focus','Year':2013}]

print(sorted(a))  # ERROR


# --------------------------------------------------
# Find outputs
a = ((10,'Rama',1000.0),(20,'Sita',2800.0),(15,'Vamsi',2000.0),(25,'Kiran',1500.0),(5,'Amar',1300.0))

print(max(a, key=lambda x: x[0]))  # (25,'Kiran',1500.0)
print(max(a, key=lambda x: x[1]))  # (20,'Sita',2800.0)
print(max(a, key=lambda x: x[2]))  # (20,'Sita',2800.0)
print(max(a))                     # (25,'Kiran',1500.0)


# --------------------------------------------------
# Find outputs
def f1():
    global a
    if a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

a = 3
f1()
print('End')

# 3 2 1 Bye Hello Hi 0 Bye Hello Hi 0 Bye Hello Hi 0 Bye End


# --------------------------------------------------
# Tricky program
def f1(x,y):
    if x > 40:
        return
    x += y
    f1(x,y)
    print(x)

x = 10
f1(x, x := x + 1)
print(x)

# 43 32 21 10 10


# --------------------------------------------------
# Find outputs
def f1(x):
    print(x)
    if x:
        f1(x-1)
    print(x)

f1(3)
# 3 2 1 0 0 1 2 3


# --------------------------------------------------
# Find outputs
def f1():
    print('f1 function')
    f2()
    print('End of f1 function')

def f2():
    print('f2 function')
    f1()
    print('End of f2 function')

f1()
# infinite recursion -> RecursionError


# --------------------------------------------------
# Find outputs
def f1():
    print('f1 function')

def f2():
    print('f2 function')

f1()
f2()
print(f1 is f2)  # False

f2 = f1
f2()             # f1 function
print(f1 is f2)  # True

f2 = f1()
print(f2)        # None
f2()             # ERROR


# --------------------------------------------------
# Assign print to p
p = print
p('Hyderabad')

p = print
print = None
p('Hello')


# --------------------------------------------------
# Assign id and len
x = id
print(x(25))

p = len
print(p('Hyd'))


# --------------------------------------------------
# Find outputs
def outer():
    print('Outer function')
    def inner():
        print('Inner function')
    print('Hello')
    inner()
    print('Back to outer function')

def other():
    inner()
    print('Other function')

print('Begin')
outer()
print('Hi')
inner()  # ERROR


# --------------------------------------------------
# Find output
def f1(a):
    def f2():
        return 10
    return f2() + 20 + a

print(f1(30))  # 60


# --------------------------------------------------
# Find outputs
def outer():
    print('Outer function')
    def inner1():
        print('1st inner function')
    def inner2():
        print('2nd inner function')
    print('Hi')
    inner2()
    print('Hello')
    inner1()
    print('Back to outer function')

print('Begin')
outer()
print('Bye')


# --------------------------------------------------
# Find outputs
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)
        print(globals()['x'])
    inner()

outer()
print('Bye')
# 30 10 Bye


# --------------------------------------------------
# Find outputs
x = 10
def outer():
    x = 20
    def inner():
        print(x)
        print(globals()['x'])
    inner()

outer()
# 20 10


# --------------------------------------------------
# Find outputs
x = 10
def outer():
    def inner():
        print(x)
    inner()

outer()
# 10


# --------------------------------------------------
# Find outputs
def outer():
    x = 10
    def inner():
        x = 20
        print(x)
        x += 7
    print(x)
    x += 5
    inner()
    print(x)

outer()
print('Bye')
# 10 20 15 Bye


# --------------------------------------------------
# Find outputs
def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)
        x = 20
        print(x)
        x += 5
    print(x)
    x += 5
    inner()
    print(x)

outer()
print(x)  # ERROR


# --------------------------------------------------
# Identify Error
def f1():
    nonlocal x  # ERROR


# --------------------------------------------------
# Find outputs
def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)
    print(a, b)
    inner()
    print(a, b)

outer()
# 10 20
# 100 200
# 100 20


# --------------------------------------------------
# Find outputs
def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x

print(f1())  # Hello


# --------------------------------------------------
# Find output
def fun():
    x = 10
    def gun():
        x = x + 20
        print(x)
    gun()

fun()  # ERROR


# --------------------------------------------------
# Identify Error
x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x  # ERROR


# --------------------------------------------------
# Find outputs
def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)
        f3()
    f2()

f1()  # 10