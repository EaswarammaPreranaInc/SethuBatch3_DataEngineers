# Multilevel  inheritance  demo  program
class  A:
	def    m1(self):
		print('class   A  method')
class  B(A):
	def  m1(self):
		print('class  B   method')
class   C(B):
	def  m1(self):
		print('class   C    method')
class   D(C):
	def   m1(self):
		print('class   D   method')
		super(D,self).m1()#How  to  call  method  m1()  of  class  C  without  creating  another  object
		super(C,self).m1()#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		super(B,self).m1()#How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		#How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		#super(A , self) . m1() 
		#super(C) . m1()   
		#super(D , D) . m1()  
# End  of  the  class
obj=D()

obj.m1()#How  to  call  method  m1()  of  class  D
#########################################################################################
# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')
class  mother:
        def  color(self):
                print('Mother  Color')
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')
# End  of  the  class
c  =  child()
c . qualification()#Child Qualification
c . color()#Mother Color
c . height()#Father Height
c . m1()#Error
#########################################################################################
#  Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
        def  m1(self):
                print('Child  Method')
# End  of  the  class
c = child()
c . m1()#child method
#########################################################################################
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')
class  child(father , mother , uncle):
	pass
# End  of  the  class
c = child()
c . m1()#Father Method 
#########################################################################################
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()#Mother Method
#########################################################################################
# Find  outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()#Uncle Method
#########################################################################################
# Find  outputs
class  uncle:
        pass
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()#error /Nothing is printed
#########################################################################################
# Identify  Error
class  c1(c1):
	     pass

#########################################################################################
# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()#Parent Method Child Method
#########################################################################################
# Identify  Error
class   c1(c2): 
	pass
class  c2(c1):
	pass
#########################################################################################
# Find  outputs
class   c2:
	def  m1(self):
			print('Parent  Method')
class   c1(c2):
	def  m1(self):
			super() . m1()
			print('Child  Method')
class  c2(c1):
	def  m1(self):
			super() . m1()#->c1().m1()-->c2().m1()=
			print('Grand  Child  Method')
a = c2()
a . m1()#Parent Method  Child Method    Grand Child method
#########################################################################################
# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		#How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		#How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')
'''
child   constructor
Bye
child   destructor'''
#########################################################################################
# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		print('child   constructor')
	def   __del__(self):
		print('child  destructor')
# End of the class
c = child()
print('Bye')
'''
child constructor
Bye
child destructor'''
#########################################################################################
# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')
'''
parent  constructor
Bye
parent  destructor'''
#########################################################################################
# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):#a2=10 b2=20 c2=30 d2=40
		#How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		#How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()#30 40
print('Object  y')
y . disp()#0 0
#########################################################################################
# Find outputs  (Home  work)
class  parent:
	x = 100
	def   __init__(self):
		self . x = 10
class   child(parent):
	def   __init__(self):
		super() . __init__()
		self . y = 20
	def disp(self):
        
		print(super().x)#How  to  print  static  variable  'x'
		print(child.x)#How  to  print  static  variable  'x'   in  another  way
		print(parent.x)##How  to  print  static  variable  'x'   in  one  more  way
		print(parent().x)#How  to  print  variable  'x'  of  object  'c'
		print(self.y)#How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
#How  to  call  disp()  method  of   child  class
c=child()
c.disp()
#########################################################################################
# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20
class   child(parent):
	def  __init__(self):
		self . x = 30
		print(self . x)   
		super() . __init__()
	def  disp(self):
		print(self . x)  #30  
		print(super() . x) #10
# End of the class
c = child()
c . disp()#30 10
'''
static   variable  --->  x=10 

Object  'c'  --->  
'''
#########################################################################################
class parent:
    a = 10   # static variable

    def __init__(self):
        print('Parent constructor')
        self.x = 30   # instance variable

    def m1(self):
        print('Parent class instance method :', self.x)

    @classmethod
    def m2(cls):
        print('Parent class "class" method :', cls.a)
        print('Parent class "class" method :', parent.a)

    @staticmethod
    def m3():
        print('Parent class static method :', parent.a)

    def __del__(self):
        print('Parent destructor :', self.x)


class child(parent):
    b = 20   # static variable

    def __init__(self):
        super().__init__()   # call parent constructor
        print('Child constructor')
        self.y = 40   # instance variable

    def m1(self):
        super().m1()   # call parent m1()
        print('Child class instance method :', self.y)

    @classmethod
    def m2(cls):
        super().m2()   # call parent m2()
        parent.m2()    # another way

        print('Child class "class" method')
        print(cls.a)
        print(parent.a)
        print(child.a)
        print(cls.__bases__[0].a)

        print(cls.b)
        print(child.b)

    @staticmethod
    def m3():
        parent.m3()   # call parent static method
        super(child, child).m3()  # another way

        print('Child class static method :', parent.a)
        print(child.a)
        print(child.b)

    def __del__(self):
        super().__del__()   # call parent destructor
        print('Child destructor :', self.y)


# Calling methods
child.m2()   # call class method
child.m3()   # call static method

obj = child()
obj.m1()     # call instance method
###########################################################################################
# Find  outputs
class   father:
	def  m1(self):
		print('m1  method  of  Father  class')
class   mother:
	def  m1(self):
		print('m1  method  of  Mother  class')
class   uncle:
	def  m1(self):
		print('m1  method  of  Uncle  class')
class   child(father , mother , uncle):
	def  m1(self):
		print('m1  method  of  child  class')
		super(child,self).m1()#How  to  call  m1()  method  of  father  class  without  creating  another  object
		super().m1()#How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father,self).m1()#How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother,self).m1()#How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		#super(uncle , self) . m1() 
# End of the class
print(child . __mro__)  
c=child()
c.m1()#How  to  call  m1()  method  of  child  class
print('Bye')
#########################################################################################
# Find outputs  (Home  work)
class  A:
	def  m1(self):
		super() . m1() 
		print('class A method')    
class  B:
	def m1(self):
		super() . m1()  
		print('class B method') 
class  C:
	def m1(self):
		super() . m1() 
		print('class C method') 
class  D:
	def m1(self):
		super() . m1()  
		print('class D method')  
class  X(A , B):
        def m1(self):
                super() . m1()  
                print('class X method') 
class  Y(B , C , D):
        def m1(self):
                super() . m1()  
                print('class Y method') 
class  P(X , Y , C):
        def m1(self):
                super() . m1() 
                print('class P method') 
# End  of  the  class
print(P . mro())   
obj = P()
obj . m1()#error
print('Bye')
#########################################################################################
# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()  
                print('class D constructor') 
class  E:
        def __init__(self):
                super() . __init__()  
                print('class E constructor') 
class  F:
        def __init__(self):
                super() . __init__()  
                print('class F constructor')  
class  B(D , E):
        def __init__(self):
                super() . __init__()  
                print('class B constructor')  
class  C(D , E , F):
        def __init__(self):
                super() . __init__()  
                print('class C constructor')  
class  A(B , C):
        def __init__(self):
                super() . __init__()  
                print('class A constructor') 
# End  of  the  class
print(A . mro())  
obj = A()
print('Bye')
'''
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye'''
#########################################################################################
#  Save  in  any  file  of  cwd  (Homework)
How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  
print(x)
#  Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in  package  p1
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  import   members  of  mod2   in  package  p1
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  
print(mod1 . x)  
from  p1   import  mod1 . *
#########################################################################################
'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)  
f1() 
a = c1()
a . m1()
#########################################################################################
'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2    import   *
from  p1 . mod1    import   *
print(x)  
f1()
a = c1()
a . m1()
''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1    import    *
from  p1 . mod2    import    *
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) 
f1()
a = c1()
a . m1()
'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
#########################################################################################
How  to  use  members  of  both  the  modules
'''
How  to  import   members  of  mod1   in  package  p1 
How  to  import   members  of  mod2   in  package  p1  
How  to  print  object  'x'  of   mod1  in  package  p1
How  to  call  function  f1()  of   mod1  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1
How  to  call  function  f1()  of   mod2  in  package  p1
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1