A) Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
            self.a = float(input("Enter side a: "))
            self.b = float(input("Enter side b: "))
            self.c = float(input("Enter side c: "))# How  to  read  three  sides  into  object  
	def  test(self):
	
        if (self.a + self.b > self.c and
            self.b + self.c > self.a and
            self.c + self.a > self.b):
            return True
        else:
            print("Not a triangle")
            return False 

	def  area(self):
		s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))#return   area  of  triangle
	def  peri(self):
		return self.a + self.b + self.c	#return  perimeter  of  triangle
# End of the class
t = Triangle() # How  to  create  triangle  class  object
t.get() # How  to  read  inputs into  object
if t.test(): # How  to  test  whether  inputs  are  valid
print("Area :", t.area())
print('Perimeter : ', t.peri())

B) outputs 
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)#10
		print(self . x)#20
		x += 5
		self . x += 7#27
	def   m2(self):
		print(x)#Error because it is not valid
		print(self . x)#27
		self . x += 6#33
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)#33
print(self . x)
print(x)

C) Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x = int(input("Enter value of x: "))
       	 	self.y = int(input("Enter value of y: "))
        	self.z = int(input("Enter value of z: ")) # How  to  read  inputs  into  variables  x , y  and  z  
	def   add(self , m , n):
		 self.x = m.x + n.x
                 self.y = m.y + n.y
                 self.z = m.z + n.z # How  to  add  objects  m  and  n  and  store  results  in  object 
	def  disp(self):
		  print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z) # How  to  print  object  
# End  of  the  class
a = Test()
b = Test()
c = Test()# How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() # How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get() # How  to  read  inputs  into  object  'b'
c.add(a, b) # How  to  add objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp() # How  to  print  object  'c'

D) outputs 
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # Type and address 


E) outputs 
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
print(a)#Type and address of obj a
print(b)#Type and address of obj b
print(c)#Type and address of obj c
print(d)#Type and address of obj d
print(b . _str_())#35
print(c . _str_())#Hyd
print(d . _str_(50))#None

F) Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		 self.roll = int(input("Enter Roll Number: "))# How  to  read  roll  number  
		 self.name = input("Enter Student Name: ") # How  to  read  student  name  
		 self.gender = input("Enter Gender: ") # How  to  read  gender  
		 self.m1 = int(input("Enter marks of Subject 1: "))
        	 self.m2 = int(input("Enter marks of Subject 2: "))
        	 self.m3 = int(input("Enter marks of Subject 3: "))#How  to  read  marks  of  3  subjects
	def   compute(self):
		self.total = self.m1 + self.m2 + self.m3 # How  to  calculate  total  marks
		self.avg = self.total / 3 # How  to  calculate  average  marks

		if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
				self.grade = 'Fail' # How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70%:
				self.grade = 'Distinction' #How  to  initilaize  grade  to  'Distinction'
		elif  self.avg >= 60%:
				self.grade = 'First class'  How  to  initilaize  grade  to  'First  class'
		elif  self.avg >= 50%:
				self.grade = 'Second class' # How  to  initilaize  grade  to  'Second  class'
		else:
				self.grade = 'Third class' # How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		 print("Roll Number :", self.roll)
        	 print("Student Name :", self.name)
        	 print("Gender :", self.gender)
        	 print("Total Marks :", self.total)
        	 print("Average :", self.avg)
        	 print("Grade :", self.grade)
        def __str__(self):
        return (f"Roll Number: {self.roll}, "
                f"Name: {self.name}, "
                f"Gender: {self.gender}, "
                f"Total: {self.total}, "
                f"Average: {self.avg}, "
                f"Grade: {self.grade}") # return  All  the   values  of  object  in  the  form  of  string
#End  of  the  class
s = Student() #How  to  create  Student  class  object
s.get() #How  to  read  inputs  into  object
s.compute() #How  to  store  results  in  object
s.disp() #How  to  print  object  with  disp()  method
print(s) #How  to  print  object  with  _str_()  method


