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
a = c1() # Object of class c1 is created
b = c1() # Object of class c1 is created
c1 . m1() 
print(a . x) # 30
print(a . y) # 20
print(b . x) # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30 40
print(cls . x , cls . y) # Error because object cls is not defined
print(self . x , self . y) # Error because object self is not defined


'''
static   variable   ---> x = 30 , y = 40

object  'a'   ---> y = 20

object  'b'   ---> y = 20
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
c1 . m1(25) # Error the static method m1() does not require any argument

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 35
a . m1() # Error the static method m1() requires one argument

#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  static method and it displays 25
a = c1()
a . m1()  #  instance method and it displays <class 'c1'> and address in hexadecimal
a . m1(35)  # instance method and it raises an error because the method m1() takes only one argument but not two arguments

#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() 
a = c1()
a . m1() # Error because the static method m1() does not takes any argument but one argument is passed

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
c1 . m1(25) # static  method <nextline> 25
a = c1()
a . m1() # static / instance  method <nextline> <class 'c1'> and address in hexa decimal

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) 
		print(self.x)
		print(x) # Error because object x is not defined
	def   m1(self):
		print(c1.x)
		print(self.x)
		print(cls . x) # Error because object cls is not defined
	@classmethod
	def   m2(cls):
		print(c1.x)
		print(cls.x)
		print(self . x) # Error because object self is not defined
	@staticmethod
	def   m3():
		print(c1.x)
		print(cls . x) # Error because object cls is not defined
		print(self . x) # Error because object self is not defined
# End  of  the  class
print(c1.x) # 25
a = c1() # 25 <nextline> 25
print(a.x) # 25 
print(x) # Error because object x is not defined
print(self . x) # Error because object self is not defined
print(cls . x) # Error because object cls is not defined
print(a.m1()) # 25 <nextline> 25 <nextline> None
print(c1.m2()) # 25 <nextline> 25 <nextline> None
print(c1.m3()) # 25 <nextline> None

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10
	def    __init__(self):
		c1.b = 20
		self.c = 30
		# cls . k = 25 # Error because object cls is not defined
	def   m1(self):
		c1.d = 40
		self.e = 50
	@classmethod
	def   m2(cls):
		c1.f = 60
		cls.g = 70
		# self . k = 25 # Error because object self is not defined
	@staticmethod
	def   m3():
		c1.h = 80
		# self . k = 25 # Error because object self is not defined
		# cls . k = 35 # Error because object cls is not defined
#End  of  the  class
print('Outside  the  class')
print(c1 .__dict__) # {'a' : 10}
print()
print()
x = c1() 
print('Constructor')
print(c1 .__dict__) # {'a' : 10 , 'b' : 20}
print()
print()
x.m1()
print('Instance  method  m1')
print(c1 .__dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40}
print()
print()
c1.m2()
print('class  method   m2')
print(c1 .__dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70}
print()
print()
c1.m3()
print('static   method   m3')
print(c1 .__dict__) # {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h': 80}
print()
print()
c1.i = 90
x.j = 100
print('Outside  the  class')
print(c1 .__dict__) #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h': 80, 'i' : 90}
print()
print()
print("Object  'x' ")
print(x .__dict__) # {'c' : 30 ,'e' : 50 , 'j' : 100}



'''
static  variable  ---> a = 10 , b = 20 , d = 40 , f = 60 , g = 70 , h = 80, i = 90

Object 'x'  ---> c = 30 , e = 50 , j = 100
'''

''' Output:
Outside  the  class
{'a' : 10}

Constructor
{'a' : 10 , 'b' : 20}

Instance  method  m1
{'a' : 10 , 'b' : 20 , 'd' : 40}

class  method   m2
{'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70}

static   method   m3
{'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h': 80}

Outside  the  class
{'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h': 80, 'i' : 90}

Object  'x' 
{'c' : 30 ,'e' : 50 , 'j' : 100}

'''

# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) # 1
print(c1.b) # 2
print(c1.c) # 3
print(c1 . _dict_) # {'a' : 1 , 'b' : 2 , 'c' : 3}

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
a . disp() # 13	      21 	31	12
b . disp() # 13	      41 	51	13
c . disp() # 13	      61 	71	14


'''
static   variable   ---> x = 13 

Object  'a'  ---> y = 21 , z = 31 , x = 12

Object  'b'  ---> y = 41 , z = 51 , x = 13

Object  'c'  ---> y = 61 , z = 71 , x = 14
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
''' Output:
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

''' Output:
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
                
''' Output:
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