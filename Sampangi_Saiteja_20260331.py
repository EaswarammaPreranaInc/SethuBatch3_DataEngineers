# Find outputs  (Home  work)
x = 5
adder1 = lambda y, x=x: x + y
x = 10
adder2 = lambda y, x=x: x + y
x = 20

print(adder1(100))        # 105
print(adder2(200))        # 210
print(adder1(300, 400))   # 700


# Nested  lambda  function  (Home  work)
add = lambda x=10: (lambda y: x + y)

a = add()
print(a(20))              # 30
print(add(30)(40))        # 70


# Find  outputs
a = (
    (10, 'Rama', 1000.0),
    (20, 'Sita', 2000.0),
    (15, 'Rajesh', 500.0),
    (18, 'Kiran', 2800.0),
    (5, 'Amar', 1300.0)
)

b = sorted(a)
print(b)
# [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

print()

c = sorted(a, reverse=True)
print(c)
# [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

print()

d = sorted(a, key=lambda x: x[1])
print(d)
# [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

print()

e = sorted(a, key=lambda x: x[2])
print(e)
# [(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

print()

f = sorted(a, key=lambda x: x[0])
print(f)
# [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

print()

g = sorted(a, key=lambda x: x[1], reverse=True)
print(g)
# [(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]

# print(sorted(a , key = x[1]))
# TypeError: 'int' object is not subscriptable


# Find outputs  (Home  work)
a = [
    {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013},
    {'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
    {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}
]

b = sorted(a, key=lambda x: x['Year'])
print(b)
# [{'Make': 'Tesla', 'Model': 'X', 'Year': 1999},
#  {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008},
#  {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]

# print(sorted(a))
# TypeError: '<' not supported between instances of 'dict' and 'dict'


# Find outputs  (Home  work)
a = (
    (10, 'Rama', 1000.0),
    (20, 'Sita', 2800.0),
    (15, 'Vamsi', 2000.0),
    (25, 'Kiran', 1500.0),
    (5, 'Amar', 1300.0)
)

print(max(a, key=lambda x: x[0]))
# (25, 'Kiran', 1500.0)

print(max(a, key=lambda x: x[1]))
# (15, 'Vamsi', 2000.0)

print(max(a, key=lambda x: x[2]))
# (20, 'Sita', 2800.0)

print(max(a))
# (25, 'Kiran', 1500.0)


#  Tricky  program
# Find  outputs  (Home  work)
def f1(x, y):
    if x > 40:
        return
    x += y
    f1(x, y)
    print(x)

x = 10
f1(x, x := x + 1)
print(x)   # 10


# Find  outputs   (Home  work)
def f1(x):
    print(x)
    if x:
        f1(x - 1)
    print(x)

f1(3)
# 3 2 1 0 0 1 2 3


# Find  outputs
def f1():
    print('f1  function')
    f2()
    print('End  of  f1  function')

def f2():
    print('f2  function')
    f1()
    print('End  of  f2  function')

f1()   # Error
# Next statements will NOT execute


# Find  outputs  (Home  work)
def f1():
    print('f1    function')

def f2():
    print('f2  function')

f1()                     # f1 function
f2()                     # f2 function
print(f1 is f2)          # False
f2 = f1
f2()                     # f1 function
print(f1 is f2)          # True
f2 = f1()                # f1 function
print(f2)                # None
f2()                     # Error
# No further execution


# Find  outputs (Home  work)
p = print
p('Hyderabad')           # Hyderabad

print = None
print('Hello')           # Error
# Next line will NOT execute
p('Hello')               # NOT executed


# Find   outputs (Home  work)
x = id
print(x(25))             # id value (some integer)

p = len
print(p('Hyd'))          # 3


# Find  outputs (Home  work)
def outer():
    print('Outer  function')
    def inner():
        print('Inner  function')
    print('Hello')
    inner()
    print('Back  to  outer  function')

def other():
    inner()
    print('Other  function')

print('Begin')           # Begin
outer()
print('Hi')              # Hi
inner()                  # Error
# Next line will NOT execute
other()                  # NOT executed


# Find  output(Home  work)
def f1(a):
    def f2():
        return 10
    return f2() + 20 + a

print(f1(30))            # 60


# Find  outputs (Home  work)
def outer():
    print('Outer  function')
    def inner1():
        print('1st  inner  function')
    def inner2():
        print('2nd  inner  function')
    print('Hi')
    inner2()
    print('Hello')
    inner1()
    print('Back  to  outer  function')

print('Begin')           # Begin
outer()
print('Bye')             # Bye


# Find  outputs  (Home  work)
x = 10
def outer():
    x = 20
    def inner():
        x = 30
        print(x)                 # 30
        print(globals()['x'])    # 10
    inner()

outer()
print('Bye')                     # Bye


# Find  outputs  (Home   work)
x = 10
def outer():
    x = 20
    def inner():
        print(x)                 # 20
        print(globals()['x'])    # 10
    inner()

outer()


# Find  outputs  (Home  work)
x = 10
def outer():
    def inner():
        print(x)                 # 10
    inner()

outer()


# Find  outputs  (Home  work)
def outer():
    x = 10
    def inner():
        x = 20
        print(x)         # 20
        x += 7
    print(x)             # 10
    x += 5
    inner()
    print(x)             # 15

outer()
print('Bye')             # Bye


# Find  outputs  (Home  work)
def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)         # 15
        x = 20
        print(x)         # 20
        x += 5
    print(x)             # 10
    x += 5
    inner()
    print(x)             # 25

outer()
print(x)                 # Error


# Find  outputs  (Home  work)
def outer():
    x = 10
    def inner():
        print(x)
        nonlocal x       # Error
        x = 20
    outer()

outer()                  # Error


# Find   outputs(Home  work)
def outer():
    x = 10
    def inner():
        global x
        x = 20
        print(x)         # 20
        x += 5
    print(x)             # 10
    x += 5
    inner()
    print(x)             # 25

outer()
print(x)                 # 25


# Find  outputs(Home  work)
def outer():
    def inner():
        nonlocal x       # Error
        x = 20
    inner()

outer()                  # Error


# Find  outputs(Home  work)
def outer():
    def inner():
        global x
        x = 20
        print(x)         # 20
        x = x + 5
    inner()
    print(x)             # 25

outer()
print(x)                 # 25


# Identify Error
def f1():
    nonlocal x      # Error


# Find outputs (Home work)
def outer():
    a = 10
    b = 20
    def inner():
        nonlocal a
        a = 100
        b = 200
        print(a, b)     # 100 200
    print(a, b)         # 10 20
    inner()
    print(a, b)         # 100 20

outer()


# Find outputs (Home work)
def f1():
    x = 'John'
    def f2():
        nonlocal x
        x = 'Hello'
    f2()
    return x

print(f1())             # Hello


# Find output(Home work)
def fun():
    x = 10
    def gun():
        x = x + 20      # Error
        print(x)
    gun()

fun()                   # Error


# Identify Error
x = 10
def outer():
    x = 20
    def inner():
        global x
        nonlocal x      # Error


# Find outputs (Home work)
def f1():
    x = 10
    def f2():
        nonlocal x
        def f3():
            nonlocal x
            print(x)    # 10
        f3()
    f2()

f1()