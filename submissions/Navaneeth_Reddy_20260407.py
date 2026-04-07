'''  
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''

import math

class triangle:
    #How  to  read  three  sides  into  object  
    def get(self) :
        self.a = int(input("Enter the 1st side : "))
        self.b = int(input("Enter the 2nd side : "))
        self.c = int(input("Enter the 3rd side : "))
        
    def test(self) :
        if  (self.a + self.b  >=  self.c) and (self.c + self.b  >=  self.a) and (self.a + self.c  >=  self.b) :
         pass
        else:
            print('Not  a  triangle')
            exit()
    
    def area(self) :
        s = (self.a + self.b+ self.c)/2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def peri(self):
        return self.a + self.b + self.c
    
x = triangle()
x.get()
x.test()
print(f'Area : {x.area()}')
print(f'Perimeter : {x.peri()}')

'''
Output :
Enter the 1st side : 5
Enter the 2nd side : 7
Enter the 3rd side : 8
Area : 17.320508075688775
Perimeter : 20
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
		print(x) # Error
		print(self . x)
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)
print(self . x) # Error
print(x) # Error,  as x is local variable to m1

'''
10
20
17
23

'''

'''  
(Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''

class  Test:
	def   get(self):
		return a+b#How  to  read  inputs  into  variables  x , y  and  z  
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		return self
# End  of  the  class
a=Test()
b=Test()
c=Test()#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b.get()#How  to  read  inputs  into  object  'b'
c.x=c.add(a.x,b.x)
c.y=c.add(a.y,b.y)
c.z=c.add(a.z,b.z)
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # type and address

#  Object  'a'  --->  dd = 15,mm = 8, yy = 1947

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
print(a)  # <class '__main__.c1'> and address
print(b) # <class '__main__.c2'> and address
print(c) # <class '__main__.c3'> and address
print(d) # <class '__main__.c4'> and address
print(b . __str__()) #35
print(c . __str__()) # None
print(d . __str__(50)) # '50'

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
		return f'{self.rno}\t{self.name}\t{self.gender}\t{self.tol}\t{self.avg}\t{self.grade} ' 
#End  of  the  class
s=Student()#How  to  create  Student  class  object
s.get()#How  to  read  inputs  into  object
s.compute()#How  to  store  results  in  object
s.disp()#How  to  print  object  with  disp()  method
print(s.__str__())#How  to  print  object  with  __str__()  method

