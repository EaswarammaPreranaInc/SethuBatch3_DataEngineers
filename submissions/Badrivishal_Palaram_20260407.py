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
print('Area : ',   ???)
print('Perimeter : ',  ???) …


import math 
class triangle:
	def get(self):
		self.a=int(input("enter value if 1st side:"))
		self.b=int(input("enter value if 2nd side:"))
		self.c=int(input("enter value if 3rd side:"))

	def test(self):
		if self.a+self.b>=self.c and self.b+self.c>=self.a and self.c+self.a>self.b:
			pass
		else:
			print("not a triangle")
			exit()
	def area(self):
		s=(self.a+self.b+self.c)/2
		tri_area =s*(s-self.a)*(s-self.b)*(s-self.c)
		return math.sqrt(tri_area)
	def peri(self):
		p=self.a+self.b+self.c
		return p
t=triangle()

t.get()
t.test()

print("area:",t.area())
print("perimeter",t.peri())













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



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
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
How  to  print  object  'c'''


class Test:

    def get(self):
        self.x = int(input())
        self.y = int(input())
        self.z = int(input())

    def add(self, a, b):
        self.x = a.x + b.x
        self.y = a.y + b.y
        self.z = a.z + b.z

    def disp(self):
        print(self.x, self.y, self.z)


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












#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)
#type and address
#<__main__.Date object at 0x7f8c20a99c10>




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
print(a)#<__main__.c1 object at 0x78744e735c40>(hexadecimal address)
print(b)#<__main__.c2 object at 0x78744e735c44>(hexadecimal address)
print(c)#<__main__.c3 object at 0x78744e735c45>(hexadecimal address)
print(d)#<__main__.c4 object at 0x78744e735c49>(hexadecimal address)
print(b . _str_())#35
print(c . _str_())#'Hyd'<nexline> none
print(d . _str_(50))#50



'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		How  to  read  roll  number  
		How  to  read  student  name  
		How  to  read  gender  
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   _str_(self):
		return  All  the   values  of  object  in  the  form  of  string
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  _str_()  method
'''
class Student:

    def get(self):
        self.roll = int(input("Enter roll number: "))
        self.name = input("Enter name: ")
        self.gender = input("Enter gender: ")
        self.m1 = int(input("Enter marks of subject 1: "))
        self.m2 = int(input("Enter marks of subject 2: "))
        self.m3 = int(input("Enter marks of subject 3: "))

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
        return f"{self.roll} {self.name} {self.gender} {self.total} {self.avg} {self.grade}"



s = Student()

s.get()

s.compute()

print("\nUsing disp():")
s.disp()

print("\nUsing __str__():")
print(s)













