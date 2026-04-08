'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input('enter first side of triangle'))
		self.b=int(input('enter second side of triangle'))
		self.c=int(input('enter third side of triangle'))	  
	def  test(self):
		if  self.a+self.b>self.c and self.b+self.c>=self.a and self.a+self.c>=self.a:
				pass				
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
			self.s=self.peri()/2
			return   math.sqrt((self.s)*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
	def  peri(self):
			return  self.a+self.b+self.c
# End of the class
t=triangle()
t.get()
t.test()
print('Area : ',   t.area())
print('Perimeter : ',  t.peri())




#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):  #self is a
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
a = c1()  #creates c1 class object
a . m1()  
'''
10
20
'''
a . m2()
'''
error
27
'''
print(a . x)  #33  
print(self . x)  #error
print(x)  #error

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x=int(input('Enter values of x '))
		self.y=int(input('Enter values of y '))
		self.z =int(input('Enter values of z ')) 
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		print('x=',self.x)
		print('y=',self.y)
		print('z=',self.z)
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
print(a) #Type and address



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
print(a)  #'25'
print(b)  #error-implicit call raises error for non str
print(c)  #Hyd
#error-None is not str
print(d)  #error missing argument
print(b . __str__())  #35
print(c . __str__())  #None
print(d . __str__(50))  #'50'


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno=int(input('Enter roll number'))  
		self.sname=input('Enter Student name')  
		self.gender=input('Enter gender(m/f)')
		self.m=[]
		self.m.append(int(input('Enter marks of subject 1 ')))
		self.m.append(eval(input('Enter marks of subject 2 ')))
		self.m.append(eval(input('Enter marks of subject 3 ')))
	def   compute(self):
		self.tot=sum(self.m)
		self.avg=sum(self.m)/3
		if  min(self.m)<40:
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
		print('Roll  Number  :  ' ,  self.rno)
		print('Student  Name  :  ' , self.sname)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tot)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  F'{self.rno} {self.sname} {self.gender} {self.tot} {self.avg:.2f} {self.grade}'
#End  of  the  class
s=Student()
s.get()
s.compute()
s.disp()
print(s.__str__())


