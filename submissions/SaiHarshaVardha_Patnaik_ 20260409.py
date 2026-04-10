# ================= cal.py =================
x = 100
y = 200

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

class c1:
    def m1(self):
        print('m1  method')


# ================= How to use members of cal module with from statement ? =================
print('Begin')

# How to import all the members of cal module
from cal import *

# How to print variable 'x' of cal module
print(x)

# How to print variable 'y' of cal module
print(y)

print(cal.x)          # This will NOT work after from cal import * (kept as in question, normally wrong)

# How to call add() function of cal module with 10 and 7
print(add(10, 7))

# How to call sub() function of cal module with 10 and 7
print(sub(10, 7))

# How to call mul() function of cal module with 10 and 7
print(mul(10, 7))

# How to call div() function of cal module with 10 and 7
print(div(10, 7))

print(add(x, y))

# How to call m1() method of class c1 in cal module
b = c1()
b.m1()


# ================= How to import only x, add, mul, c1 from cal module ? =================
print('Begin')

# How to import members x, add, mul and class c1 of cal module
from cal import x, add, mul, c1

# How to print variable 'x' of cal module
print(x)

print(y)        # This will give NameError because y is not imported
print(cal.x)    # This will also give NameError because cal is not imported

# How to call add() function of cal module with 10 and 7
print(add(10, 7))

print(sub(10, 7))   # NameError: sub not imported

# How to call mul() function of cal module with 10 and 7
print(mul(10, 7))

print(div(10, 7))   # NameError: div not imported

# How to call m1() method of class c1 in cal module
b = c1()
b.m1()


# ================= Module alias =================
print('Begin')

# How to import cal module with another name using import statement
import cal as m

# How to print variable 'x' of cal module
print(m.x)

# How to print variable 'y' of cal module
print(m.y)

# How to call add() function of cal module with 10 and 7
print(m.add(10, 7))

# How to call sub() function of cal module with 10 and 7
print(m.sub(10, 7))

# How to call mul() function of cal module with 10 and 7
print(m.mul(10, 7))

# How to call div() function of cal module with 10 and 7
print(m.div(10, 7))

# How to call m1() method of c1 class in cal module
b = m.c1()
b.m1()

print(cal.x)   # works because cal is also imported earlier

# Correct syntax for from math import * with alias does NOT exist, only module alias:
import math as mt
from math import *   # without alias; functions come directly


# ================= Member alias =================
# How to import members x, add, mul and class c1 of cal module with another name using from statement
from cal import x as x1, add as add1, mul as mul1, c1 as c1_alias

# How to print variable 'x' of cal module
print(x1)

print(x1)

# How to call add() function of cal module with 10 and 7
print(add1(10, 7))

# How to call mul() function of cal module with 10 and 7
print(mul1(10, 7))

# How to call m1() method of class c1 in cal module
b = c1_alias()
b.m1()


# ================= mod1.py =================
x = 10

def disp():
    print('disp  function  of  mod1')

class c1:
    def m1(self):
        print('m1  method  of  class  c1  in  mod1')


# ================= mod2.py =================
x = 20

def disp():
    print('disp  function  of  mod2')

class c1:
    def m1(self):
        print('m1  method of  class  c1  in  mod2')


# ================= Find outputs (1) =================
x = 30

def disp():
    print('disp  function  of  same  module ')

class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')

from mod2 import *
from mod1 import *

print(x)      # 10 (from mod1, last import)

disp()        # disp function of mod1

a = c1()
a.m1()        # m1 method of class c1 in mod1


# ================= Find outputs (2) =================
from mod1 import *
from mod2 import *

x = 30

def disp():
    print('disp  function  of  same  module ')

class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')

print(x)      # 30 (current module)

disp()        # disp function of same module

a = c1()
a.m1()        # m1 method of class c1 in same module


# ================= Use members of all 3 modules with import statement =================
# How to import mod1 and mod2
import mod1
import mod2

x = 30

def disp():
    print('disp  function  of  same  module')

class c1:
    def m1(self):
        print('m1  method of  class  c1  in  same  module')

# How to print variable 'x' of mod1
print(mod1.x)
# How to call disp() function of mod1
mod1.disp()
# How to call method m1() of class c1 in mod1
a1 = mod1.c1()
a1.m1()

print()

# How to print variable 'x' of mod2
print(mod2.x)
# How to call disp() function of mod2
mod2.disp()
# How to call method m1() of class c1 in mod2
a2 = mod2.c1()
a2.m1()

print()

# How to print variable 'x' of current module
print(x)
# How to call disp() function of current module
disp()
# How to call method m1() of class c1 in current module
a3 = c1()
a3.m1()


# ================= Use members of all 3 modules with from statement =================
# How to import members of mod1
from mod1 import x as x1_mod1, disp as disp1, c1 as c1_mod1
# How to import members of mod2
from mod2 import x as x1_mod2, disp as disp2, c1 as c1_mod2

x = 30

def disp():
    print('disp  function  of  same  module')

class c1:
    def m1(self):
        print('m1   method  of  class  c1  in  same  module')

# How to print variable 'x' of mod1
print(x1_mod1)
# How to call disp() function of mod1
disp1()
# How to call method m1() of class c1 in mod1
a4 = c1_mod1()
a4.m1()

print()
print()

# How to print variable 'x' of mod2
print(x1_mod2)
# How to call disp() function of mod2
disp2()
# How to call method m1() of class c1 in mod2
a5 = c1_mod2()
a5.m1()

print()
print()

# How to print variable 'x' of current module
print(x)
# How to call disp() function of current module
disp()
# How to call method m1() of class c1 in current module
a6 = c1()
a6.m1()


# ================= mod1.py (prevent middle 3 statements) =================
# How to prevent execution of the middle 3 statements when mod1 is imported elsewhere

if __name__ == '__main__':
    print('One')
    print('Two')
    print('Three')

print('Four')
print('Five')
print('Six')
print('Seven')
print('Eight')
print('Nine')


# ================= Find outputs (import mod1) =================
print('Begining  of  mod2')
import mod1
print('End  of  mod2')


# ================= Find outputs (cal imports) =================
import cal

print(cal.x)
print(cal.y)
print(cal.add(10, 7))
print(cal.sub(10, 7))
print(cal.mul(10, 7))
print(cal.div(10, 7))
a = cal.c1()
a.m1()

# Find outputs – from cal import y, sub, mul
from cal import y, sub, mul

print(x)              # x from current module
print(y)              # y from cal
print(add(10, 7))     # add from cal if imported earlier with from cal import *
print(sub(10, 7))     # sub from cal
print(mul(10, 7))     # mul from cal
print(div(10, 7))     # NameError if div not imported

a = c1()              # c1 from wherever last imported/defined
a.m1()

# 1. Rat class outputs
class Rat:
    def __init__(self, nr1=22, dr1=7):
        self.nr = nr1
        self.dr = dr1
    def __str__(self):
        return f'{self.nr}/{self.dr}'
# end of the class
# Assume inputs 11 and 15 for x,y
x, y = 11, 15
a = Rat()
b = Rat(9)
c = Rat(5, 8)
d = Rat(dr1=9)
e = Rat(dr1=3, nr1=2)
f = Rat(x, y)
print('a : ', a)  # 22 / 7
print('b : ', b)  # 9 / 7
print('c : ', c)  # 5 / 8
print('d : ', d)  # 22 / 9
print('e : ', e)  # 2 / 3
print('f : ', f)  # 11 / 15
c.__init__()  # defaults
print('c : ', c)  # 22 / 7
a.__init__(3.8, 4.6)
print('a : ', a)  # 3.8 / 4.6
# g = Rat(nr1=9, 5)  # SyntaxError: positional after keyword
# h = Rat(nr=9, dr=5)  # AttributeError: nr1, dr1 expected

# 2. Date class
'''
Object 'a' ---> {'dd': 15, 'mm': 8, 'yy': 1947}

Object 'b' ---> {'dd': 26, 'mm': 1, 'yy': 1950}

Object 'c' ---> {'dd': 19, 'mm': 7, 'yy': 1985}
'''
# Note: d=Date() TypeError: missing args
# e=Date(dd=30,mm=4,yy=2022) TypeError: wrong kwarg names
# f=Date(dd1=26,mm1=8,2023) SyntaxError: pos after kw

# 3. Constructors with return
class c1:
    def __init__(self):
        print('c1 class constructor')
        return 25  # ignored
class c2:
    def __init__(self):
        print('c2 class constructor')
        return None
class c3:
    def __init__(self):
        print('c3 class constructor')
a = c1()  # prints 'c1 class constructor', a=<c1 object>
b = c2()  # prints 'c2 class constructor', b=<c2 object>
print(b)  # <c2 object>
print(b.__init__())  # prints 'c2...', returns None
c = c3()  # prints 'c3...'
print(c.__init__())  # prints 'c3...', returns None

# 4. Recursive constructor
class c1:
    def __init__(self):
        print('Constructor')
        b = c1()  # RecursionError
a = c1()  # RecursionError

# 5. __init__ vs init
class c1:
    def __init__(self):
        print('Constructor')
        self.x = 10
        self.y = 20
class c2:
    def init(self):  # normal method
        print('Method')
        self.x = 30
        self.y = 40
a = c1()
print(a.__dict__)  # {'x': 10, 'y': 20}

b = c2()  # empty dict
print(b.__dict__)  # {}

b.init()  # calls method
print(b.__dict__)  # {'x': 30, 'y': 40}

'''
Object 'a' ---> {'x': 10, 'y': 20}

Object 'b' ---> {'x': 30, 'y': 40}  (after init())
'''

# 6. Attribute assignment
class c1:
    def __init__(self):
        self.a = 10
    def m1(self):
        self.b = 20
class c2:
    def m3(self):
        x.e = 50  # x is global
def f1():
    x.c = 30  # x global
x = c1()
print(x.__dict__)  # {'a': 10}

x.m1()
print(x.__dict__)  # {'a': 10, 'b': 20}

f1()
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30}

x.d = 40
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

y = c2()
y.m3()  # adds x.e=50
print(x.__dict__)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

z = c1()
print(z.__dict__)  # {'a': 10}

'''
object 'x' ---> {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

object 'z' ---> {'a': 10}

object 'y' ---> {}  (no __init__)
'''

# 7. del attributes
class c1:
    def __init__(self):
        self.x = 10
        self.y = 20
        self.z = 30
a = c1()
b = c1()
print(a.__dict__)  # {'x':10,'y':20,'z':30}
print(b.__dict__)  # {'x':10,'y':20,'z':30}
del a.x
del b.y
print(a.__dict__)  # {'y':20,'z':30}
print(b.__dict__)  # {'x':10,'z':30}
print(a.x)  # AttributeError
print(b.y)  # AttributeError

'''
Object 'a'  ---> {'y': 20, 'z': 30}

Object 'b'  ---> {'x': 10, 'z': 30}
'''

# 8. Multiple __init__ - last overrides
class c1:
    def __init__(self):
        print('1st constructor')
    def __init__(self):
        print('2nd constructor')
    def __init__(self):
        print('3rd constructor')
a = c1()  # prints '3rd constructor'

# 9. Multiple __init__ no args first fails
class c1:
    def __init__(self):
        print('No argument constructor')
    def __init__(self, x):
        print('single argument constructor : ', x)
    def __init__(self, x, y):
        print('Two argument constructor : ', x, y)
# a = c1(10,20)  # TypeError: no matching __init__
# etc - all fail

# 10. With defaults - last wins but order matters
class c1:
    def __init__(self):
        print('No argument constructor')
    def __init__(self, x):
        print('single argument constructor : ', x)
    def __init__(self, x=100, y=200):
        print('Two argument constructor : ', x, y)
a = c1(10,20)  # Two: 10 20
b = c1(30)     # Two: 30 200
c = c1()       # Two: 100 200

# 11. Function and class same name
def f1():
    print('Function')
    return 25
class f1:
    def __init__(self):
        print('Constructor')
a = f1()  # class, prints 'Constructor'
print(a)  # <f1 object>

# 12. Class and function same name (reversed)
class c1:
    def __init__(self):
        print('Constructor')
def c1():
    print('Function')
a = c1()  # function, prints 'Function', a=25? Wait no:
# Actually calls func, but print(a) error if not assigned, but code has print(a))
# Code: print(a)) syntax error, but intent: calls func, a=None? No return.
# def c1(): print('Function')  # returns None
# a = c1()  # prints 'Function', a=None
# print(a)  # None
