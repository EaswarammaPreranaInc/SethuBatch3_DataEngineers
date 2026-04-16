#1
'''
Write a program to overload + , - , * and / operators on complex class objects without using pre-defined
complex object
1) First rational number ---> 3 + 4i
   Second rational number ---> 5 + 6i
   What is the sum ? ---> 8 + 10i
   What is the difference ? ---> -2 - 2i
   What is the product ? ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 = -9 + 38i
   What is the division ? ---> (3 + 4i) / (5 + 6i) = (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) = (15 - 18i + 20i + 24) / (25 + 36) = 39 / 61 + 2i / 61
'''
import math
class complex:
	def get(self):
		# How to read real and imag
		self.real = float(input('Enter real : '))
		self.imag = float(input('Enter imag : '))
	def _str_(self):
		# How to return real and imag in the form of 3 + 4i (or) 3 - 4i
		if self.imag >= 0:
			return F'{self.real} + {self.imag}i'
		else:
			return F'{self.real} - {abs(self.imag)}i'
	def _add_(a , b):
		# How to add objects a and b
		c = complex()
		c.real = a.real + b.real
		c.imag = a.imag + b.imag
		return c
	def _sub_(a , b):
		# How to subtract objects a and b
		c = complex()
		c.real = a.real - b.real
		c.imag = a.imag - b.imag
		return c
	def _mul_(a , b):
		# How to multiply objects a and b
		c = complex()
		c.real = a.real * b.real - a.imag * b.imag
		c.imag = a.real * b.imag + a.imag * b.real
		return c
	def _truediv_(a , b):
		# How to divide objects a and b
		c = complex()
		den = b.real * b.real + b.imag * b.imag
		c.real = (a.real * b.real + a.imag * b.imag) / den
		c.imag = (a.imag * b.real - a.real * b.imag) / den
		return c
# End of the class
# How to create two complex class objects
a = complex()
b = complex()
# How to read inputs into 1st object
a.get()
# How to read inputs into 2nd object
b.get()
# How to print the results
print('Sum : ' , a + b)
print('Difference : ' , a - b)
print('Product : ' , a * b)
print('Division : ' , a / b)



#2
'''
Overload > , < , == , >= , <= , != on Rational class objects
1) Let object 'a' contain 2 / 3 and object 'b' contain 5 / 9
   What is the result of a > b ? ---> True due to 18 > 15
   What is the result of a < b ? ---> False due to 18 is not < 15
   What is the result of a == b ? ---> False due to 18 is not = 15
   What is the result of a >= b ? ---> True due to 18 >= 15
   What is the result of a <= b ? ---> False due to 18 is not <= 15
   What is the result of a != b ? ---> True due to 18 != 15
2) Imp point is cross product
3) What is the method call to __gt__() method ? ---> a > b (or) a.__gt__(b)
   What is the method call to __lt__() method ? ---> a < b (or) a.__lt__(b)
   What is the method call to __eq__() method ? ---> a == b (or) a.__eq__(b)
   What is the method call to __ge__() method ? ---> a >= b (or) a.__ge__(b)
   What is the method call to __le__() method ? ---> a <= b (or) a.__le__(b)
   What is the method call to __ne__() method ? ---> a != b (or) a.__ne__(b)
'''
import math
class Rat:
	def get(self):
		# How to read numerator and denominator into object
		self.nr = int(input('Enter numerator : '))
		self.dr = int(input('Enter denominator : '))
		while self.dr == 0:
			self.dr = int(input('Denominator can not be zero and re-enter : '))
	def _gt_(self , b):
		# return true when rational number in object self > that of 'b' and false otherwise
		return self.nr * b.dr > b.nr * self.dr
	def _lt_(self , b):
		# return true when rational number in object self < that of 'b' and false otherwise
		return self.nr * b.dr < b.nr * self.dr
	def _eq_(self , b):
		# return true when rational numbers in objects self and 'b' are same and false otherwise
		return self.nr * b.dr == b.nr * self.dr
	def _ge_(self , b):
		# return true when rational number in object self >= that of 'b' and false otherwise
		return self > b or self == b
	def _le_(self , b):
		# return true when rational number in object self <= that of 'b' and false otherwise
		return self < b or self == b
	def _ne_(self , b):
		# return true when rational numbers in objects self and 'b' are different and false otherwise
		return not (self == b)
# End of the class
# How to create two Rat class objects 'a' and 'b'
a = Rat()
b = Rat()
# How to read 1st rational number into object 'a'
a.get()
# How to read 2nd rational number into object 'b'
b.get()
if a > b:
	print('>')
if a < b:
	print('<')
if a == b:
	print('==')
if a >= b:
	print('>=')
if a <= b:
	print('<=')
if a != b:
	print('!=')



#3
# Find outputs (Home work)
class outer:
	def _init_(self):
		print('Outer class constructor')
	def m1(self):
		print('Outer class method')
	class inner:
		def _init_(self):
			print('Inner class constructor')
		def m1(self):
			print('Inner class method')
#end of the class
# How to call m1() method of outer class
o = outer()
o.m1()
# How to call m1() method of inner class
i = outer.inner()
i.m1()
# How to call m1() method of inner class in another way
i = outer().inner()
i.m1()
# How to call m1() method of inner class in one more way
o = outer()
i = o.inner()
i.m1()
# i = inner()  -> this is invalid; you must qualify with outer
# i = inner()  would give Error.



#4
# Find outputs (Home work)
class emp:
	def _init_(self):
		# How to initialize empno , ename , sal of object self to 25 , 'Rama Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		# How to create date class object
		self.dt = self.date()
	def disp(self):
		# How to print empno , ename , sal of object self
		print('empno :' , self.empno)
		print('ename :' , self.ename)
		print('sal :' , self.sal)
		# How to call disp() method of date class
		self.dt.disp()
	class date:
		def _init_(self):
			# How to initialize dd , mm , yy of object self to 15 , 8 , 1947
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			# How to print dd , mm , yy of object self
			print('dd : mm : yy ->' , self.dd , self.mm , self.yy)
# End of the class
# How to call disp() method of emp class
e = emp()
e.disp()



#5
# Find outputs (Home work)
class outer:
	def _init_(self):
		# How to initialize variable 'x' of object self to 25
		self.x = 25
		# How to create inner1 class object
		self.i1 = self.inner1()
		# How to create inner2 class object
		self.i2 = self.inner2()
	def disp(self):
		print(self.x)
	class inner1:
		def disp(self):
			print('1st inner class method')
	class inner2:
		def disp(self):
			print('2nd inner class method')
#end of the class
# How to call disp() method of outer class
o = outer()
o.disp()
# How to call disp() method of inner1 class
o.i1.disp()
# How to call disp() method of inner2 class
o.i2.disp()



#6
# Find outputs (Home work)
class c1:
	def _init_(self):
		print('outer class c1 constructor')
	class c2:
		def _init_(self):
			print('inner class c2 constructor')
#end of the class
class c2:
	def _init_(self):
		print('outer class c2 constructor')
#end of the class
# How to create c1 class object
p = c1()
# How to create inner c2 class object
q = c1.c2()
# How to create outer c2 class object
r = c2()



#7
# Find outputs (Home work)
class c2:
	def _init_(self):
		print('outer class constructor')
	class c2:
		def _init_(self):
			print('inner class constructor')
#end of the class
# How to create outer c2 class object
a = c2()
# How to create inner c2 class object
b = c2.c2()
# How to create inner c2 class object in another way
c = a.c2()
# How to create inner c2 class object in one more way
d = c2().c2()