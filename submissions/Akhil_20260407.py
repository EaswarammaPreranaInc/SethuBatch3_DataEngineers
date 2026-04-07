''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  
		self.a = float(input("Enter first side : "))
		self.b = float(input("Enter second side : "))
		self.c = float(input("Enter third side : "))
	def  test(self):
		if  self.a + self.b >= self.c and self.a + self.c >= self.b and self.b + self.c >= self.a:
			return
		else:
			print('Not  a  triangle')
			exit() #How  to  stop  execution
	def  area(self):
	    s = ((self.a + self.b + self.c)/2)
	    return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
		return  self.a + self.b + self.c
# End of the class
t = triangle()
t.get()#How  to  read  inputs  into  object
t.test()#How  to  test  whether  inputs  are  valid
print('Area : ',   t.area())
print('Perimeter : ',  t.peri())

''' Output:
Enter first side : 3
Enter second side : 4
Enter third side : 5
Area :  6.0
Perimeter :  12.0

Enter first side : 3
Enter second side : 4
Enter third side : 8
Not  a  triangle
'''
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
		# print(x) # Error there is no local variable x
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1() # Object of class c1 is created
a . m1() # 10  <nextline> 20
a . m2() # 27
print(a . x) # 33
print(self . x) # Error there is no object self
print(x) # Error there is no variable x

''' Outputs:
10
20
27
33 
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x = int(input("Enter value of x : "))
		 self.y = int(input("Enter value of y : "))
		 self.z = int(input("Enter value of z : "))
	def   add(self , m , n):
		 self.x = m.x + n.x
		 self.y = m.y + n.y
		 self.z = m.z + n.z
	def  disp(self):
		 print(f"x = {self.x}") 
		 print(f"y = {self.y}") 
		 print(f"z = {self.z}") 
# End  of  the  class
a = Test()#How  to  create  three  Test  class  objects  a , b  and c
b = Test()
c = Test()
print('First  Object')
a.get()# How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()# How  to  read  inputs  into  object  'b'
c.add(a,b)# How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()

''' Output :
First  Object
Enter value of x : 10
Enter value of y : 20
Enter value of z : 30
Second  Object
Enter value of x : 40
Enter value of y : 50
Enter value of z : 60
Addition  results
x = 50
y = 70
z = 90
'''
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # <class '__main__.Date'> and address of object a in hexa decimal

#  Object  'a'  ---> dd = 15 , mm = 8 , yy = 1947

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
a = c1() # Object of class c1 is created
b = c2() # Object of class c2 is created
c = c3() # Object of class c3 is created
d = c4() # Object of class c4 is created
print(a) # '25'
print(b) # Error because __str__() when called implicity should return a string
print(c) # 'Hyd' <nextline> Error because __str__() when called implicity should return a stringbut not None Type
print(d) # Error because __str__() when called implicity should does not have arguments
print(b . _str_()) # 35
print(c . _str_()) # 'Hyd' <nextline> None
print(d . _str_(50)) # '50'

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno = int(input("Enter roll number : ")) 
		self.sname = input("Enter student name : ")
		self.gender = input("Enter gender(m/f) : ") 
		list = []
		for i in range(1,4):
		    m = int(input(f"Enter marks of subject {i} : "))
		    list.append(m)
		self.marks = list
	def   compute(self):
		self.tot = sum(self.marks) #How  to  calculate  total  marks
		self.avg = round(sum(self.marks)/3,2) #How  to  calculate  average  marks
		if  self.marks[0] < 40 or self.marks[1] < 40 or self.marks[2] < 40:
			self.grade = 'Fail'
		elif self.avg >= 70:
			self.grade = 'Distinction'
		elif self.avg >= 60:
			self.grade = 'First class'
		elif self.avg >= 50:
			self.grade = 'Second class'
		else:
			self.grade = 'Third class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f"{self.rno} {self.sname} {self.gender} {self.tot} {self.avg} {self.grade} "
#End  of   the  class
s = Student()#How  to  create  Student  class  object
s.get() # How  to  read  inputs  into  object
s.compute() # How  to  store  results  in  object
s.disp() # How  to  print  object  with  disp()  method
print(s) #How  to  print  object  with  _str_()  method
#  Object  's'  ---> rno = 25 , sname = 'Rama Rao' , gender = 'm' , marks = [52,48,55] , tot = 155 , avg = 51.67 ,grade = 'Second class'

''' Output:
Enter roll number : 25
Enter student name : Rama Rao
Enter gender(m/f) : m
Enter marks of subject 1 : 52
Enter marks of subject 2 : 48
Enter marks of subject 3 : 55
Roll  Number  :   25
Student  Name  :   Rama Rao
Gender  :   m
Total  Marks  :   155
Average  :   51.67
Grade  :   Second class
25 Rama Rao m 155 51.67 Second class 