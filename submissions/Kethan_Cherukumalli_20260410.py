1) # Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x=10
		self.__y=25
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.—y)
		self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)
		print(self.__y)
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
NOT ALLOWED TO ACCESS Y 
print(t . __y)
print(t . _dict_)
t.m1()
5.__m2()
t . __m2()
print('End')


# Object  't'  —>

2)
#  Find  outputs
class  c1:
	def _init_(self):
		self.x=10
		self.__x=20
		self.__x__=30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)
print(a.__x__)
print(a._c1__x)
print(a . __x) #WRONG
a.m1()
a.__m1__()
A.c1__m1()
a . __m1() #ERROR


# Object  'a'   —>

3)
'''  
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

Output-
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object at address 3000 is lost
Object is created at address : 4000
Object is created at address : 4000
Object is created at address : 5000

4)
# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)
Output-
destructor : 25

5)
# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25)

Output-
destructor : 25

6)
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1()
Output-
NO OUPTUT