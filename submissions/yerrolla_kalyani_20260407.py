'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input("Enter side1:"))
		self.b=int(input("Enter side2:"))
		self.c=int(input("Enter side3:"))
			#How  to  read  three  sides  into  object  
	def  test(self):
		if   self.a+self.b>=self.c and self.a+self.c>=self.b  and self.c+self.b>=self.a:  #of  every  2  sides  >=  3rd  side:
				pass
		else:
				print('Not  a  triangle')
				exit() #How  to  stop  execution
	def  area(self):
			s=(self.a+self.b+self.c)/2
			return  math.sqrt(s * (s - self.a) * (s -self. b) * (s - self.c)) #area  of  triangle
	def  peri(self):
			return self.a+self.b+self.c  #perimeter  of  triangle
# End of the class
obj=triangle()#How  to  create  triangle  class  object
obj.get()#How  to  read  inputs  into  object
obj.test()#How  to  test  whether  inputs  are  valid
print('Area : ',   obj.area())
print('Perimeter : ', obj.peri() )



# Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5#15
		self . x += 7#27
	def   m2(self):
		print(x)#no GV x in program so error 
		print(self . x)#27
		self . x += 6#33
# End  of  the  class
a = c1()
a . m1()#10<nxt>20
a . m2()#27
print(a . x)#33
print(self . x)#error because outside the class  we have to use the object_name  and self only inside the object. 
print(x)#no GV x in program so error
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input("Enter value of x:"))
		self.y=int(input("Enter value of y:"))#How  to  read  inputs  into  variables  x , y  and  z  
		self.z=int(input("Enter value of z:"))
	def   add(self , m , n):
		self.x=m.x+n.x#How  to  add  objects  m  and  n  and  store  results  in  object 
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		print(f"x={self.x}")#How  to  print  object  
		print(f"y={self.y}")
		print(f"z={self.z}")
# End  of  the  class
a=Test()#How  to  create  three  Test  class  objects  a , b  and  c
b=Test()
c=Test()
print("First obj ")
a.get()#How  to  read  inputs  into  object  'a'
print("second obj ")
b.get()#How  to  read  inputs  into  object  'b'
c=Test()#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)
print('Addition  results')
c.disp()#How  to  print  object  'c'


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#<type and address >##<'__main__.Date' at hexa_decimal address>

#  Object  'a'  --->object creation a for class Date ie object_name
#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')#return None if not return anything
class   c4:
	def  __str__(self , x):
			return   F'{x}'
end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)#'25'
print(b)#error typeerror '__str__()'returned on string 
print(c)#Hyd<nxt>error typeerror '__str__()'returned on string
print(d)#error not passing x  value to the the method x value is missing 
print(b . __str__())#35
print(c . __str__())#Hyd<nxt>None(none type object here None )
print(d . __str__(50))#"50"
'''
# Write  a  program  to  determine  total , average  and  grade  of  a  student
# Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
# '''
class   Student:
	def   get(self):
		self.rno=int(input("enter aroll number:"))#How  to  read  roll  number  
		self.sname=(input("enter student name:"))#How  to  read  student  name  
		self.gender=(input("enter gender(m/f):"))#How  to  read  gender  
		self.m=[]
		for x in range(3):
			self.mi=int(input("Enter marks of subject i:"))#How  to  read  marks  of  3  subjects
			(self.m).append(self.mi)
	def   compute(self):
		self.tot=sum(self.m)#How  to  calculate  total  marks
		self.avg=self.tot/len(self.m)#How  to  calculate  average  marks
		if  any(mi<40 for mi in self.m):
				self.grade='Fail'#How  to  initilaize  grade  to  'Fail'
		elif  self.avg  >= 70 :
				self.grade="distinction"#How  to  initilaize  grade  to  'Distinction'
		elif  self.avg>= 60:
				self.grade="first class"#How  to  initilaize  grade  to  'First  class'
		elif self.avg  >= 50:
				self.grade="second class"#How  to  initilaize  grade  to  'Second  class'
		else:
				print("Third class")#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' , self.rno)
		print('Student  Name  :  ' ,self.sname )
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  f"Roll Number: {self.rno}\n Name: {self.sname}\n Gender: {self.gender}\n Total: {self.tot}\n Average: {self.avg} \nGrade: {self.grade}"
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#How  to  print  object  with  disp()  method
print(s)#How  to  print  object  with  _str_()  method



# Object  's'  --->object of class Student