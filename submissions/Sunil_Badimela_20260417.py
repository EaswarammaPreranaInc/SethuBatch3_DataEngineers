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
print(cls . x , cls . y)#Error
print(self . x , self . y)#Error


'''
static   variable   --->x=30 y=40

object  'a'   --->x=30 y=20

object  'b'   --->x=30 y=20

#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()#static method
a = c1()
a . m1()#static method
c1 . m1(25)#error


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method --static method
a = c1()
a . m1()  #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method--instance method
a . m1(35)  # What  about  here--error


#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35
a . m1()#error



#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() #nothing is printed
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
c1 . m1(25)#static method 25
a = c1()
a . m1()#static /instance method  <__main__.c1 object at some address>



# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print("init method",self.x)#How  to  print  static  variable  'x'
		print("init method",c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		print("m1 method",self.x)#How  to  print  static  variable  'x'
		print("m1 method",c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(cls . x)
	@classmethod
	def   m2(cls):
		print("m2 method",cls.x)#How  to  print  static  variable  'x'
		print("m2 method",c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		print("m3 method",c1.x)#How  to  print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x)
a=c1()
print(a.x)
'''
How  to  print  static  variable  'x'
How  to  print  static  variable  'x'  in  another  way
'''
#print(x)#error
#print(self . x)#error
#print(cls . x)#error
a.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()





# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10

	def    __init__(self):
		self.b=20#How  to  add  static  variable  'b'  with  value  20
		self.c=30#How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		c1.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60#How  to  add  static  variable  'f'  with  value  60
		cls.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
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
a=c1()
print("m1 method",a.m1())
#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 . __dict__)
print()
print()
print("m2 method",c1.m2())
#How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print("method3:",c1.m3())
#How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90#How  to  add  static  variable  'i'  with  value  90
c1.j=100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)



'''
static  variable  --->

Object 'x'  --->
'''



# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class

print(c1.a)#How  to  print  variable  'a'
print(c1.b)#How  to  print  variable  'b'
print(c1.c)#How  to  print  variable  'c'
print(c1 . __dict__)




# Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number   x :  '))
	def  get2(self):
		self . y = int(input('Enter  any  number y :  '))
		self . z = int(input('Enter  any  number  z:  '))
	def   compute(self):
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()#x=10
a = Test()
b = Test()
c = Test()
a . get2()#y=20 z=30
b . get2()#y=40 z=50
c . get2()#y=60 z=70
a . compute()#x=11 y=21 z=31 x=12
b . compute()#x=12 y=41 z=51 x=13
c . compute()#x=13 y=61 71 x=14
a . disp()
b . disp()
c . disp()


'''
static   variable   --->#x=13

Object  'a'  --->#x=12 y=21 z=31

Object  'b'  --->

Object  'c'  --->
'''
'''



class vector:
    @staticmethod
    def get1():
        vector.n = int(input("Enter number of elements: "))   # static variable

    def get2(self):
        self.a = []   # list for each object
        for i in range(vector.n):
            val = int(input(f"Enter element {i+1}: "))
            self.a.append(val)   # store elements in object list

    def add(self, x, y):
        self.a = []   # result list
        for i in range(vector.n):
            self.a.append(x.a[i] + y.a[i])   # add elements


# 🔹 Method Calls

vector.get1()        # read number of elements (static variable)

x = vector()
y = vector()
z = vector()

x.get2()             # read list for object x
y.get2()             # read list for object y

z.add(x, y)          # add lists of x and y → store in z

print("Result:", z.a)   # print result list




'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
a={}
print(c1.__dict__)
for i,j in c1.__dict__.items():
    if i.startswith("__") and i.endswith("__"):
        pass
    else:
        a[i]=j
print(a)

#  End  of  the  class



class Emp:
    def __init__(self, empno, ename, sal):
        self.set_empno(empno)   # use setter
        self.set_ename(ename)
        self.set_sal(sal)

    # 🔹 Setter for empno
    def set_empno(self, empno):
        if empno < 0:
            print("Invalid Emp Number")
        else:
            self.__empno = empno

    # Getter for empno
    def get_empno(self):
        return self.__empno

    # Setter for ename
    def set_ename(self, ename):
        if ename == "":
            print("Invalid Emp Name")
        else:
            self.__ename = ename

    # Getter for ename
    def get_ename(self):
        return self.__ename

    #Setter for salary
    def set_sal(self, sal):
        if sal < 0:
            print("Invalid Salary")
        else:
            self.__sal = sal

    # Getter for salary
    def get_sal(self):
        return self.__sal


# Outside the class

e = Emp(101, "Ravi", 50000)   # create object

print("Emp No  :", e.get_empno())
print("Emp Name:", e.get_ename())
print("Salary  :", e.get_sal())