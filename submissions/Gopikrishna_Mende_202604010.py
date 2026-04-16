class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self.__y)
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
print(t._Test__y)
print(t . __y)  #error-private variables cannot be called directly from outside
print(t . __dict__)  #{'x':10,'_Test__y':20}
t.m1()
t._Test__m1()
t . __m2()  #error-private methods cannot be called directly from outside
print('End')


# Object  't'  --->


#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10# How  to  initialize  public  variable  'x'  with  10
		self.__x=20# How  to  initialize  private  variable  'x'  with  20
		self.__x__=30# How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x)  #How  to  print   variable  'x'
print(a.__x__)# How  to  print  public  dunder  variable  'x'
print(a._c1__x)# How  to  print   private  variable  'x'
print(a . __x)   #error-private variables cannot be accessed from outside directly
a.m1()# How  to  call  public  method  m1()
a.__m1__()# How  to  call  public  dunder  method  m1()
a._c1__m1()# How  to  call  private  method  m1()
a . __m1()  #error-private methods cannot be accessed from outside directly


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
a = c1()  #Object  is  created  at  address  :  1000
a = None  #Object  at  address  1000  is  lost
b = c1()  #Object  is  created  at  address  :  2000
del    b  #Object  at  address  2000  is  lost
c = c1()  #Object  is  created  at  address  :  3000
c = c1()  #Object  is  created  at  address  :  other than 3000
          #Object  at  address  3000  is  lost
d = c1()  #Object  is  created  at  address  :  4000
e = c1()  #Object  is  created  at  address  :  5000
          #Object  at  address  other than 3000  is  lost
          #Object  at  address  4000  is  lost
          #Object  at  address  5000  is  lost

# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):  #destructor cannot have arguments other than self
		print('destructor : ' ,  x)
a = c1()
a . __del__(25)  #destructor takes 0 args


# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)   #destructor : 25
                  #destructot : 35


# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()   #infinite loop


# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
constructor
destructor
constructor
destructor........infinite loop
'''

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
#3rd constructor


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()  #Object  is  created  at  address  :  1000
del   a  #Ref a is deleted
print('Hello')   #Hello
del   b  #Ref b is deleted
print('Hi')  #Hi
del   c   #Object  at  address  1000  is  lost
print('Bye')  #Bye
d = c1()  #Object  is  created  at  address  :  2000
print('End')  #End
              #Object  at  address  2000  is  lost

# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list

'''
Object  is  created  at  address  :  1000
Object  is  created  at  address  :  2000
Object  is  created  at  address  :  3000
Object  at  address  1000  is  lost
Object  at  address  2000  is  lost
Object  at  address  3000  is  lost

'''


# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())  #destructor
                      #25
print('Hello')        #Hello
del   a               #destructor