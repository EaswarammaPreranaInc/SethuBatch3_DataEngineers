'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2
3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import math
class triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
    def test(self):
        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            pass  # valid triangle
        else:
            print("Not a triangle")
            exit()
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = triangle()
t.get()
t.test()
print('Area :', t.area())
print('Perimeter :', t.peri())
'''Find  outputs  (Home  work)'''
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
'''output'''
# 10
# 20
# 27
# 33
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = float(input("Enter value for x: "))
        self.y = float(input("Enter value for y: "))
        self.z = float(input("Enter value for z: "))
    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
    def disp(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")
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
'''Find  outputs (Home  work)'''
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)  #Type and Address
'''Find  outputs (Home  work)'''
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
a = c1()
b = c2()
c = c3()
d = c4()
print(a) #25
print(b) #Error --no string
print(c) #Error
print(d) #Error
print(b . __str__())
print(c . __str__()) # Hyd
print(d . __str__(50)) #50
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

import math  
class Student:
    # Method to read input data
    def get(self):
        self.rno = int(input("Enter Roll Number: "))  # How  to  read  roll  number  
        self.sname = input("Enter Student Name: ")    # How  to  read  student  name  
        self.gen = input("Enter Gender (M/F): ")      # #How  to  read  gender 
        self.marks = []                                
        for i in range(1, 4):
            mark = float(input(f"Enter marks of subject {i}: "))  
            self.marks.append(mark)                                
    def compute(self):
        self.total = sum(self.marks)          #How  to  read  marks  of  3  subjects
        self.avg = self.total / 3              

        # Determine grade
        if any(m < 40 for m in self.marks):   #At  least  one  subject  is  below  40:
            self.grade = 'Fail'                # How  to  initilaize  grade  to  'Fail
        elif self.avg >= 70:                   #  average  is  above  >= 70%:
            self.grade = 'Distinction'         # How  to  initilaize  grade  to  'Distinction'
        elif self.avg >= 60:                   #  average  is  above  >= 60%:
            self.grade = 'First class'         # How  to  initilaize  grade  to 'First class'
        elif self.avg >= 50:                   # Average is above>= 50%:
            self.grade = 'Second class'        # How  to  initilaize  grade  to 'Second class'
        else:
            self.grade = 'Third class'         # How  to  initilaize  grade  to  'Third  class
    def disp(self):
        print("Roll Number  :", self.rno)
        print("Student Name :", self.sname)
        print("Gender       :", self.gen)
        print("Total Marks  :", self.total)
        print("Average      :", self.avg)
        print("Grade        :", self.grade)
    def __str__(self):
        return (f"Roll Number: {self.rno}, Name: {self.sname}, Gender: {self.gen}, "
                f"Total: {self.total}, Average: {self.avg}, Grade: {self.grade}")
s = Student()  # Create Student class object
s.get()        # Read inputs from user
s.compute()    # Calculate total, average, and grade
s.disp()       # Display formatted output using disp() method
print(s)       # Display formatted output using __str__() method



