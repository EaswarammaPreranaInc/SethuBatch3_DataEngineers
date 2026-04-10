# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x = 10 
		self._y = 20 
	def  m1(self):
		print('m1  method')
		print(self.x)
		print(self._y) 
		__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) 
		print(self._y) 
# End  of  the  class
t = Test() # Object of class Test is created
print('Outside') # Outside
print(t.x) # 10
print(t._Test__y) # 20
# print(t . __y) # Error we cannot directly access the private variable outside the class
print(t . _dict_) # {'x' : 10 , '_Test__y': 20}
t.m1() # m1 method <nextline> 10 <nextline> 20 <nextline> Back to m1 method
t._Test__m2() # __m2 method <nextline> 10 <nextline> 20 
t . __m2() # Error we cannot directly call the private method outside the class
print('End') # End

# Object  't'  ---> x = 10 , _Test__y = 20



#  Find  outputs
class  c1:
	def __init__(self):
		self.x = 10
		self.__x = 20
		self.__x__ = 30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) # 10
print(a.__x__) # 30
print(a._c1__x) # 20
# print(a.__x) # Error we cannot directly access the private variable outside the class
a.m1() # public method
a.__m1__() # public Dunder method
a._c1__m1() # private method
# a . __m1() # Error we cannot directly call the private method outside the class


# Object  'a'   ---> x = 10 , _c1__x = 20 , __x__ = 30

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