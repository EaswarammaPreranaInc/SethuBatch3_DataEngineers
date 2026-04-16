'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		How  to  read  three  sides  into  object  
	def  test(self):
		if  sum  of  every  2  sides  >=  3rd  side:
				Do  nothing
		 else:
				print('Not  a  triangle')
				How  to  stop  execution
	def  area(self):
			return   area  of  triangle
	def  peri(self):
			return  perimeter  of  triangle
# End of the class
How  to  create  triangle  class  object
How  to  read  inputs  into  object
How  to  test  whether  inputs  are  valid
print('Area : ', t.area())
print('Perimeter : ',t.perimeter())




# Find  outputs  (Home  work)
class  c1:
	def m1(self):
		x = 10
		self . x = 20
		print(x)  # 10
		print(self . x) # 20
		x += 5 
		self . x += 7 
	def  m2(self):
		print(x)
		print(self . x)
		self . x += 6
# End  of  the class
a = c1()
a . m1() 
a . m2() 
print(a . x) 
print(self . x)
print(x)




'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 How  to  read  inputs  into  variables  x , y  and  z  
	def   add(self , m , n):
		 How  to  add  objects  m  and  n  and  store  results  in  object 
	def  disp(self):
		 How  to  print  object  
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
How  to  print  object  'c'


import sys

class Student:
    def __init__(self):
        # Initialize variables
        self.roll_no = ""
        self.name = ""
        self.gender = ""
        self.marks = []
        self.total = 0
        self.average = 0
        self.grade = ""

    def get(self):
        # Input all details
        self.roll_no = input("Enter Roll Number: ")
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender (M/F): ")
        self.marks = [float(input(f"Enter marks of subject {i+1}: ")) for i in range(3)]

    def compute(self):
        self.total = sum(self.marks)
        self.average = self.total / len(self.marks)

        # Decide grade
        if any(mark < 40 for mark in self.marks):
            self.grade = "Fail"
        elif self.average >= 70:
            self.grade = "Distinction"
        elif self.average >= 60:
            self.grade = "First class"
        elif self.average >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"

    def disp(self):
        print(f"Roll Number  : {self.roll_no}")
        print(f"Student Name : {self.name}")
        print(f"Gender       : {self.gender}")
        print(f"Total Marks  : {self.total}")
        print(f"Average      : {self.average:.2f}")
        print(f"Grade        : {self.grade}")

    def __str__(self):
        return (f"Roll Number: {self.roll_no}\n"
                f"Name: {self.name}\n"
                f"Gender: {self.gender}\n"
                f"Total Marks: {self.total}\n"
                f"Average: {self.average:.2f}\n"
                f"Grade: {self.grade}")

# --------- Usage ---------
s = Student()
s.get()
s.compute()

print("\n--- Using disp() ---")
s.disp()

print("\n--- Using __str__() ---")
print(s)