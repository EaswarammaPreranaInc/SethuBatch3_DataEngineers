# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		#How  to  initialize  public  variable  'x'  to  10
		self.x=10
		#How  to  initialize  private  variable  'y'  to  20
		self.__y=20
	def  m1(self):
		print('m1  method')
		#How  to  print   variable  'x'
		print(self.x)
		#How  to  print  private  variable  'y'
		print(self.__y)
		#How  to  call    private  method   m2()
		self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		#How  to  print   variable  'x'
		print(self.x)
		#How  to  print  private  variable   'y'
		print(self.__y)
# End  of  the  class
t = Test()
print('Outside')
#How  to  print  variable  'x'
print(t.x)
#How  to  print   variable  'y'
print(t._Test__y)
print(t . __y)#error private variable cannot access directly
print(t . __dict__)#t object is now dict variable are keys and variable value is value to the key#{}
#How  to  call  method  m1()
t.m1()
#How  to  call   method  m2()
t._Test__m2()
t . __m2()#error private methods cannot access directly
print('End')


#  Find  outputs
class  c1:
	def __init__(self):
		#How  to  initialize  public  variable  'x'  with  10
		self.x=10
		#How  to  initialize  private  variable  'x'  with  20
		self.__x=20
		#How  to  initialize  public  dunder  variable  'x'  with  30
		self.__x__=3
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
#How  to  print   variable  'x'
print(a.x)#10
#How  to  print  public  dunder  variable  'x'
print(a.__x__)#3
#How  to  print   private  variable  'x'
print(a._c1__x)#20
print(a . __x)#error
#How  to  call  public  method  m1()
a.m1()#public method 
#How  to  call  public  dunder  method  m1()
a.__m1__()#public Dunder method
#How  to  call  private  method  m1()
a._c1__m1()#private method
a . __m1()#error


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
a = c1() # Object  is  created  at  address  :  1000
a = None # Object  at  address  1000  is  lost
b = c1() # Object  is  created  at  address  :  2000
del    b # Object  at  address  2000  is  lost
c = c1() # Object  is  created  at  address  :  3000 <nextline> Object  at  address  3000  is  lost
c = c1() # Object  is  created  at  address  :  3000 
d = c1() # Object  is  created  at  address  :  4000
e = c1() # Object  is  created  at  address  :  5000

# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1() # Error the destructor cannot take the arguments while calling implicitly
a . _del_(25) # destructor : 25

# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1() # destructor : 35
a . _del_(25)  # destructor : 25

# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1() # Infinite times destructor is printed and infinite recursion

# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1() # Error infinite recursion and infinite times constructor <nextline> destructor is printed

#  Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() # 3rd  destructor

#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() # Object  is  created  at  address  :  address of object c1
del   a  
print('Hello') # Hello
del   b   
print('Hi') # Hi
del   c # Object  at  address  object c1  is  lost  
print('Bye') # Bye
d = c1() # Object  is  created  at  address  :  address of object d 
print('End') # End

# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list

''' Outputs:
Object  is  created  at  address  :  address of first object c1
Object  is  created  at  address  :  address of second object c1
Object  is  created  at  address  :  address of third object c1
Object  at  address  first object c1  is  lost 
Object  at  address  second object c1  is  lost 
Object  at  address  third object c1  is  lost 
'''

# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1() 
print(a . _del_()) # destructor <nextline> 25
print('Hello') # Hello
del   a # destructor