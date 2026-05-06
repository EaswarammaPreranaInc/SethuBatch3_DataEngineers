1) Parent  and  child  class  constructors
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		super().__init__() #How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		super().__del__() #How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')

2) outputs  
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		print('child   constructor')
	def   _del_(self):
		print('child  destructor')
# End of the class
c = child()
print('Bye')#Bye

3) outputs 
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')#Bye

4) Parent  and  Child  constructor  demo  program
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2,b2) #How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() #How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()

5) outputs  
class  parent:
	x = 100
	def   _init_(self):
		self . x = 10
class   child(parent):
	def   _init_(self):
		super() . _init_()
		self . y = 20
	def disp(self):
		parent(parent.x) #How  to  print  static  variable  'x'
		parent(child.x) #How  to  print  static  variable  'x'   in  another  way
		print(super().x) #How  to  print  static  variable  'x'   in  one  more  way
		print(self.x) #How  to  print  variable  'x'  of  object  'c'
		print(self.y) #How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
c = child()
c.disp() #How  to  call  disp()  method  of   child  class

6) outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x) #10  
		super() . _init_()
	def  disp(self):
		print(self . x)    
		print(super() . x) 
# End of the class
c = child()
c . disp()


'''
static   variable  --->  x = 30

Object  'c'  --->  x =20
'''

7) outputs
class    parent:
	How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		self.x = 30 #How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x) #How  to  print  variable  'x'
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' , cls.a) # How  to  print  static  variable  'a'
		print('Parent  class  "class"  method  :  ' , parent.a) #How  to  print  static  variable  'a'  in  another  way
		print(self . a)  
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' , parent.a) #How  to  print  static  variable  'a'
	def   _del_(self):
		print('parent  destructor  :  ' , self.x)# How  to  print  variable  'x'
class child(parent):
	b = 20 #How  to  add  static  variable  'b'  with  value  20
	def   _init_(self):
		How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y = 40 #How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method' ,self.y) # How  to  print  variable  'y'
	@classmethod
	def   m2(cls):
		super().m2() #How  to  call  m2()  method  of  parent  class
		parent.m2() #How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  another  object
		cls . m2()  
		self . m2() 
		print('Child  class  "class"  method')
		print(parent.a) #(How  to  print  static  variable  'a')
		print(cls.a) #(How  to  print  static  variable  'a'  in  another  way)
		print(child.a) #(How  to  print  static  variable  'a'  in  one  more  way)
		print(super().a) #(How  to  print  static  variable  'a'  in  last  way)
		print(cls.b) #(How  to  print  static  variable  'b')
		print(child.b) #(How  to  print  static  variable  'b'  in  another  way)
	@staticmethod
	def   m3():
		parent.m3() #How  to  call  m3()  method  of  parent  class
		super(child, child).m3() #How  to  call  m3()  method  of  parent  class  in   another  way
		super() . m3()  
		self . m3() 
		cls . m3()  
		print('child  class  static  method' , parent.a) # How  to  print  static  variable  'a')
		print(child.a) #(How  to  print  static  variable  'a'  in  another  way)
		print(child.b) #(How  to  print  static  variable  'b')
	def _del_(self):
		super().__del__() #How  to  call  destructor  of  parent  class
		print('child  destructor' , self.y) # How  to  print  variable  'y')
#end of the class
child.m2() #How  to  call  m2()  method  of  child  class
child.m3() #How  to  call  m3()  method  of  child  class
obj = child() 
obj.m1() #How  to  call  m1()  method  of  child  class

8) outputs
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
		father.m1(self) #How  to  call  m1()  method  of  father  class  without  creating  another  object
		super().m1() #How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		mother.m1(self) #How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self) #How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() 
# End of the class
print(child . _mro_)  
c = child() #How  to  call  m1()  method  of  child  class
print('Bye')

9) outputs  
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
obj . m1()
print('Bye')

10) outputs  
class  D:
        def _init_(self):
                super() . _init_()  
                print('class D constructor') 
class  E:
        def _init_(self):
                super() . _init_()  
                print('class E constructor') 
class  F:
        def _init_(self):
                super() . _init_()  
                print('class F constructor')  
class  B(D , E):
        def _init_(self):
                super() . _init_()  
                print('class B constructor')  
class  C(D , E , F):
        def _init_(self):
                super() . _init_()  
                print('class C constructor')  
class  A(B , C):
        def _init_(self):
                super() . _init_()  
                print('class A constructor') 
# End  of  the  class
print(A . mro()) #[A, B, C, D, E, F, Object]
obj = A()
print('Bye')#Bye

11) Save  in  any  file  of  cwd 
from p1 import mod1, mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) #How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x) #How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = mod2.c1()
b.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  
print(x)

12) Save  in  any  file  of  cwd
from p1.mod1 import * #How  to  import  members  of  mod1  in  package  p1
print(x) #How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = c1()
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import * #How  to  import   members  of  mod2   in  package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = c1()
b.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  
print(mod1 . x)  
from  p1   import  mod1 . *

Save  the  following  code  in    any  file  of  cwd
13) outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')#Method  of  class  c1  in same  module
from  p1 . mod1    import    *
from  p1 . mod2    import    *
print(x)  
f1() 
a = c1()
a . m1()

Save  the  following  code  in    any  file  of  cwd
14) outputs
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


Save  the  following  code  in    any  file  of  cwd
15) outputs
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

Save  the  following  code  in  any  file  of  cwd
16) How  to  use  members  of  both  the  modules
'''
from p1.mod1 import * #How  to  import   members  of  mod1   in  package  p1 
from p1.mod2 import * #How  to  import   members  of  mod2   in  package  p1  
print(x) #How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a = c1() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(x) #How  to  print  object  'x'  of   mod2  in  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  package  p1
b = c1()
b.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1

17) Multilevel  inheritance  demo  program
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
		c.m1(self) #How  to  call  method  m1()  of  class  C  without  creating  another  object
		super().m1() #How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		B.m1(self) #How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		A.m1(self) #How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() 
		super(C) . m1()   
		super(D , D) . m1()  #Error 
# End  of  the  class
obj = D()
obj.m1() #How  to  call  method  m1()  of  class  D

18) outputs 
class  father:
        def  height(self):
                print('Father  Height')#Father  Height
class  mother:
        def  color(self):
                print('Mother  Color')#Mother  Color
class  child(mother , father):
        def  qualification(self):
                print('Child Qualification')#Child Qualification
# End  of  the  class
c  =  child()
c . qualification()
c . color()
c . height()
c . m1()#Error because m1 is not defined

19) outputs
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
                print('Child  Method')#Child Method
# End  of  the  class
c = child()
c . m1()

20) outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')
class  father:
        def  m1(self):
                print('Father  Method')#Father Method
class  child(father , mother , uncle):
	pass
# End  of  the  class
c = child()
c . m1()

21) outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')
class  mother:
        def  m1(self):
                print('Mother  Method')#Mother Method
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()

22) outputs
class  uncle:
        def  m1(self):
                print('Uncle  Method')#Uncle Method
class  mother:
        pass
class  father:
        pass
class  child(father , mother , uncle):
        pass
# End  of  the  class
c = child()
c . m1()

23) outputs
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
c . m1()#Error because it is not valid

24) Identify  Error
class  c1(c1):  #c1 is not defined
	     pass

25) outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()
#Parent Method
Child Method

26) Identify  Error
class   c1(c2): #c2 is not defined
	pass
class  c2(c1):
	pass

27) outputs
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
a . m1()
#Parent Method
Child Method
Grand Child Method