# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x = 10 # How  to  initialize  public  variable  'x'  to  10
		self.__y = 20 # How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.__y) # How  to  print  private  variable  'y'
		self.__m2() # How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) # How  to  print   variable  'x'
		print(self.__y) # How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) # How  to  print  variable  'x'
print(t._Test__y) # How  to  print   variable  'y'
print(t . __y) # ERROR
print(t . _dict_)
t.m1() # How  to  call  method  m1()
t._Test__m2() # How  to  call   method  m2()
t . __m2() # ERROR 
print('End')

# Object  't'  ---> {'x': 10, '_Test__y': 20}

#  Find  outputs
class  c1:
	def _init_(self):
		self.x = 10 # How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 # How  to  initialize  private  variable  'x'  with  20
		self._x_ = 30 # How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # How  to  print   variable  'x'
print(a._x_) # How  to  print  public  dunder  variable  'x'
print(a._c1__x) # How  to  print   private  variable  'x'
print(a . __x) # ERROR 
a.m1() # How  to  call  public  method  m1()
a._m1_() # How  to  call  public  dunder  method  m1()
a._c1__m1() # How  to  call  private  method  m1()
a . __m1() # ERROR 

# Object  'a'   --->
'''
10
30
20
public method
public Dunder method
private method
'''

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
'''
Object is created at address : 1000
Object at address 1000 is lost
Object is created at address : 2000
Object at address 2000 is lost
Object is created at address : 3000
Object is created at address : 4000
Object at address 3000 is lost
Object is created at address : 4000
Object is created at address : 5000
'''

# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x): # ERROR because destructor cannot take arguments apart from self
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)

# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)
'''
destructor :  25
destructor :  35
'''

# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()
'''
destructor
destructor
destructor
...
infinite recursion
'''

# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1()
'''
constructor
destructor
constructor
destructor
constructor
destructor
...
infinite recursion
'''

#  Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor') # 3rd destructor
# End  of  the  class
a = c1()

#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
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
'''
Object is created at address : 1000
Hello
Hi
Object at address 1000 is lost
Bye
Object is created at address : 2000
End
Object at address 2000 is lost
'''

# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list
'''
Object is created at address : 1000
Object is created at address : 2000
Object is created at address : 3000
Object at address 3000 is lost
Object at address 2000 is lost
Object at address 1000 is lost
'''

# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del   a
'''
destructor
25
Hello
destructor
'''