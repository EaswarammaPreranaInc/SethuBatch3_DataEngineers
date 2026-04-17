#1
# Find outputs
import sys
class c1:
	pass
# End of the class
a = b = c = d = c1()
print(sys.getrefcount(b))
# at least 5 (b itself, a,b,c,d, and the temporary ref in sys.getrefcount); exact value depends on Python implementation.
print(sys.getrefcount(c1()))
# at least 2 (once for the object, once for the temp ref inside getrefcount)
print(sys.getrefcount(352))
# some number ≥1; depends on how many times 352 is reused in the interpreter (e.g. 3–4 or more).
print(sys.getrefcount([10 , 20 , 15 , 18]))
# 2 
print(sys.getrefcount(10.8))
# ≥1; depends on how many times 10.8 is reused in the interpreter.
print(sys.getrefcount({10 , 20 , 15 , 18}))
# 2 
print(sys.getrefcount('Hyd'))
# ≥1; may be higher due to string interning.
print(sys.getrefcount({10 : 20 , 30 : 40}))
# 2 
print(sys.getrefcount((10 , 20 , 30 , 40)))
# 2 



#2
# Find outputs (Home work)
import sys
class Test:
	def _init_(self):
		print('Constructor : ' , id(self))
		return None
	def _del_(self):
		print('Destructor : ' , id(self))
		return 25
# End of the class
t = Test()
# Constructor :  some_id
print(t._init_())
# Constructor :  some_id (again, same id) and followed by None (because __init__ returns None)
print(sys.getrefcount(t))
# some number ≥3 
print(t._del_())
# Destructor :  some_id followed by 25
print(sys.getrefcount(t))
# same refcount as before 
print('Bye')
# Bye 

#3
# Tricky program
# Find outputs (Home work)
class c1:
	def _init_(self):
		print('Object is created')
	def _del_(self):
		print('Object is lost')
# End of the class
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
#   Program Begin
#   Function Begin
#   Object is created
#   <__main__.c1 object at 0x...>
#   Function end
#   <__main__.c1 object at 0x...>
#   Program End
# At program exit: Object is lost (when b is destroyed).



#4
# Tricky program
# Find outputs (Home work)
class c1:
	def _init_(self):
		print('Object is created')
	def _del_(self):
		print('Object is lost')
# End of the class
def f1():
	print('Function begin')
	a = c1()
	print('Function end')
	return a
print('Program Begin')
f1()
print('Program End')
# Output:
#   Program Begin
#   Function begin
#   Object is created
#   Function end
#   Program End
# At program exit: Object is lost (f1() returns a, but it is not stored; refcount drops to 0).



#5
# Tricky program
# Find outputs (Home work)
class c1:
	def _init_(self):
		print('Object is created')
	def _del_(self):
		print('Object is lost')
# End of the class
def f1():
	print('Function begin')
	a = c1()
	print('Function end')
print('Program Begin')
b = f1()
print(b)
print('Program End')
# Output:
#   Program Begin
#   Function begin
#   Object is created
#   Function end
#   None (because f1 returns None by default)
#   Program End
# At program exit: Object is lost (a inside f1 is destroyed when f1 exits).



#6
# Most tricky program (Can not do figure)
# Circular reference (Home work)
class c1:
	def _init_(self , k):
		print('c1 class object is created')
		self.b = k
		print('End of c1 class constructor')
	def _del_(self):
		print('c1 class object is lost')
# End of class c1
class c2:
	def _init_(self):
		print('c2 class object is created')
		self.a = c1(self)
		print('End of c2 class constructor')
	def _del_(self):
		print('c2 class object is lost')
#End of class c2
print('Program begin')
x = c2()
print('program end')
# Output:
#   Program begin
#   c2 class object is created
#   c1 class object is created
#   End of c1 class constructor
#   End of c2 class constructor
#   program end
# Then at program exit (or when gc runs):
#   c2 class object is lost
#   c1 class object is lost



#7
# Lucky object
# Find outputs (Home work)
class c1:
	def _del_(self):
		print('Destructor')
		global b
		b = self
a = c1()
del a
print('Hello')
# Output:
#   Destructor (when del a runs)
#   Hello
# After that: b is still a live reference to the c1 object, so destructor does not print again.



#8
'''
Write a program to overload + , - , * and / operators on rational class objects
1) First rational number ---> 2 / 3
   Second rational number ---> 5 / 9
   Sum ---> 11 / 9
   Difference ---> 1 / 9
   Product ---> 10 / 27
   Division ---> 6 / 5
2) First rational number ---> 2 / 3
   Second rational number ---> 0 / 9
   Sum ---> 2 / 3
   Difference ---> 2 / 3
   Product ---> 0 / 27
   Division ---> not possible (denominator 0)
3) Modify the following program with operator overloading methods
4) Leave get() , test() , _str_() and simplify() methods unchanged
'''
import math
class rat:
	def get(self):  # Do not modify the method
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		self.test()
	def test(self): # Do not modify the method
		while self.dr == 0:
			self.dr = int(input('Denominator can not be zero and re-enter : '))
	def _str_(self):  # Do not modify the method
		return F'{self.nr} / {self.dr}'
	def add(self, a , b):  # Modify the method
		self.nr = a.nr * b.dr + a.dr * b.nr
		self.dr = a.dr * b.dr
		self.simplify()
	def sub(self, a , b):   # Modify the method
		self.nr = a.nr * b.dr - a.dr * b.nr
		self.dr = a.dr * b.dr
		self.simplify()
	def mul(self , a , b):   # Modify the method
		self.nr = a.nr * b.nr
		self.dr = a.dr * b.dr
		self.simplify()
	def div(self, a , b):   # Modify the method
		self.nr = a.nr * b.dr
		self.dr = a.dr * b.nr
		self.simplify()
	def simplify(self):   # Do not modify the method
		if self.nr != 0:
			g = math.gcd(self.nr, self.dr)
			self.nr = self.nr // g
			self.dr = self.dr // g
# End of the class
# Modify the following statements
a = rat()
b = rat()
c = rat()
d = rat()
e = rat()
f = rat()
a.get()
# Assume user enters 2 and 3
b.get()
# Assume user enters 5 and 9
c.add(a , b)
d.sub(a , b)
e.mul(a , b)
print('Sum : ' , c) # 11 / 9
print('Difference : ' , d) # 1 / 9
print('Product : ' , e) # 10 / 27
if b.nr != 0:
	f.div(a , b)
	print('Division : ' , f)
# 6 / 5
else:
	print('Division is not permitted.')



#9
# Is 10 + 20 a recursion ?
class c1:
	def _add_(a , b):
		print(10 + 20)
a = c1()
b = c1()
print(a + b)
# 30
# None (because __add__ returns None by default, so print prints None).



#10
# Is x + y a recursion ? (Home work)
class c1:
	def _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b)
# 30 (from inner print(x+y) calling __add__ again once)
# None (from outer print(a+b)).



#11
# Find outputs
class c1:
	def _init_(self , y):
		self.x = y
	def _gt_(m , n):
		print('_gt_ method : ' , m.x , n.x)
# End of the class
a = c1(10)
b = c1(20)
print(a > b)
# _gt_ method :  10 20
# None (no explicit return).
print(a < b)
# no output from __gt__ (because < is not overloaded),



#12
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ge_(m , n):
		print('_ge_ method : ' , m.x , n.x)
		return m.x > n.x
# End of the class
a = c1(10)
b = c1(20)
print(a >= b)
# _ge_ method :  10 20
# False (because 10 > 20 is False).
print(a <= b)  # b >= a
# b._ge_(a) is not called here; if not defined, may be False or NotImplemented.



#13
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _eq_(m , n):
		print('_eq_ method : ' , m.x , n.x)
		return m.x == n.x
# End of the class
a = c1(10)
b = c1(20)
print(a == b)
# _eq_ method :  10 20
# False (10 == 20 is False).
print(a != b)  # not (a == b)
# True (inversion of True/False from __eq__; if __ne__ not defined, Python does not(a==b)).



#14
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _eq_(m , n):
		print('_eq_ method : ' , m.x , n.x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b)
# _eq_ method :  25 25
# None (because __eq__ returns None by default),
print(a != b)
# True (not(a==b), and a==b is False).
print(a.x != b.x)
# False (25 != 25 is False).



#15
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ne_(m , n):
		print('_ne_ method : ' , m.x , n.x)
		return m.x != n.x
#end of the class
a = c1(25)
b = c1(25)
print(a != b)
# _ne_ method :  25 25
# False (25 != 25 is False).
print(a == b)
# True (because __ne__ returns False, so != is False, thus == is True).
print(a is b)
# False (a and b are different objects in memory).



#16
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ne_(m , n):
		print('_ne_ method : ' , m.x , n.x)
		return m.x != n.x
# End of the class
a = c1(10)
b = a
print(a != b)
# _ne_ method :  10 10
# False (10 != 10 is False).
print(a == b)
# True (a and b are same object).



#17
# Is 10 > 20 a recursion ?
class c1:
	def _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b)
# False (10 > 20)
# _gt_ method calls itself recursively once, then may hit recursion limit or raise RecursionError.



#18
# Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _gt_(p , q):
		print('c1 class _gt_ method : ' , p.x , q.x)
class c2:
	def _init_(self , y):
		self.x = y
	def _gt_(p , q):
		print('c2 class _gt_ method : ' , p.x , q.x)
# End of the class
a = c1(10)
b = c1(20)
a > b
# c1 class _gt_ method :  10 20
a < b
# No output if __lt__ not defined; may be NotImplemented or False.
m = c2(30)
n = c2(40)
a < m
# m._gt_(a) may be called; depends on how __gt__ is resolved between classes.
n < b
# b._gt_(n) may be called.



#19
# Overload * operator to multiply two different class objects
class c1:
	def _init_(self):
		self.empno = 25
		self.hr = 250
	def _mul_(x , y):
		print('_mul_ method of class c1')
		return 25 * 8
class c2:
	def _init_(self):
		self.empno = 25
		self.noh = 8
	def _mul_(x , y):
		print('_mul_ method of class c2')
		return 8 * 25
# End of the class
a = c1()
b = c2()
print(a * b)
# _mul_ method of class c1
# 200
print(b * a)
# _mul_ method of class c2
# 200



#20
# Find outputs (Home work)
class c1:
	def _add_(x , y):
		return '_add_ method of class c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b)
# a + b :  _add_ method of class c1
print('a + 7 : ' , a + 7)
# a + 7 :  _add_ method of class c1 (if __add__ is called; otherwise TypeError).
print(7 + a)
# Error if __radd__ not defined in c1; otherwise may call __radd__.
print('7 + 8 : ' , 7 + 8)
# 7 + 8 :  15
m = c2()
n = c2()
print(m + n)
# Error as no __add__ defined in c2.
print('a + m : ' , a + m)
# _add_ method of class c1 (if a.__add__ is called) or TypeError.
print(m + a)
# Error if no __radd__ in c1; otherwise may call __radd__.



#21
# Overload + operator such that numbers are added and strings are joined
class c1:
	def _init_(self , y):
		self.x = y
	def _add_(p , q):
		if isinstance(p.x , (int , float)) and isinstance(q.x , (int , float)):
			return p.x + q.x
		elif isinstance(p.x , str) and isinstance(q.x , str):
			return p.x + q.x
		else:
			return None
#end of the class
a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum: ' , a + b) # Sum:  30
print('Join:', m + n) # Join: 1020