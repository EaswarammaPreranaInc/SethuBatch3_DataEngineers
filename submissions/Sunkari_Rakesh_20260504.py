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
		self.m1()#How  to  call  method  m1()  of  class  C  without  creating  another  object
		super().m1()#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		super(C, self).m1()#How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		super(B, self).m1()#How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() 
		super(C) . m1()   
		super(D , D) . m1()  
# End  of  the  class




How  to  call  method  m1()  of  class  D
# Find  outputs  (Home  work)
class  father:
        def  height(self):
                print('Father  Height')#
class  mother:
        def  color(self):
                print('Mother  Color')#
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')#
# End  of  the  class
c  =  child()
c . qualification()#Child Qualification
c . color()#Mother  Color
c . height()#Father  Height
c . m1()#error


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
c . m1()#Child  Method


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
c . m1()#Father  Method


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
c . m1()#Mother  Method


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
c . m1()#Uncle  Method


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
c . m1()#error


# Identify  Error
class  c1(c1):
	     pass#c1 is not defined initially so cannot be used asa parent class 
		 
		 
# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')#Parent Method
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')#Child Method
a = c1()
a . m1()#Parent method <nextline> Child Method


# Identify  Error
class   c1(c2): #here c2 is not defined before c1 so cannot be considered as parent class
	pass
class  c2(c1):
	pass


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
			super() . m1()
			print('Grand  Child  Method')
a = c2()
a . m1()#Grand Child Method <nextline> Child Method <nextline> Parent Method


# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		super().__init__()#How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super().__del__()#How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')


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
c = child()# child constructor <2nextline> child destructor
print('Bye')#Bye


# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()#parent constructor <nextline> parent destructor
print('Bye')#Bye


# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2, b2)#How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp()#How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()


class parent:
    x = 100  # Static Variable
    def __init__(self):
        self.x = 10 # Instance Variable

class child(parent):
    def __init__(self):
        super().__init__()
        self.y = 20 # Instance Variable
    def disp(self):
        # How to print static variable 'x'
        print(parent.x)
        
        # How to print static variable 'x' in another way
        print(child.x)
        
        # How to print static variable 'x' in one more way
        print(self.__class__.x)
        
        # How to print variable 'x' of object 'c'
        print(self.x)
        
        # How to print variable 'y' of object 'c'
        print(self.y)

# How to call disp() method of child class
c = child()
c.disp()


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
		print(self . x)    
		print(super() . x) 
# End of the class
c = child()
c . disp()#30 20 10


'''
static   variable  ---> x =10  

Object  'c'  ---> x = 20 
'''


# Find outputs
class    parent:
	a = 10
	def    __init__(self):
		print('Parent  constructor')
		self.x = 30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   parent.a)
		print('Parent  class  "class"  method  :  ' ,  cls.a)
		# print(self . a)  # Error because self is not defined
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a)
	def   __del__(self):
		print('parent  destructor  :  ' ,  self.x)
class  child(parent):
	b = 20
	def   __init__(self):
		super().__init__()
		print('Child  constructor')
		self.y = 40
	def   m1(self):
		super().m1()
		print('Child  class  instance  method' , self.y)
	@classmethod
	def   m2(cls):
		super().m2()
		parent.m2()
		super(child,cls) . m2()  
		# self . m2()  # Error because self is not defined
		print('Child  class  "class"  method')
                print(super().a)
		print(cls.a)
		print(child.a)
		print(parent.a)
		print(child.b)
		print(cls.b)
	@staticmethod
	def   m3():
		super(child,child).m3()
		parent.m3()
		# super() . m3()  # Error because super() function should have two arguments while using inside a static method
		# self . m3() # Error self is not defined
		# cls . m3()  # Error cls is not defined
		print('child  class  static  method' ,  child.a)
		print(super(child,child).a)
		print(child.b)
	def __del__(self):
		super().__del__()
		print('child  destructor' ,  self.y)
#end of the class
m = child()
child.m2()
child.m3()
m.m1()

''' 
Output
Parent  constructor
Child  constructor
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Parent  class  "class"  method  :   10
Child  class  "class"  method
10
10
10
10
20
20
Parent  class  static  method  :   10
Parent  class  static  method  :   10
child  class  static  method 10
10
20
Parent  class  instance  method  :   30
Child  class  instance  method 40
parent  destructor  :   30
child  destructor 40

'''
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
		super().m1()
		super(child,self).m1()
		super(father,self).m1()
		super(mother,self).m1()
		# super(uncle , self) . m1() # Error because the parent of uncle class is object class which does not have m1() method
# End of the class
print(child . __mro__)  
c = child()
c.m1()
print('Bye')

'''
Output
(child , father , mother , uncle , object)
m1  method  of  child  class
m1  method  of  Father  class
m1  method  of  Father  class
m1  method  of  Mother  class
m1  method  of  Uncle  class
Bye

'''

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
		# super() . m1()  # Error parent of D class is object class which does not have method m1() 
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
obj . m1()
print('Bye')

''' 
Output
[P, X , A , Y , B , C , D ,Object]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye
'''

# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . _init_()  
                print('class D constructor') 
class  E:
        def __init__(self):
                super() . _init_()  
                print('class E constructor') 
class  F:
        def __init__(self):
                super() . _init_()  
                print('class F constructor')  
class  B(D , E):
        def __init__(self):
                super() . _init_()  
                print('class B constructor')  
class  C(D , E , F):
        def __init__(self):
                super() . _init_()  
                print('class C constructor')  
class  A(B , C):
        def __init__(self):
                super() . _init_()  
                print('class A constructor') 
# End  of  the  class
print(A . mro())  
obj = A()
print('Bye')

'''
Outputs
[ A , B , C , D , E , F , object]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye

'''

#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1,mod2
print(mod1.x)
mod1.f1()
m = mod1.c1()
m.m1()
print()
print()
print(mod2.x)
mod2.f1()
m = mod2.c2()
m.m1()
# print(p1 . mod1 . x)  # Error because p1 is not defined
# print(x) # Error because members of the module are not imported

''' 
Outputs
10
Function of mod1 module
Method  of  class  c1  in mod1  module

20
Function of mod2 module
Method  of  class  c1  in mod2  module
'''

#  Save  in  any  file  of  cwd
from p1.mod1 import *
print(x)
f1()
m = c1()
m.m1()
print()
print()
from p1.mod2 import *
print(x)
f1()
m = c1()
m.m1()
# print(p1 . mod1 . x)  # Error p1 and mod1 are not defined
# print(mod1 . x)  # Error mod1 is not imported
# from  p1   import  mod1 . * # Error cannot use dot in import clause

''' 
Outputs
10
Function of mod1 module
Method  of  class  c1  in mod1  module

20
Function of mod2 module
Method  of  class  c1  in mod2  module
'''

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

'''
Outputs
20
Function of mod2 module
Method  of  class  c1  in mod2  module
'''

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

'''
Outputs
10
Function of mod1 module
Method  of  class  c1  in mod1  module
'''

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

''' 
Outputs
30
Function of same module
Method  of  class  c1  in same  module
'''

'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1.mod1 import x as x1 , f1 as f_1 , c1 as c_1 
from p1.mod2 import x as x2 , f1 as f_2 , c1 as c_2 
print(x1)
f_1()
a = c_1()
a.m1()
print()
print()
print(x2)
f_2()
a = c_2()
a.m1()

''' 
Outputs
10
Function of mod1 module
Method  of  class  c1  in mod1  module

20
Function of mod2 module
Method  of  class  c1  in mod2  module
'''