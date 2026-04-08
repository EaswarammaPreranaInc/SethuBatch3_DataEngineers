'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input("enter side1 of triangle"))
		self.b=int(input("enter side2 of triangle"))
		self.c=int(input("enter side3 of triangle"))
	def  test(self):
		if self.a+self.b>self.c and self.b+self.c>self.a and self.c+self.a>self.b:
			print("valid inputs")
			return True
		else:
			print('Not  a  triangle')
			return False
	def  area(self):
			s=(self.a+self.b+self.c)/2
			return   math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
			return  self.a+self.b+self.c
# End of the class
a=triangle()
a.get()
if a.test():
    print('Area : ',a.area())
    print('Perimeter : ', a.peri())
#---------------------------------------------------------------------------
#Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10 #local variable of method
		self . x = 20 #a variable is created in object a of class c1 with x=20
		print(x)#10
		print(self . x) #20
		x += 5 #local varibale x modified to 15
		self . x += 7 #instance varibale modified to 27
	def   m2(self):
		#print(x)#Error no local variable
		print(self . x)#27
		self . x += 6 
# End  of  the  class
a = c1() #class c1 object is created and reference a points to it
a . m1() #self is a
a . m2() #self is a
print(a . x) #33
#print(self . x) #what is self ? python confuses
#print(x)#no global variable
#---------------------------------------------------------------------------
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input("enter value :"))
		self.y=int(input("enter value :"))
		self.z=int(input("enter value :")) 
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		print(f'x={self.x}')
		print(f'y={self.y}')
		print(f'z={self.z}')
# End  of  the  class
a=Test()
b=Test()
c=Test()
print('first object')
a.get()
print('second object')
b.get()
c.add(a,b)
print('Addition  results')
c.disp()
#---------------------------------------------------------------------------
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()#initially empty object
a . dd = 15 #dd variable added
a . mm = 8 #mm variable added
a . yy = 1947 #yy variable added
print(a)#type and address
#-----------------------------------------------------------------
#  Find  outputs (Home  work)
class   c1:
	def __str__(self):
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
print(a) #'25'
#print(b) #Error
#print(c) # 'Hyd' None is returned so -->Error
#print(d) #Error
print(b . __str__()) #35
print(c . __str__()) #Hyd ,None
print(d . __str__(50)) #'50'
#-------------------------------------------------------
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rollnum=int(input("enter roll number"))
		self.student_name=(input("enter student name"))
		self.gender=(input("enter gender(m/f)"))
		self.sub1=int(input("enter marks fo subject 1"))
		self.sub2=int(input("enter marks fo subject 2"))
		self.sub3=int(input("enter marks fo subject 3"))
	def   compute(self):
		self.grade=""
		self.total_marks=self.sub1+self.sub2+self.sub3
		self.average=self.total_marks/2
		if  self.sub1<40 or self.sub2<40 or self.sub3<40:
				self.grade='Fail'
		elif  self.average>=(70/100)*300:
				self.grade='Distinction'
		elif  self.average>=(60/100)*300:
				self.grade='First class'
		elif  self.average>=(50/100)*300:
				self.grade='Second class'
		else:
			self.grade='Third class'	
	def  disp(self):
		print('Roll  Number  :  ' ,self.rollnum)
		print('Student  Name  :  ' ,self.student_name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total_marks)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return f'{self.rollnum}  {self.student_name}  {self.gender}  { self.total_marks}  {self.average}  {self.grade}'
#End  of  the  class
s=Student()
s.get()
s.compute()
s.disp()
print(s)