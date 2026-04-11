# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x = 10	    # How  to  initialize  public  variable  'x'  to  10
		self.__y = 20	# How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)	# How  to  print   variable  'x'
		print(self.__y)	# How  to  print  private  variable  'y'
		t.__m2()	    # How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)	# How  to  print   variable  'x'
		print(self.__y)	# How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)	    # How  to  print  variable  'x'
print(t._Test__y)	# How  to  print   variable  'y'
# print(t .__y)		# error , becoz there is no __y attribute
print(t .__dict__)	# {'x' : 10 , '_Test__y' : 20}
t.m1()		        # How  to  call  method  m1()
t._Test__m2()		# How  to  call   method  m2()
# t . __m2()        # error , becoz there is no __m2 attribute
print('End')


# Object  't'  ---> x = 10  y = 20

# Outside
# 10
# 20
# {'x': 10, '_Test__y': 20}
# m1  method
# 10
# 20
# __m2  method
# 10
# 20
# Back to m1 method
# __m2  method
# 10
# 20
# End

#============================================================================================================================

#  Find  outputs
class  c1:
	def __init__(self):
		self.x = 10		# How  to  initialize  public  variable  'x'  with  10
		self.__x = 20		# How  to  initialize  private  variable  'x'  with  20
		self.__x__ = 30		# How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)	# How  to  print   variable  'x'
print(a.__x__)	# How  to  print  public  dunder  variable  'x'
print(a._c1__x)	# How  to  print   private  variable  'x'
# print(a . __x)  # error
a.m1()		# How  to  call  public  method  m1()
a.__m1__()	# How  to  call  public  dunder  method  m1()
a._c1__m1()	# How  to  call  private  method  m1()
# a . __m1()	# error , becoz there is no __m1 method attribute


# Object  'a'   --->	x = 10  __x = 20  __x__ = 30

# 10
# 20
# 30
# public method
# public dunder method
# private method

#========================================================================================================

'''  
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
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

# Object  is  created  at  address  :   a
# Object  at  address  a  is  lost
# Object  is  created  at  address  :   b
# Object  at  address  b  is  lost
# Object  is  created  at  address  :   c
# Object  is  created  at  address  :   another c
# Object  at  address  c  is  lost
# Object  is  created  at  address  :   d
# Object  is  created  at  address  :   e
# Object  at  address  another c  is  lost
# Object  at  address  d  is  lost
# Object  at  address  e  is  lost

#========================================================================================================

# Identify  Error (Home  work)
class   c1:
    
	def  __del__(self , x):             # __del__ (destructor having no arguments except self)
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)

#========================================================================================================

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)

# destructor : 25
# destructor : 35

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			# b = c1()    # recursion error , cannot call class inside the class. it call multiple time.
a = c1()

#========================================================================================================

# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		# b = c1()        # recursion error , cannot call class inside the class
a = c1()

# constuctor

#========================================================================================================

#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')        # 3rd destructor , becoz all methods having same name so last method is recognised. 
# End  of  the  class                                      remaining discarded
a = c1()

#========================================================================================================

#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')

# Object  is  created  at  address  : a b
# Hello
# Hi
# Object  at  address  c  is  lost
# Bye
