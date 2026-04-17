
#Home  work
'''
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import math
class triangle:
    def  get(self):
        self.a = int(input('Enter First Side : ')) # How  to  read  inputs  into  object
        self.b = int(input('Enter Second Side : '))
        self.c = int(input('Enter Third Side : '))
    def  test(self):
        if self.a>0 and self.b>0 and self.c>0 and (self.a+self.b >= self.c) and (self.b+self.c >= self.a) and (self.c+self.a >= self.b):
            pass # sum  of  every  2  sides  >=  3rd  side:
        else:
            print('Not  a  triangle')
            exit()
    def  area(self):
        s = (self.a+self.b+self.c)/2
        return f'{(math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))):.1f}'
    def  peri(self):
        return  f'{(self.a+self.b+self.c):.1f}'
# End of the class
t = triangle() # How  to  create  triangle  class  object
t.get() 
t.test()       # How  to  test  whether  inputs  are  valid
print('Area : ',t.area())
print('Perimeter : ',t.peri())




#Find  outputs  (Home  work)
class c1:
    def m1(self):
        x = 10
        self . x = 20   # {x=20}
        print(x)        # 10
        print(self . x) # 20
        x += 5
        self . x += 7   # 27
    def m2(self):
        print(x)        # Error
        print(self . x) # 27
        self . x += 6   # 33
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x)    # 33
print(self . x) # Error
print(x)        # Error



#Home  work)
'''  
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class test:
    def get(self):
        self.x = int(input('Enter value of x : '))
        self.y = int(input('Enter value of y : '))
        self.z = int(input('Enter value of z : '))
    def add(self , m , n):
        return m+n # How  to  add  objects  m  and  n  and  store  results  in  object 
    def  disp(self):
        return f'x={self.x}\ny={self.y}\nz={self.z}' 
# End  of  the  class

a = test() # How  to  create  three  Test  class  objects  a , b  and  c
b = test()
c = test()
print('First  Object')
a.get()
print('Second  Object')
b.get()
c.x = c.add(a.x,b.x)
c.y = c.add(a.y,b.y)
c.z = c.add(a.z,b.z)  # How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
print(c.disp())



#Find  outputs (Home  work)
class Date:
    pass
# End of the class

a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # <__main__.Date object at 0x0000022720EA86E0>



#Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd') # Hyd
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # <__main__.c1 object at 0x0000025BA21586E0>
print(b) # <__main__.c2 object at 0x0000025BA21586E0>
print(c) # <__main__.c3 object at 0x0000025BA21586E0>
print(d) # <__main__.c4 object at 0x0000025BA21586E0>
print(b . _str_())   # 35
print(c . _str_())   # None
print(d . _str_(50)) # 50



#Home Work
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   student:
	def   get(self):
		self.rol = int(input('Enter roll number : '))     # How  to  read  roll  number  
		self.name = input('Enter student name : ')        #How  to  read  student  name  
		self.gender = input('Enter Gender(m/f): ')        #How  to  read  gender  
		self.sub1 = int(input('Enter marks of sub1 : '))  #How  to  read  marks  of  3  subjects
		self.sub2 = int(input('Enter marks of sub2 : '))
		self.sub3 = int(input('Enter marks of sub3 : '))
	def   compute(self):
		self.total = self.sub1+self.sub2+self.sub3  # How  to  calculate  total  marks
		self.avg = self.total/3 # How  to  calculate  average  marks
		if  self.sub1 < 40 or self.sub2 < 40 or self.sub3 < 40:   # At  least  one  subject  is  below  40
				self.results = 'Fail'                        # How  to  initilaize  grade  to  'Fail'
		elif  self.avg >= 70:                                # average  is  above  >= 70%:
				self.results = 'Distinction'                 # How  to  initilaize  grade  to  'Distinction'
		elif  self.avg >= 60:
				self.results = 'First  class'                # How  to  initilaize  grade  to  'First  class'
		elif  self.avg >= 50:
				self.results = 'Second  class'               # How  to  initilaize  grade  to  'Second  class'
		else:
				self.results = 'Third  class'                # How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,self.rol)
		print('Student  Name  :  ' , self.name)
		print('Gender  :  ' ,  self.gender)
		print('Total  Marks  :  ' , self.total)
		print('Average  :  ' , self.avg)
		print('Grade  :  ' , self.results)
	def   __str__(self):
		return  f'{self.rol}\t{self.name}\t{self.gender}\t{self.total}\t{self.avg}\t{self.results}'
#End  of  the  class
s = student()       # How  to  create  Student  class  object
s.get()             # How  to  read  inputs  into  object
s.compute()         # How  to  store  results  in  object
s.disp()            # How  to  print  object  with  disp()  method
print(s)
