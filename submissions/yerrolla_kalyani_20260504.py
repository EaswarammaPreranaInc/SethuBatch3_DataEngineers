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
		obj_c=C()
		obj_c.m1()# How  to  call  method  m1()  of  class  C  without  creating  another  object
		super().m1# How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object
		super(C,self).m1# How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object
		super(B,self)# How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object
		super(A , self) . m1() #error 
		super(C) . m1()   #error single argument with for instance mmethod is error 
		super(D , D) . m1()  #error 
# End  of  the  class
obj_d=D()#How  to  call  method  m1()  of  class  D

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
c . color()#Mother  Color
c . height()#Father  Height
c . m1()#error there is no such method in class c and not inherited by parents

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
c . m1()#error no such methods in c and  they are not inherited by parent so error 


# Identify  Error
class  c1(c1):#Error the c1 cannot be a parent of itself
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
a . m1()   #   Parent  Method   <nxt line>  Child  Method

# Identify  Error
class   c1(c2): #error c2 class is depending on c1 class and c1 class is depending on c2 so it is a cyclic process so error
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
a . m1()#error naming conflict as there is same class c2 so last class is recogniged a but it is a cyclic process so error c2-->c1-->c2-->c1-->c2 

# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		p=super(child,self)#How  to  call  parent  class  constructor
		print('child   constructor')
	def   _del_(self):
		del p#How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()#child   constructor     <nxt> parent  constructor  <nxt>    parent  destructor   <nxt>   child   destructor
print('Bye')#Bye


# Find  outputs  (Home  work)
class   parent:
	def   _init_(self):
		print('parent  constructor')
	def   _del_(self):
		print('parent  destructor')
class  child(parent):
	def   _init_(self):
		print('child   constructor')#child   constructor
	def   _del_(self):
		print('child  destructor')#child  destructor
# End of the class
c = child()
print('Bye')#Bye

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
print('Bye')#Bye

# Parent  and  Child  constructor  demo  program  (Home  work)
class  parent:
	def   _init_(self , a1 , b1):
		self . a = a1
		self . b = b1
	def disp(self):
		print(self . a , self . b , sep = '\t' , end = '\t')
class   child(parent):
	def _init_(self , a2 = 0  , b2 = 0 , c2 = 0  , d2 = 0):
		super().__init__(50,60)#How  to  call  parent  class  constructor  with  a2 , b2
		self . c = c2
		self . d = d2
	def  disp(self):
		super().disp()#How  to  call  parent  class  disp()  method
		print(self . c , self . d , sep = '\t')
#end of the class
x = child(10 , 20 , 30 , 40)
y = child()
print(x)#type and address x
x . disp()# 50  60  30  40 <tab>
print(y)#type and address y
y . disp()#50   60  0   0 <tab>


# obj x---> c=30,d=40

# obj x---> c=0,d=0



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
		print(parent.x)# How  to  print  static  variable  'x'
		print(super().x)# How  to  print  static  variable  'x'   in  another  way
		print(super(child,self))# How  to  print  static  variable  'x'   in  one  more  way
		print(parent.x)# How  to  print  variable  'x'  of  object  'c'
		print(y)# How  to  print  variable  'y'  of  object  'c'
# End  of  the  class
c=child()
c.disp()#How  to  call  disp()  method  of   child  class

# Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x)#30   
		super() . _init_()
	def  disp(self):
		print(self . x)    #20
		print(super() . x) #20
# End of the class
c = child()
c . disp()#20 <nxt> 20


# '''
# static   variable  --->  x=10

# Object  'c'  --->  x=20
# '''






# Find outputs
class    parent:
	a=10#How  to  add  static  variable  'a'  to  parent  class  with  value  10
	def     _init_(self):
		print('Parent  constructor')
		parent.x=30#How  to  add  instance  variable  'x'  with  value  30
	def   m1(self):
		print('Parent  class  instance  method  :  ' ,  self.x)
	@classmethod
	def    m2(cls):
		print('Parent  class  "class"  method  :  ' ,   cls.x)
		print('Parent  class  "class"  method  :  ' ,  parent.a)
		print(self . a)  #error there is no self only cls so error 
	@staticmethod
	def   m3():
		print('Parent  class  static  method  :  ' ,  parent.a)
	def   _del_(self):
		print('parent  destructor  :  ' , self.x)
class  child(parent):
	b=20#How  to  add  static  variable  'b'  with  value  20
	def   _init_(self):
		super().__init__()#How  to  call  parent  class  constructor
		print('Child  constructor')
		self.y=40#How  to  add  instance  variable  'y'  with  value  40
	def   m1(self):
		super().m1()#How  to  call  m1()  method  of  parent  class
		print('Child  class  instance  method' , self.y)
	@classmethod
	def   m2(cls):
		super().m2()#How  to  call  m2()  method  of  parent  class
		parent().m2#How  to  call  m2()  method  of  parent  class  in  another  way  without  creating  another  object
		cls . m2()  
		self . m2() #error  maximum recursion depth exceeded
		print('Child  class  "class"  method')
		print(parent.a)
		print(super().a)
		print(cls.a)
		print(child.a)
		print(child.b)
		print(cls.b)
	@staticmethod
	def   m3():
		parent.m3()# How  to  call  m3()  method  of  parent  class
		super(child).m3()# How  to  call  m3()  method  of  parent  class  in   another  way
		child. m3()  
		self . m3() #error no self argument
		cls . m3() #error no cls argument
		print('child  class  static  method' ,  super().a)#child.a 
		print(parent.a)
		print(child.b)
	def _del_(self):
		super().__del__()# How  to  call  destructor  of  parent  class
		print('child  destructor' ,  self.y)
#end of the class
child.m2()# How  to  call  m2()  method  of  child  class
child.m3()# How  to  call  m3()  method  of  child  class
c=child()
c.m1()# How  to  call  m1()  method  of  child  class


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
		super().m1# How  to  call  m1()  method  of  father  class  without  creating  another  object
		father.m1(self)# How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object
		mother.m1(self)# How  to  call  m1()  method  of  mother  class   without  creating  an  object
		uncle.m1(self)# How  to  call  m1()  method  of  uncle  class  without  creating  an  object#####
		super(uncle , self) . m1() 
# End of the class
print(child . _mro_)  #(child,father,mother,uncle,object)
c=child()
c.m1()# How  to  call  m1()  method  of  child  class
print('Bye')#Bye


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
                super() . m1() # error where obj class has no m1() method in obj class  
                print('class P method') 
# End  of  the  class
print(P . mro())# [P,X,Y,C,object] 
obj = P()
obj . m1()
print('Bye')


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
                super() . _init_() #  class D constructor     <nxt>  class B constructor
                print('class A constructor') #class A constructor
# End  of  the  class
print(A . mro())  #[A,B,C,OBJECT]
obj = A()
print('Bye')#Bye


#  Save  in  any  file  of  cwd  (Homework)
from p1 import mod1,mod2 #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1.x)#How  to  print  object  'x'  of   mod1  in  package  p1
print(mod1.f1())#How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2.x)#How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1()#How  to  call  function  f1()  of   mod2  in  package  p1
b=mod2.c1()
b.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  #error module is imported but not the package is imported
print(x)#error there is no such x in current program and it is not imported from mod1 and mod2 (i.e., x is a member of the mod1 ,mod2)


#  Save  in  any  file  of  cwd
from p1.mod1 import * 	#How  to  import  members  of  mod1  in  package  p1
print(x)#How  to  print  object  'x'  of   mod1  in  package  p1
f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import * 	#How  to  import   members  of  mod2   in  package  p1
print(x)#How  to  print  object  'x'  of   mod2  in  package  p1
f1()#How  to  call  function  f1()  of   mod2  in  package  p1
a=c1()#
a.m1()#How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
print(p1 . mod1 . x)  # error the members are imported not the package and module so error .
print(mod1 . x)  #error module is not imported  members are imported .
from  p1   import  mod1 . *#error import clause not supporte the '.' ,this causing error  mod1 . * 


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
How  to  use  members  of  both  the  modules
'''

from p1.mod1 import *	# How  to  import   members  of  mod1   in  package  p1 
from p1.mod2 import *	# How  to  import   members  of  mod2   in  package  p1  
print(mod1.x)# How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()# How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
# print()
# print()
print(mod2.x)# How  to  print  object  'x'  of   mod2  in  package  p1
mod2.f1()# How  to  call  function  f1()  of   mod2  in  package  p1
a=mod2.c1()
a.m1()# How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1