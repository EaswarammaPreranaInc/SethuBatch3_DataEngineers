#1
'''
Repeat prog10a with 3 objects
Eg:  c = a + b
	 print c
	 c = a - b
	 print c
	 c = a * b
	 print c
	 c = a / b
	 print c
Hint:  Import Rat class defined in prog10a but do not define Rat class again
'''
from prog10a import rat

a = rat()
b = rat()
c = rat()

a.get()
b.get()

c = rat()
c.add(a, b)
print('c  =  a  +  b  :  ' , c)

c = rat()
c.sub(a, b)
print('c  =  a  -  b  :  ' , c)

c = rat()
c.mul(a, b)
print('c  =  a  *  b  :  ' , c)

c = rat()
if b.nr != 0:
	c.div(a, b)
	print('c  =  a  /  b  :  ' , c)
else:
	print('Division  is  not  possible  (b  is  0)')



#2
'''
Repeat prog10a with list of 6 objects
Hint:  import Rat class defined in prog10a but do not rewrite the class again
What are the object names ? --->  a[0] , a[1] , a[2] , .....a[5]
'''
from prog10a import rat

a = [rat() for _ in range(6)]

# Read 2 rational numbers: a[0] and a[1]
a[0].get()
a[1].get()

# a[2] = a[0] + a[1]
a[2] = rat()
a[2].add(a[0], a[1])
print('a[2]  =  a[0]  +  a[1]  :  ' , a[2])

# a[3] = a[0] - a[1]
a[3] = rat()
a[3].sub(a[0], a[1])
print('a[3]  =  a[0]  -  a[1]  :  ' , a[3])

# a[4] = a[0] * a[1]
a[4] = rat()
a[4].mul(a[0], a[1])
print('a[4]  =  a[0]  *  a[1]  :  ' , a[4])

# a[5] = a[0] / a[1]  (if b != 0)
a[5] = rat()
if a[1].nr != 0:
	a[5].div(a[0], a[1])
	print('a[5]  =  a[0]  /  a[1]  :  ' , a[5])
else:
	print('Division  by  zero  is  not  possible')



#3
# Find outputs (Home work)
import mod1
import mod1
import mod1
# only first import runs mod1 code; next two imports do nothing (module already in sys.modules).



#4
# reload() function demo program (Home work)
import importlib
import mod1
print()
importlib.reload(mod1)
print()
importlib.reload(mod1)
importlib.reload('mod1')
# Error as reload() argument must be a module
reload(mod1)
# Error as name 'reload' is not defined



#5
# Find outputs (Home work)
import sys , time , math
print(dir(sys))
print()
print()
print(dir(time))
print()
print(dir(math))
# all attribute names of each module printed as lists.



#6
# Find outputs (Home work)
import cal
print(dir(cal)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']



#7
# Find outputs (Home work)
x = 25
def disp():
	print('Hello')
class c1:
	def m1(self):
		pass
print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'cal', 'c1', 'disp', 'x']
print(type(dir())) # <class 'list'>
print(type(dir)) # <class 'builtin_function_or_method'>



#8
'''
Write a program to print all the members of cal module without environment variables
1) What is the result of '_name'.startswith('_') ? ---> True
2) What is the result of '_spec'.endswith('_') ? ---> True
3) What is the result of 'spec_'.startswith('_') ? ---> False
4) a = []
   Append all the elements of list returned by dir() function to list 'a' except environment variables
'''
import cal
a = []
for n in dir(cal):
	if not n.startswith('_'):
		a.append(n)
print(a) # ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']



#9
# Find outputs
print(dir())
print()
import cal
print()
print(dir())
# 1st print: names before importing cal (without cal)
# 2nd print: names after importing cal (now cal is in global namespace)



#10
# Find outputs
print(dir())
print()
from cal import *
print()
print(dir())
# 1st print: current global names before import *
# 2nd print: after from cal import *: all cal’s public names (add, sub, mul, div, c1, x, y) added to globals



#11
# Find outputs
print(dir())
print()
from cal import add , mul , x
print()
print(dir())
# 1st print: globals before the import
# 2nd print: globals plus add, mul, x from cal.



#12
# sys.path demo program
import sys
print('Original sys.path')
for x in sys.path:
	print(x)
print(len(sys.path))
import cal
# Prints each sys.path entry, then its length, then nothing extra (cal is found in available path).



#13
# Save sample.py module in c:\\sairam folder before the program is executed (Home work)
import sys
import importlib
# How to print number of directories (or) folders in sys.path
print('Before:',len(sys.path))
# How to append c:\sairam folder to sys.path
sys.path.append('c:\\sairam')
# How to print number of directories (or) folders in sys.path
print('After:',len(sys.path))
# How to print object 'x' of sample module which is in c:\\sairam folder
import sample
print(sample.x)
# How to call function f1() of sample module which is in c:\\sairam folder
sample.f1()
# How to call method m1() of class c1 of sample module which is in c:\\sairam folder
obj = sample.c1()
obj.m1()