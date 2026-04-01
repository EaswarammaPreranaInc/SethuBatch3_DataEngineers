#1. Default argument lambda
x = 5
adder1 = lambda y, x = x : x + y
x = 10
adder2 = lambda y, x = x : x + y
x = 20
print(adder1(100))        # 105
print(adder2(200))        # 210
print(adder1(300 , 400))  # 700


#2. Nested lambda
add = lambda x = 10 : lambda y : x + y
a = add()
print(a(20))              # 30
print(add(30)(40))        # 70


#3. Sorting tuples
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

print(sorted(a, key=x[1]))  
# NameError: name 'x' is not defined




# 6. Recursion with global
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

# Output:
# 3
# 2
# 1
# Bye
# Hello
# Hi
# 0
# Bye
# Hello
# Hi
# 0
# Bye
# Hello
# Hi
# 0
# Bye
# End


# 7. Recursion tricky
def f1(x, y):
    if x > 40:
        return
    x += y
    f1(x, y)
    print(x)

x = 10
f1(x, x := x + 1)
print(x)

# Output:
# 43
# 32
# 21
# 10
# 11


# 8. Recursion simple
def f1(x):
    print(x)
    if x:
        f1(x-1)
    print(x)

f1(3)

# Output:
# 3
# 2
# 1
# 0
# 0
# 1
# 2
# 3


# 9. Infinite recursion
def f1():
    print('f1 function')
    f2()
    print('End of f1 function')

def f2():
    print('f2 function')
    f1()
    print('End of f2 function')

f1()
# Infinite recursion → RecursionError


# 10. Function reference
def f1():
    print('f1 function')

def f2():
    print('f2 function')

f1()
f2()
print(f1 is f2)   # False

f2 = f1
f2()              # f1 function
print(f1 is f2)   # True

f2 = f1()
print(f2)         # None
f2()              # TypeError


# 11. inner function scope error
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
inner()     # NameError
other()




# 14. globals()
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)                # 30
        print(globals()['x'])   # 10
    inner()
outer()
print('Bye')


# 15.
x = 10
def outer():
    x = 20
    def inner():
        print(x)                # 20
        print(globals()['x'])   # 10
    inner()
outer()


# 16.
x = 10
def outer():
    def inner():
        print(x)   # 10
    inner()
outer()


# 17.
def outer():
    x = 10
    def inner():
        x = 20
        print(x)   # 20
        x += 7
    print(x)       # 10
    x += 5
    inner()
    print(x)       # 15

outer()
print('Bye')

# Output:
# 10
# 20
# 15
# Bye