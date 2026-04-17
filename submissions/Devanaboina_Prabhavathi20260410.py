# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		How  to  initialize  public  variable  'x'  to  10 # print('x =', self.x)
		How  to  initialize  private  variable  'y'  to  20 # print('y =', self.__y)
	def  m1(self):
		print('m1  method') # m1 method
		How  to  print   variable  'x' print(x) Outside # {'x': 10, '_Test__y': 20}
		How  to  print  private  variable  'y'  #print(self._y)
		How  to  call    private  method   m2() #  def m1(self):  self._m2()
		print('Back to m1 method') # Back to m1 method
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'
		How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside') # outside
How  to  print  variable  'x' # print('x =', t.x)
How  to  print   variable  'y'
print(t . __y)
print(t . __dict__) #{'x': 10, '_Test__y': 20}
How  to  call  method  m1()
How  to  call   method  m2()
t . __m2()
print('End') # End




#  Find  outputs
class  c1:
	def __init__(self):
		How  to  initialize  public  variable  'x'  with  10
		How  to  initialize  private  variable  'x'  with  20
		How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
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


# Find outputs
class c1:
    def __init__(self):
        self.x = 10
        self.__x = 20
        self.__x__ = 30

    def m1(self):
        print('public method')

    def __m1(self):
        print('private method')

    def __m1__(self):
        print('public Dunder method')


# End of the class

a = c1()

# print variables
print(a.x)          
print(a.__x__)      
print(a._c1__x)     

# call methods
a.m1()              
a.__m1__()        
a._c1__m1()         




'''  
Find  outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self)) # Object  is  created  at  address
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1() # 1000
a = None
b = c1()  # 2000
del    b # 2000 is del
c = c1() # 3000
c = c1() # 4000
d = c1() # 5000
e = c1() # 6000


# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x) # destructor 25
a = c1()
a . __del__(25) # error




# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x) #  destructor 25
a = c1()
a . __del__(25)



# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor') # destructor
			b = c1()
a = c1()



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor') # constructor
		del  self
	def  __del__(self):
		print('destructor') #
		b = c1()
a = c1()



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor') 
	def  __del__(self):
		print('2nd  destructor') 
	def  __del__(self):
		print('3rd  destructor') # 3rd  destructor
# End  of  the  class
a = c1()


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self)) # Object  is  created  at  a
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello') # Hello
del   b
print('Hi') # Hi
del   c
print('Bye') # Bye
d = c1()
print('End') #End



# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self)) # Object  is  created  at  address  :   139644129410192
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del  list



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor') # destructor
		return  25  # 25
a = c1()
print(a . __del__())
print('Hello')  # Hello
del   a