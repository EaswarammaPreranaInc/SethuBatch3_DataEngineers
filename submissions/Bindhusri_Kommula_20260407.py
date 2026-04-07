'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self): 
                self.a=float(input('Enter first side: '))  
                self.b=float(input('Enter second side: ')) 
                self.c=float(input('Enter third side: '))
	def  test(self):
		if self.a+self.b>self.c and self.b+self.c>self.a and self.a+self.c>self.b:  #if  sum  of  every  2  sides  >=  3rd  side:
		    pass  #Do  nothing
		else:
		    print('Not  a  triangle')
	            break  #How  to  stop  execution
	def  area(self):
                        s=(self.a + self.b + self.c) / 2
			return   math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def  peri(self):
			return  self.a + self.b + self.c
# End of the class
t=triangle()   #How  to  create  triangle  class  object
 
t.get()
if t.test():
    print('Area : ',   ???)
    print('Perimeter : ',  ???)



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
		print(x) # error
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1() 
a . m2()
print(a . x)
print(self . x) # error
print(x) # error

output:
10
20
27
33



'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x=int(input('Enter value of x: '))
                 self.y=int(input('Enter value of y: ')) 
                 self.z=int(input('Enter value of z: '))
	def   add(self , m , n):
		 self.x=m.x+n.y
                 self.y=m.x+n.y
                 self.z=m.x+n.y 
	def  disp(self):
		 print(self.x)
                 print(self.y)
                 print(self.z)  
# End  of  the  class
a=Test()  #How  to  create  three  Test  class  objects  a , b  and  c
b=Test() 
c=Test() 
print('First  Object')
a.get()   #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()   #How  to  read  inputs  into  object  'b'
c.add(a,b)  #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()   #How  to  print  object  'c'



#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # type and add



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
print(a)  # 25
print(b) # error non-string
print(c) # error
print(d)# error
print(b . __str__()) # 35
print(c . __str__()) # Hyd None
print(d . __str__(50)) # 50




'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.roll_num=int(input('Enter Roll Number: '))  #How  to  read  roll  number  
		self.name=input('Enter student name: '))  #How  to  read  student  name  
		self.gender=input('Enter gender (m/f) : '))  #How  to  read  gender  
		self.m1=int(input('Enter marks of subject 1 : '))  #How  to  read  marks  of  3  subjects
                self.m2=int(input('Enter marks of subject 2 : '))
                self.m3=int(input('Enter marks of subject 3 : '))
	def   compute(self):
		total_marks=(self.m1+self.m2+self.m3)  #How  to  calculate  total  marks
		avg_marks=(self.m1+self.m2+self.m3)/3   #How  to  calculate  average  marks
		if  self.m1<40 or self.m2<40 or self.m3<40:
				self.grade='Fail'
		elif  self.avg_marks >= 70:
				self.grade='Distinction'
		elif  self.avg_marks  >= 60:
				self.grade='First  class'
		elif  self.avg_marks  >= 50:
				self.grade='Second  class'
		else:
				self.grade='Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   self.roll_num)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' , self.gender)
		print('Total  Marks  :  ' , self.total_marks)
		print('Average  :  ' , self.avg_marks)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return (f"Roll: {self.roll}, Name: {self.name}, Gender: {self.gender}, "
                f"Total: {self.total}, Average: {self.avg}, Grade: {self.grade}")
#End  of  the  class
s=student()    #How  to  create  Student  class  object
s.get()   #How  to  read  inputs  into  object
s.compute()   #How  to  store  results  in  object
s.disp()  #How  to  print  object  with  disp()  method
print(s)   #How  to  print  object  with  __str__()  method



#  Object  's'  --->




