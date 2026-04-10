 # Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
                self.x=10
		How  to  initialize  public  variable  'x'  to  10           
                How  to  initialize  private  variable  'y'  to  20
                self.__y=20
	def  m1(self):
		print('m1  method')
		How  to  print   variable  'x'
                print(self.x)
		How  to  print  private  variable  'y'
                print(self.__y)
		How  to  call    private  method   m2()
                self.m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'
                print(self.x)
		How  to  print  private  variable   'y'
                print(self.__y)
# End  of  the  class
t = Test()
print('Outside') #outside
How  to  print  variable  'x'
print(t.x)
How  to  print   variable  'y'
print(t . __y)#error
print(t . _dict_)
How  to  call  method  m1()
t.m1()
How  to  call   method  m2()
t . __m2()#error
print('End') #end


# Object  't'  --->
#  Find  outputs
class  c1:
	def _init_(self):
		How  to  initialize  public  variable  'x'  with  10
                self.x=10
		How  to  initialize  private  variable  'x'  with  20
                self.y=20
		How  to  initialize  public  dunder  variable  'x'  with  30
                self._x_=30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
How  to  print   variable  'x'
print(x) #10
How  to  print  public  dunder  variable  'x'
print(__x__)#30
How  to  print   private  variable  'x'
print(a . __x)#20
How  to  call  public  method  m1()
t.m1() #public method
How  to  call  public  dunder  method  m1()
t._m1_()#public diunder method
How  to  call  private  method  m1()
a . __m1() #private method


# Object  'a'   --->''' x=10,y=20 
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1() #1000
a = None#destroy 1000
b = c1()#2000
del    b#destroy 2000
c = c1()#2000
c = c1()#new 3000 created
d = c1()#4000
e = c1()#5000
# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1()
a . _del_(25) #error
 # Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25) #destructor:25
# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1()
# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1()
#  Find  outputs( Home  work)
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor') #3rd destructor
# End  of  the  class
a = c1()
#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()# object created
del   a
print('Hello') #hello
del   b
print('Hi')#hi
del   c
print('Bye')
d = c1()
print('End')#end
# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list
 # Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25 #25
a = c1() #destructor
print(a . _del_())
print('Hello') #hello
del   a#destructor