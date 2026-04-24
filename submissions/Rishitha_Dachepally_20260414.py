'''
Repeat  prog10a  with  3  objects
Hint:  Import  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class  again
'''
import prog10a
a = prog10a.Rat()
b = prog10a.Rat()
c = prog10a.Rat()
a.get()
b.get()
c.add(a, b); print(c) # Sum
c.sub(a, b); print(c) # Difference
c.mul(a, b); print(c) # Product
if b.nr != 0:
    c.div(a, b); print(c) # Division
else:
    print('Division  is  not  permitted')

# -----------------------------------------------------------------------------------------------------

'''
Repeat  prog10a  with  list  of  6  objects
What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
import prog10a
a = []
for i in range(6):
    a.append(prog10a.Rat()) # Correct way to store Rat objects in list 'a'

a[0].get(); a[1].get()
a[2].add(a[0], a[1])
a[3].sub(a[0], a[1])
a[4].mul(a[0], a[1])
if a[1].nr != 0:
    a[5].div(a[0], a[1])
    print(a[5]) # 11 / 15
else:
    print('Division  is  not  permitted')

# -----------------------------------------------------------------------------------------------------

# mod1.py (Home  work)
print('Hyd')  # Hyd
print('Sec')  # Sec
print('Cyb')  # Cyb

# Find outputs (Home  work)
import mod1 # Hyd, Sec, Cyb (Only prints once per session)
import mod1 
import mod1 

# -----------------------------------------------------------------------------------------------------

# reload() function demo program (Home  work)
import importlib
import mod1 # Hyd, Sec, Cyb
print()
importlib.reload(mod1) # Hyd, Sec, Cyb
print()
importlib.reload(mod1) # Hyd, Sec, Cyb
# importlib.reload('mod1') # Error because argument must be a module object, not a string
# reload(mod1) # Error because reload is not in the global namespace; must use importlib.reload()

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home  work) - dir() on modules
import sys, time, math
# print(dir(sys)) # List of all members (functions/variables) in sys module
# print(dir(time)) # List of all members in time module
# print(dir(math)) # List of all members in math module

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home  work) - dir() in local scope
x = 25
def disp(): print('Hello')
class c1:
    def m1(self): pass

print(dir()) # ['c1', 'disp', 'x', ...] (plus environment variables)
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>

# -----------------------------------------------------------------------------------------------------

'''
Write a program to print all members of cal module without environment variables
'''
import cal
a = []
for x in dir(cal):
    if x.startswith('__') and x.endswith('__'):
        continue
    a.append(x)
print(a) # List of user-defined members in cal module

# -----------------------------------------------------------------------------------------------------

# Find outputs - Sequence of dir()
print(dir()) # List of environment variables (initially)
import cal
print(dir()) # List of environment variables + 'cal'

# Find outputs - from...import *
from cal import * print(dir()) # Environment variables + all members of cal (add, sub, x, etc.)

# Find outputs - from...import specific
from cal import add, mul, x
print(dir()) # Environment variables + ['add', 'mul', 'x']

# -----------------------------------------------------------------------------------------------------

# sys.path demo program
import sys
print('Original sys.path')
for x in sys.path:
    print(x) # List of search directories (current dir, site-packages, etc.)
print(len(sys.path)) # e.g., 6

# -----------------------------------------------------------------------------------------------------

# External Module Access (Home work)
import sys
# Assume sample.py is in D:\Python\
sys.path.append('D:\\Python') # How to add new directory to search path
print(len(sys.path)) # 7

# import sairam # Assume sairam.py exists in the added path
# print(sairam.x)
# sairam.f1()
# obj = sairam.c1(); obj.m1()