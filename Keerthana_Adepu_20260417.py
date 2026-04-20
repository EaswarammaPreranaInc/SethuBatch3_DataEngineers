# Find  outputs  (Home  work)
class   c1:
	x = 10 # static variable
	def  _init_(self):
		self . y = 20 # instance variable
	@classmethod
	def   m1(cls):
		cls . x = 30 # modifies static variable
		cls . y = 40 # creates new static variable
# End  of  the  class
a = c1()
b = c1()
c1 . m1()
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30 40
print(cls . x , cls . y) # error because cls is not defined outside method
print(self . x , self . y) # error because self is not defined outside class

'''
static variable ---> x = 30 , y = 40
object 'a' ---> x = 30 , y = 20
object 'b' ---> x = 30 , y = 20
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
c1 . m1(25) # error m1 needs no arguments

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1() # object created
a . m1(35) # 35
a . m1() # error because we are not passing any argument to self

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25 ---> static  method 
a = c1()
a . m1()  #  type and address of object ---> instance  method
a . m1(35)  # error because we are passing an argument and it already has self='a'

#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1()  # static  method 
a = c1()
a . m1() # static  method 

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
c1 . m1(25) # static / instance method <> 25
a = c1()
a . m1() # static / instance method <> type and address of object 'a'

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25 # static variable
	def   _init_(self):
		print(self.x) # How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(x) # Error because we can't call directly
	def   m1(self):
		print(self.x) # How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(cls . x) # Error because cls can't be used here
	@classmethod
	def   m2(cls):
		print(cls.x) # How  to  print  static  variable  'x'
		print(c1.x) # How  to  print  static  variable  'x'  in  another  way
		print(self . x) # Error because self can't be used here
	@staticmethod
	def   m3():
		print(c1.x) # How  to  print  static  variable  'x'
		print(cls . x) # Error because cls can't be used here
		print(self . x) # Error because self can't be used here
# End  of  the  class
print(c1.x) # How  to  print  static  variable  'x'
a = c1()
print(a.x) # How  to  print  static  variable  'x'  in  another  way
print(x) # error because x is not defined
print(self . x) # error self can't be called outside
print(cls . x) # error clas can't be called outside
a.m1() # How  to  call  method  m1()
c1.m2() # How  to  call  method  m2()
c1.m3() # How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.b = 20 # How  to  add  static  variable  'b'  with  value  20
		self.c = 30 # How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # error cls can't be called here
	def   m1(self):
		c1.d = 40 # How  to  add  static  variable  'd'  with  value  40
		self.e = 50 # How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 # How  to  add  static  variable  'f'  with  value  60
		c1.g = 70 # How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # error self can't be called here
	@staticmethod
	def   m3():
		c1.h = 80 # How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # error self can't be called here
		cls . k = 35 # error cls can't be called here
#End  of  the  class
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_)
print()
print()
x.m1() # How  to  call  m1()  method
print('Instance  method  m1')
print(c1 . _dict_)
print()
print()
c1.m2() # How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_)
print()
print()
c1.m3() # How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_)
print()
print()
c1.i = 90 # How  to  add  static  variable  'i'  with  value  90
x.j = 100 # How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
print("Object  'x' ")
print(x . _dict_)

'''
static  variable  ---> a, b, d, f, g, h, i

Object 'x'  ---> c, e, j
'''

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # How  to  print  variable  'a'
print(c1.b) # How  to  print  variable  'b'
print(c1.c) # How  to  print  variable  'c'
print(c1 . _dict_)

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
13    21    31    12
13    41    51    13
13    61    71    14

static variable ---> x = 13

Object 'a' ---> y = 21 , z = 31 , x = 12

Object 'b' ---> y = 41 , z = 51 , x = 13

Object 'c' ---> y = 61 , z = 71 , x = 14
'''

#1
'''
Write  a  program  to  add  two  Vector  objects
1) What  are  the  names  of  objects ?  --->  x , y   and  z
2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a
3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]
4) How  to  access  static  variable  'n' ?  --->  vector . n
class  vector:
	@staticmethod
	def get1():
		How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		How  to  read  the  list  into  the  object
	def add(self , x , y):
		How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
How  to  call  get1()  method
How  to  read  the  list  into  1st  object
How  to  read  the  list  into  2nd  object  'b'
How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
How  to  print  the  list  of  3rd   object'''
class vector:
    n = 0   
    @staticmethod
    def get1():
        vector.n = int(input('How many elements? : '))
    def get2(self):
        self.a = []
        for i in range(vector.n):
            val = int(input('Enter any number : '))
            self.a.append(val)
    def add(self, x, y):
        self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])
vector.get1()
x = vector()
y = vector()
z = vector()
print('1st object')
x.get2()
print('2nd object')
y.get2()
z.add(x, y)
print('Result :', z.a)
'''
static variable ---> vector.n

Object 'x' ---> First vector object --> x.a

Object 'y' ---> Second vector object  ---> y.a

Object 'z' ---> Result vector object --> z.a
'''

#2
'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class c1:
    x = 1
    y = 2
    z = 3
# End of class
d = c1.__dict__
print(d)
for key, value in d.items():
    if not (key.startswith('__') and key.endswith('__')):
        print(key, "=", value)


#3
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
    def __init__(self, empno=None, ename=None, sal=None):
        if empno is not None:
            self.empno = empno
        if ename is not None:
            self.ename = ename
        if sal is not None:
            self.sal = sal

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self, value):
        if value < 0:
            print('Empno cannot be negative')
            exit()
        self.__empno = value

    @property
    def ename(self):
        return self.__ename

    @ename.setter
    def ename(self, value):
        if value.strip() == '':
            print('Emp name cannot be empty string')
            exit()
        self.__ename = value

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, value):
        if value < 0:
            print('Salary cannot be negative')
            exit()
        self.__sal = value

e = Emp()   
e.empno = int(input('Enter employee number : '))
e.ename = input('Enter employee name : ')
e.sal = float(input('Enter salary : '))
print('Employee number  :', e.empno)
print('Employee name    :', e.ename)
print('Employee salary  :', e.sal)
