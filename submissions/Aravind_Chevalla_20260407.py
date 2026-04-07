'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self,x,y,z):
	    a.x=x
	    a.y=y
	    a.z=z
	def  test(self):
		if  a.x+a.y>a.z and a.y+a.z>a.x and a.x+a.z>a.y:
		    pass
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
	    s=(a.x+a.y+a.z)/2
	    return math.sqrt(s*(s-a.x)*(s-a.y)*(s-a.z))
	def  peri(self,x,y,z):
			return  x+y+z
# End of the class
a=triangle()
x=int(input("Enter a 1st side of triangle: "))
y=int(input("Enter a 2nd side of triangle: "))
z=int(input("Enter a 3rd side of triangle: "))
a.get(x,y,z)
a.test()
print('Area : ', a.area())
print('Perimeter : ',a.peri(x,y,z))


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
a . m1() #10 20
a . m2() #27
print(a . x) #33
print(self . x) #Error
print(x) #Error



'''  (Home  work)
class  Test:
	def   get(self):
	    x=a.x
	    y=a.y
	    z=a.z
	def   add(self):
		 c.x=a.x+b.x
		 c.y=a.y+b.y
		 c.z=a.x+b.z
	def  disp(self):
		 print(f'x={c.x}')
		 print(f'y={c.y}')
		 print(f'z={c.z}')
# End  of  the  class
a=Test()
b=Test()
c=Test()
print('First  Object')
a.x=int(input("Enter 1st number: "))
a.y=int(input("Enter 2nd number: "))
a.z=int(input("Enter 3rd number: "))
print('Second  Object')
b.x=int(input("Enter 1st number: "))
b.y=int(input("Enter 2nd number: "))
b.z=int(input("Enter 3rd number: "))
a.get()
print('Addition  results')
a.add()
a.disp()




# Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) 

#  Object  'a'  --->

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
print(a) #'__main__.c1' and address of c1
print(b) #'__main__.c2' and address of c2
print(c) #'__main__.c3' and address of c3
print(d) #'__main__.c4' and address of c4
print(b . _str_()) # 35
print(c . _str_()) # Hyd None
print(d . _str_(50)) #50


'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		a.r=int(input('Enter a roll number: '))
		a.n=input("Enter student name: ")
		a.g=input("Enter gender (m/f): ")
		a.x=int(input("Enter marks in subject 1: "))
		a.y=int(input("Enter marks in subject 2: "))
		a.z=int(input("Enter marks in subject 3: "))
	def   compute(self):
		a.t=a.x+a.y+a.z
		a.avg=a.t/3
		if  a.x<40 or a.y<40 or a.z<40:
				a.gr="Fail"
		elif  a.avg>= 70:
				a.gr='Distinction'
		elif  a.avg>= 60:
				a.gr='First  class'
		elif  a.avg>= 50:
				a.gr='Second  class'
		else:
				print('Third  class')
	def  disp(self):
		print('Roll  Number  :  ' ,   a.r)
		print('Student  Name  :  ' , a.n)
		print('Gender  :  ' ,  a.g)
		print('Total  Marks  :  ' , a.t)
		print('Average  :  ' , a.avg)
		print('Grade  :  ' ,a.gr )
	def   __str__(self):
		print(f'{a.r}  {a.n}  {a.g}  {a.t}  {a.avg}  {a.gr}')
#End  of  the  class
a=Student()
a.get()
a.compute()
a.disp()
a.__str__()