import math

class Triangle:
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self):
        # Check triangle validity
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Input from user
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Create object
t = Triangle(a, b, c)

# Validate and display results
if t.is_valid():
    print("Perimeter:", t.perimeter())
    print("Area:", t.area())
else:
    print("Not a triangle")





#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)	#10	
		print(self . x)	#20
		x += 5
		self . x += 7
	def   m2(self):
		print(x)	#27
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()	#error
print(a . x)
print(self . x)	#error x is not defined
print(x)	#error x is not defined




class Test:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, obj1, obj2):
        self.x = obj1.x + obj2.x
        self.y = obj1.y + obj2.y
        self.z = obj1.z + obj2.z

    def display(self):
        print("x =", self.x, "y =", self.y, "z =", self.z)


# create objects
a = Test(int(input("Enter the  value x: ")),
         int(input("Enter the value y: ")),
         int(input("Enter the value y: ")))
print("Enter the values for second object")
b =Test(int(input("Enter the value x: ")),
        int(input("Enter the value y: ")),
        int(input("Enter the value z: ")))
   # 2nd object
c = Test(0, 0, 0)      # 3rd object to store result

# add objects a and b, store in c
c.add(a, b)

# display result
print("Addition Results:")
c.display()







#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)	#<__main__.date object at address of the object>




#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()	#25
b = c2()	#error it does not return int datatype
c = c3()	#Hyd
d = c4()	#error required positional argument is not given
print(a)
print(b)
print(c)	#error
print(d)
print(b . __str__())
print(c . __str__())	#None
print(d . __str__(50))	#50






class Student:

    def get(self):
        # read inputs
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.m1 = int(input("Enter marks of subject 1: "))
        self.m2 = int(input("Enter marks of subject 2: "))
        self.m3 = int(input("Enter marks of subject 3: "))

    def compute(self):
        # calculate total and average
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3

        # grade calculation
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
        print('Roll Number :', self.roll)
        print('Student Name :', self.name)
        print('Gender :', self.gender)
        print('Total Marks :', self.total)
        print('Average :', self.avg)
        print('Grade :', self.grade)

    def __str__(self):
        return (f"Roll Number : {self.roll}\n"
                f"Student Name : {self.name}\n"
                f"Gender : {self.gender}\n"
                f"Total Marks : {self.total}\n"
                f"Average : {self.avg}\n"
                f"Grade : {self.grade}")


# create object
s = Student()

# read inputs
s.get()

# compute results
s.compute()

# print using disp()
print("\nUsing disp() method:")
s.disp()

# print using __str__()
print("\nUsing __str__() method:")
print(s)