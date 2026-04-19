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
print(cls . x , cls . y)#cls is not access outside the clas we have to claa with class_name i.e c1.x and c1.y
print(self . x , self . y)#we should call with respect to object but not self outside the class obj.variable_name


'''
static   variable   --->x=10

object  'a'   --->y=20

object  'b'   --->y=20'''


 #  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1()#static  method
a = c1()
a . m1()#static  method
c1 . m1(25)#error static method doesnot accept the agument in this case but we are passing 25



#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)#25
a = c1()
a . m1(35)#35
a . m1()#error due to static method  demands anrgument and the method call wit respect to obj is not sending it to the static method 


#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #treated as static method #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
a = c1()
a . m1()  #instance method due to prepix obj#  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
a . m1(35)#static call # What  about  here

#  Find  outputs
class   c1:
	def   m1():
		print()
#  End  of  the   class
c1 . m1() #nothing is printed 
a = c1()
a . m1()#error no instance method m1 in class c1 ,and in this call a is passed to m1() which is static method where m1() not allow   arguments 

# 
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
c1 . m1(25)#static  method<nxt>25
a = c1()
a . m1()#static / instance  method<nxt>type and address of the object.
# 


# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(x)#error there is no local variable x and global variable x 
	def   m1(self):
		print(c1.x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(cls . x)#error there is no cls  ie error cls for the static method argument but not for regular method,if it is self.x it may ok 
	@classmethod
	def   m2(cls):
		print(cls.x)#How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		print(self . x)#error we cannot print it with another than cls.var_name or class_name.var_name ie,error 
	@staticmethod
	def   m3():
		print(c1.x)#How  to  print  static  variable  'x'
		print(cls . x)#errorthere is no cls  ie error cls for the static method argument but not for regular method,if it is self.x it may ok 
		print(self . x)#error we cannot print it with another than cls.var_name or class_name.var_name ie,error 
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
print()#How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)#error, outside the clss we cant use self as obj name we should only use objname only
print(cls . x)# error ,outside the class method we cant use the class method so error 
a=c1()#
a.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()  or 
a.m3()#How  to  call  method  m3()




 # How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10#How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20#How  to  add  static  variable  'b'  with  value  20
		c1.c=30#How  to  add  instance  variable  'c'  with  value  30
		cls . k = 25#error no cls outside the class method so error only self is accepted other than that computer asks whts is cls 
	def   m1(self):
		c1.d=40#How  to  add  static  variable  'd'  with  value  40
		c1.e=50#How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		c1.f=60#How  to  add  static  variable  'f'  with  value  60
		cls.g=70#How  to  add  static  variable  'g'  with  value  70  in  another  way
		self . k = 25#error inside class we use cls or class name no self to use here in class method so ie error 
	@staticmethod
	def   m3():
		c1.h=80#How  to  add  static  variable  'h'  with  value  80
		self . k = 25#error inside class we use cls or class name no self to use here in class method so ie error 
		cls . k = #error inside static method no  self to use here in static  method   
#End  of  the  class
print('Outside  the  class')#Outside  the  class
print(c1 . _dict_)#{10}
print()#nothing 
print()#nothing
x = c1()
print('Constructor')#Constructor
print(c1 . _dict_)#{'a':10,'b':20,'c':30}
print()#nothing
print()#nothing
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')#Instance  method  m1
print(c1 . _dict_)#{'a':10,'b':20,'c':30,'d'=:40,'e':50}
print()#nothing
print()#nothing
c1.m1()#How  to  call  m2()  method
print('class  method   m2')#class  method   m2
print(c1 . _dict_)#{'a':10,'b':20,'c':30,'d'=:40,'e':50,'f':60,'g':70}
print()#nothing
print()#nothing
c1.m3()#How  to  call  m3()  method
print('static   method   m3')#static   method   m3
print(c1 . _dict_)#{'a':10,'b':20,'c':30,'d'=:40,'e':50,'f':60,'g':70,'h':80}
print()#nothing
print()#nothing
c1.i=90#How  to  add  static  variable  'i'  with  value  90
x.j=100#How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')#Outside  the  class
print(c1 . _dict_)#{'a':10,'b':20,'c':30,'d'=:40,'e':50,'f':60,'g':70,'h':80}
print()#nothing
print()#nothing
print("Object  'x' ")#Object  type and address of x 
print(x . _dict_)#{'j':100}



'''
static  variable  --->a=10,b=20,c=30,d=40,e=50,f=60,g=70,h=80,i=90

Object 'x'  --->j=100
'''



# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)#1,2,3
# End  of  the  class
c1.a#How  to  print  variable  'a'
c1.b#How  to  print  variable  'b'
c1.c#How  to  print  variable  'c'
print(c1 . __dict__)#{'a':1,'b':2,'c':3}






# Tricky  program
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):#class method
		cls . x = int(input('Enter  any  number    :  '))#10
	def  get2(self):#instance method
		self . y = int(input('Enter  any  number  :  '))
		self . z = int(input('Enter  any  number  :  '))
	def   compute(self):#instance method
		Test . x += 1
		self . y  += 1
		self . z  += 1
		self . x  += 1
	def    disp(self):#instance method
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()#x=12
b . compute()#13
c . compute()#14
a . disp()#13      21      31      12
b . disp()#13      41      51      13
c . disp()#13      61      71      14


'''
# static   variable   --->x=13

# Object  'a'  --->y=21,z=31

# Object  'b'  --->y=41,z=51

# Object  'c'  --->y=61,z=71

'''
'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  --->  x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  ---> x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n'''

class  vector:
	@staticmethod
	def get1():
		vector.n=int(input("Enter the n value:"))#  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.a=[]#How  to  read  the  list  into  the  object
		for i in range(vector.n):
                        val = int(input(f"Enter element {i}: "))
                        self.a.append(val)
	def add(self , x , y):
		self.a=[]
		for i in range(vector.n):
		        self.a.append(x.a[i]+y.a[i])##How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
vector.get1()#How  to  call  get1()  method
a=vector()#
print("Enter elements of vector a:")
a.get2()#How  to  read  the  list  into  1st  object
b=vector()#
print("Enter elements of vector b:")
b.get2()#How  to  read  the  list  into  2nd  object  'b'
c=vector()#
c.add(a,b)#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print("resultvector c:",c)#How  to  print  the  list  of  3rd   object



'''
static variable ---> n = 3

Object 'x' ---> x.a = [1, 2, 3]

Object 'y' ---> y.a = [4, 5, 6]

Object 'z' ---> z.a = [5, 7, 9]
'''





