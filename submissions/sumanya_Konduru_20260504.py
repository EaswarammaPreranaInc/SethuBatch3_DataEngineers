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
		super().m1()#How  to  call  method  m1()  of  class  C  without  creating  another  object
		super(D,self).m1()#How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		super(C,self).m1()#How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		super(B,self).m1()#How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		#super(A , self) . m1() 
		#super(C) . m1() # Error, no one arg
		#super(D , D) . m1()  #Error, since instance method arg should be self
# End  of  the  class
d=D()
d.m1()#How  to  call  method  m1()  of  class  D 


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
c . qualification()# Child Qualification
c . color()# Mother Color
c . height()# Farther height
#c . m1()#Error


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
c . m1()# Chlid Method


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
c . m1()# Father Method

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
c . m1()# Mother Method

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
c . m1()# Uncle Method


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
#c . m1()# Error , bcz no m1() in object class


# Identify  Error
#class  c1(c1):# Error we cannoit derive class from same class
#	     pass

# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()# Parent Method   Child Method


# Identify  Error
#Errorclass   c1(c2): 
#	pass
#class  c2(c1):
#	pass

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
a . m1() # Parent Method   Child Method   Grand child method


# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		p=parent()#How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		super().__del__() #How  to  call  parent  class  destructor
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
c = child()#child   constructor    Bye    Child destructor
print('Bye')


# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()# Parent constructor  Bye  Parent destructor
print('Bye')


# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   __init__(self , a1 , b1):
		self . a = a1#10
		self . b = b1#20
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def __init__(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2,b2) #How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2#30
		self . d = d2#40
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
		print(super().x) #How  to  print  static  variable  'x'
		print(parent.x) #How  to  print  static  variable  'x'   in  another  way
		print(super(child,self).x)  #How  to  print  static  variable  'x'   in  one  more  way
		print(self.x) #How  to  print  variable  'x'  of  object  'c'
		print(self.y) #How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
c=child()
c.disp() #How  to  call  disp()  method  of   child  class


# Find  outputs
class  parent:
	x = 10
	def  __init__(self):
		self . x = 20
class   child(parent):
	def  __init__(self):
		self . x = 30
		print(self . x)   # 30 
		super() . __init__()
	def  disp(self):
		print(self . x)    
		print(super() . x) 
# End of the class
c = child()
c . disp()# 20    10 


# Find outputs
class    parent:
	a=10 #How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self.x=30 #How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   cls.a)
		print('Parent  class  "class"  method  :  ' ,  parent.a)
		#print(self . a)  
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a)
	def   __del__(self):
		print('parent  destructor  :  ' ,  self.x)
class  child(parent):
	b=20
	def   __init__(self):
		super().__init__() #How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40 #How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() #How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method' , self.y)
	@classmethod
	def   m2(cls):
		super().m2() #How  to  call  m2()  method  of  parent  class
		parent.m2() #How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  another  object
		cls . m2()  
		#self . m2() #error
		print('Child  class  "class"  method')
		print(super().a)
		print(parent.a)
		print(super(child,cls).a)
		print(cls.a)
		print(cls.b)
		print(child.b)
	@staticmethod
	def   m3():
		super(child, child).m3() #How  to  call  m3()  method  of  parent  class
		parent.m3() #How  to  call  m3()  method  of  parent  class  in   another  way
		super() . m3()  
		#self . m3() 
		#cls . m3()  
		print('child  class  static  method' ,  super().a)
		print(parent.a)
		print(child.b)
	def __del__(self):
		super().__del__() #How  to  call  destructor  of  parent  class
		print('child  destructor' ,  self.y)
#end of the class
child.m2() #How  to  call  m2()  method  of  child  class
child.m3() #How  to  call  m3()  method  of  child  class
c=child()
c.m1() #How  to  call  m1()  method  of  child  class


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
		super().m1() #How  to  call  m1()  method  of  father  class  without  creating  another  object
		super(child,self).m1() #How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		super(father,self).m1() #How  to  call  m1()  method  of  mother  class   without  creating  an  object
		super(mother,self).m1() #How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		#super(uncle , self) . m1() #Error
# End of the class
print(child . __mro__)  # (child, father, mother , uncle, object)
c=child()
c.m1() #How  to  call  m1()  method  of  child  class
print('Bye')

# Find outputs  (Home  work)
class  A:
	def  m1(self):
		#super() . m1() #Error
		print('class A method')  # 1..class A method  
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
                print('class X method') #2... class x method
class  Y(B , C , D):
        def m1(self):
                super() . m1()  
                print('class Y method') 
class  P(X , Y , C):
        def m1(self):
                super() . m1() 
                print('class P method') # 3..class p method
# End  of  the  class
print(P . mro())   #[P,X,A,Y,B,C,D,O]
obj = P()
obj . m1()
print('Bye')#Bye

# Find  outputs  (Home  work)
class  D:
        def __init__(self):
                super() . __init__()  
                print('class D constructor') #4...
class  E:
        def __init__(self):
                super() . __init__()  
                print('class E constructor') #3...
class  F:
        def __init__(self):
                super() . __init__()  #1... EMPTY 
                print('class F constructor')  #2....
class  B(D , E):
        def __init__(self):
                super() . __init__()  
                print('class B constructor')  
class  C(D , E , F):
        def _init_(self):
                super() . __init__()  
                print('class C constructor') 
class  A(B , C):
        def __init__(self):
                super() . __init__()  
                print('class A constructor') #5...
# End  of  the  class
print(A . mro())  # [A,B,D,E,F,O]
obj = A()
print('Bye')


#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1,mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
mod1.x #How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
c=mod1.c1()
c.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
mod2.x #How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
c=mod2.c1() 
c.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)  # Error
#print(x)# Error

#  Save  in  any  file  of  cwd
from package.mod1 import * #How  to  import  members  of  mod1  in  package  p1
print(x) #How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
c=c1() 
c.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from package.mod2 import * #How  to  import  members  of  mod2  in  package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  package  p1
c=c1() 
c.m1()
#print(p1 . mod1 . x)  Error
#print(mod1 . x)  Error
#from  p1   import  mod1 . *# error, bcz cannot use '.' in import cluase

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
print(x)  # x of p1.mod2 
f1() # f1() of p   1.mod2
a = c1()
a . m1()# m1() of p1.mod2

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
print(x)  # x of p1.mod1 
f1() # f1() of p1.mod1
a = c1()
a . m1()# m1() of p1.mod1

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
print(x) #30
f1()# Function of same module
a = c1()
a . m1()#Method  of  class  c1  in same  module

'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
import p1.mod1 #How  to  import   members  of  mod1   in  package  p1 
import p1.mod2  #How  to  import   members  of  mod2   in  package  p1  
print(p1.mod1.x) #How  to  print  object  'x'  of   mod1  in  package  p1
p1.mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
c=p1.mod1.c1() 
c.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(p1.mod2.x) #How  to  print  object  'x'  of   mod2  in  package  p1
p1.mod2.f1() #How  to  call  function  f1()  of   mod2  in  package  p1
c=p1.mod2.c1() 
c.m1() #How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1