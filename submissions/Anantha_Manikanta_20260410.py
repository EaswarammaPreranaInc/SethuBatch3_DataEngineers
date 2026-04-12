'''
1) # Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		How  to  initialize  public  variable  'x'  to  10
            self.x = 10
		How  to  initialize  private  variable  'y'  to  20
            self.__y = 20

	def  m1(self):
		print('m1  method')
		How  to  print   variable  'x'
            print(self.x)
		How  to  print  private  variable  'y'
            print(self.__y)
		How  to  call    private  method   m2()
            self.__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		How  to  print   variable  'x'
            print(self.x)
		How  to  print  private  variable   'y'
            print(self.x)

# End  of  the  class
t = Test()
print('Outside')
How  to  print  variable  'x'
print(t.x)
How  to  print   variable  'y'
print(t . __y)
print(t . __dict__)
How  to  call  method  m1()
t.m1()
How  to  call   method  m2()
t . __m2()
print('End')  # Outside <nextline> 10 <nextline> Error because Test dont have '__y' <nextline> {'x': 10, '_Test__y': 20} <nextline> m1 method <nextline> 10 <nextline> 20 <nextline> __m2 method <nextline> 10 <nextline> 10 <nextline> Back to m1 method <nextline> Error because Test dont have '__m2' <nextline> End
'''
'''
2) class c1:
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
print(a.__x)
a.m1()
a.__m1__()
a.__m1() # 10 <nextline> 30 <nextline> Error because c1 dont have '__x' <nextline> public method <nextline> public Dunder method <nextline> Error because c1 dont have '__m1'
'''
'''
3) class c1:
    def __init__(self):
        print('Object is created at address : ', id(self))

    def __del__(self):
        print(f'Object at address {id(self)} is lost')
# End of the class
a = c1()
a = None
b = c1()
del b
c = c1()
c = c1()
d = c1()
e = c1()  # Object is created at address : 1000 <nextline> Object at address 1000 is lost <nextline> Object is created at address : 2000 <nextline> Object at address 2000 is lost <nextline> Object is created at address : 3000 <nextline> Object is created at address : 4000 <nextline> Object at address 3000 is lost <nextline> Object is created at address : 5000 <nextline> Object is created at address : 6000
'''
'''
4) # Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' ,  x)
a = c1()
a.__del__(25)  # Error because 1 argument is missing
'''
'''
5) # Find  outputs (Home  work)
class   c1:
	def  __del__(self , x = 35):
		print('destructor : ' , x)
a = c1()
a.__del__(25)   # destructor : 25 <nextline> destructor : 35
'''
'''
6) # Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1()   # destructor <nextline> destructor <nextline> destructor <nextline> ... <nextline> RecursionError
'''
'''
7) # Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()
'''
'''
8) # Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()  # constructor <nextline> destructor <nextline> constructor <nextline> destructor <nextline> constructor <nextline> ... <nextline> RecursionError
'''
'''
9) #  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()
'''
'''
10) #  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()  # 3rd  destructor
'''
'''
11) #Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
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
print('End')  3 d = c1()   # Object is created at address : 1000 <nextline> Hello <nextline> Hi <nextline> Object at address 1000 is lost <nextline> Bye <nextline> Object is created at address : 2000 <nextline> End <nextline> Object at address 2000 is lost
'''
'''
12) # Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()]
del list  # Object is created at address : 1000 <nextline> Object is created at address : 2000 <nextline> Object is created at address : 3000 <nextline> Object at address 3000 is lost <nextline> Object at address 2000 is lost <nextline> Object at address 1000 is lost
'''
'''
13) # Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
print(a . __del__())
print('Hello')
del a   # destructor <nextline> 25 <nextline> Hello <nextline> destructor
'''
'''