#1
# Find outputs (Home work)
class c1:
	x = 10
	def _init_(self):
		self.y = 20
	@classmethod
	def m1(cls):
		cls.x = 30
		cls.y = 40
# End of the class
a = c1()
b = c1()
c1.m1()
print(a.x) # 30  (a.x reads modified class x)
print(a.y) # 20
print(b.x) # 30  (b.x reads class x via c1.x)
print(b.y) # 20
print(c1.x , c1.y) # 30 40
print(cls.x , cls.y) # Error as name 'cls' is not defined
print(self.x , self.y) # Error as name 'self' is not defined



#2
# Find outputs
class c1:
	@staticmethod
	def m1():
		print('static method')
# End of the class
c1.m1() # static method
a = c1()
a.m1() # static method
c1.m1(25) # static method  (extra arg 25 is ignored, but call is valid; no error).



#3
# Find outputs
class c1:
	@staticmethod
	def m1(self):
		print(self)
# End of the class
c1.m1(25) # 25
a = c1()
a.m1(35) # 35
a.m1() # Error as m1() missing 1 required positional argument: 'self'



#4
# Find outputs
class c1:
	def m1(self):
		print(self)
# End of the class
c1.m1(25) # How is method m1() treated i.e. static method (or) instance method
# 25 (when treated as plain function; no error if you pass something).
# How it’s treated: m1 is an instance method, but here you call it without instance binding.
a = c1()
a.m1()  # How is method m1() treated i.e. static method (or) instance method
# <__main__.c1 object at 0x...>
a.m1(35)  # What about here
# 35  (self = a; 35 is passed to self parameter).



#5
# Find outputs
class c1:
	def m1():
		print()
# End of the class
c1.m1() # (empty line, function runs)
a = c1()
a.m1() # (empty line, function runs)



#6
# Find outputs
class c1:
	@staticmethod
	def m1(self):
		print('static method')
		print(self)
	def m1(self):
		print('static / instance method')
		print(self)
# End of the class
c1.m1(25) # static / instance method 25  (instance version wins; static is shadowed).
a = c1()
a.m1() # static / instance method <__main__.c1 object at 0x...>



#7
# How to access static variable in different ways ?
class c1:
	x = 25
	def _init_(self):
		# How to print static variable 'x'
		print(c1.x)
		# How to print static variable 'x' in another way
		print(self.__class__.x)
		print(x) # Error as name 'x' is not defined (no global x).
	def m1(self):
		# How to print static variable 'x'
		print(c1.x)
		# How to print static variable 'x' in another way
		print(self.__class__.x)
		# print(cls.x) # Error as name 'cls' is not defined
		print(self.x)
	def m2(cls):
		@classmethod  # inside method is wrong; correct decorator is on method.
		def m2(cls):
			# How to print static variable 'x'
			print(cls.x)
			# How to print static variable 'x' in another way
			print(c1.x)
			# print(self.x) # Error: name 'self' is not defined
	# Corrected:
	@classmethod
	def m2(cls):
		# How to print static variable 'x'
		print(cls.x)
		# How to print static variable 'x' in another way
		print(c1.x)
		# print(self.x)  -> invalid at class‑method top‑level.
	@staticmethod
	def m3():
		# How to print static variable 'x'
		print(c1.x)
		# print(cls.x) # Error as name 'cls' is not defined
		# print(self.x) # Error as name 'self' is not defined
# End of the class
# How to print static variable 'x'
print(c1.x)
# How to print static variable 'x' in another way
print(c1.__dict__['x'])
print(x) # Error as name 'x' is not defined (no global x).
print(self.x) # Error as name 'self' is not defined.
print(cls.x) # Error as name 'cls' is not defined.
# How to call method m1()
o = c1()
o.m1()
# How to call method m2()
c1.m2()
# How to call method m3()
c1.m3()



#8
# How to add static variable to the class at different locations of the program ?
class c1:
	# How to add static variable 'a' with value 10
	a = 10
	def _init_(self):
		# How to add static variable 'b' with value 20
		c1.b = 20
		# How to add instance variable 'c' with value 30
		self.c = 30
		c1.k = 25
	def m1(self):
		# How to add static variable 'd' with value 40
		c1.d = 40
		# How to add instance variable 'e' with value 50
		self.e = 50
	@classmethod
	def m2(cls):
		# How to add static variable 'f' with value 60
		cls.f = 60
		# How to add static variable 'g' with value 70 in another way
		c1.g = 70
		cls.k = 25
	@staticmethod
	def m3():
		# How to add static variable 'h' with value 80
		c1.h = 80
		# self.k = 25  -> invalid; no self
		# cls.k = 35  -> invalid; no cls
#End of the class
print('Outside the class')
print(c1._dict_)
print()
print()
x = c1()
print('Constructor')
print(c1._dict_)
print()
print()
# How to call m1() method
x.m1()
print('Instance method m1')
print(c1._dict_)
print()
print()
# How to call m2() method
c1.m2()
print('class method m2')
print(c1._dict_)
print()
print()
# How to call m3() method
c1.m3()
print('static method m3')
print(c1._dict_)
print()
print()
# How to add static variable 'i' with value 90
c1.i = 90
# How to add instance variable 'j' with value 100
x.j = 100
print('Outside the class')
print(c1._dict_)
print()
print()
print("Object 'x' ")
print(x._dict_)



#9
# Find outputs (Home work)
class c1:
        a , b , c  = range(1 , 4)
# End of the class
# How to print variable 'a'
print(c1.a)
# How to print variable 'b'
print(c1.b)
# How to print variable 'c'
print(c1.c)
print(c1._dict_)



#10
# Tricky program
# What are the outputs if inputs are 10 , 20 , 30 , 40 , 50 , 60 , 70 (Home work)
class Test:
	@classmethod
	def get1(cls):
		cls.x = int(input('Enter any number : '))
	def get2(self):
		self.y = int(input('Enter any number : '))
		self.z = int(input('Enter any number : '))
	def compute(self):
		Test.x += 1
		self.y += 1
		self.z += 1
		self.x += 1
	def disp(self):
		print(Test.x , self.y , self.z , self.x , sep = '\t')
# End of the class
Test.get1()      # user enters 10 -> Test.x = 10
a = Test()
b = Test()
c = Test()
a.get2()         # user enters 20, 30 -> a.y=20, a.z=30
b.get2()         # user enters 40, 50 -> b.y=40, b.z=50
c.get2()         # user enters 60, 70 -> c.y=60, c.z=70
a.compute()      # Test.x=11; a.y=21, a.z=31, a.x=1 -> but a.x is instance x
b.compute()      # Test.x=12; b.y=41, b.z=51, b.x=1
c.compute()      # Test.x=13; c.y=61, c.z=71, c.x=1
a.disp()         # 13	21	31	1
b.disp()         # 13	41	51	1
c.disp()         # 13	61	71	1



#11
'''
Write a program to add two Vector objects
1) What are the names of objects ? --->  x , y and z
2) What are the names of lists held by each object ? ---> x.a , y.a , z.a
3) How to access elements of 1st list ? ---> x.a[i]
   How to access elements of 2nd list ? ---> y.a[i]
4) How to access static variable 'n' ? --->  vector.n
'''
class vector:
	n = 0
	@staticmethod
	def get1():
		vector.n = int(input('How many elements? '))
	def __init__(self):
		self.a = []
	def get2(self):
		for i in range(vector.n):
			self.a.append(int(input('Enter any number : ')))
	def add(self , x , y):
		self.a = []
		for i in range(vector.n):
			self.a.append(x.a[i] + y.a[i])
	def __str__(self):
		return str(self.a)

vector.get1()
print('1st object')
a = vector()
a.get2()
print('2nd object')
b = vector()
b.get2()
c = vector()
c.add(a , b)
print('Result : ' , c)



#12
'''
Write a program to print only static variables but not environment variables of classname.__dict__
Hint: Use startswith() and endswith() methods
'''
class c1:
	x = 1
	y = 2
	z = 3
# End of the class
for k in c1.__dict__:
	if not k.startswith('_') and not k.endswith('_'):
		print(k , '-->' , c1.__dict__[k])



#13
'''
1) Write a program to validate emp number , emp name and salary and also print them
2) Emp number and salary can not be -ve
3) Emp name can not be empty string
4) class name is Emp
5) 3 getter and 3 setter methods
6) Constructor initializes empno , ename and sal
7) Outside the class
   ----------------------
   a) Create Emp class object
   b) Print empno , ename and sal
'''
class Emp:
	def _init_(self , empno , ename , sal):
		self.set_empno(empno)
		self.set_ename(ename)
		self.set_sal(sal)
	def set_empno(self , n):
		if n < 0:
			print('Employee number cannot be negative')
		else:
			self._empno = n
	def set_ename(self , e):
		if not e:
			print('Employee name cannot be empty')
		else:
			self._ename = e
	def set_sal(self , s):
		if s < 0:
			print('Salary cannot be negative')
		else:
			self._sal = s
	def get_empno(self):
		return self._empno
	def get_ename(self):
		return self._ename
	def get_sal(self):
		return self._sal
emp = Emp(101 , 'Ram' , 50000)
print('Employee number : ' , emp.get_empno())
print('Employee name : ' , emp.get_ename())
print('Salary : ' , emp.get_sal())