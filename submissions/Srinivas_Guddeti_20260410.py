# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x = 10
		self.__y = 20
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.__y)
		self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)
		print(self.__y)

t = Test()
print('Outside')
print(t.x) # 10
print(t._Test__y) # 20 (Accessed via Name Mangling)
# print(t . __y)  # Error because private variables cannot be called directly from outside
print(t . __dict__)  # {'x': 10, '_Test__y': 20}
t.m1() # m1 method, 10, 20, __m2 method, 10, 20, Back to m1 method
# t._Test__m1() # Error because m1 is public, not mangled. Should be t.m1()
# t . __m2()  # Error because private methods cannot be called directly from outside
print('End')

# -----------------------------------------------------------------------------------------------------

# Find  outputs
class  c1_mangling:
	def __init__(self):
		self.x = 10 # Public
		self.__x = 20 # Private
		self.__x__ = 30 # Public Dunder
	def  m1(self): print('public method')
	def  __m1(self): print('private method')
	def  __m1__(self): print('public Dunder method')

a = c1_mangling()
print(a.x)  # 10
print(a.__x__) # 30
print(a._c1_mangling__x) # 20
# print(a . __x)   # Error because private variables cannot be accessed directly
a.m1() # public method
a.__m1__() # public Dunder method
a._c1_mangling__m1() # private method (via mangling)
# a . __m1()   # Error because private methods cannot be accessed directly

# -----------------------------------------------------------------------------------------------------

# Find outputs - Destructors (Assuming addresses 1000, 2000, 3000, 4000, 5000)
class  c1_del:
	def   __init__(self):
		print('Object is created at address : ' , id(self))
	def   __del__(self):
		print(F'Object at address {id(self)} is lost')

a = c1_del()  # Object is created at address : 1000
a = None  # Object at address 1000 is lost
b = c1_del()  # Object is created at address : 2000
del    b  # Object at address 2000 is lost
c = c1_del()  # Object is created at address : 3000
c = c1_del()  # Object is created at address : 3500 (new object) / Object at address 3000 is lost
d = c1_del()  # Object is created at address : 4000
e = c1_del()  # Object is created at address : 5000
# At end of program:
# Object at address 3500 is lost
# Object at address 4000 is lost
# Object at address 5000 is lost

# -----------------------------------------------------------------------------------------------------

# Identify Error (Home work)
class  c1_err:
	def __del__(self , x): # Note: Logic allowed if called manually, but GC will fail
		print('destructor : ' ,  x)

# a = c1_err()
# del a # Error because destructor takes 2 arguments (self and x) but GC only provides self

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work)
class  c1_loop:
	def __init__(self):
		print('constructor')
	def __del__(self):
		print('destructor')
		# b = c1_loop() # This would cause infinite recursion if triggered

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work) - Reference Counting
class  c1_ref:
	def   __init__(self):
		print('Object is created at address : ' , id(self))
	def   __del__(self):
		print(F'Object at address {id(self)} is lost ')

c = b = a = c1_ref()  # Object is created at address : 1000
del   a  # (No output - reference count is still 2)
print('Hello')   # Hello
del   b  # (No output - reference count is still 1)
print('Hi')  # Hi
del   c   # Object at address 1000 is lost
print('Bye')  # Bye
d = c1_ref()  # Object is created at address : 2000
print('End')  # End
# Object at address 2000 is lost (GC at exit)

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work) - List of objects
class  c1_list:
        def      __init__(self): print('Object created')
        def      __del__(self): print('Object lost')

list_obj = [c1_list() , c1_list() , c1_list()] # Object created (x3)
del  list_obj # Object lost (x3) because list is the only reference

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home work) - Manual call vs GC
class  c1_return:
	def __del__(self):
		print('destructor')
		return 25

a = c1_return()
print(a . __del__())  # destructor / 25
print('Hello')        # Hello
del   a               # destructor (Return value 25 is ignored by GC)