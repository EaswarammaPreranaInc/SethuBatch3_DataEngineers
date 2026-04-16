'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
	def  get(self):
		#How  to  read  three  sides  into  object  
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))
        
	def  test(self):
		#if  sum  of  every  2  sides  >=  3rd  side: Do  nothing
        if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
            return True 
		 else:
				print('Not  a  triangle')
				return False
	def  area(self):
			area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
            
            return area
	def  peri(self):
			return  self.a + self.b + self.c #perimeter  of  triangle
# End of the class
t=triangle()
t.get()
if t.test():#   How  to  test  whether  inputs  are  valid
print('Area : ',   ???)
print('Perimeter : ',  ???)





#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10     # local variable         
		self . x = 20   # instance variable
		print(x) # 10
		print(self . x) # 20
		x += 5 # local → 15
		self . x += 7 # # instance → 27
	def   m2(self):
		print(x) # error
		print(self . x) # 27
		self . x += 6 # 33
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # 10
print(self . x) # 20
print(x) # err




'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 #How  to  read  inputs  into  variables  x , y  and  z 
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))   
	
    def   add(self , m , n):
		# How  to  add  objects  m  and  n  and  store  results  in  object 
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z
        
	def  disp(self):
		 #How  to  print  object
        print("x =", self.x)
        print("y =", self.y)
        print("z =", self.z)
# End  of  the  class
#How  to  create  three  Test  class  objects  a , b  and  c

a = Test()
b = Test()
c = Test()

print('First  Object')
a.get()   #How  to  read  inputs  into  object  'a'
print('Second  Object')
a.get()          #How  to  read  inputs  into  object  'b'
c.add(a,b)                  #How  to  add  objects  a  and  b  and  store  results in  object  'c'
print('Addition  results')
c.disp()     #How  to  print  object  'c'





#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date() # obj a is created
a . dd = 15  # Attributes are added to object a
a . mm = 8
a . yy = 1947
print(a) # type and Address



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
print(a) # 25
print(b) # error
print(c) # Hyd
print(d)
print(b . __str__())
print(c . __str__())
print(d . __str__(50))




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