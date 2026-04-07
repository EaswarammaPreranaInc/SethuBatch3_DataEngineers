import math

class Triangle:
    
    def get(self):
        # Read three sides
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    
    def test(self):
        # Triangle validity condition
        if (self.a + self.b > self.c and
            self.b + self.c > self.a and
            self.c + self.a > self.b):
            return True
        else:
            print("Not a triangle")
            exit()   # Stop execution
    
    def area(self):
        s = (self.a + self.b + self.c) / 2   # semi-perimeter
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area
    
    def peri(self):
        return self.a + self.b + self.c


# Creating object
t = Triangle()

# Reading inputs
t.get()

# Validating triangle
t.test()

# Printing results
print("Area :", t.area())
print("Perimeter :", t.peri())



class c1:
    def m1(self):
        x = 10              # local x = 10
        self.x = 20         # instance x = 20
        print(x)            # 10
        print(self.x)       # 20
        x += 5              # x = 15 (local, will be lost)
        self.x += 7         # self.x = 27 (stored in object)

    def m2(self):
        print(x)            # Error (x not defined here)
        print(self.x)       # not executed
        self.x += 6         # not executed

# End of class

a = c1()                   # object created
a.m1()                     # prints: 10, 20
a.m2()                     # error occurs here
print(a.x)                 # not executed
print(self.x)              # not executed
print(x)                   # not executed


class Test:
    
    def get(self):
        self.x = int(input("Enter x: "))   # e.g., 10
        self.y = int(input("Enter y: "))   # e.g., 20
        self.z = int(input("Enter z: "))   # e.g., 30
    
    def add(self, m, n):
        self.x = m.x + n.x                # 10 + 40 = 50
        self.y = m.y + n.y                # 20 + 50 = 70
        self.z = m.z + n.z                # 30 + 60 = 90
    
    def disp(self):
        print("x =", self.x)              # x = 50
        print("y =", self.y)              # y = 70
        print("z =", self.z)              # z = 90


# Creating objects
a = Test()                               # object a created
b = Test()                               # object b created
c = Test()                               # object c created

print("First Object")                    # First Object
a.get()                                  # user enters: 10, 20, 30

print("Second Object")                   # Second Object
b.get()                                  # user enters: 40, 50, 60

c.add(a, b)                              # c.x=50, c.y=70, c.z=90

print("Addition results")                # Addition results
c.disp()                                 # prints final values

find output

class Date:
    pass

a = Date()                          # object created
a.dd = 15                           # instance variables
a.mm = 8
a.yy = 1947

print(a)                            # <__main__.Date object at 0xXXXX>


#find output

class c1:
    def _str_(self):                # error- wrong method name
        return '25'

class c2:
    def _str_(self):
        return 35

class c3:
    def _str_(self):
        print('Hyd')

class c4:
    def _str_(self, x):
        return f'{x}'


a = c1()                            # object created
b = c2()
c = c3()
d = c4()

print(a)                            # <__main__.c1 object at 0xXXXX>
print(b)                            # <__main__.c2 object at 0xXXXX>
print(c)                            # <__main__.c3 object at 0xXXXX>
print(d)                            # <__main__.c4 object at 0xXXXX>

print(b._str_())                    # 35

print(c._str_())                    # Hyd
                                    # None

print(d._str_(50))                  # 50


class Student:

    def get(self):
        self.roll = int(input("Enter Roll Number: "))     # e.g., 101
        self.name = input("Enter Student Name: ")         # e.g., Sai
        self.gender = input("Enter Gender: ")             # e.g., M
        self.m1 = int(input("Enter Marks1: "))            # e.g., 80
        self.m2 = int(input("Enter Marks2: "))            # e.g., 70
        self.m3 = int(input("Enter Marks3: "))            # e.g., 60

    def compute(self):
        self.total = self.m1 + self.m2 + self.m3          # 80+70+60 = 210
        self.avg = self.total / 3                         # 210/3 = 70.0

        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = 'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'
        elif self.avg >= 60:
            self.grade = 'First class'
        elif self.avg >= 50:
            self.grade = 'Second class'
        else:
            self.grade = 'Third class'

    def disp(self):
        print("Roll Number :", self.roll)                 # 101
        print("Student Name :", self.name)                # Sai
        print("Gender :", self.gender)                   # M
        print("Total Marks :", self.total)               # 210
        print("Average :", self.avg)                     # 70.0
        print("Grade :", self.grade)                     # Distinction

    def __str__(self):   # ✅ correct method
        return f"{self.roll}, {self.name}, {self.gender}, {self.total}, {self.avg}, {self.grade}"


# Creating object
s = Student()                                         # object created

# Reading inputs
s.get()

# Computing results
s.compute()

# Display using method
print("\nUsing disp()")
s.disp()

# Display using print(object)
print("\nUsing __str__()")
print(s)