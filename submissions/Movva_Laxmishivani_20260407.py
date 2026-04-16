'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2
3) What  is  the  perimeter  of  triangle ?  ---> a + b + c

Sample output:
Enter first side : 3
Enter second side : 4
Enter third side : 5
Area : 6.0
Perimeter : 12.0

Enter first side : 3
Enter second side : 4
Enter third side : 8
Not a triangle

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
print('Perimeter : ',  ???)
'''
import math
class triangle:
    def get(self):
        self.a = float(input('Enter first side : '))
        self.b = float(input('Enter second side : '))
        self.c = float(input('Enter third side : '))
    def test(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        else:
            print('Not a triangle')
            return False
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def peri(self):
        return self.a + self.b + self.c
t = triangle()
t.get()
if t.test():
    print('Area :', t.area())
    print('Perimeter :', t.peri())

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
		print(x) # Error because x is not defined here
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
print(self . x) #Error because self can't be  defined outside class
print(x) # Error because x is not global
'''
10
20
27
33
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and store  results  in   third  object
1st  object   --->  x = 10 , y = 20 , z = 30
2nd  object --->  x = 40 , y = 50 , z = 60
3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90

Sample output:
First Object
Enter value of x:10
Enter value of y:20
Enter value of z:30

Second Object
Enter value of x:40
Enter value of y:50
Enter value of z:60

Addition results
x=50
y=70
z=90

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
'''
class Test:
    def get(self):
        self.x = int(input('Enter value of x: '))
        self.y = int(input('Enter value of y: '))
        self.z = int(input('Enter value of z: '))
    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
    def disp(self):
        print('x =', self.x)
        print('y =', self.y)
        print('z =', self.z)
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

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) #Type and address of object 'a'

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
print(a) # 25
print(b) # Error because 35 is not string
print(c) # Hyd 
print(d) # Error because argument should be self only
print(b . _str_()) # 35
print(c . _str_()) # Hyd <nextline>None
print(d . _str_(50)) # 50

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

Sample output:
Enter roll number : 25
Enter student name : Rama Rao
Enter gender (m/f) : m
ENter marks of subject 1 : 52
ENter marks of subject 2 : 48
ENter marks of subject 3 : 55

Roll Number  :  25
Student Name :  Rama Rao
Gender  :  m
Total Marks  :  155.0
Average  :  51.67
Grade  :  Second class

25   Rama Rao   m   155.0   51.67   Second class

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
        self.roll = int(input('Enter roll number : '))
        self.name = input('Enter student name : ')
        self.gender = input('Enter gender (m/f) : ')
        self.m1 = float(input('Enter marks of subject 1 : '))
        self.m2 = float(input('Enter marks of subject 2 : '))
        self.m3 = float(input('Enter marks of subject 3 : '))
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
        else:
            self.grade = 'Third class'
    def disp(self):
        print('Roll Number  : ', self.roll)
        print('Student Name : ', self.name)
        print('Gender       : ', self.gender)
        print('Total Marks  : ', self.total)
        print('Average      : ', round(self.avg, 2))
        print('Grade        : ', self.grade)
    def __str__(self):
        return f'{self.roll}   {self.name}   {self.gender}   {self.total}   {round(self.avg,2)}   {self.grade}'
s = Student()
s.get()
s.compute()
s.disp()
print(s)