'''Find  outputs  (Home  work)'''
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
print(a . x) # 30
print(a . y) # 20
print(b . x) #30
print(b . y) #20
print(c1 . x , c1 . y) # 30 40
# print(cls . x , cls . y) # Error---cls cannot cal outside the class
# print(self . x , self . y) #Error---self cannot cal outside the class
'''
static   variable   ---> x =30 , y = 40
object  'a'   --->y = 20
object  'b'   --->y = 20
'''
'''Find  outputs'''
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() # static  method
a = c1()
a . m1() #static  method
c1 . m1(25) #Error-- in method there are no arguments but giving 1 arg
'''Find  outputs'''
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) #35
#a . m1() #error---missing 1 arg
'''Find  outputs'''
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  static  method --25
a = c1()
a . m1()  #  instance  method # Type and address
#a . m1(35)  # Error --arguments are not required
'''Find  outputs'''
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() 
a = c1()
#a . m1() # Error
'''Find  outputs'''
class   c1:
	@staticmethod
	def  m1(self): # Discarded
		print('static  method')
		print(self)
	def  m1(self): # Recognized
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) # static / instance  method <nextline> 25
a = c1()
a . m1() #static / instance  method <nextline> Type and Address of obj a
'''How  to  access  static  variable  in  different  ways  ?'''
class   c1:
	x = 25
	def   __init__(self):
		self.x#How  to  print  static  variable  'x'
		c1.x#How  to  print  static  variable  'x'  in  another  way
		#print(x) # Error---x is not defined locally
	def   m1(self):
		self.x#How  to  print  static  variable  'x'
		c1.x#How  to  print  static  variable  'x'  in  another  way
		#print(cls . x) # Error--cls is not defined in this method
	@classmethod
	def   m2(cls):
		cls.x#How  to  print  static  variable  'x'
		c1.x#How  to  print  static  variable  'x'  in  another  way
		#print(self . x) # Error--- self is not defined in this method
	@staticmethod
	def   m3():
		c1.x#How  to  print  static  variable  'x'
		#print(cls . x) # Error---cls is not defined in this method
		#print(self . x) # Error---self is not defined in this method
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
a=c1()
print(a.x)#How  to  print  static  variable  'x'  in  another  way
#print(x)# Error---x is searched for global variable
#print(self . x)# Error--self is cannot cal outside
#print(cls . x)# Error--cls is cannot cal outside
c1.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()
'''How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?'''
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		self.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25 #Error---cls is not defined
	def   m1(self):
		self.d = 40#How  to  add  static  variable  'd'  with  value  40
		self.e = 50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60#How  to  add  static  variable  'f'  with  value  60
		cls.g = 70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25 # Error---self is not Defined in this Method
	@staticmethod
	def   m3():
		x.h = 80#How  to  add  static  variable  'h'  with  value  80
		#self . k = 25 # Error---self is not Defined in this Method
		#cls . k = 35 # Error---cls is not Defined in this Method
#End  of  the  classprint('Outside  the  class') #Outside  the  class
print(c1 . __dict__) # {'a': 10, EV}
print()
print()
x = c1()
print('Constructor') # Constructor
print(c1 . __dict__)# {'a': 10,'b': 20, 'c': 30, EV}
print()
print()
x.m1()#How  to  call  m1()  method
print('Instance  method  m1') # Instance  method  m1
print(c1 . __dict__) # {'a': 10,'b': 20, 'c': 30, 'd': 40, 'e': 50, EV}
print()
print()
x.m2()#How  to  call  m2()  method
print('class  method   m2') # class  method   m2
print(c1 . __dict__) #{'a': 10,'b': 20, 'c': 30, 'd': 40, 'e': 50,'f': 60, 'g': 70, EV}
print()
print()
x.m3()#How  to  call  m3()  method
print('static   method   m3') # static   method   m3
print(c1 . __dict__) #{'a': 10,'b': 20, 'c': 30, 'd': 40, 'e': 50,'f': 60, 'g': 70,'h': 80 , EV}
print()
print()
c1.i = 90#How  to  add  static  variable  'i'  with  value  90
c1.j = 100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__) # {'a': 10,'b': 20, 'c': 30, 'd': 40, 'e': 50,'f': 60, 'g': 70, 'h': 80 , 'i': 90 , 'j': 100 , EV}
print()
print()
print("Object  'x' ") 
print(x . __dict__) #{'b': 20, 'c': 30, 'd': 40, 'e': 50,'f': 60, 'g': 70, 'h': 80 }
'''
static  variable  ---> a = 10, i = 90, j =100
Object 'x'  ---> b = 20 , c= 30 , d= 40 , e= 50, f=60, g=70
'''
'''Find  outputs  (Home  work)'''
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # 1  How  to  print  variable  'a'
print(c1.b)#2   How  to  print  variable  'b'
print(c1.c)# 3   How  to  print  variable  'c'
print(c1 . __dict__)# {'a':1 , 'b':2 , 'c':3, EV}
'''Tricky  program'''
#What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  ')) # 10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  ')) #20
		self . z = int(input('Enter  any  number  :  ')) # 30
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
a . disp() # 13  21  31  12
b . disp() # 13  41  51  13 
c . disp() # 13  61  71  14
'''
static   variable   ---> x= 13
Object  'a'  --->y= 21 , z = 31 ,x =12
Object  'b'  --->y = 41 , z = 51 , x = 13
Object  'c'  --->y = 61 , z = 71 , x = 14
'''


'''Write  a  program  to  add  two  Vector  objects
1) What  are  the  names  of  objects ?  --->  x , y   and  z
2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a
3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]
4) How  to  access  static  variable  'n' ?  --->  vector . n
'''

class Vector:
    n = 0   
    @staticmethod
    def get1():
        Vector.n = int(input("Enter number of elements: "))
    def get2(self):
        self.a = []
        for i in range(Vector.n):
            self.a.append(int(input()))
    def add(self, x, y):
        self.a = []
        for i in range(Vector.n):
            self.a.append(x.a[i] + y.a[i])
Vector.get1()
a = Vector()
b = Vector()
c = Vector()
a.get2()
b.get2()
c.add(a, b)
print("Resultant vector:")
print(c.a)
'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_
Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
d={}
for k in c1.__dict__:
    if not k.startswith("__") and not  k.endswith("__") :
       d[k]= c1.__dict__[k]
print(d)    
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
class  emp:
    def  __init__(self):  
        self . empno = int(input('Enter employee no: '))  
        self . ename = input('Enter employee name: ') 
        self . sal = float(input('Enter employee salary: '))   
    @property
    def  empno(self):  
        return  self . _empno  
    @property
    def  ename(self):   
        return  self . _ename    
    @property
    def  sal(self):  
        return  self . _sal   
    @empno.setter
    def  empno(self , x):   
        if x < 0:
            raise  ValueError('Empno cannot be negative')
        self . _empno = x  
    @ename.setter
    def  ename(self , x): 
        if  x == '':
            raise ValueError('Ename cannot be empty')
        self . _ename = x    
    @sal.setter
    def  sal(self , x):  
        if x < 0:
            raise  ValueError('Salary cannot be negative')
        self . _sal = x  
try:
	e = emp()  
	print('Employee  number : ' , e . empno)  
	print('Employee  name : ' , e . ename)   
	print('Salary : ' , e . sal)   
except  ValueError  as  msg:
	print(msg)



