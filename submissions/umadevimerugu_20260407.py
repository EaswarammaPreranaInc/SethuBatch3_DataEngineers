'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import math

class triangle:
    def get(self):
        self.a = int(input("Enter a value: "))
        self.b = int(input("Enter b value: "))
        self.c = int(input("Enter c value: "))

    def test(self):
        if (self.a + self.b > self.c and
            self.b + self.c > self.a and
            self.a + self.c > self.b):
            return True
        else:
            print("Not a Triangle")
            return False   # stops further execution

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
            return self.a+self.b+self.c

# Main program


'''
How  to  create  triangle  class  object
How  to  read  inputs  into  object
How  to  test  whether  inputs  are  valid
'''
t=triangle()
t.get()
t.test()
print('Area : ',  t.area() )
print('Perimeter : ',  t.perimeter())

###########################################################################################
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
a . m1()#10 20
a . m2()#error 27 
print(a . x)#error
print(self . x)#error
print(x)#error

###########################################################################################
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class Test:
    def get(self):
        # How to read inputs into variables x, y and z
        self.x = int(input("Enter x value: "))
        self.y = int(input("Enter y value: "))
        self.z = int(input("Enter z value: "))

    def add(self, m, n):
        # How to add objects m and n and store results in object
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)
		#How  to  print  object  
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c
a=Test()
b=Test()
c=Test()
print('First  Object')
#How  to  read  inputs  into  object  'a'
a.get()
print('Second  Object')
b.get()
#How  to  read  inputs  into  object  'b'
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c.add(a,b)
print('Addition  results')
#How  to  print  object  'c'
c.disp()
###########################################################################################
#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#<__main__.Date object at address>

#  Object  'a'  --->
###########################################################################################
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
print(a)#25
print(b)#error
print(c)#error
print(d)#error
print(b . __str__())#35
print(c . __str__())#Hyd None
print(d . __str__(50))#50
###########################################################################################
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		How  to  read  roll  number  
		How  to  read  student  name  
		How  to  read  gender  
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   __str__(self):
		return  All  the   values  of  object  in  the  form  of  string
#End  of  the  class
How  to  create  Student  class  object
How  to  read  inputs  into  object
How  to  store  results  in  object
How  to  print  object  with  disp()  method
How  to  print  object  with  __str__()  method



#  Object  's'  --->
----------------code--------------------------------
class Student:
    def get(self):
        self.rollno = int(input("Enter roll number: "))
        self.name = input("Enter the name: ")
        self.gender = input("Enter the gender (m/f): ")
        self.sub1 = int(input("Enter marks of 1st subject: "))
        self.sub2 = int(input("Enter marks of 2nd subject: "))
        self.sub3 = int(input("Enter marks of 3rd subject: "))

    def compute(self):
        self.total = self.sub1 + self.sub2 + self.sub3
        self.avg = self.total / 3

        if self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:
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
        print("Roll Number :", self.rollno)
        print("Student Name :", self.name)
        print("Gender :", self.gender)
        print("Total Marks :", self.total)
        print("Average :", self.avg)
        print("Grade :", self.grade)

    def __str__(self):
        return f"Roll Number: {self.rollno}, Name: {self.name}, Gender: {self.gender}, Total: {self.total}, Average: {self.avg}, Grade: {self.grade}"


# Main Program
s = Student()
s.get()
s.compute()

print("\nUsing disp() method:")
s.disp()

print("\nUsing __str__ method:")
print(s)