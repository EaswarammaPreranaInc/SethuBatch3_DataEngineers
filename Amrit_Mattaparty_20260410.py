#1
# Public and Private members demo program
class Test:
	def _init_(self):
		# How to initialize public variable 'x' to 10
		self.x = 10
		# How to initialize private variable 'y' to 20
		self.__y = 20
	def m1(self):
		print('m1 method')
		# How to print variable 'x'
		print(self.x)
		# How to print private variable 'y'
		print(self.__y)
		# How to call private method m2()
		self.__m2()
		print('Back to m1 method')
	def __m2(self):
		print('__m2 method')
		# How to print variable 'x'
		print(self.x)
		# How to print private variable 'y'
		print(self.__y)
# End of the class
t = Test()
print('Outside')
# How to print variable 'x'
print(t.x)           # 10
# How to print variable 'y'
print(t._Test__y)    # 20 (name mangling)
# print(t.__y) # Error as 'Test' object has no attribute '__y'
print(t._dict_)      # {'x': 10, '_Test__y': 20}
# How to call method m1()
t.m1()               # m1 method, then __m2 method, then "Back to m1 method"
# How to call method m2()
# t.__m2() # Error as 'Test' object has no attribute '__m2'
print('End')



#2
# Find outputs
class c1:
	def _init_(self):
		# How to initialize public variable 'x' with 10
		self.x = 10
		# How to initialize private variable 'x' with 20
		self.__x = 20
		# How to initialize public dunder variable 'x' with 30
		self.__x__ = 30
	def m1(self):
		print('public method')
	def __m1(self):
		print('private method')
	def _m1_(self):
		print('public Dunder method')
# End of the class
a = c1()
# How to print variable 'x'
print(a.x)           # 10
# How to print public dunder variable 'x'
print(a.__x__)       # 30
# How to print private variable 'x'
print(a._c1__x)      # 20
# print(a.__x) # Error as 'c1' object has no attribute '__x'
# How to call public method m1()
a.m1()               # public method
# How to call public dunder method m1()
a._m1_()             # public Dunder method
# How to call private method m1()
# a.__m1() # Error as 'c1' object has no attribute '__m1'
a._c1__m1()          # private method



#3
'''
Find outputs
Assume that addresses of objects 'a' , 'b' , 'c' , 'd' and 'e' are 1000 , 2000 , 3000 , 4000 and 5000 respectively
'''
class c1:
	def _init_(self):
		print('Object is created at address : ' , id(self))
	def _del_(self):
		print(F'Object at address {id(self)} is lost')
# End of the class
a = c1() # Object is created at address : 1000
a = None # Object at address 1000 is lost (if refcount drops to 0 immediately)
b = c1() # Object is created at address : 2000
del b # Object at address 2000 is lost
c = c1() # Object is created at address : 3000
c = c1() # Object is created at address : 4000 # Old c (3000) is lost: Object at address 3000 is lost
d = c1() # Object is created at address : 5000
e = c1() # Object is created at address : 6000



#4
# Identify Error (Home work)
class c1:
	def _del_(self , x):
		print('destructor : ' , x)
		return None
a = c1()
a._del_(25)
# Error as c1.__del__() takes 2 positional arguments but 3 were given
# Also: __del__ should not take extra parameters; it must be _del_(self).



#5
# Find outputs (Home work)
class c1:
	def _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a._del_(25)
# Error as c1.__del__() takes 2 positional arguments but 3 were given



#6
# Find outputs (Home work)
class c1:
	def _del_(self):
		print('destructor')
		b = c1()
a = c1()
# Output (if refcount drops immediately):
#   destructor
#   destructor
#   ...
#   RecursionError likely (or infinite destructor chain) because inside __del__ you create a new c1().
 


#7
# Find outputs (Home  work)
class c1:
	def _init_(self):
		print('constructor')
		del self
	def _del_(self):
		print('destructor')
		b = c1()
a = c1() # 'constructor'



#8
# Find outputs (Home work)
class c1:
	def _del_(self):
		print('1st destructor')
	def _del_(self):
		print('2nd destructor')
	def _del_(self):
		print('3rd destructor')
# End of the class
a = c1() # 3rd destructor (if the object is destroyed at module end, etc.)



#9
#Find outputs (Home work)
class c1:
	def _init_(self):
		print('Object is created at address : ' , id(self))
	def _del_(self):
		print(F'Object at address {id(self)} is lost ')
#end of the class
c = b = a = c1()
# Object is created at address : 1000 (1000 is representative)
del a
# none (only reference to object gone; c and b still refer to it).
print('Hello')
del b
# none (only reference to object gone; c still refers to it).
print('Hi')
del c
# Object at address 1000 is lost
print('Bye')
d = c1()
# Object is created at address : 2000
print('End') # End 



#10
# Find outputs (Home work)
class c1:
	def _init_(self):
		print('Object is created at address : ' , id(self))
	def _del_(self):
		print(F'Object at address {id(self)} is lost ')
# End of the class
list = [c1() , c1() , c1()]
#   Object is created at address : 1000
#   Object is created at address : 2000
#   Object is created at address : 3000
del list
#   Object at address 1000 is lost
#   Object at address 2000 is lost
#   Object at address 3000 is lost



#11
# Find outputs (Home work)
class c1:
	def _del_(self):
		print('destructor')
		return 25
a = c1()
print(a._del_()) # destructor followed by 25 
print('Hello')
del a
# destructor