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
c . qualification()  #Child Qualification
c . color()     #Mother Color
c . height()    #Father Height
c . m1()     #Error
----------------------------------------------------------------------------------------------
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
d=D() 
d.m1() 
c.m1(d) 
B.m1(d)
super(C,d).m1()

		How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() 
		super(C) . m1()   
		super(D , D) . m1()  
# End  of  the  class
How  to  call  method  m1()  of  class  D
-----------------------------------------------------------------------------------------------
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
c . m1()   Child Method
-----------------------------------------------------------------------------------------------
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
c . m1()   #Father Method
---------------------------------------------------------------------------------------------
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
c . m1()   #Mother Method
---------------------------------------------------------------------------------------------
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
c . m1()     #Uncle Method
----------------------------------------------------------------------------------------------
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
c . m1()  #Error
----------------------------------------------------------------------------------------------
# Identify  Error
class  c1(c1):   #Error
	     pass
---------------------------------------------------------------------------------------------
 # Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()        #Parent Method    Child Method
----------------------------------------------------------------------------------------------
 # Identify  Error
class   c1(c2):  #Error c2 is not defined at
	pass
class  c2(c1):
	pass
---------------------------------------------------------------------------------------------
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
a . m1()
----------------------------------------------------------------------------------------------
 # Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')
---------------------------------------------------------------------------------------------
 # Find  outputs  (Home  work)
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
print('Bye')
--------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()
print('Bye')
---------------------------------------------------------------------------------------------
# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()
-------------------------------------------------------------------------------------------
# Find outputs  (Home  work)
class  parent:
	x = 100
	def   _init_(self):
		self . x = 10
class   child(parent):
	def   _init_(self):
		super() . _init_()
		self . y = 20
	def disp(self):
		How  to  print  static  variable  'x'
		How  to  print  static  variable  'x'   in  another  way
		How  to  print  static  variable  'x'   in  one  more  way
		How  to  print  variable  'x'  of  object  'c'
		How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
How  to  call  disp()  method  of   child  class
---------------------------------------------------------------------------------------------
 # Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x)   
		super() . _init_()
	def  disp(self):
		print(self . x)    
		print(super() . x) 
# End of the class
c = child()
c . disp()


'''
static   variable  --->  

Object  'c'  --->  
'''
-------------------------------------------------------------------------------------------
# Find outputs
class    parent:
	How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  How  to  print  variable  'x')
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   How  to  print  static  variable  'a')
		print('Parent  class  "class"  method  :  ' ,  How  to  print  static  variable  'a'  in  another  way)
		print(self . a)  
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  How  to  print  static  variable  'a')
	def   _del_(self):
		print('parent  destructor  :  ' ,  How  to  print  variable  'x')
class…
--------------------------------------------------------------------------------------------
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
		How  to  call  m1()  method  of  father  class  without  creating  another  object
		How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		How  to  call  m1()  method  of  mother  class   without  creating  an  object
		How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() 
# End of the class
print(child . _mro_)  
How  to  call  m1()  method  of  child  class
print('Bye')
--------------------------------------------------------------------------------------------
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
obj . m1()
print('Bye')
---------------------------------------------------------------------------------------------
# Find  outputs  (Home  work)
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
print(A . mro())  
obj = A()
print('Bye')
------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------------------------
'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
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
-------------------------------------------------------------------------------------------