'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
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


import  math
class  triangle:
	def  get(self):
		self.x = int(input('Enter x'))  
		self.y = int(input('Enter y')) 
		self.z = int(input('Enter z')) 
	def  test(self):
		if  self.x + self.y > self.z and self.x + self.z > self.y and self.z + self.y > self.x:
			pass
		 else:
				print('Not  a  triangle')
				exit
	def  area(self):
			 s = (self.x + self.y + self.z)/2
			return   sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))
	def  peri(self):
			return  self.x + self.y + self.z

#t =  triangle()
#t.get()
#t.test()
#print(t.area())
#print(t.peri())

# input as float is recomended
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
		print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
print(self . x)
print(x)

#10
#20
#Error
#27
#33
#Error
#Error




 '''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
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


class  Test:
	def   get(self):
		 self.x = int(input('Enter x'))  
		self.y = int(input('Enter y')) 
		self.z = int(input('Enter z')) 
	def   add(self , m , n):
		 self.x = m.x + n.x 
		 self.y = m.y + n.y 
		 self.z = m.z + n.z 

	def  disp(self):
		 print(self.x)
		 print(self.y)
		 print(self.z)
		
		

a = Test()
b=Test()
c=Test()
print(a)
a.get()
print(b)
b.get()
c=Test()
c.add(a,b)
c.disp()


 #  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)

#  Object  'a'  --->

#<__main__.Date object at Address>



 '''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno = int(input('Enter roll no'))
		self. name = input('Enter name')
		print(Enter marks in 3 subjects')
		self.marks[0] = int(input('Enter m1 marks'))
		self.marks[1] = int(input('Enter m2 marks'))
		self.marks[2] = int(input('Enter m3 marks'))
		self.gender = input('Enter gendeer')  
	
		def   compute(self):
		self.total =self.sum(marks)
		self.avg = self.total/3
		if any(mark in marks if mark<40) :
				self.grade = 'Fail'
		elif  self.avg  >= 70:
				self.grade = 'Distinction'
		elif self.avg  >= 60%:
				self.grade ='First  class'
		elif  self.avg  >= 50%:
		elif  average  is  above  >= 50%:
				self.grade ='Second  class'
		else:
				self.grade ='Third  class'
	       def  disp(self):
			print('Roll  Number  :  ' ,   self.rno)
			print('Student  Name  :  ' , self. name)
			print('Gender  :  ' ,  self.gender)
			print('Total  Marks  :  ' , self.total)
			print('Average  :  ' ,self.avg)
			print('Grade  :  ' , self.grade)
	def   _str_(self):
		return  f'{self.rno}:{self. name}:{self.gender}:{self.marks}:{self.total}:{self.avg }:{self.grade }}'
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  _str_()  method

#s =Student()
s.get()
a.disp()
print(a._str_())



#  Object  's'  --->		rno, sname,marks,gender,total,avg,grade



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
print(a)
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))

#25
#Error
#Hyd
#Error
#TYpe and address
#35
#Hyd
#None
#50
