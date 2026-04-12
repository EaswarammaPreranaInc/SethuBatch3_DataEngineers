# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x=  10
		self.__y = 20
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.y)
		t=_Test.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		pirnt(self.x)
		print(self.y)
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
print(t._Test__y)
print(t . __y) #Error
print(t . _dict_) #{x:10,__y:20)
t.m1()
t._Test.__m2()
t . __m2() #Error
print('End')


# Object  't'  --->
#  Find  outputs
class  c1:
	def _init_(self):
		How  to  initialize  public  variable  'x'  with  10
		How  to  initialize  private  variable  'x'  with  20
		How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
How  to  print   variable  'x'
How  to  print  public  dunder  variable  'x'
How  to  print   private  variable  'x'
print(a . __x)
How  to  call  public  method  m1()
How  to  call  public  dunder  method  m1()
How  to  call  private  method  m1()
a . __m1()


# Object  'a'   --->

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
# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)

# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25)

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
		print('3rd  destructor')
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


# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list
[1:33 pm, 10/04/2026] +91 99482 50500: # Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del   a