#1
'''  
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import math
class triangle:
    def get(self):
        self.x = int(input("first side :"))
        self.y = int(input("second side :"))
        self.z = int(input("third side :"))
    def test(self):
        if self.x+self.y > self.z:
            pass
        else:
            print("Not a triangle")
            exit()
    def area(self):
        s = (self.x+self.y+self.z)/2
        return math.sqrt(s*(s-self.x)*(s-self.y)*(s-self.z))
    def peri(self):
        return self.x+self.y+self.z
    
a = triangle()
a.get()
a.test()
print("Area :",a.area())
print("Perimeter :",a.peri())                
        
'''
Output :
Enter the 1st side : 5
Enter the 2nd side : 7
Enter the 3rd side : 8
Area : 17.320508075688775
Perimeter : 20
'''


#2
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

#3
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
		self.x=int(input("enter value :"))
		self.y=int(input("enter value :"))
		self.z=int(input("enter value :")) 
	def   add(self , m , n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		print(f'x={self.x}')
		print(f'y={self.y}')
		print(f'z={self.z}')
# End  of  the  class
a=Test()
b=Test()
c=Test()
print('first object')
a.get()
print('second object')
b.get()
c.add(a,b)
print('Addition  results')
c.disp()



#4
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

#5
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


#6
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class student:
    def get(self):
        self.rn = int(input("Enter roll no :"))
        self.name = (input("Enter student name :"))
        self.gender = input("gender (m/f) :")
        self.m = []
        self.n = int(input("no of sub :"))
        for i in range(self.n):
            marks = int(input("Enter marks :"))
            self.m.append(marks)
    def compute(self):
        self.tot=sum(self.m)
        self.avg=self.tot/self.n  
        if min(self.m) < 40:
            self.grade = "Fail"
        elif self.avg  >= 70:
            self.grade = "Distinction"         
        elif self.avg >= 60:
            self.grade = "First class"  
        elif self.avg >= 50:
            self.grade = "Second class"
        else:
            self.grade = "Third class"
    def  disp(self):
        print("Roll Number :",self.rn)
        print("Student Nmae :",self.name)
        print("Gender :",self.gender)
        print("Total marks :",self.tot)
        print("Average :",self.avg)
        print("Grade :",self.grade)
    def __str__(self):
        return f'{self.rn}  {self.name} {self.gender}   {self.tot}  {self.avg}  {self.grade}'              

s = student()
s.get()
s.compute()
s.disp()
print(s)    
