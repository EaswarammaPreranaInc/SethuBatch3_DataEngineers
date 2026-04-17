
# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		How  to  initialize  public  variable  'x'  to  10 # self.x=10
		How  to  initialize  private  variable  'y'  to  20 # self.__y=20
	def  m1(self):
		print('m1  method') # m1 method
		How  to  print   variable  'x' # print(self.x) 10
		How  to  print  private  variable  'y' # print(self.__y)  20
		How  to  call    private  method   m2() # self.__m2()
		print('Back to m1 method') # Back to m1 method
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x' # print(self.x)
		How  to  print  private  variable   'y' # print(self.__y)
# End  of  the  class
t = Test()
print('Outside') # Outside
How  to  print  variable  'x' # print(t.x)
How  to  print   variable  'y' # print(t._Test__y)
print(t . __y) # Error
print(t . __dict__) # {'x': 10, '_Test__y': 20}
How  to  call  method  m1() # t.m1()
How  to  call   method  m2() # t._Test__m2()
t . __m2() # Error
print('End') # End



#  Find  outputs
class  c1:
	def __init__(self):
		How  to  initialize  public  variable  'x'  with  10 # self.x=10
		How  to  initialize  private  variable  'x'  with  20 self.__x=10
		How  to  initialize  public  dunder  variable  'x'  with  30 #  self.__x__=10
	def  m1(self):
		print('public method') # public method
	def  __m1(self):
		print('private method') # private method
	def  __m1__(self):
		print('public Dunder method') # public Dunder method
#  End  of  the  class
a = c1()
How  to  print   variable  'x' # print(a.x)
How  to  print  public  dunder  variable  'x' # print(a.__x__)
How  to  print   private  variable  'x'# print(a._c1__x)
print(a . __x) # Error 
How  to  call  public  method  m1() # a.m1()
How  to  call  public  dunder  method  m1() # a.__m1__()
How  to  call  private  method  m1() # a._c1__m1()
a . __m1() # Error



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
b = c1() # Object  is  created  at  address  :  1000
del    b # Object  at  address  1000  is  lost
c = c1() # Object  is  created  at  address  :  1000 
c = c1() # Object  is  created  at  address  :  2000 Object  at  address  1000  is  lost
d = c1() # Object  is  created  at  address  :  3000
e = c1() # Object  is  created  at  address  :  4000
Object  at  address 2000  is  lost
Object  at  address 3000  is  lost
Object  at  address 4000  is  lost


# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x) # destructor :  25
a = c1()
a . __del__(25) # Error



# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x) # destructor :  25
a = c1() 
a . __del__(25) # destructor :  25 is deleted



# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # destructor infinite
			b = c1()
a = c1()



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor') # constructor infinite
		del  self
	def  __del__(self):
		print('destructor') # destructor infinite
		b = c1()
a = c1()



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor') # 3rd destructor
# End  of  the  class
a = c1()



#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() # Object  is  created  at  address  :  10000
del   a # object at address 10000 is lost 
print('Hello') # Hello
del   b # object at address 10000 is lost
print('Hi') # Hi
del   c # object at address 10000 is lost
print('Bye') # Bye
d = c1() # Object  is  created  at  address  :  20000
print('End') # End




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
Object  is  created  at  address  :   10000
Object  is  created  at  address  :   20000
Object  is  created  at  address  :   30000
Object  at  address  10000 address  is  lost 
Object  at  address  20000 address  is  lost 
Object  at  address  30000 address  is  lost 
'''



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__()) # destructor <nextline> 25
print('Hello') # Hello
del   a # object a will be deleted


