#Apr 08 Mod-3 Homeworks


print('Hello')
import mod1 # This will print all statements that include print("Hyd")
#Hyd <next line> Sec <next line> Cyb
print(mod1.x) # This will print variable x of mod1
#25
mod1.f1() # This line will call f1 function of mod1
#Function
a = mod1.c1() # This will create object of c1 class of mod1

a.m1() # This line will call method1 of class c1
#Method
print('Bye') #Bye

import runpy
print('Before') # Before
runpy.run_module('mod1') # This will run the module
#Hyd <next line> Sec <next line> Cyb
print('After') # After

from cal import *
print('Begin') # Begin
print(x) # 100
print(y) # 200
print(add(10, 7)) # 17
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
print(div(10, 7)) # 1.4285
obj = c1()
obj.m1() # m1 method

from cal import x, add, mul, c1
print('Begin')
print(x) # 100
print(y) # Error, as name 'y' is not defined and not imported from other module
print(add(10, 7)) # 17
print(sub(10, 7)) # Error as name 'sub' is not defined and not imported from other module
print(mul(10, 7)) # 70
obj = c1()
obj.m1() # m1 method


import cal as c
print('Begin') # Begin
print(c.x) # 100
print(c.y) # 200
print(c.add(10, 7)) # 17
print(c.sub(10, 7)) # 3
print(c.mul(10, 7)) # 70
print(c.div(10, 7)) # 1.4285
obj = c.c1()
obj.m1() # m1 method

from cal import x as x1, add as a1, mul as m1, c1 as cls1
print(x1) # 100
print(a1(10, 7)) # 17
print(m1(10, 7)) # 70
obj = cls1()
obj.m1()

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

from mod1 import *
from mod2 import *
x = 30
def disp():
    print('disp function of same module ')
class c1:
    def m1(self):
        print('m1 method of class c1 in same module')
print(x) # 30 
disp() # disp function of same module
a = c1()
a.m1() # m1 method of class c1 in same module

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

print('Begining of mod2') # Begining of mod2
import mod1
# One
# Two
# Three
# Seven
# Eight
# Nine
print('End of mod2') # End of mod2

import cal
print(cal.x) # 100
print(cal.y) # 200
print(cal.add(10, 7)) # 17
print(cal.sub(10, 7)) # 3
print(cal.mul(10, 7)) # 70
print(cal.div(10, 7)) # 1.4285714285714286
a = cal.c1()
a.m1() # m1 method

from cal import y, sub, mul
print(x) # Error as name 'x' is not defined and  not imported
print(y) # 200
print(add(10, 7)) # Error as name 'add' is not defined and it was not imported
print(sub(10, 7)) # 3
print(mul(10, 7)) # 70
print(div(10, 7)) # Error as name 'div' is not defined and it was not imported
a = c1() # Error as name 'c1' is not defined and it was not imported


#Apr 09 Homeworks

class Rat:
	def _init_(self , nr1 = 22, dr1 = 7):
		self.nr = nr1
		self.dr = dr1
	def _str_(self):
		return F'{self.nr} / {self.dr}'
#end of the class
a = Rat()
b = Rat(9)
c = Rat(5, 8)
d = Rat(dr1 = 9)
e = Rat(dr1 = 3 , nr1 = 2)
x = eval(input('Enter numerator : '))  # Assume that input is 11
y = eval(input('Enter Denominator : '))   # Assume that input is 15
f = Rat(x , y)
print('a : ' , a)   # a :  22 / 7
print('b : ' , b)   # b :  9 / 7
print('c : ' , c)   # c :  5 / 8
print('d : ' , d)   # d :  22 / 9
print('e : ' , e)   # e :  2 / 3
print('f : ' , f)   # f :  11 / 15
c._init_()
print('c : ' , c)   # c :  22 / 7, as it uses default 22/7
a._init_(3.8 , 4.6)
print('a : ' , a)   # a :  3.8 / 4.6
g = Rat(nr1 = 9 , 5) #Error, because positional argument follows keyword argument
h = Rat(nr = 9 , dr = 5) #Error as Rat.__init__() got an wrong  argument 'nr'

class Date:
	def _init_(self , dd1 , mm1 , yy1):
		self.dd = dd1
		self.mm = mm1
		self.yy = yy1
# End of the class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a : ' , a._dict_)   # a :  {'dd': 15, 'mm': 8, 'yy': 1947}
print('b : ' , b._dict_)   # b :  {'dd': 26, 'mm': 1, 'yy': 1950}
print('c : ' , c._dict_)   # c :  {'dd': 19, 'mm': 7, 'yy': 1985}
d = Date() #Error as Date.__init__() requires 3 positional arguments: 'dd1', 'mm1', 'yy1'
e = Date(dd = 30 , mm = 4 , yy = 2022) #Error as Date.__init__() got an wrong keyword arguments 'dd', 'mm', 'yy'
f = Date(dd1 = 26 , mm1 = 8 , 2023) #Error,  as positional argument follows keyword argument


class c1:
	def _init_(self):
		print('c1 class constructor')
		return 25
class c2:
	def _init_(self):
		print('c2 class constructor')
		return None
class c3:
	def _init_(self):
		print('c3 class constructor')
# End of the class
a = c1()   # c1 class constructor
b = c2()   # c2 class constructor
print(b)   # <__main__.c2 object at 0x...>
print(b._init_()) # c2 class constructor followed by None
c = c3()   # c3 class constructor
print(c._init_()) # c3 class constructor followed by None

class c1:
	def _init_(self):
		print('Constructor')
		b = c1()   
a = c1() # Error , because it runs for infinite times

class c1:
	def _init_(self):
		print('Constructor')
		self.x = 10
		self.y = 20
class c2:
	def init(self):
		print('Method')
		self.x = 30
		self.y = 40
a = c1()   # Constructor
print(a._dict_)   # {'x': 10, 'y': 20}
b = c2()  
print(b._dict_)   # {}
b.init()   # Method
print(b._dict_)   # {'x': 30, 'y': 40}


class c1:
	def _init_(self):
		self.a = 10
	def m1(self):
		self.b = 20
# End of class c1
class c2:
	def m3(self):
		x.e = 50   # x is not defined in this scope.
# End of class c2
def f1():
	x.c = 30   # x is not defined in this scope.
# End of function f1
x = c1()   # x is created here.
print(x._dict_)   # {'a': 10}
x.m1()   # Adds b = 20 to x.
print(x._dict_)   # {'a': 10, 'b': 20}
#f1() #Error: name 'x' is not defined
x.d = 40   # Adds d = 40 to x.
print(x._dict_)   # {'a': 10, 'b': 20, 'd': 40}
y = c2()   
y.m3()   # m3 modifies x.e 
print(x._dict_)   # {'a': 10, 'b': 20, 'd': 40, 'e': 50}
z = c1()   # z is a new instance.
print(z._dict_)   # {'a': 10}

class c1:
	def _init_(self):
		self.x = 10
		self.y = 20
		self.z = 30
#end of the class
a = c1()
b = c1()
print(a._dict_)   # {'x': 10, 'y': 20, 'z': 30}
print(b._dict_)   # {'x': 10, 'y': 20, 'z': 30}
del a.x
del b.y
print(a._dict_)   # {'y': 20, 'z': 30}
print(b._dict_)   # {'x': 10, 'z': 30}
print(a.x) # Error as 'c1' object has no value 'x'
print(b.y) # Error as 'c1' object has no value 'y'

class c1:
	def _init_(self):
		print('1st constructor')
	def _init_(self):
		print('2nd constructor')
	def _init_(self):
		print('3rd constructor')
# End of the class
a = c1() # 3rd constructor


class c1:
	def _init_(self):
		print('No argument constructor')
	def _init_(self , x):
		print('single argument constructor : ' , x)
	def _init_(self , x , y):
		print('Two argument constructor : ' , x , y)
# End of the class
a = c1(10 , 20) # Two argument constructor : 10 20
b = c1(30) # single argument constructor : 30
c = c1() # No argument constructor

class c1:
	def _init_(self):
		print('No argument constructor')
	def _init_(self , x):
		print('single argument constructor : ' , x)
	def _init_(self , x = 100 , y = 200):
		print('Two argument constructor : ' , x , y)
# End of the class
a = c1(10 , 20) # Two argument constructor : 10 20
b = c1(30) # Two argument constructor : 30 200
c = c1() # Two argument constructor : 100 200


def f1():
	print('Function')
	return 25
class f1:
	def _init_(self):
		print('Constructor')
# End of the class
a = f1() # Constructor
print(a) # Type and address of object a

class c1:
	def _init_(self):
		print('Constructor')
def c1():
	print('Function')
#end of the class
a = c1() # Function
print(a) # None, because function returns default value None

class c1:
	def _init_(self):
		print('Constructor')
def c1(x):
	print('Function : ' , x)
# End of class c1
# a = c1() # Error as c1() missing 1 required positional argument: 'x'
b = c1(25) # Function : 25
print(b)   # None 

from prog9a import c1
class c1:
	def _init_(self):
		print('c1 class of prog9b')
a = c1() # c1 class of prog9b


# Find outputs (Home work)
class c1:
	def _init_(self):
		print('c1 class of prog9c')
from prog9a import c1
a = c1() # c1 class of prog9a

# How to use both the classes (i.e. c1 of prog9a and c1 of current program)
from prog9a import c1 as c19a #How to import class c1 from prog9a
class c1:
	def _init_(self):
		print('c1 class of prog9d')
current = c1() # How to create c1 class object of current module # Output: c1 class of prog9d
c9a = c19a()

'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)
'''

import prog9a 

class c1:
    def _init_(self):
        print('c1 class of prog9e')

# How to create c1 class object of current module
obj_current = c1()
obj_current._init_() # c1 class of prog9e

# How to create c1 class object of prog9a
obj_imported= prog9a.c1()
obj_imported._init_() # c1 class of prog9a