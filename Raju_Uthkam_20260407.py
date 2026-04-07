'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
            self.a = float(input('Enter 1st side : '))
            self.b = float(input('Enter 2nd side : '))
            self.c = float(input('Enter 3rd side : '))
            
        
	def  test(self):
    		if  (self.a + self.b >= self.c) and (self.a + self.c >= self.b) and (self.b + self.c >= self.a) : 
    				pass #Do  nothing
    		else:
    				print('Not  a  triangle')
    				return  #How  to  stop  execution
                
	def  area(self):
            s = (self.a + self.b + self.c) / 2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        
	def  peri(self):
            return  self.a + self.b + self.c 
# End of the class
t = triangle() #How  to  create  triangle  class  object
t.get()  #How  to  read  inputs  into  object
t.test() #How  to  test  whether  inputs  are  valid
print('Area : ', t.area())
print('Perimeter : ', t.peri())



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
#a . m2() #Error there is no varible x in m2() method 
print(a . x) #27
#print(self . x) #Error
#print(x) #Error there is global varible in progam 


'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
    def   get(self):
            self.x = int(input('Enter value of x : '))
            self.y = int(input('Enter value of y : '))
            self.z = int(input('Enter value of z : ')) #How  to  read  inputs  into  variables  x , y  and  z  
    def   add(self , m , n):
        self.x = a.x + b.x
        self.y = a.y + b.y
        self.z = a.z + b.z #How  to  add  objects  m  and  n  and  store  results  in  object 
    def  disp(self):
    	return "x =", self.x, "y =", self.y, "z =", self.z #How  to  print  object   
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c
print('First  Object')
a = Test()
a.get() #How  to  read  inputs  into  object  'a'
print('Second  Object')
b = Test()
b.get() #How  to  read  inputs  into  object  'b'
#How  to  add  objects  a  and  b  and  store  results in  object  'c'
c = Test()
c.add(a,b)
print('Addition  results')
print(c.disp())



#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)


#  Object  'a'  ---> dd = 15, mm = 8 ,yy = 1947



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
#print(b) #Error if you are calling object implicityly the return object must be string 
print(c) #'Hyd'
print(d) #x
print(b . __str__()) #35
print(c . __str__()) #
print(d . __str__(50)) #50



class Student:
    def get(self):
        self.rno = int(input('Enter roll no: '))
        self.sname = input('Enter student name: ')
        self.gender = input('Enter gender(m/f): ')
        self.a = int(input('Enter marks of first subject: '))
        self.b = int(input('Enter marks of second subject: '))
        self.c = int(input('Enter marks of third subject: '))

    def compute(self):
        self.total = self.a + self.b + self.c
        self.avg = self.total / 3

        if self.a < 40 or self.b < 40 or self.c < 40:
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
        print('Roll Number  :', self.rno)
        print('Student Name :', self.sname)
        print('Gender       :', self.gender)
        print('Total Marks  :', self.total)
        print('Average      :', f'{self.avg:.2f}')
        print('Grade        :', self.grade)

    def __str__(self):
        return (f'Roll Number: {self.rno}, '
                f'Student Name: {self.sname}, '
                f'Gender: {self.gender}, '
                f'Total Marks: {self.total}, '
                f'Average: {self.avg:.2f}, '
                f'Grade: {self.grade}')


# Main program
s = Student()
s.get()
s.compute()       # compute total, average, grade
s.disp()          # display nicely
print(s)          # print string representation



