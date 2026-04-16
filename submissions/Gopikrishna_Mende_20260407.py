'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import math

class triangle:
    
    def get(self):
        self.a = float(input('Enter side a : '))
        self.b = float(input('Enter side b : '))
        self.c = float(input('Enter side c : '))
    
    def test(self):
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.c + self.a > self.b):
            return True
        else:
            print('Not a triangle')
            return False
    
    def area(self):
        self.s = (self.a + self.b + self.c) / 2
        return math.sqrt(self.s * (self.s - self.a) * (self.s - self.b) * (self.s - self.c))
    
    def peri(self):
        return self.a + self.b + self.c


# End of the class
t = triangle()
t.get()

if t.test():
    print('Area : ', t.area())
    print('Perimeter : ', t.peri())

# ==========================================================================

#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) #20
		x += 5
		self . x += 7 
	def   m2(self):
		print(x) #Error
		print(self . x) #27
		self . x += 6 
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # 33
print(self . x) #Error
print(x) #Error

# ==========================================================================

'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		#  How  to  read  inputs  into  variables  x , y  and  z 
            self.x = float(input('Enter x : '))
            self.y = float(input('Enter y : ')) 
            self.z = float(input('Enter z : '))
	def   add(self , m , n):
        #  How  to  add  objects  m  and  n  and  store  results in  object  'self'
            self.x = m.x + n.x
            self.y = m.y + n.y
            self.z = m.z + n.z
	def  disp(self):
		#  How  to  print  object  
          print(f'x : {self.x} , y : {self.y} , z : {self.z}')

# End  of  the  class
# How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()  
c = Test()

print('First  Object')
# How  to  read  inputs  into  object  'a'
a.get()
print('Second  Object')
# How  to  read  inputs  into  object  'b'
b.get()

# How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)

print('Addition  results')
# How  to  print  object  'c'
c.disp()

# ===========================================================================

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # <__main__.Date object at address>



#  Object  'a'  --->



# ==================================================================

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
print(a) #25
print(b) # Error
print(c) # Error
print(d) #Error
print(b . __str__()) #35
print(c . __str__()) #Hyd
print(d . __str__(50)) # 50


# ==========================================================================

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
from venv import create

class Student:
    
    def get(self):
        # read inputs
        self.roll = input('Enter roll number : ')
        self.name = input('Enter student name : ')
        self.gender = input('Enter gender : ')
        
        self.m1 = float(input('Enter marks of subject 1 : '))
        self.m2 = float(input('Enter marks of subject 2 : '))
        self.m3 = float(input('Enter marks of subject 3 : '))
    
    def compute(self):
        # total and average
        self.total = self.m1 + self.m2 + self.m3
        self.avg = self.total / 3
        
        # grade calculation
        if self.m1 < 40 or self.m2 < 40 or self.m3 < 40:
            self.grade = 'Fail'
        
        elif self.avg >= 70:
            self.grade = 'Distinction'
        
        elif self.avg >= 60:
            self.grade = 'First Class'
        
        elif self.avg >= 50:
            self.grade = 'Second Class'
        
        else:
            self.grade = 'Third Class'
    
    def disp(self):
        print('Roll Number :', self.roll)
        print('Student Name :', self.name)
        print('Gender :', self.gender)
        print('Total Marks :', self.total)
        print('Average :', self.avg)
        print('Grade :', self.grade)
    
    def __str__(self):
        return f'Roll Number: {self.roll}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.avg}, Grade: {self.grade}'



s = Student()
s.get()
s.compute()

s.disp()     
print(s) 