
# === 1. Generator to divide a string into words (without using list) ===

import time

def words(s):
    # Split the string directly and yield each word in the loop
    for word in s.split():
        yield word

s = input('Enter any string: ')   # Example: "M.G.Story"
g = words(s)                      # Generator object
print('Words of the string')
for y in g:
    print(y)
    time.sleep(1)


# === 2. Output of this generator (f1) ===

def f1():
    x = 1
    while x <= 100000000000000000000:
        yield x
        x += 1

g = f1()
print('Begin')
print(*g)           # Will keep printing numbers 1, 2, 3, ... forever (infinite stream)
print('End')        # This line will NEVER execute (loop never ends)


# === 3. Output of this generator expression (g) ===

g = (x * x for x in range(500000000000000000))
print(*g)           # Tries to print all squares 0, 1, 4, 9, 16, ... in a huge range
                    # In practice, it will just print all squares until it runs out of memory/time


# === 4. Output and flow of f1() used in loop and unpacking ===

def f1():
    print('One')
    yield 1
    print('Two')
    yield 2
    print('Three')
    yield 3
    print('End')

g = f1()
for m in g:
    print(m)

# Output:
# One
# 1
# Two
# 2
# Three
# 3
# End

# Now unpack from a fresh generator
x, y, z = f1()
print(x)            # 1
print(y)            # 2
print(z)            # 3


# === 5. Identify error in unpacking ===

def f1():
    yield 10
    yield 20
    yield 30
    yield 40

# a, b, c = f1()           # ERR: too many values to unpack (3 variables, 4 yielded values)
# p, q, r, s, m = f1()     # ERR: too few values to unpack (5 variables, 4 yielded values)
# Correction (if needed):
a, b, c, d = f1()
print(a, b, c, d)           # 10 20 30 40


# === 6. Errors due to len(), indexing, * on generator ===

def f1():
    yield 1
    yield 2
    yield 3

g = f1()
# print(len(g))             # TypeError: object of type 'generator' has no len()
# print(g * 3)              # TypeError: unsupported operand type(s) for *: 'generator' and 'int'
# print(g[0])               # TypeError: 'generator' object is not subscriptable
# print(g[1:3])             # TypeError: 'generator' object is not subscriptable

# BUT this works:
print(*g)                   # 1 2 3


# === 7. Identify syntax error in class definition ===

class c1:
    def m1(self):
        pass

class c2:
    pass

# class c3:                 # ERR: empty class body not allowed without 'pass' or members
#     pass                    # Add this line to fix


# === 8. Outputs of basic class c1 object operations ===

class c1:
    pass    # End of the class

a = c1()
print(id(a))                # prints a unique integer (object identity)
print(type(a))              # <class '__main__.c1'>
print(a.__dict__)           # {} (empty dictionary of instance attributes)
print(a)                    # <__main__.c1 object at 0x...>

del a
# print(a)                  # NameError: name 'a' is not defined


# === 9. Outputs of function and method with same name (m1) ===

def m1():
    print('Function')

class c1:
    def m1(self):
        print('1st method')
    def m1(self):
        print('2nd method')  # last definition overwrites
    def m1(self):
        print('3rd method')  # only this one remains

a = c1()
a.m1()                       # Output: 3rd method
m1()                         # Output: Function


# === 10. Overriding method with multiple argument versions (without default) ===

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x, y):
        print('Two argument method :', x, y)

a = c1()
a.m1(10, 20)                 # Output: Two argument method : 10 20
# a.m1(30)                   # ERR: m1() now expects 3 arguments (self, x, y)
# a.m1()                     # ERR: m1() now expects 3 arguments (self, x, y)
# Note: Only the last definition is used


# === 11. Overriding method with default parameters ===

class c1:
    def m1(self):
        print('No argument method')
    def m1(self, x):
        print('Single argument method :', x)
    def m1(self, x=1, y=2):
        print('Two argument method :', x, y)

a = c1()
a.m1(10, 20)                 # Output: Two argument method : 10 20
a.m1(30)                     # Output: Two argument method : 30 2
a.m1()                       # Output: Two argument method : 1 2


# === 12. Multiple class c1 definitions (last one wins) ===

class c1:
    def m1(self):
        print('Method of first c1 class')

class c1:
    def m1(self):
        print('Method of second c1 class')

class c1:
    def m1(self):
        print('Method of third c1 class')

a = c1()
a.m1()                       # Output: Method of third c1 class


# === 13. When last c1 has no m1 method ===

class c1:
    def m1(self):
        print('Method of first c1 class')

class c1:
    def m1(self):
        print('Method of second c1 class')

class c1:
    pass                    # No m1 method here

a = c1()
# a.m1()                    # AttributeError: 'c1' object has no attribute 'm1'


# === 14. Outputs of __dict__ and dynamic attribute creation ===

class c1:
    pass                    # End of class

a = c1()
print(a.__dict__)           # {} (empty dict)

a.x = 10
print(a.__dict__)           # {'x': 10}

a.y = 20
print(a.__dict__)           # {'x': 10, 'y': 20}

a.x = 30
print(a.__dict__)           # {'x': 30, 'y': 20}

a.y = 40
print(a.__dict__)           # {'x': 30, 'y': 40}

del a.x
print(a.__dict__)           # {'y': 40}

del a.y
print(a.__dict__)           # {}

del a
# print(a.__dict__)         # NameError: name 'a' is not defined