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
print(a . y) # 20
print(b . x) # 40
print(b . y) # 20
print(c1 . x , c1 . y) # 30 40
print(cls . x , cls . y) # error
print(self . x , self . y) # error


'''
static   variable   --->x=30 y=40

object  'a'   --->y=20

object  'b'   --->y=20



#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() # static  method
a = c1()
a . m1() # static  method
c1 . m1(25) # error



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1()
a . m1(35) # 35
a . m1() # error



#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25 static  method  
a = c1()
a . m1()  #  type and obj, instance  method
a . m1(35)  # error


#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1()  # ntg
a = c1()
a . m1() # error


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
c1 . m1(25) # static / instance  method 25
a = c1()
a . m1() # static / instance  method



# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x)How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(self.x)How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x) #How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x) #How  to  print  static  variable  'x'
a=c1()
print(a.x) #How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
b=c1() #
b.m1() #How  to  call  method  m1()
c1.m2() #How  to  call  method  m2()
c1.m3() #How  to  call  method  m3()


# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25 # error
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60 #How  to  add  static  variable  'f'  with  value  60
		cls.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25 # error
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		self . k = 25 # error
		cls . k = 35 # error
#End  of  the  class
print('Outside  the  class') # Outside  the  class
print(c1 . __dict__) # {'a':10}
print()
print()
x = c1()
print('Constructor') # Constructor
print(c1 . __dict__) # {'a':10, 'b':20}
print()
print()
x.m1() #How  to  call  m1()  method
print('Instance  method  m1') # Instance  method  m1
print(c1 . __dict__) # {'a':10, 'b':20, 'd':40}
print()
print()
c1.m2() #How  to  call  m2()  method
print('class  method   m2') # class  method   m2
print(c1 . __dict__) # # {'a':10, 'b':20, 'd':40, 'f':60, 'g':70}
print()
print()
c1.m3() #How  to  call  m3()  method
print('static   method   m3') # static   method   m3
print(c1 . __dict__) # # {'a':10, 'b':20, 'd':40, 'f':60, 'g':70,'h':80}
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class') # Outside  the  class
print(c1 . __dict__) # # {'a':10, 'b':20, 'd':40, 'f':60, 'g':70,'h':80, 'i':90}
print()
print()
print("Object  'x' ") # Object  'x' 
print(x . __dict__) # {'c':30, 'e':50, 'j':100}



'''
static  variable  --->a=10 b=20 d=40 f=60 g=70 i=90 h=80 

Object 'x'  --->c=30 e=50 j=100
'''


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'
print(c1 . __dict__) # {'a':1,'b':2,'c':3}


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

output:
Enter  any  number    :  10
Enter  any  number  :  20
Enter  any  number  :  30
Enter  any  number  :  40
Enter  any  number  :  50
Enter  any  number  :  60
Enter  any  number  :  70
13      21      31      12
13      41      51      13
13      61      71      14


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
class  vector:
	@staticmethod
	def get1():
		vecotr.n=int(input('Enter number of elements:'))
	def get2(self):
		self.a=[]
                for i in range(vector.n):
                    val = int(input(f"Enter element {i+1}: "))
                    self.a.append(val)
	def add(self , x , y):
		self.a = []
                for i in range(vector.n):
                    self.a.append(x.a[i] + y.a[i])
vector.get1() #How  to  call  get1()  method
a = vector()
b = vector()
c = vector()
a.get2() #How  to  read  the  list  into  1st  object
b.get2() #How  to  read  the  list  into  2nd  object  'b'
c.add(a, b) #How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(c.a) #How  to  print  the  list  of  3rd   object


'''
static  variable  --->  

Object  'x'   ---> 

Object  'y'   ---> 

Object  'z'   --->  
'''



'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
b=c1.__dict__
a={}
for x,y in b.items():
    if x.startswith('__') or x.endswith('__'):
        pass
    else:
       a[x]=y
print(a)




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


