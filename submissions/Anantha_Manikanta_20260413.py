'''
1) # Find outputs
import sys
class c1:
	pass
# End of the class
a = b = c = d = c1()
print(sys.getrefcount(b))  # at least 5
print(sys.getrefcount(c1())) # at least 2
print(sys.getrefcount(352)) # some number ≥1
print(sys.getrefcount([10 , 20 , 15 , 18])) # 2 
print(sys.getrefcount(10.8)) # ≥1
print(sys.getrefcount({10 , 20 , 15 , 18})) # 2 
print(sys.getrefcount('Hyd')) # ≥1
print(sys.getrefcount({10 : 20 , 30 : 40})) # 2 
print(sys.getrefcount((10 , 20 , 30 , 40)))
'''
'''
2) # Find outputs (Home work)
import sys
class Test:
	def _init_(self):
		print('Constructor : ' , id(self))
		return None
	def _del_(self):
		print('Destructor : ' , id(self))
		return 25
# End of the class
t = Test() # Constructor :  1000
print(t._init_()) # Constructor :  1000 <nextline> None 
print(sys.getrefcount(t)) # some number ≥3 
print(t._del_()) # Destructor :  2000 <nextline> 25
print(sys.getrefcount(t)) # same refcount 
print('Bye') # Bye 
'''
'''
3) # Tricky program
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
print('Program End')  # Program Begin <nextline> Function Begin <nextline> Object is created <nextline>  <__main__.c1 object at 0x1A3> <nextline> Function end <nextline> <__main__.c1 object at 0x123> <nextline> Program End <nextline> Object is lost
'''
'''
4) # Tricky program
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
print('Program End')  # Program Begin <nextline> Function Begin <nextline> Object is created <nextline> Function end <nextline> Program End
'''
'''
5)  # Tricky program
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
print('Program End')  #   # Program Begin <nextline> Function Begin <nextline> Object is created <nextline> Function end <nextline> None <nextline> Program End
'''
'''
6) # Most tricky program (Can not do figure)
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
print('program end')  # Program begin <nextline> c2 class object is created <nextline> c1 class object is created <nextline> End of c1 class constructor <nextline> End of c2 class constructor <nextline> program end
'''
'''
7) # Lucky object
# Find outputs (Home work)
class c1:
	def _del_(self):
		print('Destructor')
		global b
		b = self
a = c1()
del a
print('Hello')  # Destructor <nextline> Hello
'''
'''
8) Write a program to overload + , - , * and / operators on rational class objects
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
	def get(self):
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
'''
8) # Modify the following statements
a = rat()
b = rat()
c = rat()
d = rat()
e = rat()
f = rat()
a.get()
b.get()
# Assume user enters 5 and 9
c.add(a , b)
d.sub(a , b)
e.mul(a , b)
print('Sum : ', c)
print('Difference : ', d)
print('Product : ', e)
if b.nr != 0:
	f.div(a , b)
	print('Division : ', f)
else:
	print('Division is not permitted.')
'''
'''
9) # Is 10 + 20 a recursion ?
class c1:
	def _add_(a , b):
		print(10 + 20)
a = c1()
b = c1()
print(a + b) # 30 <nextline> # None
'''
'''
10) # Is x + y a recursion ? (Home work)
class c1:
	def _add_(a , b):
		x = c1()
		y = c1()
		print(x + y)
a = c1()
b = c1()
print(a + b) # 30 <nextline> None
'''
'''
11) # Find outputs
class c1:
	def _init_(self , y):
		self.x = y
	def _gt_(m , n):
		print('_gt_ method : ' , m.x , n.x)
# End of the class
a = c1(10)
b = c1(20)
print(a > b)  # _gt_ method :  10 20 <nextline> None
print(a < b) # no output
'''
'''
12) # Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ge_(m , n):
		print('_ge_ method : ' , m.x , n.x)
		return m.x > n.x
# End of the class
a = c1(10)
b = c1(20)
print(a >= b) # _ge_ method :  10 20 # False
print(a <= b)  # b >= a
'''
'''
13) # Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _eq_(m , n):
		print('_eq_ method : ' , m.x , n.x)
		return m.x == n.x
# End of the class
a = c1(10)
b = c1(20)
print(a == b) # _eq_ method :  10 20
# False (10 == 20 is False).
print(a != b)  # not (a == b)
'''
'''
14) # Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _eq_(m , n):
		print('_eq_ method : ' , m.x , n.x)
#end of the class
a = c1(25)
b = c1(25)
print(a == b) # _eq_ method :  25 25
print(a != b) # True
print(a.x != b.x) # False
'''
'''
15) # Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ne_(m , n):
		print('_ne_ method : ' , m.x , n.x)
		return m.x != n.x
#end of the class
a = c1(25)
b = c1(25)
print(a != b) # _ne_ method :  25 25 <nextline> False
print(a == b) # True
print(a is b) # False
'''
'''
16) # Find outputs (Home work)
class c1:
	def _init_(self , y):
		self.x = y
	def _ne_(m , n):
		print('_ne_ method : ' , m.x , n.x)
		return m.x != n.x
# End of the class
a = c1(10)
b = a
print(a != b) # _ne_ method :  10 10 <nextline> False
print(a == b) # True
'''
'''
17) # Is 10 > 20 a recursion ?
class c1:
	def _gt_(a , b):
		print(10 > 20)
		print(a > b)
a = c1()
b = c1()
print(a > b) # False
'''
'''
18) # Find outputs (Home work)
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
a > b # c1 class _gt_ method :  10 20
a < b # No output
m = c2(30)
n = c2(40)
a < m # m._gt_(a)
n < b # b._gt_(n)
'''
'''
19) Overload * operator to multiply two different class objects
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
print(a * b) _mul_ method of class c1<nextline> 200
print(b * a) # _mul_ method of class c2 <nextline> 200
'''
'''
20) Find outputs (Home work)
class c1:
	def _add_(x , y):
		return '_add_ method of class c1'
class c2:
	pass
#end of the class
a = c1()
b = c1()
print('a + b : ' , a + b) # a + b :  _add_ method of class c1
print('a + 7 : ' , a + 7) # a + 7 :  _add_ method of class c1
print(7 + a) # Error
print('7 + 8 : ' , 7 + 8) # 7 + 8 :  15
m = c2()
n = c2()
print(m + n) # Error
print('a + m : ' , a + m) # _add_ method of class c1
print(m + a) # Error
'''
'''
21) # Overload + operator such that numbers are added and strings are joined
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
print('Sum: ' , a + b) # Sum: 30
print('Join:', m + n) # Join: 1020
'''