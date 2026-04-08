'''  (Home  work)
1.Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''

import math

class Triangle:
    def get(self):
        # Reading sides into object
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Triangle validity check
        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            return True
        else:
            print("Not a triangle")
            return False   # Stops further execution

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# ---- Main Program ----
t = Triangle()        # Create object
t.get()               # Read inputs into object

if t.test():          # Validate inputs
    print("Area :", t.area())
    print("Perimeter :", t.peri())
    



2.#  Find  outputs  (Home  work)

class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) # 20 
		x += 5
		self . x += 7
	def   m2(self):
#		print(x) # NameError: name 'x' is not defined
		print(self . x) # 27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # 33
#print(self . x) # NameError: name 'self' is not defined
#print(x) # NameError: name 'x' is not defined





3.'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        # read inputs into x, y, z
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        # add objects m and n, store in current object
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        # print object values
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)


# ---- Create three objects ----
a = Test()
b = Test()
c = Test()

print("First Object")
a.get()          # read inputs into object 'a'

print("Second Object")
b.get()          # read inputs into object 'b'

# add objects a and b, store results in object 'c'
c.add(a, b)

print("Addition results")
c.disp()         # print object 'c'




4.#Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # <__main__.Date object at 0x0000023176AFC150>

#  Object  'a'  --->




5.#  Find  outputs (Home  work)
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
'''
<__main__.c1 object at 0x0000026E9FB01310>
<__main__.c2 object at 0x0000026E9FB01350>
<__main__.c3 object at 0x0000026E9FB01390>
<__main__.c4 object at 0x0000026E9FB013D0>
35
Hyd
None
50
'''



'''
6.Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class Student:
    def get(self):
        # read inputs
        self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")

        self.m1 = int(input("Enter marks of Subject 1: "))
        self.m2 = int(input("Enter marks of Subject 2: "))
        self.m3 = int(input("Enter marks of Subject 3: "))

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
        print('Roll Number  : ', self.roll)
        print('Student Name : ', self.name)
        print('Gender       : ', self.gender)
        print('Total Marks  : ', self.total)
        print('Average      : ', self.avg)
        print('Grade        : ', self.grade)

    def __str__(self):
        return (f"Roll: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.avg}, Grade: {self.grade}")


# ---- Create object ----
s = Student()

# ---- Read inputs into object ----
s.get()

# ---- Store results in object ----
s.compute()

# ---- Print using disp() ----
print("\nUsing disp() method")
s.disp()

# ---- Print using __str__() ----
print("\nUsing __str__() method")
print(s)