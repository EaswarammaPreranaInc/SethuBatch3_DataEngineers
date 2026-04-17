1) outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()#Static Method
a = c1()
a . m1()#static method
c1 . m1(25)#Error because of 25

2) outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35
a . m1()#Error because expected 1 argument but 0 argument is given

3) outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method #Static method
a = c1()
a . m1()  #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method #Instance method
a . m1(35)  # What  about  here

4) outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() #Nothing
a = c1()
a . m1()#Nothing

5) outputs
class   c1:
	@staticmethod
	def  m1(self):
		print('static  method')
		print(self)
	def  m1(self):
		print('static / instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25)#static / instance  method
	    25
a = c1()
a . m1()#static / instance  method
	 Type and address

6) How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   _init_(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(x)
	def   m1(self):
		print(c1.x) #How  to  print  static  variable  'x'
		print(self.x) #How  to  print  static  variable  'x'  in  another  way
		print(cls . x)
	@classmethod
	def   m2(cls):
		print(cls.x) #How  to  print  static  variable  'x'
		print(c1.x) #How  to  print  static  variable  'x'  in  another  way
		print(self . x)
	@staticmethod
	def   m3():
		print(c1.x) #How  to  print  static  variable  'x'
		print(cls . x)
		print(self . x)
# End  of  the  class
print(c1.x) #How  to  print  static  variable  'x'
print(self.x) #How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
obj = c1() 
obj.m1()#How  to  call  method  m1()
c1.m2() 
obj.m2()#How  to  call  method  m2()
c1.m3() 
obj.m3()#How  to  call  method  m3()

7) How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 #How  to  add  static  variable  'a'  with  value  10
	def    _init_(self):
		c1.x = 20 #How  to  add  static  variable  'b'  with  value  20
		self.c = 30 #How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25
	def   m1(self):
		c1.d = 40 #How  to  add  static  variable  'd'  with  value  40
		self.e = 50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f = 60 #How  to  add  static  variable  'f'  with  value  60
		c1.g = 70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25
	@staticmethod
	def   m3():
		c1.h = 80 #How  to  add  static  variable  'h'  with  value  80
		self . k = 25
		cls . k = 35
#End  of  the  class
print('Outside  the the  class')
print(c1 . _dict_)
print()
print()
x = c1()
print('Constructor')
print(c1 . _dict_)
print()
print()
x.m1() #How  to  call  m1()  method
print('Instance  method  m1')
print(c1 . _dict_)
print()
print()
c1.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . _dict_)
print()
print()
c1.m3() #How  to  call  m3()  method
print('static   method   m3')
print(c1 . _dict_)
print()
print()
c1.i = 90 #How  to  add  static  variable  'i'  with  value  90
x.j = 100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . _dict_)
print()
print()
print("Object  'x' ")
print(x . _dict_)



'''
static  variable  --->

Object 'x'  --->
'''
8) outputs  
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'
print(c1 . _dict_)

9) Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 
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
# 13 21 31 12
  13 41 51 13
  13 61 71 14


'''
static   variable   --->x = 16

Object  'a'  ---> y = 21, z = 31

Object  'b'  ---> y = 41, z = 51

Object  'c'  ---> y = 61, z = 71
'''

10) Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n
'''
class  vector:
	@staticmethod
	def get1():
		vector.n = int(input("Enter number of elements: "))
#How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a = [] #How  to  read  the  list  into  the  object
                for i in range(vector.n):
                    self.a.append(int(input("Enter element: ")))
	def add(self , x , y):
		 self.a = []
                 for i in range(vector.n):
                      self.a.append(x.a[i] + y.a[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1() #How  to  call  get1()  method
x = vector() #How  to  read  the  list  into  1st  object
y = vector() #How  to  read  the  list  into  2nd  object  'b'
z = vector() 
x.get2()
y.get2()

z.add(x. y)
print("Result:", z.a) #How  to  print  the  list  of  3rd   object


'''
static  variable  --->  vector.n

Object  'x'   ---> x.a

Object  'y'   ---> y.a

Object  'z'   --->  z.a
'''


11) Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . _dict_

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  clas
for k, v in c1.__dict__.items():
    if not (k.startswith('__') and k.endswith('__')):
        print(k, '=', v)

