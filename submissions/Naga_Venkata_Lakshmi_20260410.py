# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x = 10
		self.__y = 20

	def  m1(self):
		print('m1  method')
		How  to  print   variable  'x'
                print("x =",self.x)
		How  to  print  private  variable  'y'
                print("y =",self.__y)
		How  to  call    private  method   m2()
                self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'
                print("x =", self.x)
		How  to  print  private  variable   'y'
                print("y =",self.__y)
# End  of  the  class
t = Test()
print('Outside')
How  to  print  variable  'x'
print(t.x)
How  to  print   variable  'y'
print(t._Test__y)
print(t . __y) #Error
print(t . _dict_)
How  to  call  method  m1()
t.m1()
How  to  call   method  m2()
t._Test__m2()
t . __m2() #Error
print('End')

#outputs
outside
x = 10
y = 20
{'x' : 10, '_Test__y' : 20}
m1 method
x = 10
y = 20
__m2 method
x = 10
y = 20
Back to m1 method
__m2 method
x = 10
y = 20





#  Find  outputs
class  c1:
	def _init_(self):
		How  to  initialize  public  variable  'x'  with  10
                self.x = 10
		How  to  initialize  private  variable  'x'  with  20
                self.__x = 20
		How  to  initialize  public  dunder  variable  'x'  with  30
                self.__x__ = 30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
How  to  print   variable  'x'
print(a.x)
How  to  print  public  dunder  variable  'x'
print(a.__x__)
How  to  print   private  variable  'x'
print(a._c1__x)
print(a . __x)
How  to  call  public  method  m1()
a.m1()
How  to  call  public  dunder  method  m1()
a.__m1__()
How  to  call  private  method  m1()
a._c1__m1()
a . __m1() #Error

#output
10
30
20
public method
public Dunder method
private method





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
#outputs
Object  is  created  at  address  : 1000
Object  at  address 1000 is lost
Object  is  created  at  address  : 2000
Object  at  address 2000 is lost
Object  is  created  at  address  : 3000
Object  is  created  at  address  : 4000
Object  at  address 3000 is lost
Object  is  created  at  address  : 5000
Object  is  created  at  address  : 6000




# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x): #Error del takes only self  not x.
		print('destructor : ' ,  x)
a = c1()
a . _del_(25) 



# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . _del_(25)
#outputs
destructor : 25
destructor : 35


# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1()
a = c1()
#outputs
destructor
destructor
destructor
infinite recursion
Recursion Error: maximum recursion depth exceeded.





# Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  _del_(self):
		print('destructor')
		b = c1()
a = c1()
#outputs
constructor 
destructor
constructor
destructor

infinite recursion
RecursionError : maximum recursion depth exceeded.



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
#outputs
3rd destructor



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
#outputs
Object is created at address : 140234567890
Hello
Hi
Object at address 140234567890 is lost
Bye
Object is created at address : 140234567891
End



# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list
#outputs
Object  is  created  at  address  :  140234567890
Object  is  created  at  address  :  140234567891
Object  is  created  at  address  :  140234567892
Object  at  address  140234567890 is  lost 
Object  at  address  140234567891 is  lost 
Object  at  address  140234567892 is  lost 


# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())
print('Hello')
del   a

#ouputs
destructor
25
Hello
destructor

