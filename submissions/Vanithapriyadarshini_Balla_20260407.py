#Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
import  math
class  triangle:
	def  get(self):
		t.a=eval(input("Enter a value : "))
		t.b=eval(input("Enter b value : "))  
		t.c=eval(input("Enter c value : "))
	def  test(self):
		if  t.a+t.b > t.c and t.b+t.c >t.a and t.c+t.a>t.b:
				pass
		else:
				print('Not  a  triangle')
		exit()
	def  area(self):
			s=(t.a+t.b+t.c)/2
			return   math.sqrt(s*(s-t.a)*(s-t.b)*(s-t.c))
	def  peri(self):
			return  float(t.a+t.b+t.c)
# End of the class
t=triangle()
t.get()
t.test()
print('Area : ',   t.area())
print('Perimeter : ',  t.peri())

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
		#print(x)# error
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()# 10 20 
a . m2()# 27
print(a . x)# 33
#print(self . x) # error bcz no self 
# print(x) errror, bcz no x 

#Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
#store  results  in   third  object
class  Test:
	def   get(self):
		self.x=eval(input("Enter x value of obj a : "))  
		self.y=eval(input("Enter y value of obj a : ")) 
		self.z=eval(input("Enter z value of obj a : ")) 
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		 print(f' x : {c.x} , y : {c.y} , z : {c.z}')  
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
print(a)# type and address
#  Object  'a'  ---> dd=15,mm=8,yy=1947

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
print(a)# 25
#print(b)# Error
#print(c)# Hyd, Error
#print(d)# Error
print(b . __str__())# 35
print(c . __str__())# Hyd None
print(d . __str__(50))# 50

# Write  a  program  to  determine  total , average  and  grade  of  a  student
#Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class   Student:
	def   get(self):
		self.rno=int(input("Enter roll number : "))  
		self.sname=input("Enter name : ") 
		self.gender=input("Enter 'M' or 'F' : ")  
		self.marks=eval(input("Enter marks in list : "))
	def   compute(self):
		self.tot=sum(self.marks)
		self.average=round(self.tot/len(self.marks),2)
		if  self.marks[0]< 40 or self.marks[1]<40 or self.marks[2]<40:
			self.grade='Fail'
		elif  self.average >= 70:
			self.grade='Distinct'
		elif  self.average >= 60:
			self.grade='First  class'
		elif  self.average >= 50:
			self.grade='Second  class'
		else:
			self.grade='Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.average)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f' rno :{self.rno},sname=:{self.sname},gender:{self.gender},Total marks:{self.tot},Average marks:{self.average},Grade:{self.grade}'
#End  of  the  class
s=Student()
s.get()
s.compute()
s.disp()
print(s.__str__())

