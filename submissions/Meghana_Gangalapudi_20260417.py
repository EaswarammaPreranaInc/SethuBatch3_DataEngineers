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
print(a . x)  # 30
print(a . y)  # 20
print(b . x)  # 30
print(b . y) # 20
print(c1 . x , c1 . y) # 30 40
#print(cls . x , cls . y) error
#print(self . x , self . y) error


'''
static   variable   ---> x=30,y=40

object  'a'   ---> y=20

object  'b'   --->y=20
'''
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() # static method
a = c1()
a . m1() #static method
#c1 . m1(25) # error

class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) # 25
a = c1() 
a . m1(35) #35
# a . m1() # error


class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #static  method  becoz calling with class  name
a = c1()
# . m1()  #  How  is  method  m1()  treated  i.e.  static  method  (or)  instance  method
#a . m1(35)  # instance becoz calling with object error


class   c1:
	def   m1():
		print("method")
#  End  of  the   class
c1 . m1() #  
a = c1()
#a . m1()  # error


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
a . m1()   # static / instance  method type and address



class   c1:
	x = 25
	def   __init__(self):
		print(c1.x) 
		print(self.x)
	def   m1(self):
		print(self.x)
		print(c1.x)
		#print(cls . x) Error
	@classmethod
	def   m2(cls):
		print(c1.x)
		print(cls.x)
		 #print(self . x) error
	@staticmethod
	def   m3():
		print(c1.x)
		#print(cls . x) # error
		#print(self . x) # error
# End  of  the  class
print(c1.x)
#print(x) error
#print(self . x) Error
#print(cls . x) error
c1.m1(c1())
c1.m2()
c1.m2()




class   c1:
	a=10
	def    __init__(self):
		c1.b=20
		self.c=30
		#cls . k = 25 erro
	def   m1(self):
		c1.d=40
		self.e=50
	@classmethod
	def   m2(cls):
		c1.f=60
		cls.g=70
		#self . k = 25 error
	@staticmethod
	def   m3():
		c1.h=80
		#self . k = 25 #error
		#cls . k = 35  #error
#End  of  the  class
print('Outside  the  class') 
print(c1 . __dict__) #{a:10,ev's}
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__) #{a:10.b:20}
print()
print()
x.m1()
print('Instance  method  m1')
print(c1 . __dict__) #{a:10,b:20,d:40}
print()
print()
c1.m2()
print('class  method   m2') 
print(c1 . __dict__) #{a:10,b:20,d:40,f:60,g:70}
print()
print()
c1.m3()
print('static   method   m3')
print(c1 . __dict__)#{a:10,b:20,d:40,f:60,g:70,h:80}
print()
print()
c1.i=90
x.j=100

print('Outside  the  class')
print(c1 . __dict__)  # #{a:10,b:20,d:40,f:60,g:70,h:80,i:90}
print()
print()
print("Object  'x' ")
print(x . __dict__)#{c:30,e:50,j:100}



'''
static  variable  ---> a=10,b=20,d=40,f=60.g=70

Object 'x'  ---> c=30,e=50
'''


class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #1
print(c1.b)  #2
print(c1.c)  #3
print(c1 . __dict__) #{a:1,b:2,c:3,ev's}


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
static   variable   ---> x:13

Object  'a'  ---> y:21,z:31,x=12

Object  'b'  --->y:41,z:51,x:13

Object  'c'  --->y:61,z:71,x:14

13 21 31 12
13 41 51 13
13 61 71 14

'''
class Vector:
	@staticmethod
	def get1():
		Vector.n=int(input("enter the number of values"))
	def get2(self):
		self.a=[]
		for i in range(Vector.n):
			v=int(input(f"enter the{i+1}th values :"))
			self.a.append(v)
	def add(self,x,y):
		self.a=[]
		for i in range(Vector.n):
			val=x.a[i]+y.a[i]
			self.a.append(val)
Vector.get1()
x=Vector()
y=Vector()
z=Vector()
print("first object ")
x.get2()
print("second object")
y.get2()
z.add(x,y)
print(f"results {z.a}")


class  c1:
	x = 1
	y = 2
	z = 3
di=dict()
for x in c1.__dict__:
	if (x.startswith("__") and x.endswith("__")):
		pass
	else:
	  di[x]=c1.__dict__[x]
		
print(di)
#  End  of  the  class