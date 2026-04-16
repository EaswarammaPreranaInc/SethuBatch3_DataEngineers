# Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
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
print(t . _dict_)
How  to  call  method  m1()
How  to  call   method  m2()
t . __m2()
print('End')




class Test:
    def __init__(self):
        self.x = 10
        
        self.__y = 20

    def m1(self):
        print('m1 method')
      
        print(self.x)
        
        print(self.__y)
     
        self.__m2()
        
        print('Back to m1 method')

    def __m2(self):
        print('__m2 method')
    
        print(self.x)
        
        print(self.__y)

t = Test()

print('Outside')
print(t.x)
print(t._Test__y)

print(t.__dict__)
t.m1()
t._Test__m2()

print('End')


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


class c1:
    def __init__(self):
        self.x = 10
        self.__x = 20
        self._x_ = 30

    def m1(self):
        print('public method')

    def __m1(self):
        print('private method')

    def _m1_(self):
        print('public Dunder method')

a = c1()

print(a.x)
print(a._x_)
print(a._c1__x)

a.m1()
a._m1_()
a._c1__m1()


'''Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively'''

class c1:
    def __init__(self):
        print('Object is created at address :', id(self))

    def __del__(self):
        print(f'Object at address {id(self)} is lost')

a = c1()     # 1000
a = None     # old object (1000) destroyed

b = c1()     # 2000
del b        # object (2000) destroyed

c = c1()     # 3000
c = c1()     # new object (4000), old (3000) destroyed

d = c1()     # 4000
e = c1()     # 5000


# Identify  Error (Home  work)
class   c1:
	def  _del_(self , x): #doubleunder score is missing
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)

# Find  outputs (Home  work)
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x) #25
a = c1()
a . _del_(25)

# Find  outputs (Home  work)
class   c1:
	def  _del_(self):
			print('destructor') #destructor
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
a = c1() #empty

#Find  outputs (Home  work)
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello') #Hello
del   b
print('Hi') #Hi
del   c
print('Bye') #Bye
d = c1()
print('End') #End


# Find  outputs(Home  work)
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
# End  of  the  class
list = [c1() , c1() , c1()] #empty
del  list


# Find  outputs  (Home  work)
class   c1:
	def  _del_(self):
		print('destructor') #destructor
		return  25 #25
a = c1()
print(a . _del_())
print('Hello') #Hello
del   a



