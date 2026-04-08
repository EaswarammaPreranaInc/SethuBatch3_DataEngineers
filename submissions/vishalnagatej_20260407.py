'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self , a , b , c):
		self.a = a 		# How  to  read  three  sides  into  object  
		self.b = b
		self.c = c
	def  test(self):
		if  self.a + self.b >= self.c:	# sum  of  every  2  sides  >=  3rd  side:
				pass	# Do  nothing
		else:
			print('Not  a  triangle')
					# How  to  stop  execution
	def  area(self):
			s = (self.a + self.b + self.c) / 2
			return   math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))	# area  of  triangle
	def  peri(self):
			return  self.a + self.b + self.c	# perimeter  of  triangle
# End of the class
a = int(input('Enter first side : '))
b = int(input('Enter second side : '))
c = int(input('Enter third side : '))
n = triangle()		# How  to  create  triangle  class  object
m = n.get(a , b , c)	# How  to  read  inputs  into  object
# How  to  test  whether  inputs  are  valid
print('Area : ',   n.area())
print('Perimeter : ', n.peri())

#===============================================================================================================================

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
		# print(x)          # error becoz x is only defined in method m1(). it excutes only in m1() method
		print(self . x)     # self is owner variable. so it is applicable for any method in class c1().
		self . x += 6		
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
# print(self . x)           # error , becoz self.x is not defined
# print(x)                  # error , x is not defined.

# 10
# 20
# 27
# 33

#===============================================================================================================================

# '''  (Home  work)
# Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
# store  results  in   third  object

# 1st  object   --->  x = 10 , y = 20 , z = 30

# 2nd  object --->  x = 40 , y = 50 , z = 60

# 3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
# '''
# class  Test:
# 	def   get(self , x , y , z):
# 		self.x = x      
# 		self.y = y
# 		self.z = z

# 	def   add(self , m , n):
# 		#  How  to  add  objects  m  and  n  and  store  results  in  object 
# 	def  disp(self):
# 		#  How  to  print  object  
# # End  of  the  class
# # a = Test()    # How  to  create  three  Test  class  objects  a , b  and  c
# # print('First  Object')
# x = int(input('Enter value of x : '))   # How  to  read  inputs  into  object  'a'
# y = int(input('Enter value of y : '))
# z = int(input('Enter value of z : '))
# print('Second  Object')
# x = int(input('Enter value of x : '))   # How  to  read  inputs  into  object  'b'
# y = int(input('Enter value of y : '))
# z = int(input('Enter value of z : '))
# # How  to  add  objects  a  and  b  and  store  results in  object  'c'
# print('Addition  results')
# # How  to  print  object  'c'

#===============================================================================================================================

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)		# type and address of an object


#  Object  'a'  --->

#===============================================================================================================================

#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print ('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)	
# print(b)	# error , becoz it passes integer in the __str__
# print(c)	# error
# print(d)	# error , becoz it reequire 1 positional argument
print(b . __str__())		
print(c . __str__())		
print(d . __str__(50))		

# 25
# 35
# Hyd
# None     # due to presence of print is returns None also
# 50

#===============================================================================================================================

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self , rollno , sname , gender , sub1 , sub2 , sub3):
		self.rollno = rollno    # How  to  read  roll  number  
		self.sname = sname      # How  to  read  student  name  
		self.gender = gender    # How  to  read  gender  
		self.sub1 = sub1        # How  to  read  marks  of  3  subjects
		self.sub2 = sub2 
		self.sub3 = sub3 
	def   compute(self):
		self.total_marks = sub1 + sub2 + sub3     # How  to  calculate  total  marks
		self.average = self.total_marks / 3                      # How  to  calculate  average  marks
		if  self.sub1 or self.sub2 or self.sub3  < 40:           # at least  one  subject  is  below  40
				return 'Fail'
		elif  self.average >= 70:
				return 'Distinction'
		elif  self.average >= 60:
				return 'First  class'
		elif  self.average >= 50:
				return 'Second  class'
		else:
				return 'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  rollno)
		print('Student  Name  :  ' , sname)
		print('Gender  :  ' , gender)
		# # print('Total  Marks  :  ' , total_marks)
		# print('Average  :  ' , average)
		# # print('Grade  :  ' , self.compute)
	def   __str__(self):
		return  self.disp     # All  the   values  of  object  in  the  form  of  string
#End  of  the  class
a = Student()   # How  to  create  Student  class  object

rollno = int(input('Enter rollno : '))        # How  to  read  inputs  into  object
sname = input('Enter student name : ')      
gender = input('enter gender (m/f) : ')
sub1 = int(input('Enter marks of subject 1 : '))
sub2 = int(input('Enter marks of subject 2 : '))
sub3 = int(input('Enter marks of subject 3 : '))

# a.compute()         # How  to  store  results  in  object
a.disp()            # How  to  print  object  with  disp()  method
a.__str__()         # How  to  print  object  with  __str__()  method



#  Object  's'  --->

