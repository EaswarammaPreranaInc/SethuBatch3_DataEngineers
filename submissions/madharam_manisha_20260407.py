'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object
     self.a = float(input("Enter side a: "))
     self.b = float(input("Enter side b: "))
     self.c = float(input("Enter side c: "))  
	def  test(self):
		if  sum  of  every  2  sides  >=  3rd  side:
			Do  nothing
		    else:
			    print('Not  a  triangle')
			exit()#How  to  stop  execution
	def  area(self):
			return   area  of  triangle
	def  peri(self):
			return  perimeter  of  triangle
# End of the class
t = triangle()#How  to  create  triangle  class  object
t.get()#How  to  read  inputs  into  object
t.test()#How  to  test  whether  inputs  are  valid
print('Area : ', t.area())
print('Perimeter : ', t.peri())

#========================================================================================================
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

10
20
#========================================================================================================
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 #How  to  read  inputs  into  variables  x , y  and  z 
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: ")) 
	def   add(self , m , n):
		 #How  to  add  objects  m  and  n  and  store  results  in  object 
		 self.x = m.x + n.x
         self.y = m.y + n.y
         self.z = m.z + n.z
	def  disp(self):
		#How  to  print  object  
		print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)
# End  of  the  class
a = Test()
b = Test()
c = Test()#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get()#How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()#How  to  read  inputs  into  object  'b'
c.add(a, b)#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()#How  to  print  object  'c'
#========================================================================================================
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)

<__main__.Date object at 0xXXXXXXXX>
#====================================================================================================================
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
print(a)
print(b)
print(c)
print(d)
print(b . __str__())
print(c . __str__())
print(d . __str__(50))
	
25
#===============================================================================================================
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		'''How  to  read  roll  number  
		How  to  read  student  name  
		How  to  read  gender  
		How  to  read  marks  of  3  subjects'''
		self.roll = int(input("Enter Roll Number: "))
        self.name = input("Enter Student Name: ")
        self.gender = input("Enter Gender: ")
        self.m1 = int(input("Enter marks of Subject 1: "))
        self.m2 = int(input("Enter marks of Subject 2: "))
        self.m3 = int(input("Enter marks of Subject 3: "))
	def   compute(self):
		self.total = self.m1 + self.m2 + self.m3   #How  to  calculate  total  marks
		self.avg = self.total / 3      #How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
			self.grade = "Fail"#How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
			self.grade = "Distinction"#How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
			self.grade = "First class"#How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
			self.grade = "Second class"#How  to  initilaize  grade  to  'Second  class'
		else:
			self.grade = "Third class"#How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.roll)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return  (f"Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.avg}, Grade: {self.grade}")#All  the   values  of  object  in  the  form  of  string
#End  of  the  class
s = Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
print("\nUsing disp() method:")
s.disp()#How  to  print  object  with  disp()  method
print("\nUsing __str__():")
print(s)#How  to  print  object  with  __str__()  method

	
	
	    
	