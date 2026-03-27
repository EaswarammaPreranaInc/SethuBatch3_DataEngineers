# 1) Find outputs (Home work)
def f1():
    a = 20
    print(a)
    a += 1
# End of the function

a = 10
print(a)
a += 1
f1()
print(a)
# Output:
# 10
# 20
# 11


# 2) Find outputs (Home work)
def f1():
    a = 20
    print(a)
    d = globals()
    print(d['a'])
    a = 30
    d['a'] = 40
# End of f1() function

a = 10
print(a)
a += 1
f1()
print(a)
# Output:
# 10
# 20
# 11
# 40


# 3) Find outputs (Home work)
x = 10
def f1():
    print(x)
    print(globals()['x'])
# end of the function

f1()
# Output:
# 10
# 10


# 4) Find outputs (Home work)
def f1():
    x = 20
    print(x)
    print(globals()['x'])
# End of the function

f1()
# Output:
# 20
# NameError: name 'x' is not defined


# 5) Find outputs (Home work)
def f1():
    a = 40
    b = 50
    c = 60
    print(a, b, c)
    d = globals()
    print(d['a'], d['b'], d['c'])
    d['a'] = 100
    d['b'] = 200
    d['c'] = 300

def f2():
    print(a, b, c)
# End of f2 function

a = 10
b = 20
c = 30
f1()
f2()
# Output:
# 40 50 60
# 10 20 30
# 100 200 300


# 6) global keyword demo program (Home work)
def f1():
    x = 20
    print(x)

def f2():
    global x
    x = 30
    print(x)
    x += 1

def f3():
    global y
    y = 40
    print(y)
    y += 1

def f4():
    global x
    x = 50
# End of the functions

x = 10
print(x)
x += 1
f1()
print(x)
f2()
print(x)
x += 1
f3()
print(y)
f4()
print(x)
# Output:
# 10
# 11
# 20
# 30
# 31
# 40
# 40
# 50


# 7) Find outputs (Home work)
def f1():
    global a
    a = 20
    print(a)
    print(globals()['a'])
    a = 30
# End of the function

a = 10
print(a)
f1()
print(a)
# Output:
# 10
# 20
# 20
# 30


# 8) Find outputs (Home work)
def f1():
    global a
    print(a)
    a = 10
    print(globals()['a'])
    a = 20
    print(a)
    a = 30

def f2():
    print(a)
# End of f2 function

# This program raises error when f1() is called
f1()
f2()
print(a)
# Output:
# NameError: name 'a' is not defined (at first print(a) inside f1)


# 9) Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a)
    a = 20

def f2():
    global a
    print(a)
    a = 30

def f3():
    print(a)
    globals()['a'] = 40
# End of the functions

f1()
f2()
f3()
print(a)
# Output:
# 10
# 20
# 30
# 40
# 40


# 10) Find outputs (Home work)
def f1():
    global a
    a = 10
    print(a)
    a = 20

def f2():
    print(a)
    a = 30
    print(a)

def f3():
    print(a)
    globals()['a'] = 40
# End of the functions

f1()
f2()
f3()
print(a)
# Output:
# 10
# 20
# 30
# 40
# 40


# 11) Find outputs (Home work)
def f1():
    a = 10
    global a
    print(a)
    global b
    b = 20
# End of f1() function

# This program raises syntax error (cannot assign to name and then declare global)
# Output:
# SyntaxError: name 'a' is used prior to global declaration


# 12) Find outputs (Home work)
def f1():
    global a
    print(a)
    a += 1

def f2():
    global a
    print(a)
    a += 1
# End of the functions

a = 10
print(a)
a += 1
f1()
print(a)
a += 1
f2()
print(a)
# Output:
# 10
# 11
# 11
# 12
# 12
# 13


# 13) Find outputs (Home work)
def f1():
    a = 20
    print(a)

def f2():
    print(a)
    a += 1
# End of the functions

a = 10
print(a)
f1()
a += 1
f2()
print(a)
# Output:
# 10
# 20
# 11
# UnboundLocalError: local variable 'a' referenced before assignment in f2


# 14) Find outputs (Home work)
def f1():
    a = 20
    global a
    print(a)
    print(globals()['a'])
    a = 30
    globals()['a'] = 40
# End of f1() function

a = 10
print(a)
a += 1
f1()
print(a)
# Output:
# 10
# 11
# SyntaxError: name 'a' is used prior to global declaration (in f1)


# 15) Find outputs (Home work)
def f1():
    x = x + 5
# End of f1 function

def f2():
    x = globals()['x'] + 5
    print(x)
# End of f2 function

x = 10
f1()
f2()
print(x)
# Output:
# UnboundLocalError in f1 (x referenced before assignment)
# 15
# 10
