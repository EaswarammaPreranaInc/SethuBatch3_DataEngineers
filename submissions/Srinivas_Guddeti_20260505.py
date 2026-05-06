#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1()  #Overridden  Method
x = child()
x . m1()  #Overriding  Method



# Find  outputs   (Home  work)
class   parent:
	def  m1(self):
		print('m1  method  of  parent  class')
	def  m2(self):
		print('m2  method  of  parent class')
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
	def  m3(self):
		print('m3  method  of  child  class')
# End  of  the  class
x = parent()
x . m1()  #m1  method  of  parent  class
x . m2()  #m2  method  of  parent class
x . m3()  #error-no m3 class in parent class
x = child()
x . m1()  #m1  method  of  child  class
x . m2()  #m2  method  of  parent class
x . m3()  #m3  method  of  child  class



# Find  outputs  (Home  work)
class  parent:
	def  marriage(self):
		print('Arranged Marriage')
	def  property(self):
		print('One  Crore')
	def  study(self):
		print('Studies only' , end = '\t')
class  child(parent):
	def  marriage(self):
		print('Love Marriage')
	def  study(self):
		super() . study()
		print(' + Entertainment')
# End  of  the  class
c = child()  
c . marriage()  #Love Marriage
c . property()  #One  Crore
c . study()  #Studies only	 + Entertainment






# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))   #60
print(c . add(10 , 20))  #error-child add() is expecting 3 args,but we are sending only 2
print(super(child , c) . add(40,50))  #90







# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')
		return  x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))
'''
child  method
60
'''
print(c . add(10 , 20))
'''
child  method
33
'''





#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)  #child  method  --->  x  :  10		y  :  20
c . m1(30 , 40)   #child  method  --->  x  :  30		y  :  40





# Find  outputs (Home  work)
from  abc  import  ABC , abstractmethod
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()  #error-we cant create object because it is abstract class and has abstract method
c2()  #c2  class  constructor
c3()  #c3  class  constructor
c4() #c4  class  constructor
c5()  #error-when parent class has ABC ,child has to implement abstract method





import math
from abc import *
class shape(ABC):
	def get(self):
		pass
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def peri(self):
		pass
	@abstractmethod
	def test(self):
		pass

class triangle(shape):
	def get(self):
		print('Enter 3 sides of triangle')
		self.a = float(input())
		self.b = float(input())
		self.c = float(input())
	def area(self):
		s = (self.a + self.b + self.c) / 2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def peri(self):
		return self.a + self.b + self.c
	def test(self):
		if self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b:
			pass
		else:
			print('Not a triangle')
			exit()

class circle(shape):
	def get(self):
		print('Enter radius of circle : ', end='\t')
		self.a = float(input())
	def area(self):
		return 3.14159 * self.a ** 2
	def peri(self):
		return 2 * 3.14159 * self.a
	def test(self):
		if self.a < 0:
			print('Radius can not be -ve')
			exit()

class rectangle(shape):
	def get(self):
		print('Enter length and breadth of rectangle')
		self.a = float(input())
		self.b = float(input())
	def area(self):
		return self.a * self.b
	def peri(self):
		return 2 * (self.a + self.b)
	def test(self):
		if self.a == self.b:
			print('Not a rectangle')
			exit()

class square(shape):
	def get(self):
		print('Enter any side of square : ', end='\t')
		self.a = float(input())
	def area(self):
		return self.a ** 2
	def peri(self):
		return 4 * self.a
	def test(self):
		pass

def menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
def operation(s):
	s.get()
	s.test()
	print('Area : ', s.area())
	print('Perimeter : ', s.peri())


while True:
	menu()
	ch = int(input('Enter choice : '))

	match ch:
		case 1:
			operation(triangle())
		case 2:
			operation(circle())
		case 3:
			operation(rectangle())
		case 4:
			operation(square())
		case 5:
			exit()
print('Good Bye')





# Find  outputs (Home  work)
from   abc    import    *
class   parent(ABC):
	@abstractmethod
	def  m1(self):
		pass
	@abstractmethod
	def  m2(self):
		pass
	@abstractmethod
	def  m3(self):
		pass
class  child(parent):
	def  m1(self):
		print('m1  method  of  child  class')
class  gc(child):
	def  m2(self):
		print('m2  method  of    gc  class')
class  ggc(gc):
	def  m3(self):
		print('m3  method  of  ggc  class')
# End  of  the  class
a = ggc()
a . m3()  #m3  method  of  ggc  class
a . m2()  #m2  method  of    gc  class
a . m1()  #m1  method  of  child  class
parent()  #error-we cant create object because it is abstract class and has abstract method
child()  #error-we cant create object because it is abstract class and has abstract method(because of m2 and m3)
gc()  #error-we cant create object because it is abstract class and has abstract method(inherited m1 m3)




# Save  in  any  file  of  cwd
from p1 import mod1 # How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() # How  to  call  function  f1()  of   mod1  in  package  p1
obj = mod1.c1()
obj.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)  # ERROR because p1 is not imported
print()
print()
from p1.p2 import mod2 # How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
obj2 = mod2.c1()
obj2.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)  # ERROR because p1 and p2 are not imported
from  p1  import   p2 . mod2  # ERROR because p2 is not imported
from  p2  import  mod2 # ERROR because p2 is in p1 which is to be called wrt to p1 


# Save  in  any  file  of  cwd
from p1.mod1 import * # How  to  import  members  of  mod1  in   package  p1
print(x) # How  to  print  object  'x'  of   mod1  in  package  p1
f1() # How  to  call  function  f1()  of   mod1  in  package  p1
obj = c1()
obj.m1() # How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * # How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) # How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() # How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
obj2 = c1()
obj2.m1() # How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . * # ERROR because '.' can't be used in import clause
