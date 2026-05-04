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
		How  to  call  method  m1()  of  class  C  without  creating  another  object  			#c.m1(self)
		How  to  call  method  m1()  of  class  C  in  another  way  without  creating  another  object #super().m1()
		How  to  call  method  m1()  of  class  B  in  another  way  without  creating  another  object #super(c,self).m1()
		How  to  call  method  m1()  of  class  A  in  another  way  without  creating  another  object #super(b,self).m1()
		super(A , self) . m1() #error
		super(C) . m1()   #error super requires 0 or 2 args
		super(D , D) . m1()  #class c method
# End  of  the  class
How  to  call  method  m1()  of  class  D
o=D()
o.m1()


# Find  outputs
class  parent:
	x = 10
	def  _init_(self):
		self . x = 20
class   child(parent):
	def  _init_(self):
		self . x = 30
		print(self . x)   #30
		super() . _init_() #
	def  disp(self):
		print(self . x)    #20
		print(super() . x) #10
# End of the class
c = child()
c . disp()


'''
static   variable  --->  x=10

Object  'c'  --->  x=20
'''




# Find outputs
class parent:
    # How to add static variable 'a' to parent class with value 10
    a = 10

    def __init__(self):
        print('Parent constructor')
        # How to add instance variable 'x' with value 30
        self.x = 30

    def m1(self):
        print('Parent class instance method : ', self.x)

    @classmethod
    def m2(cls):
        print('Parent class "class" method : ', cls.a)
        print('Parent class "class" method : ', parent.a)

    @staticmethod
    def m3():
        print('Parent class static method : ', parent.a)

    def __del__(self):
        print('parent destructor : ', self.x)

class child(parent):
    # How to add static variable 'b' with value 20
    b = 20

    def __init__(self):
        # How to call parent class constructor
        super().__init__()
        print('Child constructor')
        # How to add instance variable 'y' with value 40
        self.y = 40

    def m1(self):
        # How to call m1() method of parent class
        super().m1()
        print('Child class instance method', self.y)

    @classmethod
    def m2(cls):
        # How to call m2() method of parent class
        super().m2()
        # How to call m2() method of parent class in another way without creating another object
        parent.m2()

        print('Child class "class" method')
        print(cls.a)
        print(parent.a)
        print(child.a)
        print(super().a)
        print(cls.b)
        print(child.b)

    @staticmethod
    def m3():
        # How to call m3() method of parent class
        parent.m3()
        # How to call m3() method of parent class in another way
        super(child, child).m3()

        print('child class static method', parent.a)
        print(child.a)
        print(child.b)

    def __del__(self):
        # How to call destructor of parent class
        super().__del__()
        print('child destructor', self.y)


# end of the class

# How to call m2() method of child class
child.m2()

# How to call m3() method of child class
child.m3()

# How to call m1() method of child class
c = child()
c.m1()

#print(self.m1())


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
		How  to  call  m1()  method  of  father  class  without  creating  another  object 		 #super().m1()
		How  to  call  m1()  method  of  father  class  in  another  way  without  creating  an  object  #father.m1(self)
		How  to  call  m1()  method  of  mother  class   without  creating  an  object 			 #mother.m1(self)  
		How  to  call  m1()  method  of  uncle  class  without  creating  an  object			 #uncle.m1(self)  
		super(uncle , self) . m1() 
# End of the class
print(child . _mro_)  
How  to  call  m1()  method  of  child  class
c=child()
c.m1()
print('Bye')




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
print(P . mro())   #[P, X, A, Y, B, C, D, object]
obj = P()
obj . m1()
'''
class D method
class C method
class B method
class Y method
class A method
class X method
class P method'''
print('Bye')#Bye




#Find  outputs  (Home  work)
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
                print('class A constructor…

#  Save  in  any  file  of  cwd  (Homework)
How  to  import  mod1   and  mod2  of  package  p1  with  from  statement #from p1 import mod1, mod2
How  to  print  object  'x'  of   mod1  in  package  p1  		  #print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1		  #mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1	  #obj = mod1.c1()
									   obj.m1()
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1			 #print(mod2.x)
How  to  call  function  f1()  of   mod2  in  package  p1		 #mod2.f1()
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1	 #obj = mod2.c1()
									  obj.m1()
print(p1 . mod1 . x)  #error,works only if import p1
print(x) #error  x not defined directly






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
How  to  import   members  of  mod1   in  package  p1 #from p1 import mod1
How  to  import   members  of  mod2   in  package  p1 #from p1 import mod2
How  to  print  object  'x'  of   mod1  in  package  p1 #print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1 #mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1 #obj1 = mod1.c1()
									obj1.m1()
print()
print()
How  to  print  object  'x'  of   mod2  in  package  p1#print(mod2.x)
How  to  call  function  f1()  of   mod2  in  package  p1 #mod2.f1()
How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1#obj2 = mod2.c1()
								       obj2.m1()


