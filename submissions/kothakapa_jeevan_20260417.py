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
print(a . x) # 30
print(a . y) # 40 
print(b . x) # 30 
print(b . y) # 40 
print(c1 . x , c1 . y) # 30 40 
print(cls . x , cls . y) # Error due to class is not defined
print(self . x , self . y) # Error due to self is not defined

'''
static   variable   ---> 30, 40

object  'a'   ---> 30 40

object  'b'   ---> 30 40 
'''


#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() # static method
a = c1() # instance class
a . m1() # static method 
c1 . m1(25) # Error because static method m1() does not take any parameters



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25 
a = c1() # instance class
a . m1(35) # 35 
a . m1() # Error due to missing positional argument 



#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #   25
a = c1() # instance class 
a . m1()  #  instance method 
a . m1(35)  # Error due to position arguments 



#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() --> nothing printed
a = c1() --> instance class
a . m1() --> nothing printed




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
--> Here first m1 method is ignored and second m1 method recognised because both methods have same names
c1 . m1(25)--> statice / instance method 
	       25 
a = c1()
a . m1() # statice/instance method 



# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		print(self.x) #How  to  print  static  variable  'x' 25
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way 25 
		print(x) # Error due to name 'x' is not defined
	def   m1(self):
		print(self.x)   #How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x)#How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x' 25
print(c1.__dict__['x'])#How  to  print  static  variable  'x'  in  another  way 25 
print(x) #  Error due to name 'x'is not defined
print(self . x) # Error due to name self is not defined
print(cls . x) # Error due to name 'cls' is not defined 
c1.m1() #How  to  call  method  m1() Error due to missing positional argument
c1.m2() #How  to  call  method  m2() Error due to missing positional argument
c1.m3() #How  to  call  method  m3() Error due to missing positional argument



# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class c1:
    a = 10   # static variable 'a'

    def __init__(self):
        c1.b = 20        # static variable 'b'
        self.c = 30      # instance variable 'c'
        c1.k = 25

    def m1(self):
        c1.d = 40        # static variable 'd'
        self.e = 50      # instance variable 'e'

    @classmethod
    def m2(cls):
        cls.f = 60       # static variable 'f'
        c1.g = 70        # static variable 'g' (another way)
        cls.k = 25

    @staticmethod
    def m3():
        c1.h = 80        # static variable 'h'
        c1.k = 35

# End of the class

print('Outside the class')
print(c1.__dict__)
print()
print()

x = c1()

print('Constructor')
print(c1.__dict__)
print()
print()

x.m1()   # call m1()

print('Instance method m1')
print(c1.__dict__)
print()
print()

c1.m2()   # call m2()

print('class method   m2')
print(c1.__dict__)
print()
print()

c1.m3()   # call m3()

print('static   method   m3')
print(c1.__dict__)
print()
print()

c1.i = 90     # static variable 'i'
x.j = 100     # instance variable 'j'

print('Outside the class')
print(c1.__dict__)
print()
print()

print("Object  'x' ")
print(x.__dict__)

'''
static  variable  --->

Object 'x'  --->
'''




# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a)  # How  to  print  variable  'a' --> print(c1.a) -> 1
print(c1.b)  # How  to  print  variable  'b' -->  print(c1.b) -> 2
print(c1.c)  # How  to  print  variable  'c' --> print(c1.c) -> 3
print(c1 . __dict__) --> evnironmetal variables 
			 'a': 1,
 			 'b': 2,
 			 'c': 3,




# Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class Test:
    @classmethod
    def get1(cls):
        # Input 1: 10
        cls.x = int(input('Enter any number : '))
        
    def get2(self):
        # Inputs 2 & 3: 20, 30 for 'a' | 40, 50 for 'b' | 60, 70 for 'c'
        self.y = int(input('Enter any number : '))
        self.z = int(input('Enter any number : '))
        
    def compute(self):
        Test.x += 1
        self.y += 1
        self.z += 1
        # self.x creates an instance variable shadows the static variable for this object
        self.x = Test.x + 1 
        
    def disp(self):
        print(Test.x, self.y, self.z, self.x, sep='\t')
# End of the class

''' 
(Uncomment inputs below to run manually)
Test.get1()
a = Test()
b = Test()
c = Test()

a.get2()
b.get2()
c.get2()

a.compute()
b.compute()
c.compute()

a.disp()
b.disp()
c.disp()
'''
'''
Outputs for given inputs (10, 20, 30, 40, 50, 60, 70):
13      21      31      12
13      41      51      13
13      61      71      14
'''


'''
static   variable   --->

Object  'a'  --->

Object  'b'  --->

Object  'c'  --->
'''



'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class vector:
    
    @staticmethod
    def get1():
        vector.n = int(input('Enter any number : '))  # number of elements

    def get2(self):
        self.a = []  # list for object
        for i in range(vector.n):
            self.a.append(int(input(f"Enter element {i+1}: ")))

    def add(self, x, y):
        # add lists of x and y into current object
        self.a = [x.a[i] + y.a[i] for i in range(vector.n)] #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object

vector.get1() #How  to  call  get1()  method
a = vector() #How  to  read  the  list  into  1st  object
b = vector() #How  to  read  the  list  into  2nd  object  'b'
c = vector() #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
a.get2()
b.get2()
c.add(a, b) #How  to  call  the  add() method
print(c.a) #How  to  print  the  list  of  3rd   object
'''
static  variable  --->  

Object  'x'   ---> 

Object  'y'   ---> 

Object  'z'   --->  
'''



'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
for key, value in c1.__dict__.items():
    if not (key.startswith('__') and key.endswith('__')):
        print(key, "=", value)
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

    # constructor
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    # setter for empno
    def set_empno(self, empno):
        if empno < 0:
            print("Emp number cannot be negative")
            self.__empno = 0
        else:
            self.__empno = empno

    # getter for empno
    def get_empno(self):
        return self.__empno

    # setter for ename
    def set_ename(self, ename):
        if ename == "":
            print("Emp name cannot be empty")
            self.__ename = "Unknown"
        else:
            self.__ename = ename

    # getter for ename
    def get_ename(self):
        return self.__ename

    # setter for salary
    def set_sal(self, sal):
        if sal < 0:
            print("Salary cannot be negative")
            self.__sal = 0
        else:
            self.__sal = sal

    # getter for salary
    def get_sal(self):
        return self.__sal



# Outside the class

# creating object
# Create Emp class object
emp1 = Emp(101, "Srinivas", 50000)

# printing values
print("Emp Number :", emp1.get_empno())
print("Emp Name   :", emp1.get_ename())
print("Salary     :", emp1.get_sal())