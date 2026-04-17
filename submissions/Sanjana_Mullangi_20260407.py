'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=float(input("Enter first side:")) 
		self.b=float(input("Enter second side:")) 
		self.c=float(input("Enter third side:")) 
	def  test(self):
		if  (self.a +self.b>=self.c) and (self.b+self.c>=self.a) and (self.c+self.a>=self.b):
				pass
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
			s=(self.a+self.b+self.c)/2
			area=math.sqrt(s*(s-self.a)*(s-self.b)*(s - self.c))
			return   area  
	def  peri(self):
			p =self.a+self.b+self.c
			return  p
# End of the class
t=triangle()
t.get()
t.test()
print('Area : ', t.area())
print('Perimeter : ',  t.peri())
	  


#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#x=10
		print(self . x)#x=20
		x += 5#15
		self . x += 7#27
	def   m2(self):
		print(x)#error-there is no local variable x in m2
		print(self . x)#27
		self . x += 6#33
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)#33
print(self . x)#error
print(x)#error-x is not defined



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x = int(input("Enter the value of x:"))
		self.y = int(input("Enter the value of y:"))
		self.z = int(input("Enter the value of z:"))
	def add(self, m, n):
		self.x = m.x + n.x
		self.y = m.y + n.y
		self.z = m.z + n.z
	def  disp(self):
		print(f'x={self.x},y={self.y},z={self.z}')
# End  of  the  class
a=Test()
b=Test()
c=Test()
print('First  Object')
a.get()
print('Second  Object')
b.get()
c.add(a,b)
print('Addition  results')
c.disp()



#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a.__str__)#type and address of a

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
print(a)#25
print(b)#error-35 is not string
print(c)#error-there is no return statement
print(d)#error-the argument x is not passed
print(b . __str__())#35
print(c . __str__())#Hyd None
print(d . __str__(50))#50


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.r=int(input("Enter roll no:"))#roll number
		self.s=input("Enter student name:")#student name
		self.g=input("Enter gender (m/f):")#gender
		self.marks=[]
		for i in range(3):
			self.marks.append(int(input(f'Enter marks for subject {i+1}: ')))
	def   compute(self):
		self.total = float(sum(self.marks))
		self.average = self.total/3
		if  any(mark < 40 for mark in self.marks):
				self.grade = 'Fail'
		elif self.average >= 70:
				self.grade = 'Distinction'
		elif self.average >= 60:
				self.grade = 'First class'
		elif self.average >= 50:
				self.grade = 'Second class'
		else:
				self.grade = 'Third class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.r)
		print('Student  Name  :  ' , self.s)
		print('Gender  :  ' ,  self.g)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , round(self.average,2))
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return f'{self.r}  {self.s}  {self.g}  {self.total}  {round(self.average,2)}  {self.grade}'
#End  of  the  class
c=Student()
c.get()
c.compute()
c.disp()
print(c.__str__())

#  Object  's'  --->
