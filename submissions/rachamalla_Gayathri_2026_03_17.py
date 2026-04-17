#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35
a . m1()#error no argument
#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
a = c1()
a . m1()  #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
a . m1(35)  # What  about  here
 #  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() # 
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
c1 . m1(25) #static /instance method 25
a = c1()
a . m1()#static/instance method
# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		How  to  print  static  variable  'x'
                print(c1.x)
		How  to  print  static  variable  'x'  in  another  way
                print(self.x)
		print(x)
	def   m1(self):
		How  to  print  static  variable  'x'
                print(c1.x)
		How  to  print  static  variable  'x'  in  another  way
                print(self.x)
		print(cls . x)
	@classmethod
	def   m2(cls):
		How  to  print  static  variable  'x'
                print(cls.x)
		How  to  print  static  variable  'x'  in  another  way
                print(c1.x)
		print(self . x)
	@staticmethod
	def   m3():
		How  to  print  static  variable  'x'
                print(c1.x)
		print(cls . x)
		print(self . x)
# End  of  the  class
How  to  print  static  variable  'x'
print(c1.x)
How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
How  to  call  method  m1()
a.m1()
How  to  call  method  m2()
c1.m2()
How  to  call  method  m3()
c1.m3()
# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		How  to  add  static  variable  'b'  with  value  20
		How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def   m1(self):
		How  to  add  static  variable  'd'  with  value  40
		How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		How  to  add  static  variable  'f'  with  value  60
		How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def   m3():
		How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Outside  the …
[11:46 AM, 4/17/2026] SRINIVAS Sir Maths: # Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
How  to  print  variable  'a'
How  to  print  variable  'b'
How  to  print  variable  'c'
print(c1 . _dict_)
[11:46 AM, 4/17/2026] SRINIVAS Sir Maths: # Tricky  program
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
static   variable   --->

Object  'a'  --->

Object  'b'  --->

Object  'c'  --->
'''
[11:53 AM, 4/17/2026] SRINIVAS Sir Maths: '''
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
		How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		How  to  read  the  list  into  the  object
	def add(self , x , y):
		How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
How  to  call  get1()  method
How  to  read  the  list  into…
[11:56 AM, 4/17/2026] SRINIVAS Sir Maths: '''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
[1:08 PM, 4/17/2026] SRINIVAS Sir Maths: '''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    def set_empno(self, empno):
        if empno < 0:
            print("Invalid empno")
        else:
            self.empno = empno

    def get_empno(self):
        return self.empno

    def set_ename(self, ename):
        if ename == "":
            print("Invalid name")
        else:
            self.ename = ename

    def get_ename(self):
        return self.ename

    def set_sal(self, sal):
        if sal < 0:
            print("Invalid salary")
        else:
            self.sal = sal

    def get_sal(self):
        return self.sal


# Outside
a = Emp(101, "Gayathri", 25000)
print(a.get_empno(), a.get_ename(), a.get_sal())

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
