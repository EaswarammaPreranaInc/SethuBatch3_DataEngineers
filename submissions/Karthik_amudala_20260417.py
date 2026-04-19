# Find outputs
class c1_A:
    @staticmethod
    def m1():
        print('static method')
# End of the class
c1_A.m1()   # Output: static method
a = c1_A()
a.m1()      # Output: static method
# c1_A.m1(25) # Output: TypeError: m1() takes 0 positional arguments but 1 was given


# Find outputs
class c1_B:
    @staticmethod
    def m1(self):
        print(self)
# End of the class
c1_B.m1(25) # Output: 25
a = c1_B()
a.m1(35)    # Output: 35
# a.m1()    # Output: TypeError: m1() missing 1 required positional argument: 'self'


# Find outputs
class c1_C:
    def m1(self):
        print(self)
# End of the class
c1_C.m1(25) # How is method m1() treated: As an instance method (Unbound, but we pass 25 explicitly as 'self'). Output: 25
a = c1_C()
a.m1()      # How is method m1() treated: As an instance method (Bound, 'a' is passed as 'self'). Output: <__main__.c1_C object at ...>
# a.m1(35)  # What about here: TypeError: m1() takes 1 positional argument but 2 were given ('a' and 35)


# Find outputs
class c1_D:
    def m1():
        print()
# End of the class
c1_D.m1()   # Output: (Prints an empty line. Acts like a static method when called directly on the class in Python 3).
a = c1_D()
# a.m1()    # Output: TypeError: m1() takes 0 positional arguments but 1 was given (the instance 'a' is passed automatically)


# Find outputs
class c1_E:
    @staticmethod
    def m1(self):
        print('static method')
        print(self)
    
    # In Python, the second definition overwrites the first. 
    # Therefore, m1 becomes a standard instance method.
    def m1(self):
        print('static / instance method')
        print(self)
# End of the class
c1_E.m1(25) # Output: static / instance method \n 25
a = c1_E()
a.m1()      # Output: static / instance method \n <__main__.c1_E object at ...>


# How to access static variable in different ways ?
class c1_F:
    x = 25
    def __init__(self):
        print(c1_F.x)   # How to print static variable 'x'
        print(self.x)   # How to print static variable 'x' in another way
        # print(x)      # (Would raise NameError unless x is global)
    
    def m1(self):
        print(c1_F.x)   # How to print static variable 'x'
        print(self.x)   # How to print static variable 'x' in another way
        # print(cls.x)  # (Would raise NameError, cls is not defined here)
    
    @classmethod
    def m2(cls):
        print(cls.x)    # How to print static variable 'x'
        print(c1_F.x)   # How to print static variable 'x' in another way
        # print(self.x) # (Would raise NameError, self is not defined here)
    
    @staticmethod
    def m3():
        print(c1_F.x)   # How to print static variable 'x'
        # print(cls.x)  # (Would raise NameError)
        # print(self.x) # (Would raise NameError)
# End of the class

print(c1_F.x)           # How to print static variable 'x' outside
# print(x)              # (Would raise NameError)
# print(self.x)         # (Would raise NameError outside class context)
# print(cls.x)          # (Would raise NameError outside class context)

obj_f = c1_F()
obj_f.m1()              # How to call method m1()
c1_F.m2()               # How to call method m2()
c1_F.m3()               # How to call method m3()


# How to add static variable to the class at different locations of the program ?
class c1_G:
    a = 10              # How to add static variable 'a' with value 10
    def __init__(self):
        c1_G.b = 20     # How to add static variable 'b' with value 20
        self.c = 30     # How to add instance variable 'c' with value 30
        c1_G.k = 25     # Using ClassName for static variable definition
        
    def m1(self):
        c1_G.d = 40     # How to add static variable 'd' with value 40
        self.e = 50     # How to add instance variable 'e' with value 50
        
    @classmethod
    def m2(cls):
        c1_G.f = 60     # How to add static variable 'f' with value 60
        cls.g = 70      # How to add static variable 'g' with value 70 in another way
        # self.k = 25   # 'self' is not defined in a class method
        
    @staticmethod
    def m3():
        c1_G.h = 80     # How to add static variable 'h' with value 80
        # self.k = 25   # 'self' is not defined in a static method
        c1_G.k = 35     # cls is also not defined, must use c1_G

# End of the class
print('Outside the class')
print(c1_G.__dict__)
print("\n")

x = c1_G()
print('Constructor')
print(c1_G.__dict__)
print("\n")

x.m1()                  # How to call m1() method
print('Instance method m1')
print(c1_G.__dict__)
print("\n")

c1_G.m2()               # How to call m2() method
print('class method m2')
print(c1_G.__dict__)
print("\n")

c1_G.m3()               # How to call m3() method
print('static method m3')
print(c1_G.__dict__)
print("\n")

c1_G.i = 90             # How to add static variable 'i' with value 90
x.j = 100               # How to add instance variable 'j' with value 100

print('Outside the class (Final)')
print(c1_G.__dict__)
print("\n")

print("Object 'x' ")
print(x.__dict__)


# Find outputs (Home work)
class c1_H:
    a, b, c = range(1, 4)
# End of the class
print(c1_H.a)           # How to print variable 'a' (Output: 1)
print(c1_H.b)           # How to print variable 'b' (Output: 2)
print(c1_H.c)           # How to print variable 'c' (Output: 3)
print(c1_H.__dict__)


# Tricky program
class Test:
    @classmethod
    def get1(cls):
        # Input 1: 10
        cls.x = int(input('Enter any number : '))
        
    def get2(self):
        # Inputs 2 & 3: 20, 30 for 'a' | 40, 50 for 'b' | 60, 70 for 'c'
        self.y = int(input('Enter any number : '))
        self.z = int(input('Enter any number : '))
        
    def compute(self):
        Test.x += 1
        self.y += 1
        self.z += 1
        # self.x creates an instance variable shadows the static variable for this object
        self.x = Test.x + 1 
        
    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')
# End of the class

''' 
(Uncomment inputs below to run manually)
Test.get1()
a = Test()
b = Test()
c = Test()

a.get2()
b.get2()
c.get2()

a.compute()
b.compute()
c.compute()

a.disp()
b.disp()
c.disp()
'''
'''
Outputs for given inputs (10, 20, 30, 40, 50, 60, 70):
13      21      31      12
13      41      51      13
13      61      71      14
'''


# Add two Vector objects
class vector:
    @staticmethod
    def get1():
        # How to read number of elements into variable 'n'
        vector.n = int(input("Enter number of elements 'n': "))
        
    def get2(self):
        # How to read the list into the object
        self.a = []
        for i in range(vector.n):
            self.a.append(int(input(f"Enter element {i+1}: ")))
            
    def add(self, x, y):
        # How add the lists held by objects 'x' and 'y' and store the results in list held by owner object
        self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])

# How to call get1() method
# vector.get1()

a = vector()
# a.get2()        # How to read the list into 1st object

b = vector()
# b.get2()        # How to read the list into 2nd object 'b'

c = vector()
# c.add(a, b)     # How to add the lists held by objects 'a' and 'b' and store the results in list of 3rd object 'c'
# print(c.a)      # How to print the list of 3rd object


# Print only static variables
class c1_I:
    x = 1
    y = 2
    z = 3
# End of the class
print("Static Variables:")
for key, value in c1_I.__dict__.items():
    if not (key.startswith('__') and key.endswith('__')):
        print(f"{key} = {value}")


# Emp Class Validations
class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    # 3 Getter Methods
    def get_empno(self):
        return self.empno
        
    def get_ename(self):
        return self.ename
        
    def get_sal(self):
        return self.sal

    # 3 Setter Methods (with Validations)
    def set_empno(self, empno):
        if empno < 0:
            print("Invalid: Emp number cannot be -ve")
            self.empno = 0
        else:
            self.empno = empno
            
    def set_ename(self, ename):
        if ename == "":
            print("Invalid: Emp name cannot be an empty string")
            self.ename = "Unknown"
        else:
            self.ename = ename
            
    def set_sal(self, sal):
        if sal < 0:
            print("Invalid: Salary cannot be -ve")
            self.sal = 0
        else:
            self.sal = sal

# Outside the class
# a) Create Emp class object
emp1 = Emp(101, "Srinivas", 50000)

# b) Print empno, ename and sal
print(f"Emp No: {emp1.get_empno()}, Name: {emp1.get_ename()}, Salary: {emp1.get_sal()}")