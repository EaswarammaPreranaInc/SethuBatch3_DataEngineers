 Multilevel inheritance demo program

class A:
    def m1(self):
        print("class A method")

class B(A):
    def m1(self):
        print("class B method")

class C(B):
    def m1(self):
        print("class C method")

class D(C):
    def m1(self):
        print("class D method")

        print("\nCalling C.m1():")
        C.m1(self)   # direct call

        print("\nCalling C.m1() using super():")
        super().m1()   # goes to C

        print("\nCalling B.m1():")
        B.m1(self)

        print("\nCalling A.m1():")
        A.m1(self)


# Driver code
d = D()
d.m1()





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
c  =  child()	#Creates an object c of class child
c . qualification()	#Child Qualification
c . color()		#Mother Color
c . height()		#Father Height
c . m1()		#error



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
c = child()	#Creates an object of class child
c . m1()	#Child Method




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
c = child()	#Creates object c of class child
c . m1()	#Father Method



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
c = child()	#Object c of class child is created
c . m1()	#Father Method




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
c = child()	#Object c of class child is created
c . m1()	#Mother Method



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
c = child()	#Creates object c of class child
c . m1()	#Uncle Method




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
c = child()	#Object c is created
c . m1()	#error child object has no attribute 'm1'




# Identify  Error
class  c1(c1):
	     pass    #NameError: name 'c1' is not defined




# Find  outputs
class   c1:
	def  m1(self):
			print('Parent  Method')
class  c1(c1):
	def  m1(self):
		super() . m1()
		print('Child  Method')
a = c1()	#Defines class c1 with method
a . m1()	#Parent  Method <next> Child  Method




# Identify  Error
class   c1(c2): 
	pass
class  c2(c1):
	pass	#error name c2 is not defined




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
a = c2()	#Defines class c2
a . m1()	#error recursion error




# Parent  and  child  class  constructors (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	def   __init__(self):
		How  to  call  parent  class  constructor
		print('child   constructor')
	def   __del__(self):
		How  to  call  parent  class  destructor
		print('child   destructor')
# End of the class
c = child()	#parent constructor <next> child constructor 
print('Bye')    #Bye 





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
c = child()	#child constructor
print('Bye')	#Bye

#child destructor




class parent:
    def __init__(self):
        print('parent constructor')

    def __del__(self):
        print('parent destructor')


class child(parent):
    def __init__(self):
        print('child constructor')

    def __del__(self):
        print('child destructor')


c = child()	#child constructor
print('Bye')	#Bye

#child destructor





# Find  outputs  (Home  work)
class   parent:
	def   __init__(self):
		print('parent  constructor')
	def   __del__(self):
		print('parent  destructor')
class  child(parent):
	pass
# End of the class
c = child()	#parent constructor
print('Bye')	#Bye

#parent destructor






# Parent and Child constructor demo program

class parent:
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    def disp(self):
        print(self.a, self.b, sep='\t', end='\t')


class child(parent):
    def __init__(self, a2=0, b2=0, c2=0, d2=0):
        super().__init__(a2, b2)   # call parent constructor with a2, b2
        self.c = c2
        self.d = d2

    def disp(self):
        super().disp()            # call parent disp() method
        print(self.c, self.d, sep='\t')


# end of the class

x = child(10, 20, 30, 40)
y = child()

print('Object x')
x.disp()

print('\nObject y')
y.disp()





# Parent and Child class demo program

class parent:
    x = 100   # static (class) variable

    def __init__(self):
        self.x = 10   # instance variable


class child(parent):
    def __init__(self):
        super().__init__()   # call parent constructor
        self.y = 20          # instance variable

    def disp(self):
        # 1. Print static variable x (using class name)
        print(parent.x)

        # 2. Print static variable x (using super class)
        print(super().x)

        # 3. Print static variable x (using instance but via class)
        print(self.__class__.x)

        # 4. Print instance variable x of object c
        print(self.x)

        # 5. Print instance variable y of object c
        print(self.y)


# End of the class

c = child()

# Call disp() method
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
c . disp()

#outputs:
30
20
10




class parent:
    # static variable
    a = 10

    def __init__(self):
        print('Parent constructor')
        # instance variable
        self.x = 30

    def m1(self):
        print('Parent class instance method:', self.x)

    @classmethod
    def m2(cls):
        print('Parent class class method:', cls.a)
        print('Parent class class method (another way):', parent.a)

    @staticmethod
    def m3():
        print('Parent class static method:', parent.a)

    def __del__(self):
        print('parent destructor:', self.x)


class child(parent):
    # static variable
    b = 20

    def __init__(self):
        super().__init__()   # call parent constructor
        print('Child constructor')
        self.y = 40          # instance variable

    def m1(self):
        super().m1()         # call parent m1()
        print('Child class instance method:', self.y)

    @classmethod
    def m2(cls):
        # calling parent class method
        super().m2()

        print('Child class class method')

        print(parent.a)          # way 1
        print(cls.a)             # way 2
        print(child.a)           # way 3
        print(super(child, cls).a)  # way 4

        print(cls.b)             # static variable b
        print(child.b)           # another way

    @staticmethod
    def m3():
        parent.m3()   # call parent static method
        print('Child class static method:', parent.a)
        print(child.b)

    def __del__(self):
        parent.__del__(self)   # call parent destructor
        print('child destructor:', self.y)


# =========================
# Object creation and calls
# =========================

print("\n--- m2 call ---")
child.m2()

print("\n--- m3 call ---")
child.m3()

print("\n--- m1 call ---")
c = child()
c.m1()

print("\nBye")






class father:
    def m1(self):
        print('m1 method of Father class')

class mother:
    def m1(self):
        print('m1 method of Mother class')

class uncle:
    def m1(self):
        print('m1 method of Uncle class')

class child(father, mother, uncle):
    def m1(self):
        print('m1 method of child class')

        # Call father class m1 without creating object
        father.m1(self)

        # Another way
        super(child, self).m1()

        # Call mother class m1
        mother.m1(self)

        # Call uncle class m1
        uncle.m1(self)

        # super with explicit class
        super(uncle, self).m1()


# MRO print
print(child.__mro__)

# Object creation and method call
c = child()
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
print(P . mro()) 	#[P, X, A, Y, B, C, D, object]  
obj = P()
obj . m1()
print('Bye')

#outputs:
class D method
class C method
class B method
class Y method
class A method
class X method
class P method
Bye




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
print(A . mro()) 	#[A, B, C, D, E, F, object] 
obj = A()
print('Bye')


#outputs:
[A, B, C, D, E, F, object]

class F constructor
class E constructor
class D constructor
class C constructor
class B constructor
class A constructor
Bye
