##########################################################################################
 # Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
		'''How  to  initialize  public  variable  'x'  to  10
		How  to  initialize  private  variable  'y'  to  20'''
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.__y)
		self.__m2()

		'''How  to  print   variable  'x'
		How  to  print  private  variable  'y'
		How  to  call    private  method   m2()'''
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)
		print(self.__y)
		'''How  to  print   variable  'x'
		How  to  print  private  variable   y'''
# End  of  the  class
t = Test()
print('Outside')
print("x",t.x)
print("y",t._Test__y)
'''How  to  print  variable  'x'
How  to  print   variable  'y'''
print(t . __y)#error
print("hello",t . __dict__)
t.m1()
t.__m2()
'''How  to  call  method  m1()
How  to  call   method  m2()
'''
t . __m2()#error
print('End')


# Object  't'  --->
##########################################################################################
 #  Find  outputs
class  c1:
	def __init__(self):
		self.x=10
		self.__x=20
		self.__x__=30
		'''How  to  initialize  public  variable  'x'  with  10
		How  to  initialize  private  variable  'x'  with  20
		How  to  initialize  public  dunder  variable  'x'  with  30'''
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print("x",a.x)
print("y",a.__x__)
print("z",a._c1__x)
'''How  to  print   variable  'x'
How  to  print  public  dunder  variable  'x'
How  to  print   private  variable  'x'''
print(a . __x)#error
a.m1()
a.__m1__()
a._c1__m1()
'''How  to  call  public  method  m1()
How  to  call  public  dunder  method  m1()
How  to  call  private  method  m1()'''
a . __m1()#error


# Object  'a'   --->
##########################################################################################
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
a = c1()#
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

#-----output----
'''
Object  at  address    is  lost
Object  is  created  at  address  :   address
Object  at  address  some address  is  lost
Object  is  created  at  address  :   some address
Object  is  created  at  address  :   some address
Object  at  address  some address  is  lost
Object  is  created  at  address  :   some address
Object  is  created  at  address  :   some address
Object  at  address  some address  is  lost
Object  at  address  adress  is  lost
Object  at  address  address  is  lost
'''##########################################################################################
# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)

destructor :  25
Exception ignored while calling deallocator <function c1.__del__ at 0x00000255EC927690>:
TypeError: c1.__del__() missing 1 required positional argument: 'x'
##########################################################################################
 # Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)

destructor :  25
destructor :  35
##########################################################################################
 # Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
# Output:
# destructor
# destructor
# destructor
# ...
# (Infinite loop / program crash due to recursive object creation in destructor)
##########################################################################################
 # Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
# 2️⃣
# Output:
# constructor
# destructor
# constructor
# destructor
# constructor
# destructor
# ...
# (Infinite loop)
##########################################################################################
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()

# Output:
# 3rd destructor

##########################################################################################
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


Output:
# Object is created at address : <addr1>
# Hello
# Hi
# Object at address <addr1> is lost
# Bye
# Object is created at address : <addr2>
# End
# Object at address <addr2> is lost
##########################################################################################
# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list


# Output:
# Object is created at address : <addr1>
# Object is created at address : <addr2>
# Object is created at address : <addr3>
# Object at address <addr1> is lost
# Object at address <addr2> is lost
# Object at address <addr3> is lost
##########################################################################################
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a

Output:
# destructor
# 25
# Hello
# destructor