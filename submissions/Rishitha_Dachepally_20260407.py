# Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # Output : 10
		print(self . x) # Output : 20
		x += 5
		self . x += 7
	def   m2(self):
		# print(x) # Error because name 'x' is not defined
		print(self . x) # Output : 27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # Output : 33
# print(self . x) # Error because name 'self' is not defined
# print(x) # Error because name 'x' is not defined

# -----------------------------------------------------------------------------------------------------

# Add two objects (Home  work)
class  Test:
	def   get(self):
		self.x=int(input('Enter value of x:')) # Input : 10 (Obj 1) / 40 (Obj 2)
		self.y=int(input('Enter value of y:')) # Input : 20 (Obj 1) / 50 (Obj 2)
		self.z =int(input('Enter value of z:')) # Input : 30 (Obj 1) / 60 (Obj 2)
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		print('x=',self.x) # Output : x= 50
		print('y=',self.y) # Output : y= 70
		print('z=',self.z) # Output : z= 90
# End  of  the  class
a=Test(); b=Test(); c=Test()
print('First Object'); a.get()
print('Second Object'); b.get()
c.add(a,b)
print('Addition results'); c.disp()

# -----------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # Output : <__main__.Date object at 0x...> (Type and address)
# Object 'a' ---> dd: 15, mm: 8, yy: 1947

# -----------------------------------------------------------------------------------------------------

# Find outputs (Home  work) - Note: Using _str_ instead of __str__ per your prompt
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
a = c1(); b = c2(); c = c3(); d = c4()
print(a) # Output : <__main__.c1 object at 0x...> (Error because _str_ is not __str__)
print(b) # Output : <__main__.c2 object at 0x...>
print(c) # Output : <__main__.c3 object at 0x...>
print(d) # Output : <__main__.c4 object at 0x...>
print(b . _str_()) # Output : 35
print(c . _str_()) # Output : Hyd 
                   # None
print(d . _str_(50)) # Output : 50

# -----------------------------------------------------------------------------------------------------

# Student grading program (Home  work)
class   Student:
	def   get(self):
		self.rno=int(input('Enter roll number : ')) # Input : 25
		self.sname=input('Enter student name :') # Input : Rama Rao
		self.gender=input('Enter gender (m/f) : ') # Input : m
		self.m1=int(input('Enter marks of subject 1 : ')) # Input : 52
		self.m2=int(input('Enter marks of subject 2 : ')) # Input : 48
		self.m3=int(input('Enter marks of subject 3 : ')) # Input : 55
	def   compute(self):
		self.tot=float(self.m1 + self.m2 + self.m3)
		self.avg=round(self.tot/3, 2)
		if  self.m1<40 or self.m2<40 or self.m3<40:
			self.grade='Fail'
		elif   self.avg>= 70:
			self.grade='Distinction'
		elif  self.avg >= 60:
			self.grade='First  class'
		elif  self.avg  >= 50:
			self.grade='Second  class'
		else:
			self.grade='Third  class'
	def  disp(self):
		print('Roll Number : ', self.rno) # Output : Roll Number : 25
		print('Student Name : ', self.sname) # Output : Student Name : Rama Rao
		print('Gender : ', self.gender) # Output : Gender : m
		print('Total Marks : ', self.tot) # Output : Total Marks : 155.0
		print('Average : ', self.avg) # Output : Average : 51.67
		print('Grade : ', self.grade) # Output : Grade : Second class
	def   _str_(self):
		return  F'{self.rno} {self.sname} {self.gender} {self.tot} {self.avg} {self.grade}'

s=Student()
s.get()
s.compute()
s.disp()
print(s._str_()) # Output : 25 Rama Rao m 155.0 51.67 Second class
# Object 's' ---> rno: 25, sname: Rama Rao, gender: m, tot: 155.0, avg: 51.67, grade: Second class