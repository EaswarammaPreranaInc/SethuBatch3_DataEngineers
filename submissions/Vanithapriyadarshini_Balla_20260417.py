# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x)# 30
print(a . y)# 20
print(b . x)# 30
print(b . y)# 20
print(c1 . x , c1 . y)# 30 40
#print(cls . x , cls . y)# error
#print(self . x , self . y)# error'''


'''
static   variable   ---> x=30, y=40

object  'a'   ---> y=20 , 

object  'b'   ---> y=20 , 
'''


#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()# static method
a = c1()
a . m1()# static method
#c1 . m1(25)# Error

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)# 25
a = c1()
a . m1(35)# 35
#a . m1()# Error

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)# static method #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
a = c1()
a . m1()  #instance method and error #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
#a . m1(35)  # Error # What  about  here

#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() # static method
a = c1()
#a . m1()#Error

#  Find  outputs
class   c1:
	@staticmethod
	def  m1(self):
		print('static  method')
		print(self)
	def  m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25)# static /instance method 25
a = c1()
a . m1()# static /instance method    address

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x)
		print(c1.x)
		#print(x)
	def   m1(self):
		print(self.x)
		print(c1.x)
		#print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x)
		print(c1.x)
		#print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x)
ob=c1()
ob.x
#print(x)
#print(self . x)
#print(cls . x)
ob.m1()
c1.m2()
c1.m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.x=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60 #How  to  add  static  variable  'f'  with  value  60
		c1.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		##cls . k = 35
#End  of  the  class
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)
print()
print()
x.m1()
print('Instance  method  m1')
print(c1 . __dict__)
print()
print()
c1.m2()
print('class  method   m2')
print(c1 .__dict__)
print()
print()
c1.m2()
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'
print(c1 . __dict__) # {'a':1,'b':2,'c':3, envrm var's}

# Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()
b . compute()
c . compute()
a . disp()# 13 21 31 12
b . disp()# 13 41 51 13
c . disp()# 13 61 71 14




# Write  a  program  to  add  two  Vector  objects

class  vector:
	@staticmethod
	def get1():
		vector.n=int(input("Enter how many elements  : ")) #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		l=[]
		for i in range(vector.n):
			l.append(int(input("Enter value : ")))
		self.a=l
	def add(self, x, y):
		self.c = []   # create empty list
		for i in range(vector.n):
			self.c.append(x.a[i] + y.a[i])  #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() #How  to  call  get1()  method
x=vector()
x.get2()
y=vector()
y.get2()
z=vector() 
z.add(x,y) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print('results :' , z.c) #How  to  print  the  list  of  3rd   object

#Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

# Hint:  Use  startswith()  and  endswith()  methods

class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
l={}
for k,v in c1.__dict__.items():
	if k.startswith('__') and k.endswith('__'):
		pass
	else:
		l[k]=v
print(l)

# Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

class Emp:
    def __init__(self):
        self.EmpNo=int(input("Enter empno : "))
        self.Ename=input("Enter ename : ")
        self.sal=float(input("Enter salary : "))
    @property
    def EmpNo(self):
        return self._EmpNo
    @EmpNo.setter
    def EmpNo(self,y):
        if y>0:
            self._EmpNo=y
        else:
            raise ValueError("EmpNO can't be negative")
    @property
    def Ename(self):
        return self._Ename
    @Ename.setter
    def Ename(self,name):
        if name.isalpha() and name!='':
            self._Ename=name
        else:
            raise ValueError("Invalid Ename")
    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self,s):
        if s>0:
            self._sal=s
        else:
            raise ValueError("sal can't be negative")
try:
    e=Emp()
    print(e.EmpNo)
    print(e.Ename)
    print(e.sal)
except ValueError as v:
    print(v)


    


		