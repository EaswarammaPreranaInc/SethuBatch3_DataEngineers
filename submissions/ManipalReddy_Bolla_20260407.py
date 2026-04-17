'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object
1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))
2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2
3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
import sys
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  
		self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
	def  test(self):
		if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass
		 else:
			print('Not  a  triangle')
			sys.exit()
	def  area(self):
			s=(self.a+self.b+self.c)/2
			res=math.sqrt(s*(s-self.a)*(s-self.b)(s-self.c))
			return res
	def  peri(self):
			peri=self.a+self.b+self.c
			return peri
# End of the class
#How  to  create  triangle  class  object
t=triangle()
#How  to  read  inputs  into  object
t1.get()
#How  to  test  whether  inputs  are  valid
t1.test()
print('Area : ',t1.area)
print('Perimeter : ',t1.peri)


'''
output
Enter side a: 3
Enter side b: 4
Enter side c: 5
Area :  6.0
Perimeter :  12.0
Enter side a: 3
Enter side b: 4
Enter side c: 8
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
		#print(x)
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()#10 <nextline> 20
a . m2()#error comment print(x) in m2() then ot prints 27
print(a . x)#33
print(self . x)#self cannot be identified outside of class
print(x)#error x is not defined outside class i.e globally 




'''
 (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		self.x = int(input("Enter side x: "))
		self.y = int(input("Enter side y: "))
		self.z = int(input("Enter side z: "))
	def   add(self , m , n):
		#How  to  add  objects  m  and  n  and  store  results  in  object
		self.x = m.x + n.x
		self.y = m.y + n.y
		self.z = m.z + n.z
	def  disp(self):
		#How  to  print  object
		print('x=',self.x)
		print('y=',self.y)
		print('z=',self.z)
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()
print('First  Object')
#How  to  read  inputs  into  object  'a'
a.get()
print('Second  Object')
#How  to  read  inputs  into  object  'b'
b.get()
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)
print('Addition  results')
#How  to  print  object  'c'
c.disp()


'''
output
First  Object
Enter side x: 10
Enter side y: 20
Enter side z: 30
Second  Object
Enter side x: 40
Enter side y: 50
Enter side z: 60
Addition  results
x= 50
y= 70
z= 90
'''


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#type and address




#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'#
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
print(a)#'25'
print(b)#error
print(c)#'Hyd' error Nonetype object is returned
print(d)#error
print(b . __str__())#35
print(c . __str__())#Hyd <nextline> None
print(d . __str__(50))#50




'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rno=int(input("Enter roll no : "))#How  to  read  roll  number  
		self.name=input('Enter Name: ')#How  to  read  student  name  
		self.gender=input('Enter gender(m/f) : ')#How  to  read  gender  
		self.marks=[0,0,0]
		self.marks[0]=int(input("Enter marks of subject 1: "))
		self.marks[1]=int(input("Enter marks of subject 2: "))
		self.marks[2]=int(input("Enter marks of subject 3: "))
		#aHow  to  read  marks  of  3  subjects
	def   compute(self):
		self.tol=sum(self.marks)#How  to  calculate  total  marks
		self.avg=sum(self.marks)/3#How  to  calculate  average  marks
		if   self.marks[0] < 40 or self.marks[1] < 40 or self.marks[2] < 40 :
			self.grade = 'Fail'
		elif  (self.tol/300)*100 >= 70 :
			self.grade = 'DIstinction'
		elif  (self.tol/300) >= 60:
				self.grade = 'First  class'
		elif  (self.tol/300)>= 50:
				self.grade =  'Second  class'
		else:
				self.grade = 'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  self.rno)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.tol)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.grade)
	def   __str__(self):
		return f'{self.rno} \t {self.name} \t {self.gender} \t {self.tol} \t {self.avg} \t {self.grade} ' 
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#How  to  print  object  with  disp()  method
print(s.__str__())#How  to  print  object  with  __str__()  method










