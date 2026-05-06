# Multilevel inheritance demo program
class A:
    def m1(self):
        print('class A method')
class B(A):
    def m1(self):
        print('class B method')
class C(B):
    def m1(self):
        print('class C method')
class D(C):
    def m1(self):
        print('class D method')
        super(D, self).m1()     # How to call method m1() of class C without creating another object
        C.m1(self)              # How to call method m1() of class C in another way without creating another object
        super(C, self).m1()     # How to call method m1() of class B in another way without creating another object
        super(B, self).m1()     # How to call method m1() of class A in another way without creating another object
# End of the class
obj = D()                      # How to call method m1() of class D
obj.m1()




# Find outputs (Home work)
class father:
    def height(self):
        print('Father Height')   # c.height()
class mother:
    def color(self):
        print('Mother Color')    # c.color()
class child(mother, father):
    def qualification(self):
        print('Child Qualification')  # c.qualification()
# End of the class
c = child()
c.qualification()   # Child Qualification
c.color()           # Mother Color
c.height()          # Father Height
c.m1()            # AttributeError: 'child' object has no attribute 'm1'




# Find outputs
class uncle:
    def m1(self):
        print('Uncle Method')   # not executed
class mother:
    def m1(self):
        print('Mother Method')  # not executed
class father:
    def m1(self):
        print('Father Method')  # not executed
class child(father, mother, uncle):
    def m1(self):
        print('Child Method')   # c.m1()
# End of the class
c = child()
c.m1()   # Child Method




# Find outputs
class uncle:
    def m1(self):
        print('Uncle Method')   # not executed
class mother:
    def m1(self):
        print('Mother Method')  # not executed
class father:
    def m1(self):
        print('Father Method')  # executed
class child(father, mother, uncle):
    pass
# End of the class
c = child()
c.m1()   # Father Method




# Find outputs
class uncle:
    def m1(self):
        print('Uncle Method')   # not executed
class mother:
    def m1(self):
        print('Mother Method')  # executed
class father:
    pass
class child(father, mother, uncle):
    pass
# End of the class
c = child()
c.m1()   # Mother Method




# Find outputs
class uncle:
    def m1(self):
        print('Uncle Method')   # executed
class mother:
    pass
class father:
    pass
class child(father, mother, uncle):
    pass
# End of the class
c = child()
c.m1()   # Uncle Method




# Find outputs
class uncle:
    pass
class mother:
    pass
class father:
    pass
class child(father, mother, uncle):
    pass
# End of the class
c = child()
# c.m1()   # AttributeError: 'child' object has no attribute 'm1'




# Identify Error
class c1(c1):   # Error due to name 'c1' is not defined
    pass



# Find outputs
class c1:
    def m1(self):
        print('Parent Method')   # executed first
class c1(c1):
    def m1(self):
        super().m1()             # calls Parent Method
        print('Child Method')    # executed next
a = c1()
a.m1()   # Parent Method
         # Child Method




# Identify Error
class c1(c2):   # Error due to name 'c2' is not defined
    pass
class c2(c1):
    pass




# Find outputs
class c2:
    def m1(self):
        print('Parent Method')
class c1(c2):
    def m1(self):
        super().m1()
        print('Child Method')
class c2(c1):   # Error due to it Cannot create a consistent method resolution order (MRO)
    def m1(self):
        super().m1()
        print('Grand Child Method')
a = c2()
a.m1()




# Parent and child class constructors (Home work)
class parent:
    def __init__(self):
        print('parent constructor')     # executed via super()
    def __del__(self):
        print('parent destructor')      # executed via super()
class child(parent):
    def __init__(self):
        super().__init__()              # How to call parent class constructor
        print('child constructor')
    def __del__(self):
        super().__del__()               # How to call parent class destructor
        print('child destructor')
# End of the class
c = child()
print('Bye')




# Find outputs (Home work)
class parent:
    def __init__(self):
        print('parent constructor')     # not executed
    def __del__(self):
        print('parent destructor')      # not executed
class child(parent):
    def __init__(self):
        print('child constructor')      # executed
    def __del__(self):
        print('child destructor')       # executed
# End of the class
c = child()      # child constructor
print('Bye')     # Bye




# Find outputs (Home work)
class parent:
    def __init__(self):
        print('parent constructor')   # executed
    def __del__(self):
        print('parent destructor')    # executed at end
class child(parent):
    pass
# End of the class
c = child()      # parent constructor
print('Bye')     # Bye




# Parent and Child constructor demo program (Home work)
class parent:
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1
    def disp(self):
        print(self.a, self.b, sep='\t', end='\t')
class child(parent):
    def __init__(self, a2=0, b2=0, c2=0, d2=0):
        super().__init__(a2, b2)     # How to call parent class constructor with a2, b2
        self.c = c2
        self.d = d2
    def disp(self):
        super().disp()              # How to call parent class disp() method
        print(self.c, self.d, sep='\t')
# end of the class
x = child(10, 20, 30, 40)
y = child()
print('Object x')
x.disp()
print('\nObject y')
y.disp()




# Find outputs (Home work)
class parent:
    x = 100   # static (class) variable
    def __init__(self):
        self.x = 10   # instance variable
class child(parent):
    def __init__(self):
        super().__init__()
        self.y = 20
    def disp(self):
        print(parent.x)          # How to print static variable 'x'
        print(self.__class__.x)   # How to print static variable 'x' in another way
        print(child.x)           # How to print static variable 'x' in one more way
        print(self.x)            # How to print variable 'x' of object 'c'
        print(self.y)            # How to print variable 'y' of object 'c'
# End of the class
c = child()
c.disp()   # How to call disp() method of child class




# Find outputs

class parent:
    x = 10   # static (class) variable

    def __init__(self):
        self.x = 20   # instance variable

class child(parent):
    def __init__(self):
        self.x = 30
        print(self.x)        # 30
        super().__init__()

    def disp(self):
        print(self.x)        # 20
        # print(super().x)   # Error due to invalid usage
# End of the class
c = child()   # 30
c.disp()





# Find outputs

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
        print('parent destructor :', self.x)


class child(parent):
    b = 20   # static variable

    def __init__(self):
        super().__init__()     # call parent constructor
        print('Child constructor')
        self.y = 40            # instance variable

    def m1(self):
        super().m1()           # call parent m1()
        print('Child class instance method', self.y)

    @classmethod
    def m2(cls):
        super().m2()           # call parent m2()
        parent.m2()            # another way without object

        print('Child class "class" method')
        print(parent.a)        # static variable a
        print(cls.a)
        print(child.a)
        print(super(child, cls).a)
        print(cls.b)           # static variable b
        print(child.b)

    @staticmethod
    def m3():
        parent.m3()            # call parent static method
        print('child class static method', parent.a)
        print(child.a)
        print(child.b)

    def __del__(self):
        super().__del__()      # call parent destructor
        print('child destructor', self.y)


# end of the class

# Calling methods
child.m2()
child.m3()
c = child()
c.m1()



# Find outputs

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

        father.m1(self)                 # father m1() without another object
        super(father, self).m1()        # another way to call father m1()

        mother.m1(self)                 # mother m1() without object
        uncle.m1(self)                  # uncle m1() without object

        super(uncle, self).m1()         # correct super usage (follows MRO)

# End of the class

print(child.__mro__)   # MRO order

c = child()
c.m1()                 # child m1()

print('Bye')





# Find outputs (Home work)

class A:
    def m1(self):
        super().m1()
        print('class A method')

class B:
    def m1(self):
        super().m1()
        print('class B method')

class C:
    def m1(self):
        super().m1()
        print('class C method')

class D:
    def m1(self):
        super().m1()
        print('class D method')

class X(A, B):
    def m1(self):
        super().m1()
        print('class X method')

class Y(B, C, D):
    def m1(self):
        super().m1()
        print('class Y method')

class P(X, Y, C):
    def m1(self):
        super().m1()
        print('class P method')

# End of the class

print(P.mro())

obj = P()
obj.m1()
print('Bye')




# Find outputs (Home work)

class D:
    def __init__(self):
        super().__init__()
        print('class D constructor')   # class D constructor

class E:
    def __init__(self):
        super().__init__()
        print('class E constructor')   # class E constructor

class F:
    def __init__(self):
        super().__init__()
        print('class F constructor')   # class F constructor

class B(D, E):
    def __init__(self):
        super().__init__()
        print('class B constructor')   # class B constructor

class C(D, E, F):
    def __init__(self):
        super().__init__()
        print('class C constructor')   # class C constructor

class A(B, C):
    def __init__(self):
        super().__init__()
        print('class A constructor')   # class A constructor

# End of the class

print(A.mro())   # MRO list printed first

obj = A()        # triggers constructor chain
print('Bye')     # Bye




# Save in any file of cwd (Homework)

# How to import mod1 and mod2 of package p1 with from statement
from p1 import mod1, mod2

# How to print object 'x' of mod1 in package p1
print(mod1.x)          # output: object x of mod1

# How to call function f1() of mod1 in package p1
mod1.f1()              # output: mod1 f1() output

# How to call method m1() of class c1 in mod1 of package p1
obj1 = mod1.c1()
obj1.m1()              # output: mod1 c1 m1()

print()
print()

# How to print object 'x' of mod2 in package p1
print(mod2.x)          # output: object x of mod2

# How to call function f1() of mod2 in package p1
mod2.f1()              # output: mod2 f1() output

# How to call method m1() of class c1 in mod2 of package p1
obj2 = mod2.c1()
obj2.m1()              # output: mod2 c1 m1()
# print(p1.mod1.x)  only works if package imported as p1
print(mod1.x)          # correct usage
print(mod1.x)          # same output as above




# Save in any file of cwd
# How to import members of mod1 in package p1
from p1.mod1 import *
# How to print object 'x' of mod1 in package p1
print(x)              # mod1.x value
# How to call function f1() of mod1 in package p1
f1()                  # mod1.f1() output
# How to call method m1() of class c1 in mod1 of package p1
obj = c1()
obj.m1()              # mod1.c1.m1()
print()
print()
# How to import members of mod2 in package p1
from p1.mod2 import *
# How to print object 'x' of mod2 in package p1
print(x)              # mod2.x value
# How to call function f1() of mod2 in package p1
f1()                  # mod2.f1() output
# How to call method m1() of class c1 in mod2 of package p1
obj = c1()
obj.m1()              # mod2.c1.m1()
print(p1.mod1.x)      # incorrect unless p1 imported as package
print(mod1.x)         # works only if "from p1 import mod1" used




''' (Home work)
Save the following code in any file of cwd
Find outputs
'''
x = 30
def f1():
    print('Function of same module')   # f1()
class c1:
    def m1(self):
        print('Method of class c1 in same module')   # a.m1()
from p1.mod1 import *
from p1.mod2 import *
print(x)      # 30
f1()          # Function of same module
a = c1()
a.m1()        # Method of class c1 in same module




''' (Home work)
Save the following code in any file of cwd
Find outputs
'''
x = 30
def f1():
    print('Function of same module')   # f1()
class c1:
    def m1(self):
        print('Method of class c1 in same module')   # a.m1()
from p1.mod2 import *
from p1.mod1 import *
print(x)      # 30
f1()          # Function of same module
a = c1()
a.m1()        # Method of class c1 in same module





''' (Home work)
Save the following code in any file of cwd
Find outputs
'''
from p1.mod1 import *
from p1.mod2 import *
x = 30
def f1():
    print('Function of same module')   # f1()
class c1:
    def m1(self):
        print('Method of class c1 in same module')   # a.m1()
print(x)      # 30
f1()          # Function of same module
a = c1()
a.m1()        # Method of class c1 in same module





''' (Home work)
Save the following code in any file of cwd
How to use members of both the modules
'''
# How to import members of mod1 in package p1
from p1.mod1 import *
# How to import members of mod2 in package p1
from p1.mod2 import *
# How to print object 'x' of mod1 in package p1
print(x)              # mod1.x
# How to call function f1() of mod1 in package p1
f1()                  # mod1.f1()
# How to call method m1() of class c1 in mod1 of package p1
obj1 = c1()
obj1.m1()            # mod1.c1.m1()
print()
print()
# How to print object 'x' of mod2 in package p1
print(x)              # mod2.x (last imported module overrides name if same)
# How to call function f1() of mod2 in package p1
f1()                  # mod2.f1()
# How to call method m1() of class c1 in mod2 of package p1
obj2 = c1()
obj2.m1()            # mod2.c1.m1()