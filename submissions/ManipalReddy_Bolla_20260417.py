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
print(a . x)#30
print(a . y)#20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#30 40
print(cls . x , cls . y)#error because The variable cls only exists inside the m1 method. Once that method finishes, cls is no longer defined in the global scope
print(self . x , self . y)#error because self is a parameter name used inside class methods. Outside the class, the computer has no idea what self refers to


'''
static   variable   --->x=30 y=40
object  'a'   --->y=20
object  'b'   --->y=20
'''


#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()#static method
a = c1()
a . m1()#static method
c1 . m1(25)#error 1 positional argument not present in this method call


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35
a . m1()#error 1 positional argument not present in this method call


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method#static method prints 25
a = c1()
a . m1()  #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method #instance method and prints type and address 
a . m1(35)  # What  about  here #instance method but error c1.m1() takes 1 positional argument but 2 were given


#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1()#empty
a = c1()
a . m1()#error


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
c1 . m1(25)#static / instance  method <nextline> 25
a = c1()
a . m1()#static / instance  method <nextline> type and address of object self i.e a


 # How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)#25
		print(self.x)#25
		#print(x) error
	def   m1(self):
		print(c1.x)#25
		print(self.x)#25
		#print(cls . x) error
	@classmethod
	def   m2(cls):
		print(c1.x)#25
		print(cls.x)#25
		#print(self . x) error
	@staticmethod
	def   m3():
		print(c1.x)#25
		#print(cls . x) error
		#print(self . x) error
# End  of  the  class
print(c1.x)#25
a=c1()
print(a.x)#25
#print(x) error
#print(self . x) error
#print(cls . x) error
a.m1()
c1.m2()
c1.m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10
	def    __init__(self):
		c1.b=20
		self.c=30
		#cls . k = 25
	def   m1(self):
		c1.d=40
		self.e=50
	@classmethod
	def   m2(cls):
		c1.f=60
		cls.g=70
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80
		#self . k = 25
		#cls . k = 35
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
print(c1 . __dict__)
print()
print()
c1.m3()
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90
x.j=100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)



'''
static  variable  --->a=10 b=20 d=40 f=60 g=70 h=80 i=90

Object 'x'  --->c=30 e=50 j=100
'''


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
#How  to  print  variable  'a'
print(c1.a)
#How  to  print  variable  'b'
print(c1.b)
#How  to  print  variable  'c'
print(c1.c)
print(c1 . __dict__)


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
Test . get1()#10
a = Test()
b = Test()
c = Test()
a . get2()#a.y=20 a.z=30
b . get2()#b.y=40 b.z=50
c . get2()#c.y=60 c.z=70
a . compute()#Test.x=11 a.y=21 a.z=31 a.x=12
b . compute()#Test.x=12 b.y=41 b.z=51 b.x=13
c . compute()#Test.x=13 c.y=61 c.z=71 b.x=14
a . disp()#Test.x=13 a.y=21 a.z=31 a.x=12
b . disp()#Test.x=13 b.y=41 b.z=51 b.x=13
c . disp()#Test.x=13 c.y=61 c.z=71 c.x=14


'''
static   variable   --->x=13
Object  'a'  --->y=21 z=31 x=12
Object  'b'  --->y=41 z=51 x=13
Object  'c'  --->y=61 z=71 x=14
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
		vector.n = int(input('How many elements ? : '))
	def get2(self):
		list = []
		for i in range(vector.n):
		    list.append(int(input('Enter any number : ')))
		self.a = list
	def add(self , x , y):
	    list = []
	    for i in range(vector.n):
		    list.append(x.a[i]+y.a[i])
	    self.a = list
vector.get1()
print('1st Object')
a = vector()
a.get2()
print('2nd Object')
b = vector()
b.get2()
c = vector()
c.add(a,b)
print('Result : ',c.a)


'''
static  variable  --->  n = 4

Object  'x'   ---> a = [10 , 20 , 15 , 18]

Object  'y'   ---> b = [30 , 40 , 35 , 12]

Object  'z'   ---> c = [40 , 60 , 50 , 30]
'''


''' 
Output
How many elements ? : 4
1st Object
Enter any number : 10
Enter any number : 20
Enter any number : 15
Enter any number : 18
2nd Object
Enter any number : 30
Enter any number : 40
Enter any number : 35
Enter any number : 12
Result :  [40, 60, 50, 30]
'''


'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
# End of the class
d = c1.__dict__
res = {}
for x in d:
    if x.startswith('__') and x.endswith('__'):
        pass
    else:
        res[x] = d.get(x)
print('Result :  ',res)

''' 
Output
Result :   {'x': 1, 'y': 2, 'z': 3}
'''


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
# Code : 
class Emp:
    def __init__(self):
        self.empno = int(input('Enter employee number : '))
        self.ename = input('Enter employee name : ')
        self.sal = int(input('Enter salary : '))
    @property
    def empno(self):
        return self._empno
    @empno.setter
    def empno(self,val):
        if val < 0 :
            raise ValueError('Empno cannot be negative')
        self._empno = val
    @property
    def ename(self):
        return self._ename;
    @ename.setter
    def ename(self,val):
        if val == '':
            raise ValueError('Emp name cannot be empty string')
        self._ename = val
    @property
    def sal(self):
        return self._sal;
    @sal.setter
    def sal(self,val):
        if val < 0 :
            raise ValueError('Salary cannot be negative')
        self._sal = val
try :
    e = Emp()
    print('Employee number :  ',e.empno)
    print('Employee name :  ',e.ename)
    print('Employee salary :  ',e.sal)
except ValueError as msg:
    print(msg)
  
  
''' 
Output
Enter employee number : -25
Empno cannot be negative

Enter employee number : 25
Enter employee name : 
Emp name cannot be empty string

Enter employee number : 25
Enter employee name : Rama Rao
Enter salary : -10000
Salary cannot be negative

Enter employee number : 25
Enter employee name : Rama Rao
Enter salary : 10000
Employee number :   25
Employee name :   Rama Rao
Employee salary :   10000
'''