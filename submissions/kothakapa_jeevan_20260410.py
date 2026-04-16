# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		How  to  initialize  public  variable  'x'  to  10
		How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		How  to  print   variable  'x'
		How  to  print  private  variable  'y'
		How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'
		How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
How  to  print  variable  'x'
How  to  print   variable  'y'
print(t . __y)
print(t . __dict__)
How  to  call  method  m1()
How  to  call   method  m2()
t . __m2()
print('End')

# Object  't'  --->
Outside
10
20
{'x': 10, '_Test__y': 20}
m1 method
10
20
__m2 method
10
20
Back to m1 method
__m2 method
10
20
End




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

# Object  'a'   --->


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
print(a.x)
print(a.__x__)
print(a._c1__x)
print(a.__x)
a.m1()
a.__m1__()

a._c1__m1()

# direct call (ERROR)
# a.__m1()




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
a = c1() --> Object created
a = None --> 
b = c1() --> old object lost ref 1000 and new object 2000 created
del  b --> object ref 2000 lost
c = c1() --> object created ref 3000
c = c1() --> same object as above
d = c1() --> recent object lost and new object created ref 4000
e = c1() --> last object lost and new object created ref 5000



# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x): --> (destructor not recommend any argument ,here we are passing an argument)
		print('destructor : ' ,  x)
a = c1()
a . __del__(25) --> (argument given here,for destructor arguments not recommended)




# Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a . __del__(25)---> destructor, 25



# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() --> infinite recursion



# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1() --> same as last program here also we get infinite recursion



#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1() --> 3rd destructor ( here last one is recognised rest are discarded)


#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1() --> object created
del   a --> object deleted but a and b points to same object
print('Hello') --> Hello
del   b --> ref b lost and c point to the same object
print('Hi') --> Hi
del   c --> object lost
print('Bye' --<> Bye
d = c1() --> new object created
print('End') --> End



# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()] --> list of 3 tuples created
del  list --> deleted list of 3 tuples



# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor') --> destructor
		return  25  --> 25
a = c1()
print(a . __del__())
print('Hello') --> Hello
del   a --> destructor








