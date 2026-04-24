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
print(a . x)	#30
print(a . y)	#20
print(b . x)	#30
print(b . y)	#20
print(c1 . x , c1 . y)	#30 40
print(cls . x , cls . y)	#error cls ids not defined
print(self . x , self . y)	#error self is not defined



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)
a = c1()	#25
a . m1(35)	#35
a . m1()	#error


#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()	#static method
a = c1()
a . m1()	#static method
c1 . m1(25)	#error


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1()  #type and address of the object
a . m1(35)  #error



#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1()	#blank line 
a = c1()
a . m1()	#error 



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
c1 . m1(25)	#static / instance method <next line> 25
a = c1()
a . m1()	#static / instance method <next line> type and address of the object






# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)	#How  to  print  static  variable  'x'
		print(self.x)	#How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(c1.x)	#How  to  print  static  variable  'x'
		print(self.x)	#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x)	#How  to  print  static  variable  'x'
		print(c1.x)	#How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		print(c1.x)	#How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x)	#How  to  print  static  variable  'x'
obj=c1()	#How  to  print  static  variable  'x'  in  another  way
print(obj.x)
print(x)
print(self . x)
print(cls . x)
obj.m1	#How  to  call  method  m1()
c1.m2()	#How  to  call  method  m2()
c1.m3()	#How  to  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10	#How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20		#How  to  add  static  variable  'b'  with  value  20
		self.c=30	#How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25	#error cls is not defined
	def   m1(self):
		c1.d=40	#How  to  add  static  variable  'd'  with  value  40
		self.e=50	#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=70	#How  to  add  static  variable  'f'  with  value  60
		c1.g=70		#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25	#error 
	@staticmethod
	def   m3():
		c1.h=80		#How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
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
s=c1()	#How  to  call  m1()  method
c1.m1()
print('Instance  method  m1')
print(c1 . __dict__)
print()
print()
c1.m2()	#How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
c1.m3()		#How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90		#How  to  add  static  variable  'i'  with  value  90
x.j=100		#How  to  add  instance  variable  'j'  with  value  100
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
print(c1.a)	#How  to  print  variable  'a'
print(c1.b)	#How  to  print  variable  'b'
print(c1,c)	#How  to  print  variable  'c'
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
Test . get1()	#10
a = Test()
b = Test()
c = Test()
a . get2()	#20 30
b . get2()	#40 50
c . get2()	#60 70
a . compute()
b . compute()
c . compute()
a . disp()	#13 21 31 12
b . disp()	#13 41 51 13
c . disp()	#13 61 71 14



class vector:
    n = 0   # static variable (number of elements)

    @staticmethod
    def get1():
        # How to read number of elements into variable 'n'
        vector.n = int(input("Enter number of elements: "))

    def get2(self):
        # How to read the list into the object
        self.a = []
        for i in range(vector.n):
            self.a.append(int(input("Enter element: ")))

    def add(self, x, y):
        # How to add lists of objects x and y
        self.a = []
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])


# -------------------- MAIN PROGRAM --------------------

# How to call get1() method
vector.get1()

# Creating objects x, y, z
x = vector()
y = vector()
z = vector()

# How to read list into 1st object
x.get2()

# How to read list into 2nd object
y.get2()

# How to add lists of x and y into z
z.add(x, y)

# How to print list of 3rd object
print("Result vector:", z.a)




class c1:
    x = 1
    y = 2
    z = 3
# End of class


# Printing only static variables
for name, value in c1.__dict__.items():
    if not (name.startswith("__") and name.endswith("__")):
        print(name, "=", value)




class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)
        self.set_ename(ename)
        self.set_sal(sal)

    # ---------------- SETTERS ----------------

    def set_empno(self, empno):
        if empno < 0:
            print("Invalid empno (cannot be negative). Setting to 0")
            self.empno = 0
        else:
            self.empno = empno

    def set_ename(self, ename):
        if ename.strip() == "":
            print("Invalid name (cannot be empty). Setting to 'Unknown'")
            self.ename = "Unknown"
        else:
            self.ename = ename

    def set_sal(self, sal):
        if sal < 0:
            print("Invalid salary (cannot be negative). Setting to 0")
            self.sal = 0
        else:
            self.sal = sal

    # ---------------- GETTERS ----------------

    def get_empno(self):
        return self.empno

    def get_ename(self):
        return self.ename

    def get_sal(self):
        return self.sal


# ---------------- OUTSIDE THE CLASS ----------------

# Creating object
e = Emp(101, "John", 50000)

# Printing values using getters
print("Emp No  :", e.get_empno())
print("Emp Name:", e.get_ename())
print("Salary  :", e.get_sal())


