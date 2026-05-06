#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1()	#Overridden  Method
x = child()
x . m1()	#Overriding  Method



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
c . marriage()	#Love Marriage
c . property()	#One Crore
c . study()	#Studies only	 + Entertainment




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
x = parent()	#x is a parent object
x . m1()	#m1 method of parent class
x . m2()	#m2 method of parent class
x . m3()	#error parent object has no attribute 'm3'  
x = child()	#x is a child object
x . m1()	#m1  method  of  child  class
x . m2()	#m2  method  of  parent class
x . m3()	#m3  method  of  child  class




# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))	#60 
print(c . add(10 , 20))		#error positional argument is missing
print(super(child , c) . add(40,50))






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
print(c . add(10 , 20 , 30))	#child method <next> 60
print(c . add(10 , 20))		#child method <next> 33




#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)	   #child  method  --->  x  :  10  	  y  :  20
c . m1(30 , 40)		   #child  method  --->  x  :  30  	  y  :  40





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
c1()		#error   
c2() 		#c2 class constructor
c3()		#c3 class constructor 
c4()		#c4 class constructor 
c5()		#error




import math
from abc import ABC, abstractmethod

# Parent class
class shape(ABC):

    @abstractmethod
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


# Triangle class
class triangle(shape):

    def get(self):
        print('Enter 3 sides of triangle:')
        self.a = float(input('a = '))
        self.b = float(input('b = '))
        self.c = float(input('c = '))

    def test(self):
        if (self.a + self.b > self.c and
            self.b + self.c > self.a and
            self.c + self.a > self.b):
            return True
        else:
            print('Not a triangle')
            return False

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# Circle class
class circle(shape):

    def get(self):
        self.r = float(input('Enter radius of circle: '))

    def test(self):
        if self.r < 0:
            print('Radius cannot be negative')
            return False
        return True

    def area(self):
        return 3.14159 * self.r ** 2

    def peri(self):
        return 2 * 3.14159 * self.r


# Rectangle class
class rectangle(shape):

    def get(self):
        print('Enter length and breadth:')
        self.l = float(input('Length = '))
        self.b = float(input('Breadth = '))

    def test(self):
        if self.l == self.b:
            print('Not a rectangle (it is a square)')
            return False
        return True

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)


# Square class
class square(shape):

    def get(self):
        self.a = float(input('Enter side of square: '))

    def test(self):
        return True

    def area(self):
        return self.a ** 2

    def peri(self):
        return 4 * self.a


# Menu
def menu():
    print('\n1. Triangle')
    print('2. Circle')
    print('3. Rectangle')
    print('4. Square')
    print('5. Exit')


# Operation function
def operation(s):
    s.get()
    if s.test():
        print('Area :', s.area())
        print('Perimeter :', s.peri())


# Main program
while True:
    menu()
    ch = int(input('Enter choice: '))

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
            break
        case _:
            print('Invalid choice')

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
a . m3()   # m3  method  of  ggc  class
a . m2()   # m2  method  of    gc  class
a . m1()   # m1  method  of  child  class
#parent()  # Error
#child()   # Error
#gc()      # Error
'''

# Save  in  any  file  of  cwd
from p1 import mod1 #How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) # How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
a=mod1.c1() 
a.m1()                   #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
#print(p1 . mod1 . x)   #Error 
print()
print()
from p1.p2 import mod2  #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)		#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1()		 #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=mod2.c1() 
a.m1()				 #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#print(p1 . p2 . mod2 . x)  #Error
#from  p1  import   p2 . mod2  #Error
#from  p2  import  mod2  	#Error

# Save  in  any  file  of  cwd
from p1.mod1 import x as x1, f1 as f11, c1 as c11 	# How  to  import  members  of  mod1  in   package  p1
print(x1)						 #How  to  print  object  'x'  of   mod1  in  package  p1
f11() 							#How  to  call  function  f1()  of   mod1  in  package  p1
a=c11() 
a.m1()							 #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import *					 #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) 						#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() 							#How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1()							 #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . *				 #Error