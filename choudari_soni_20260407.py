# '''  (Home  work)
# Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

# 1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

# 2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

# 3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
# '''
import math

class triangle:
    def get(self):
        self.a = int(input('Enter side a = '))
        self.b = int(input('Enter side b = '))
        self.c = int(input('Enter side c = '))

    def test(self):
        if self.a + self.b >= self.c and self.b + self.c >= self.a and self.c + self.a >= self.b:
            pass
        else:
            print('Not a triangle')
            exit()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c

# End of the class

obj = triangle()
obj.get()
obj.test()
print('Area : ', obj.area())
print('Perimeter : ', obj.peri())

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5#15
		self . x += 7#27
	def   m2(self):
		print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)#10
print(self . x)#20
print(x)#

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        self.x = int(input('Enter x = '))
        self.y = int(input('Enter y = '))
        self.z = int(input('Enter z = '))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print('x =', self.x)
        print('y =', self.y)
        print('z =', self.z)

# Create objects
a = Test()
b = Test()
c = Test()

print('First Object')
a.get()

print('Second Object')
b.get()

# Add objects a and b, store in c
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
print(a)#type and address



#  Object  'a'  --->

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
a = c1()
b = c2()
c = c3()
d = c4()
print(a)#'25'
print(b)#error
print(c)#error
print(d)#error
print(b . __str__())#35
print(c . __str__())#Hyd
print(d . __str__(50))#50

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.roll_number=int(input('Enter a number ='))
		self.student_name=int(input('Enter a number ='))
		self.gender=int(input('Enter a number ='))  
		self.m1=int(input('Enter marks of student 1='))
		self.m2=int(input('Enter marks of student 2='))
		self.m3=int(input('Enter marks of student 3='))
	def   compute(self):
		self.total=self.m1+self.m2+self.m3
		self.average=self.total/3
		if  self.m1<40 or self.m2<40 or self.m3<40:
				self.grade='Fail'
		elif  self.avg >= 70:
				self.grade='distinction'
		elif  self.avg >= 60:
				self.grade='first class'
		elif self.avg >= 50:
				self.avg='second class'
		else:
				self.avg='third class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   __str__(self):
		return f"Roll: {self.roll_number}, Name: {self.student_name}, Gender: {self.gender}, Total: {self.total}, Avg: {self.avg}, Grade: {self.grade}"
#End  of  the  class
s=student()
s.get()
s.compute()
print('\nusind disp() method:')
s.disp()



# #  Object  's'  --->

