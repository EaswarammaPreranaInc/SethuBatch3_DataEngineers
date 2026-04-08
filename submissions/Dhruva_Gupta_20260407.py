Name-Dhruva Gupta
Roll Number-D238

1)
import math
class Triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        if (self.a + self.b > self.c and
            self.b + self.c > self.a and
            self.c + self.a > self.b):
            return True
        else:
            print("Not a triangle")
            exit() 
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = Triangle()
t.get()
t.test()
print("Area :", t.area())
print("Perimeter :", t.peri())

2)
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self . x += 7
	def   m2(self):
		print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
print(self . x)
print(x)

Output-
10
20
#Error

3)
class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))
    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
    def disp(self):
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)
a = Test()
b = Test()
c = Test()
print("First Object")
a.get()
print("Second Object")
b.get()
c.add(a, b)
print("Addition results")
c.disp()

4)
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)


Output-
__main__.Date with address

5)
#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))

Output-
__main__.c1 with address
__main__.c2 with address
__main__.c3 with address
__main__.c4 with address
35
Hyd
None
50

6)
class Student:
    
    def get(self):
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.m1 = int(input("Enter marks of Subject 1: "))
        self.m2 = int(input("Enter marks of Subject 2: "))
        self.m3 = int(input("Enter marks of Subject 3: "))
    def compute(self):
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3
       if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = "Fail"
        elif self.avg >= 70:
            self.grade = "Distinction"
        elif self.avg >= 60:
            self.grade = "First class"
        elif self.avg >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"
    def disp(self):
        print("Roll Number :", self.roll)
        print("Student Name :", self.name)
        print("Gender :", self.gender)
        print("Total Marks :", self.total)
        print("Average :", self.avg)
        print("Grade :", self.grade)
    def __str__(self): 
        return (f"Roll Number: {self.roll}, Name: {self.name}, "
                f"Gender: {self.gender}, Total: {self.total}, "
                f"Average: {self.avg}, Grade: {self.grade}")
# create object
s = Student()
# read inputs
s.get()
# compute results
s.compute()
# display using method
print("\nUsing disp() method")
s.disp()
# display using __str__()
print("\nUsing print(object)")
print(s)

