# # Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x=10#How  to  initialize  public  variable  'x'  to  10
		self.__y=20#How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x)#How  to  print   variable  'x'
		print(self._Test__y)#How  to  print  private  variable  'y'
		t.__m2()#How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(t.x)#How  to  print   variable  'x'
		print(self._Test__y)#How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x)#How  to  print  variable  'x'
print(t._Test__y)#How  to  print   variable  'y'
print(t . __y)#error cannot access like this directly out side the class, ie t ._Text __y
print(t . _dict_)#{x:10,Test._y__=20}
t.m1()#How  to  call  method  m1()
t._Test__m2()#How  to  call   method  m2()
t . __m2()#__m2  method<nxt> 10<nxt>20
print('End')


# Object  't'  --->x=10, (private variable) y=20


 #  Find  outputs
class  c1:
	def _init_(self):
		self.x=10#How  to  initialize  public  variable  'x'  with  10
		self.__y=20#How  to  initialize  private  variable  'x'  with  20
		self.__x__ =30#How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)#How  to  print   variable  'x'
print(a.__x__)#How  to  print  public  dunder  variable  'x'
print(a._c1__x)#How  to  print   private  variable  'x'
print(a . __x)#error because we cannot acees the private variable directly
a.m1()#How  to  call  public  method  m1()
a.__m1__#How  to  call  public  dunder  method  m1()
a.__m1()#How  to  call  private  method  m1()
a . __m1()#public Dunder method


# Object  'a'   --->x=10,__y=20,__x__=30


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
a = c1()#Object  is  created  at  address  :  ' , id(self)      ##here self is a
a = None#Object  at  address  {id(self)}  is  lost              ###here self is a
b = c1()#Object  is  created  at  address  :  ' , id(self)      ##here self is b
del    b#Object  at  address  {id(self)}  is  lost              ##here self is b
c = c1()#Object  is  created  at  address  :  ' , id(self) <nxt>Object  at  address  {id(self)}  is  lost'
c = c1()#Object  is  created  at  address  :  ' , id(self)      ##here self is c
d = c1()#Object  is  created  at  address  :  ' , id(self)      ##here self is d
e = c1()#Object  is  created  at  address  :  ' , id(self)      ##here self is e
#   
# 

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()#__del__ expects one argument both 0 are passing
a . __del__(25)



# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()#destructor : ' ,35
a . __del__(25)#destructor : 25




# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()



#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()#constructor<nxt>destructor<nxt>constructor<nxt>destructor<nxt>constructor<nxt>...............constructor<nxt>destructor<nxt>constructor...



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()#3rd  destructor




# 
#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()#Object  is  created  at  address  :  ' , id(a)<nxt>Object  is  created  at  address  :  ' , id(b)<nxt>Object  is  created  at  address  :  ' , id(c)
del   a#Object  at  address  {id(a)}  is  lost 
print('Hello')#Hello
del   b#Object  at  address  {id(b)}  is  lost
print('Hi')#Hi
del   c##Object  at  address  {id(b)}  is  lost
print('Bye')#Bye
d = c1()#Object  is  created  at  address  :  ' , id(d)
print('End')#End
#
# 

 # Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list#no __init__method is ececuted as it is not deleting obj of class c1
#


#  Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . _del_())#25
print('Hello')#Hello
del   a#destructor