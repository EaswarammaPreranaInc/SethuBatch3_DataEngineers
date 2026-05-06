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
		C.m1(self) # How  to  call  method  m1()  of  class  C  without  creating  another  object
		super(D, self).m1() # How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		B.m1(self) # How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		A.m1(self) # How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() 
		super(C) . m1()  # ERROR because super() can take 0 or 2 arguments only.
		super(D , D) . m1()  # ERROR because 2nd argument should be self for this cases
# End  of  the  class
D().m1() # How  to  call  method  m1()  of  class  D


'''
class   D   method
class   C    method
class   C    method
class  B   method
class   A  method
class  B   method
'''

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
c . qualification()
c . color()
c . height()
c . m1() # ERROR because child class has no method m1()


'''
child → mother → father
Child Qualification
Mother  Color
Father  Height
'''



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
c . m1()


'''
Child  Method
'''

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
c . m1()


'''
Father  Method
'''

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
c . m1()

'''
Mother  Method
'''



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
c . m1()


'''
Uncle  Method
'''




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
c . m1()


'''
Error-child class doesn't have method m1() 
'''



# Identify  Error
class  c1(c1):# Error
	     pass


# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()
a . m1()

'''
Parent  Method
Child  Method
'''


# Identify  Error
class   c1(c2): # c2 class is not defined.Can't be inherited without defining
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
class  c2(c1): # Error
	def  m1(self):
			super() . m1()
			print('Grand  Child  Method')
a = c2()
a . m1()



# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		super().__init__() # How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		super().__del__() # How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()
print('Bye')


'''
parent  constructor
child   constructor
Bye
parent  destructor
child   destructor
'''
''
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


'''
child   constructor
Bye
child  destructor
'''



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


'''
parent  constructor
Bye
parent  destructor
'''

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(a2, b2) # How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp() # How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print('Object  x')
x . disp()
print('Object  y')
y . disp()



'''
Object  x
10	20	30	40
Object  y
0	0	0	0
'''

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
		print(parent.x)  # How  to  print  static  variable  'x'
		print(child.x) # How  to  print  static  variable  'x'   in  another  way
		print(self.__class__.x) # How  to  print  static  variable  'x'   in  one  more  way
		print(self.x) # How  to  print  variable  'x'  of  object  'c'
		print(self.y) # How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
# How  to  call  disp()  method  of   child  class
c = child()
c.disp()
'''
100
100
100
10
20
'''




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
30
20
10
'''




# Find outputs
class    parent:
	a = 10 # How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     __init__(self):
		print('Parent  constructor')
		self.x = 30 # How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   cls.a)
		print('Parent  class  "class"  method  :  ' ,  parent.a)
		print(self . a)  # Error because there is no argument self 
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a)
	def   __del__(self):
		print('parent  destructor  :  ' ,  self.x)
class  child(parent):
	b = 20 # How  to  add  static  variable  'b'  with  value  20
	def   __init__(self):
		super().__init__() # How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y = 40 # How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1() # How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method' ,self.y)
	@classmethod
	def   m2(cls):
		super().m2() # How  to  call  m2()  method  of  parent  class
		parent.m2() # How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  another  object
		cls . m2()  #infinite recursion
		self . m2() # Error because there is no argument self 
		print('Child  class  "class"  method')
		print(cls.a) # How  to  print  static  variable  'a'
		print(parent.a) # How  to  print  static  variable  'a'  in  another  way
		print(child.a) # How  to  print  static  variable  'a'  in  one  more  way
		print(super().a) # How  to  print  static  variable  'a'  in  last  way
		print(cls.b) # How  to  print  static  variable  'b'
		print(child.b) # How  to  print  static  variable  'b'  in  another  way
	@staticmethod
	def   m3():
		parent.m3() # How  to  call  m3()  method  of  parent  class
		How  to  call  m3()  method  of  parent  class  in   another  way
		super() . m3()  # Error because super() must have 2 arguments in static method
		self . m3() # Error because no argument self 
		cls . m3() # Error because no argument cls  
		print('child  class  static  method' ,  parent.a)
		print(child.a) # How  to  print  static  variable  'a'  in  another  way
		print(child.b) # How  to  print  static  variable  'b'
	def __del__(self):
		super().__del__() # How  to  call  destructor  of  parent  class
		print('child  destructor' , self.y)
#end of the class
c = child()
c.m1() # How  to  call  m2()  method  of  child  class
child.m2()  # How  to  call  m3()  method  of  child  class
child.m3()  # How  to  call  m1()  method  of  child  class


'''
Parent constructor
Child constructor

Parent class instance method : 30
Child class instance method 40

Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Parent class "class" method : 10
Child class "class" method
10
10
10
10
20
20

Parent class static method : 10
child class static method 10
10
20
parent destructor : 30
child destructor 40
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
		father.m1(self) # How  to  call  m1()  method  of  father  class  without  creating  another  object
		super(child, self).m1() # How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		mother.m1(self) # How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self) # How  to  call  m1()  method  of  uncle  class  without  creating  an  object
		super(uncle , self) . m1() # ERROR because parent(uncle) is object which has no m1 method.
# End of the class
print(child . __mro__)  
c = child()
c.m1() # How  to  call  m1()  method  of  child  class
print('Bye')


'''
MRO: (child, father, mother, uncle, object)
(<class '__main__.child'>, <class '__main__.father'>, <class '__main__.mother'>, <class '__main__.uncle'>, <class 'object'>)
m1 method of child class
m1 method of Father class
m1 method of Father class
m1 method of Mother class
m1 method of Uncle class
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
		super() . m1() # ERROR because parent(D) is object which has no m1 method.
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
[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>,
 <class '__main__.D'>, <class 'object'>]
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
'''



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
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>,<class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>,<class 'object'>]
class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye
'''

#---------------------------------------------

#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1, mod2 # How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = mod1.c1()
obj1.m1()
print()
print()
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = mod2.c1()
obj2.m1() 
print(p1 . mod1 . x)  # Error because p1 is not imported
print(x) # Error because x is not imported 




#  Save  in  any  file  of  cwd
from p1.mod1 import * # How  to  import  members  of  mod1  in  package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = c1()
obj1.m1()
print()
print()
from p1.mod2 import * # How  to  import   members  of  mod2   in  package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = c1()
obj2.m1() 
print(p1 . mod1 . x)  # Error because p1 and mod1 are not imported
print(mod1 . x) # Error because mod1 is not imported  
from  p1   import  mod1 . * # Error because we can't use . in import clause


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
x of mod2
f1() of mod2
m1() of c1 in mod2
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
x of mod1
f1() of mod1
m1() of c1 in mod1
'''




''' 
(Home work)
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
30
Function of same module
Method of class c1 in same module
'''



'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from p1 import mod1, mod2 # How  to  import   members  of  mod1   in  package  p1 .How  to  import   members  of  mod2   in  package  p1  
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
obj1 = mod1.c1() 
obj1.m1() 
print()
print()
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  package  p1
# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
obj2 = mod2.c1()   
obj2.m1() 
'''
x of mod1
f1() of mod1
m1() of c1 in mod1

x of mod2
f1() of mod2
m1() of c1 in mod2
'''