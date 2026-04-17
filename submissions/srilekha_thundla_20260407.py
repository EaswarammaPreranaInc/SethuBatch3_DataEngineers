'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
# import math

# class triangle:
#     def get(self):
#         self.a = int(input("Enter first side : "))
#         self.b = int(input("Enter second side : "))
#         self.c = int(input("Enter third side : ")) 
    
#     def test(self):
#         if (self.a + self.b > self.c and
#             self.b + self.c > self.a and
#             self.a + self.c > self.b):
#             pass
#         else:
#             print('Not a triangle')
#             exit()

#     def area(self):
#         s = (self.a + self.b + self.c) / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) 

#     def peri(self):
#         return self.a + self.b + self.c

# # Main
# t = triangle()
# t.get()
# t.test()

# print('Area : ', t.area())
# print('Perimeter : ', t.peri())

#  Find  outputs  (Home  work)
# class   c1:
# 	def  m1(self):
# 		x = 10
# 		self . x = 20
# 		print(x)
# 		print(self . x)
# 		x += 5
# 		self . x += 7
# 	def   m2(self):
# 		# print(x)#x is niot defined
# 		print(self . x)
# 		self . x += 6
# # End  of  the  class
# a = c1()
# a . m1()
# a . m2()
# print(a . x)
# print(self . x)#can not use self
# print(x)

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
	
	
# class Test:
#     def get(self):
#         self.x = int(input("Enter value of X : "))
#         self.y = int(input("Enter value of Y : "))
#         self.z = int(input("Enter value of Z : "))
    
#     def add(self, m, n):
#         self.x = m.x + n.x
#         self.y = m.y + n.y
#         self.z = m.z + n.z
    
#     def disp(self):
#         print("x =", self.x)
#         print("y =", self.y)
#         print("z =", self.z)

# # Create objects
# a = Test()
# b = Test()
# c = Test()

# print('First Object')
# a.get()

# print('Second Object')
# b.get()

# # Add a and b, store in c
# c.add(a, b)

# print('Addition results')
# c.disp()

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''

		



#  Object  's'  --->

class Student:
    def get(self):
        self.Roll_Number = int(input("Enter roll no : "))
        self.Student_name = input("Enter student name : ")
        self.gender = input("Enter gender (m/f) : ") 
        self.marks_sub1 = int(input("Enter marks of subject 1 : "))
        self.marks_sub2 = int(input("Enter marks of subject 2 : "))
        self.marks_sub3 = int(input("Enter marks of subject 3 : "))

    def compute(self):
        self.total = self.marks_sub1 + self.marks_sub2 + self.marks_sub3
        self.avg = self.total / 3

        if (self.marks_sub1 < 40 or 
            self.marks_sub2 < 40 or 
            self.marks_sub3 < 40):
            self.grade = 'Fail'
        elif self.avg >= 70:
            self.grade = 'Distinction'
        elif self.avg >= 60:
            self.grade = 'First Class'
        elif self.avg >= 50:
            self.grade = 'Second Class'
        else:
            self.grade = 'Third Class'

    def disp(self):
        print('Roll Number :', self.Roll_Number)
        print('Student Name :', self.Student_name)
        print('Gender :', self.gender)
        print('Total Marks :', self.total)
        print('Average :', self.avg)
        print('Grade :', self.grade)

    def __str__(self):
        return (f"Roll Number : {self.Roll_Number}\n"
                f"Student Name : {self.Student_name}\n"
                f"Gender : {self.gender}\n"
                f"Total Marks : {self.total}\n"
                f"Average : {self.avg}\n"
                f"Grade : {self.grade}")

# Main
s = Student()
s.get()
s.compute()

s.disp()

# print(s)