'''
1) Repeat prog5a such that methods are called in a different way

1) What are the two ways to call a method ? --> object . method()  and  classname . method(object)

2) Reuse triangle class defined in prog5a but do not define triangle class again

from prog5a import triangle
t = triangle()
triangle.get(t)
triangle.test(t)
print('Area : ', triangle.area(t))
print('Perimeter: ', triangle.peri(t))
'''
'''
2) What are the outputs if inputs are 25 , Rama Rao , male , 52 , 48 , 55 (Home work)
from prog9a import student
s = student()
print(s.__dict__) 
# {}
s.get() 
# (Input: 25, Rama Rao, male, 52, 48, 55)
print(s.__dict__) 
# {'roll': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55}
s.compute()
print(s.__dict__) 
# {'roll': 25, 'name': 'Rama Rao', 'gender': 'male', 'm1': 52, 'm2': 48, 'm3': 55, 'total': 155, 'avg': 51.66}
'''
'''
3) Repeat student program for 'n' students

1) import student class defined in prog9a but do not rewrite

2) Use list of objects
'''
from prog9a import student
n = int(input('Enter number of students: '))
a = [student() for i in range(n)]
for s in a:
    s.get()
for s in a:
    s.compute()
for s in a:
    print(s.__dict__)
'''
4) Write a program to add, subtract, multiply and divide two rational numbers

1) 1st rational number ---> 2/3
   2nd rational number ---> 5/9
   What is the sum? ---> 2/3 + 5/9 = (18 + 15)/27 = 33/27 = 11/9
   What is the difference? ---> 2/3 - 5/9 = (18 - 15)/27 = 3/27 = 1/9
   What is the product? ---> 2/3 * 5/9 = 10/27 = 10/27
   What is the division? ---> 2/3 / 5/9 = 2/3 * 9/5 = 18/15 = 6/5 ---> Successful division

2) 1st rational number ---> 2/3
   2nd rational number ---> 0/9
   What is the sum? ---> 2/3 + 0/9 = (18 + 0)/27 = 18/27 = 2/3
   What is the difference? ---> 2/3 - 0/9 = (18 - 0)/27 = 18/27 = 2/3
   What is the product? ---> 2/3 * 0/9 = 0/27 = 0/27 ---> Simplification is not required because numerator is 0
   What is the division? ---> 2/3 / 0/9 = 2/3 * 9/0 = 18/0 ---> Division is not permitted

3) When is simplification needed? ---> When numerator is non-zero
'''
import math
class Rat:
    def get(self):
        self.nr = int(input('Enter numerator: '))
        self.dr = int(input('Enter denominator: '))
        self.test()
    def test(self):
        while self.dr == 0:
            self.dr = int(input('Denominator cannot be zero. Re-enter: '))
    def __str__(self):
        return f'{self.nr} / {self.dr}'
    def add(self, a, b):
        self.nr = (a.nr * b.dr) + (b.nr * a.dr)
        self.dr = a.dr * b.dr
        self.simplify()
    def sub(self, a, b):
        self.nr = (a.nr * b.dr) - (b.nr * a.dr)
        self.dr = a.dr * b.dr
        self.simplify()
    def mul(self, a, b):
        self.nr = a.nr * b.nr
        self.dr = a.dr * b.dr
        self.simplify()
    def div(self, a, b):
        self.nr = a.nr * b.dr
        self.dr = a.dr * b.nr
        self.simplify()
    def simplify(self):
        if self.nr != 0:
            common = math.gcd(self.nr, self.dr)
            self.nr //= common
            self.dr //= common

a, b, c, d, e, f = Rat(), Rat(), Rat(), Rat(), Rat(), Rat()
a.get()
b.get()
c.add(a, b)
d.sub(a, b)
e.mul(a, b)
print('Sum:', c)
print('Difference:', d)
print('Product:', e)
if b.nr != 0:
    f.div(a, b)
    print('Division:', f)
else:
    print('Division is not permitted')
'''
5) dir() function demo program (Home work)
from prog10a import Rat
a = Rat()
a.nr = 22
a.dr = 7
print(dir(Rat)) # Returns list of all class attributes and methods including add, div, get, mul, etc.
print(dir(a)) # Returns list of all class attributes plus instance attributes 'nr' and 'dr'
'''
'''
6) Find outputs (Home work)
class Rat:
    def m1():
        pass
#End of the class
a = Rat()
a.nr = 22
print(hasattr(a, 'nr')) # True
print(hasattr(a, 'dr')) # False
print(hasattr(a, 'm1')) # True
print(hasattr(a, 'm2')) # False
print(hasattr(Rat, 'm1')) # True
print(hasattr(Rat, 'm2')) # False
print(hasattr(Rat, 'nr')) # False (nr is an instance variable, not class variable)
'''
'''
7) Find outputs (Home work)
class Cat:
    def talk(self): print('Meow Meow Meow ....')
class Dog:
    def bark(self): print('Bhow Bhow Bhow ....')
class Goat:
    def talk(self): print('Mehar Mehar Mehar ....')
#End of the classes
a = [Cat(), Dog(), Goat()]
for x in a:
    if hasattr(x, 'talk'): x.talk()
    else: x.bark()
# Meow Meow Meow ....
# Bhow Bhow Bhow ....
# Mehar Mehar Mehar ....
'''
'''
8) Find outputs (Home work)
class c1:
    pass
#End of the class
a = c1()
a.x = 10
varname = 'y' 
value = 20    
setattr(a, varname, value)
print(a.__dict__) # {'x': 10, 'y': 20}
print(a.x) # 10
# Iteration 1 (x): 10
# Iteration 2 (y): 20
# Iteration 3 (z): Invalid variable name : z (getattr fails as 'z' doesn't exist)
'''
'''
9) (Home work) Write a  program to convert a dictionary {'Empno' : 25 , 'Ename' : 'Rama Rao' , 'Sal' : 10000.0} to Emp class object
i.e. object should contain empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint: Use setattr() and getattr() functions
'''
class Emp:
    pass
d = {'Empno' : 25, 'Ename' : 'Rama Rao', 'Sal' : 10000.0}
e = Emp()
for k, v in d.items():
    setattr(e, k, v)
for k in d.keys():
    print(f'{k} : {getattr(e, k)}')
'''
10) How to reuse mod1? (Home work)
print('Hello')
import mod1 
# Hyd
# Sec
# Cyb
print(mod1.x) # 25
mod1.f1() # Function
obj = mod1.c1()
obj.m1() # Method
print('Bye')
'''
'''
11) Find outputs (Home work)
import runpy
print('Before')
runpy.run_module('mod1')
# Hyd
# Sec
# Cyb
print('After')
'''
'''
12) How to use members of cal module with from statement? (Home work)
from cal import *
print('Begin')
print(x) # 100
print(y) # 200
print(add(10, 7)) # 17
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
print(div(10, 7)) # 1.4285714285714286
obj = c1()
obj.m1() # m1 method
'''
'''
13) How to import only variable 'x' , functions add() and mul() and class c1 of cal module? (Home work)
from cal import x, add, mul, c1
print('Begin')
print(x) # 100
# print(y) # Error as name 'y' is not defined (not imported)
print(add(10, 7)) # 17
# print(sub(10, 7)) # Error as name 'sub' is not defined (not imported)
print(mul(10, 7)) # 70
obj = c1()
obj.m1() # m1 method
'''
'''
14) Module Alias
import cal as c
print('Begin')
print(c.x) # 100
print(c.y) # 200
print(c.add(10, 7)) # 17
print(c.sub(10, 7)) # 3
print(c.mul(10, 7)) # 70
print(c.div(10, 7)) # 1.4285714285714286
obj = c.c1()
obj.m1() # m1 method
'''
'''
15) Member Alias
from cal import x as v1, add as f1, mul as f2, c1 as cls1
print(v1) # 100
print(f1(10, 7)) # 17
print(f2(10, 7)) # 70
obj = cls1()
obj.m1() # m1 method
'''
'''
16) Find outputs (Home work)
x = 30
def disp():
    print('disp function of same module ')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
from mod2 import *
from mod1 import *
print(x) # 10 (Last imported 'x' from mod1 overrides others)
disp() # disp function of mod1
a = c1()
a.m1() # m1 method of class c1 in mod1
'''
'''
17) Find outputs (Home work)
from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp function of same module ')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x) # 30 (Local definition overrides imported definitions)
disp() # disp function of same module
a = c1()
a.m1() # m1 method of class c1 in same module
'''
'''
18) How to use members of all the 3 modules(mod1 , mod2 and current module) with import statement?
import mod1, mod2
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(mod1.x) # 10
mod1.disp() # disp function of mod1
mod1.c1().m1() # m1 method of class c1 in mod1

print(mod2.x) # 20
mod2.disp() # disp function of mod2
mod2.c1().m1() # m1 method of class c1 in mod2

print(x) # 30
disp() # disp function of same module
c1().m1() # m1 method of class c1 in same module
'''
'''
19) How to use members of all the three modules with from statement?
from mod1 import x as x1, disp as d1, c1 as cls1
from mod2 import x as x2, disp as d2, c1 as cls2
x = 30
def disp():
    print('disp function of same module')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x1) # 10
d1() # disp function of mod1
cls1().m1() # m1 method of class c1 in mod1

print(x2) # 20
d2() # disp function of mod2
cls2().m1() # m1 method of class c1 in mod2

print(x) # 30
disp() # disp function of same module
c1().m1() # m1 method of class c1 in same module
'''
'''
21) Find outputs (Home work)
print('Begining of mod2')
import mod1
# One
# Two
# Three
# Seven
# Eight
# Nine
print('End of mod2')
'''
'''
22) Find outputs (Home work)
import cal
print(cal.x) # 100
print(cal.y) # 200
print(cal.add(10, 7)) # 17
print(cal.sub(10, 7)) # 3
print(cal.mul(10, 7)) # 70
print(cal.div(10, 7)) # 1.4285714285714286
a = cal.c1()
a.m1() # m1 method
'''
'''
23) Find outputs (Home work)
from cal import y, sub, mul
# print(x) # Error as name 'x' is not defined (x was not imported)
print(y) # 200
# print(add(10, 7)) # Error as name 'add' is not defined (add was not imported)
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
# print(div(10, 7)) # Error as name 'div' is not defined (div was not imported)
# a = c1() # Error as name 'c1' is not defined (c1 was not imported)
'''