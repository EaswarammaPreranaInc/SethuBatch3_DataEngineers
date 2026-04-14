# --------------------

import sys
class c1:
    pass

a = b = c = d = c1()
print(sys.getrefcount(b))          # 5
print(sys.getrefcount(c1()))       # 2
print(sys.getrefcount(352))        # implementation dependent (usually large, e.g., 2 or more)
print(sys.getrefcount([10,20,15,18]))  # 2
print(sys.getrefcount(10.8))       # 2
print(sys.getrefcount({10,20,15,18}))  # 2
print(sys.getrefcount('Hyd'))      # 2
print(sys.getrefcount({10:20,30:40}))  # 2
print(sys.getrefcount((10,20,30,40)))  # 2


# -------------------------------------

import sys
class Test:
    def _init_(self):
        print('Constructor : ', id(self))
        return None
    def _del_(self):
        print('Destructor : ', id(self))
        return 25

t = Test()
print(t._init_())          # Constructor : <id> \n None
print(sys.getrefcount(t))  # 2
print(t._del_())           # Destructor : <id> \n 25
print(sys.getrefcount(t))  # 2
print('Bye')               # Bye


# -------------------------------------

class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')

def f1():
    print('Function Begin')
    a = c1()
    print(a)
    print('Function end')
    return a

print('Program Begin')
b = f1()
print(b)
print('Program End')

# Output:
# Program Begin
# Function Begin
# <c1 object>
# Function end
# <c1 object>
# Program End


# -------------------------------------

class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')

def f1():
    print('Function begin')
    a = c1()
    print('Function end')
    return a

print('Program Begin')
f1()
print('Program End')

# Output:
# Program Begin
# Function begin
# Function end
# Object is lost
# Program End


# -------------------------------------

class c1:
    def _init_(self):
        print('Object is created')
    def _del_(self):
        print('Object is lost')

def f1():
    print('Function begin')
    a = c1()
    print('Function end')

print('Program Begin')
b = f1()
print(b)
print('Program End')

# Output:
# Program Begin
# Function begin
# Function end
# None
# Program End


# -------------------------------------
#  (Circular reference)
class c1:
    def _init_(self, k):
        print('c1 class object is created')
        self.b = k
        print('End of c1 class constructor')
    def _del_(self):
        print('c1 class object is lost')

class c2:
    def _init_(self):
        print('c2 class object is created')
        self.a = c1(self)
        print('End of c2 class constructor')
    def _del_(self):
        print('c2 class object is lost')

print('Program begin')
x = c2()
print('program end')

# Output:
# Program begin
# program end


# -------------------------------------
# 
class c1:
    def _del_(self):
        print('Destructor')
        global b
        b = self

a = c1()
del a
print('Hello')

# Output:
# Destructor
# Hello


# -------------------------------------
# 
class c1:
    def _add_(a, b):
        print(10 + 20)

a = c1()
b = c1()
print(a + b)

# Output:
# TypeError


# -------------------------------------
# 
class c1:
    def _add_(a, b):
        x = c1()
        y = c1()
        print(x + y)

a = c1()
b = c1()
print(a + b)

# Output:
# TypeError


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _gt_(m, n):
        print('_gt_ method : ', m.x, n.x)

a = c1(10)
b = c1(20)
print(a > b)   # TypeError
print(a < b)   # TypeError


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _ge_(m, n):
        print('_ge_ method : ', m.x, n.x)
        return m.x > n.x

a = c1(10)
b = c1(20)
print(a >= b)   # TypeError
print(a <= b)   # TypeError


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _eq_(m, n):
        print('_eq_ method : ', m.x, n.x)
        return m.x == n.x

a = c1(10)
b = c1(20)
print(a == b)   # False
print(a != b)   # True


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _eq_(m, n):
        print('_eq_ method : ', m.x, n.x)

a = c1(25)
b = c1(25)
print(a == b)       # False
print(a != b)       # True
print(a.x != b.x)   # False


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _ne_(m, n):
        print('_ne_ method : ', m.x, n.x)
        return m.x != n.x

a = c1(25)
b = c1(25)
print(a != b)   # False
print(a == b)   # False
print(a is b)   # False


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _ne_(m, n):
        print('_ne_ method : ', m.x, n.x)
        return m.x != n.x

a = c1(10)
b = a
print(a != b)   # False
print(a == b)   # True


# -------------------------------------
# 
class c1:
    def _gt_(a, b):
        print(10 > 20)
        print(a > b)

a = c1()
b = c1()
print(a > b)

# Output:
# TypeError


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _gt_(p, q):
        print('c1 _gt_ :', p.x, q.x)

class c2:
    def _init_(self, y):
        self.x = y
    def _gt_(p, q):
        print('c2 _gt_ :', p.x, q.x)

a = c1(10)
b = c1(20)
a > b     # TypeError
a < b     # TypeError
m = c2(30)
n = c2(40)
a < m     # TypeError
n < b     # TypeError


# -------------------------------------
# 
class c1:
    def _init_(self):
        self.empno = 25
        self.hr = 250
    def _mul_(x, y):
        return 25 * 8

class c2:
    def _init_(self):
        self.empno = 25
        self.noh = 8
    def _mul_(x, y):
        return 8 * 25

a = c1()
b = c2()
print(a * b)   # TypeError
print(b * a)   # TypeError


# -------------------------------------
# 
class c1:
    def _add_(x, y):
        return '_add_ method of class c1'

class c2:
    pass

a = c1()
b = c1()
print(a + b)   # TypeError
print(a + 7)   # TypeError
print(7 + a)   # TypeError
print(7 + 8)   # 15
m = c2()
n = c2()
print(m + n)   # TypeError
print(a + m)   # TypeError
print(m + a)   # TypeError


# -------------------------------------
# 
class c1:
    def _init_(self, y):
        self.x = y
    def _add_(p, q):
        return p.x + q.x

a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')

print(a + b)   # TypeError
print(m + n)   # TypeError