# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  _init_(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x) # 10
print(a . y) # 20
print(b . x) # 10
print(b . y) # 20
print(c1 . x , c1 . y) # 30 y=40
print(cls . x , cls . y) # error 
print(self . x , self . y) # error


'''
static   variable   --->x=30, y=40

object  'a'   ---> y=20

object  'b'   ---> y=20
'''

#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() # static method
a = c1()
a . m1() # static method
c1 . m1(25) # error

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 25
a . m1() # error

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  static  method 
a = c1()
a . m1()  #   instance  method
a . m1(35)  # What  about  here   static  method 

#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1()  # empty line
a = c1()
a . m1() # empty line

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
c1 . m1(25) 
a = c1()
a . m1()
'''
Static method
25
static / instance  method
a
'''

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		print(c1.x)
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(x) # error ... searches for local variable
	def   m1(self):
		print(c1.x)
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # error
	@classmethod
	def   m2(cls):
		print(c1.x)
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		print(self . x) # error
	@staticmethod
	def   m3():
		print(c1.x)How  to  print  static  variable  'x'
		print(cls . x) # error
		print(self . x) # error
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
a=c1()
print(a.x)#How  to  print  static  variable  'x'  in  another  way
print(x) # error
print(self . x) # error
print(cls . x) # error
a.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # error
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		self.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60#How  to  add  static  variable  'f'  with  value  60
		cls.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # error
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # error
		cls . k = 35 # error
#End  of  the  class
print('Outside  the  class')
print(c1 . _dict_) # {'a':10,'b','d','f','g','h':}
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_) # {'a':10,'b':20}
print()
print()
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 . _dict_) #{'a':10,'b':20,'d':40}
print()
print()
c1.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_) ##{'a':10,'b':20,'d':40,'g':70}
print()
print()
c1.m3()#How  to  call  m3()  method
print('static   method   m3') 
print(c1 . _dict_) #{'a':10,'b':20,'d':40,'g':70,'h':80}
print()
print()
c1.i=90#How  to  add  static  variable  'i'  with  value  90
x.j=100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_) #{'a':10,'b':20,'d':40,'g':70,'h':80,'i':90}
print()
print()
print("Object  'x' ")
print(x . _dict_) #{'c':30,'e':50,'j':100}



'''
static  variable  --->'a':10,'b':20,'d':40,'g':70,'h':80,'i':90

Object 'x'  --->'c':30,'e':50,'j':100
'''

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)#How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'
print(c1 . _dict_) #{'a':1,'b':2,'c':3}

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
a . disp()
b . disp()
c . disp()
'''
11 21 31 12
11 41 51 12
11 61 71 12
'''


'''
static   variable   ---> x=11

Object  'a'  ---> y=21 ,z=31,x=12

Object  'b'  ---> y=41, z=51,x=12

Object  'c'  ---> y=61, z=71,x=12
'''

'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n=int(input('How many Elements : '))
	def get2(self):
		self.a=[]
		for i in range(vector.n):
			self.a.append(int(input('Enter any number :')))
	def add(self , x , y):
		self.a=[]
		for i in range(vector.n):
			self.a.append(x.a[i]+y.a[i])
vector.get1()#How  to  call  get1()  method
a=vector()
print('1st object')
a.get2()#How  to  read  the  list  into  1st  object
b=vector()
print('2nd object')
b.get2()
c=vector()
c.add(a,b)
print('Result: ', c.a)

'''
static  variable  --->   n=4

Object  'x'   ---> a=[1,2,3,4]

Object  'y'   ---> a=[5,6,7,8]

Object  'z'   ---> a=[6, 8, 10, 12]
'''

'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
di={}
c1_di=c1.__dict__
for i in c1_di:
	if i.startswith('__') and i.endswith('__'):
		continue
	di[i]=c1_di[i]
print(di)
#  End  of  the  class

'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''

class Emp:

    def __init__(self):
        self.empno=int(input('Enter empno: '))
        self.empname=input('Enter empname: ')
        self.sal=int(input('Enter salary: '))
    @property
    def empno(self):
        return self._empno
    @empno.setter
    def empno(self,x):
        if x<0:
            raise ValueError('Value cannot be negative')
        self._empno=x

    @property
    def empname(self):
        return self._empname
    @empname.setter
    def empname(self,x):
        if x=="":
            raise ValueError('Value cannot be empty')
        self._empname=x

    @property
    def sal(self):
        return self._sal
    @sal.setter
    def sal(self,x):
        if x<0:
            raise ValueError('Value cannot be negative')
        self._sal=x
try:
    e=Emp()
    print(e.empno,e.empname,e.sal)
except ValueError as msg:
    print(msg)