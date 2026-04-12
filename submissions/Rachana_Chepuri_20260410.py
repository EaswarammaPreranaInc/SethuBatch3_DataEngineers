'''Public  and  Private  members  demo  program'''
class  Test:
	def  _init_(self):
		self.x#How  to  initialize  public  variable  'x'  to  10
		self.__y#How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable  'y'
		self.__m2()#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x)#How  to  print   variable  'x'
		print(self.__y)#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)#How  to  print  variable  'x'
print('t._Test__y')#How  to  print   variable  'y'
print(t . __y) #Error-- private variable cannot directly called 
print(t . __dict__)
t.m1()#How  to  call  method  m1()
t._Test.__m2()#How  to  call   method  m2()
t . __m2() #Error---private method cannot directly called 
print('End')
'''output'''

# Outside
# 10
# 20
# {'x':10 ,'t._Test__y':20 }
# m1 method
# 10
# 20
# __m2 method
# 10
# 20
# Bck to m1 method
# __m2 method
# 10
# 20
# End
'''Find  outputs'''
class  c1:
	def _init_(self):
		self.x= 10#How  to  initialize  public  variable  'x'  with  10
		self.__x= 20#How  to  initialize  private  variable  'x'  with  20
		self.__x__= 30#How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)#How  to  print   variable  'x'
print('a._c1__x')#How  to  print  public  dunder  variable  'x'
print(a.__x__)#How  to  print   private  variable  'x'
print(a . __x) # Error--private variable cannot called diectly
a.m1()#How  to  call  public  method  m1()
a.__m1__#How  to  call  public  dunder  method  m1()
a._c1__m1#How  to  call  private  method  m1()
a . __m1() # Error---private method cannot called diectly
'''outside'''

# 10
# 30
# 20
# public method
# public Dunder method
# private method
'''Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1() # c1 obj created and constructor executed
a = None # None obj created with ref a , c1() deleted before delete destructor executes
b = c1() # another c1() created  and  constructor executed
del    b # b is deleted before deleted   destructor executes
c = c1() # another c1() created and  constructor executed
c = c1() # another c1() created, before c1() deleted before delete destructor executes and neww c1() constructor executed
d = c1() # another c1() created and  constructor executed
e = c1() #  another c1() created and  constructor executed
'''output'''
# Object is created at address : 1000
# Object at address 1000 is lost
# Object is created at address : 2000
# Object at address 2000 is lost
# Object is created at address : 3000
# Object is created at address : 4000
# Object at address 3000 is lost
# Object is created at address : 4000
# Object is created at address : 5000
'''Identify  Error (Home  work)'''
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a . __del__(25) #Error--destructor cannot have arguments
'''Find  outputs (Home  work)'''
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)
'''output'''
# destructor : 35
# destructor : 25
'''Find  outputs (Home  work)'''
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() # it deleted  before deletion destructor executed
'''output'''
# destructor
# destructor
#.....
'''Find  outputs (Home  work)'''
class   c1:
	def  __init__(self):
		print('constructor')
		del  self   # self delete brfore delete destructor executes
	def  __del__(self):
		print('destructor')
		b = c1() # another c1()  and destuctor exectes for 1st c1()
a = c1()# c2() creates and constructor executes
'''output'''
# constructor
# destructor
# constructor
# destructor
# constructor
# destructor.....
'''Find  outputs( Home  work)'''
class   c1:
	def  __del__(self): # Discarded
		print('1st  destructor')
	def  __del__(self): # Discarded
		print('2nd  destructor')
	def  __del__(self): # Recognized
		print('3rd  destructor')
# End  of  the  class
a = c1() # object a is created but no deletion in is there
'''Find  outputs (Home  work)'''
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
'''output'''
# Object  is  created  at  address  :   1000
# Hello
# Hi
# Object  at  address  1000  is  lost  
# Bye
# Object  is  created  at  address  :   2000
# End
# Object  at  address  2000 is  lost
'''Find  outputs(Home  work)'''
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list
'''output'''
# Object  is  created  at  address  :   1000
# Object  is  created  at  address  :   2000
# Object  is  created  at  address  :   3000
# Object  at  address  3000  is  lost 
# Object  at  address  2000  is  lost 
# Object  at  address  1000 is  lost
'''Find  outputs  (Home  work)'''
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del   a
'''output'''
# destructor
# 25
# Hello
# destructor








