#1
'''
(Home work)

Write a program to determine area and perimeter of triangle and represent triangle by an object

1) What is the area of triangle? ---> sqrt(s * (s - a) * (s - b) * (s - c))

2) What is the formula for 's'? ---> (a + b + c) / 2

3) What is the perimeter of triangle? ---> a + b + c
'''
import math
import sys

class triangle:
    def get(self):
        self.a = float(input('Enter side a: '))
        self.b = float(input('Enter side b: '))
        self.c = float(input('Enter side c: '))
    
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass # Valid triangle
        else:
            print('Not a triangle')
            sys.exit() 
            
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        
    def peri(self):
        return self.a + self.b + self.c

# End of the class
t = triangle() 
t.get()        
t.test()       
print('Area : ', t.area())
print('Perimeter : ', t.peri())



#2
# Find outputs (Home work)
class c1:
    def m1(self):
        x = 10         # Local variable
        self.x = 20    # Instance variable
        print(x)       # 10
        print(self.x)  # 20
        x += 5         
        self.x += 7    
        
    def m2(self):
        # print(x)     # Error as name 'x' is not defined
        print(self.x)  # 27 
        self.x += 6    # Instance x becomes 33
# End of the class
a = c1()
a.m1()
a.m2()
print(a.x)             # 33
# print(self.x)        # Error as name 'self' is not defined
# print(x)             # Error as name 'x' is not defined



#3
'''
(Home work)

Write a program to add two objects where each object contains three values and
store results in third object

1st object ---> x = 10 , y = 20 , z = 30

2nd object ---> x = 40 , y = 50 , z = 60

3rd object ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = int(input('Enter x: '))
        self.y = int(input('Enter y: '))
        self.z = int(input('Enter z: '))
        
    def add(self, m, n):
        # Adding attributes of objects m and n and storing in current object (self)
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
        
    def disp(self):
        print(f"x={self.x}, y={self.y}, z={self.z}")

# End of the class
a = Test()
b = Test()
c = Test()

print('First Object')
a.get()
print('Second Object')
b.get()

c.add(a, b)
print('Addition results')
c.disp()



#4
# Find outputs (Home work)
class Date:
    pass

a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a) # <__main__.Date object at 0x...>



#5
# Find outputs (Home work)
class c1:
    def __str__(self): # Assuming double underscores for magic method
        return '25'
class c2:
    def __str__(self):
        return 35 
class c3:
    def __str__(self):
        print('Hyd')
class c4:
    def __str__(self, x):
        return f'{x}'

a = c1()
b = c2()
c = c3()
d = c4()

print(a) # 25
# print(b) # Error as __str__ returned non-string (type int)
# print(c) # Error as __str__ returned non-string (type NoneType)
# print(d) # Error as __str__() missing 1 required positional argument: 'x'
print(b.__str__())    # 35 (Manual call allows returning ints)
# print(c.__str__())  # Hyd then prints None
print(d.__str__(50))  # 50



#6
'''
Write a program to determine total , average and grade of a student
Inputs are Roll Number , Stud Name , Marks of 3 subjects and Gender
'''
class Student:
    def get(self):
        self.roll = int(input("Enter roll number: "))
        self.name = input("Enter student name: ")
        self.gender = input("Enter gender (m/f): ")
        self.m1 = int(input("Enter marks for subject 1: "))
        self.m2 = int(input("Enter marks for subject 2: "))
        self.m3 = int(input("Enter marks for subject 3: "))

    def compute(self):
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3
        
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = 'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'
        elif self.avg >= 60:
            self.grade = 'First class'
        elif self.avg >= 50:
            self.grade = 'Second class'
        elif self.avg >= 40:
            self.grade = 'Third class'
        else:
            self.grade = 'Fail'

    def disp(self):
        print('Roll Number  : ', self.roll)
        print('Student Name : ', self.name)
        print('Gender       : ', self.gender)
        print('Total Marks  : ', self.total)
        print('Average      : ', self.avg)
        print('Grade        : ', self.grade)

    def __str__(self):
        return f"Roll: {self.roll}, Name: {self.name}, Total: {self.total}, Grade: {self.grade}"

s = Student()
s.get()
s.compute()
s.disp()
print(s)