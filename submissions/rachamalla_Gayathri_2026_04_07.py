 Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=float(input("enter side a:"))
                self.b=float(input("enter side b:"))
                self.c=float(input("enter side c:")) 
	def  test(self):
		if  (self.a +self.b >self.c and self.a+self.c>self.b and self.b+self.c>self.a):
                      pass
		else:
			print('Not  a  triangle')
		        exit()
	def  area(self):
			s=(self.a+self.b+self.c)/2
                        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
			return self.a+self.b+self.c
# End of the class
t=Triangle
print("area=",t.area())
print("perimeter=",t.peri())
 #  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) #10
		print(self . x)#20
		x += 5 #15
		self . x += 7#17
	def   m2(self):
		print(x)#error no variable
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()#error
print(a . x)#10
print(self . x)
print(x)
 (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x=int(input("enter x:"))
                 self.y=int(input("enter y:"))
                 self.z=int(input("enter z:"))
	def   add(self , m , n):
		 self.x=m.x+n.x
                 self.y=m.y+n.y
                 self.z=m.z+n.z
	def  disp(self):
		 print("x=",self.x,"y=",self.y,"z=",self.z)
# End  of  the  class
How  to  create  three  Test  class  objects  a , b  and  c
a=test()
b=test()
c=test()
print('First  Object')
How  to  read  inputs  into  object  'a'
print('Second  Object')
How  to  read  inputs  into  object  'b'
How  to  add…
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
print(a) #address



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
a = c1()# 25
b = c2()#not str
c = c3()#hyd
d = c4()#error
print(a)#25
print(b)
print(c)
print(d)
print(b . _str_())
print(c . _str_())
print(d . _str_(50))
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		How  to  read  roll  number  
                 self.roll=int(input("enter roll n0:"))
		How  to  read  student  name 
                 self.name=int(input("enter name")) 
		How  to  read  gender 
                 self.gender=input("enter gender:")) 
		How  to  read  marks  of  3  subjects
                self.m1=int(input("enter marks1:"))
                self.m2=int(input("enter marks2:"))
                self.m3=int(input("enter marks3:"))
	def   compute(self):
		How  to  calculate  total  marks
                self.total=self.m1+self.m2+self.m3
		How  to  calculate  average  marks
                self.avg=self.total/3
		if  self.m1<40 or self.m2<40 or self.m3<40:
                      self.grade="fail"
                
				How  to  initilaize  grade  to  'Fail'
		elif self.avg>=70%:
                         self.grade="distinction"
     def disp(self):
               print("roll",self.roll)
               print("name:",self.name)