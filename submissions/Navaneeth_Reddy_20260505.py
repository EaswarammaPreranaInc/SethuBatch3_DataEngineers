
#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1() #Overridden  Method
x = child() 
x . m1() #Overriding  Method


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
x . m1() #m1  method  of  parent  class
x . m2() #m2  method  of  parent  class
x . m3()  #Error
x = child()
x . m1() #m1  method  of  child  class
x . m2() #m2  method  of  parent  class
x . m3() #m3  method  of  child  class'''


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
c . marriage() #Love Marriage
c . property() #One  Crore
c . study() #Studies only   + Entertainment'''


# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30)) #60
print(c . add(10 , 20)) #30
print(super(child , c) . add(40,50)) #90'''


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
print(c . add(10 , 20 , 30)) #60
print(c . add(10 , 20))#30'''

'''
output:
child  method
60
child  method
33 '''


#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20) #child  method  --->  x  :  10    y  :  20
c . m1(30 , 40) #child  method  --->  x  :  30    y  :  40


# Find  outputs (Home  work)
from  abc  import  ABC , abstractmethod
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(self):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  __init__(self):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  __init__(self):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  __init__(self):
		print('c4  class  constructor')
class  c5(c1):
	def  __init__(self):
		print('c1  class  constructor')
# End  of  the  class
c1() #Error  
c2() #c2  class  constructor
c3() #c3  class  constructor
c4() #c4  class  constructor
c5()#Error


'''
Write a program to determine area and perimeter of triangle, circle, rectangle and square

1) What is the parent class? ---> shape
   What are child classes? ---> triangle, circle, rectangle, square

2) What is the area of triangle? ---> sqrt(s * (s - a) * (s - b) * (s - c))
   What is the value of 's'? ---> (a + b + c) / 2
   What is the perimeter of triangle? ---> a + b + c

3) What is the area of circle? ---> 3.14159 * a^2 where 'a' is radius of circle
   What is the circumference of circle? ---> 2 * 3.14159 * a

4) What is the area of rectangle? ---> a * b where 'a' is length and 'b' is breadth
   What is the perimeter of rectangle? ---> 2 * (a + b)

5) What is the area of square? ---> a^2
   What is the perimeter of square? ---> 4 * a
'''

import math
from abc import *
class shape(ABC):
	def get(self):
		 # How to read value of 'a'
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
		print('Enter  3  sides  of  triangle')
		# How to read the 3 sides of triangle
		pass
	def area(self):
		return 0
	def peri(self):
		return 0
	def test(self):
		if False:
				pass
		else:
			print('Not    a  triangle')
			# How to stop execution
			raise SystemExit
class circle(shape):
	def get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		# How to read radius
		pass
	def area(self):
		return 0
	def peri(self):
		return 0
	def test(self):
		if False:
		    print('Radius  can  not  be  -ve')
		    # How to stop execution
		    raise SystemExit
class rectangle(shape):
	def get(self):
		print('Enter  length  and  breadth  of  rectangle')
		# How to read length and breadt
		pass
	def area(self):
		return 0
	def peri(self):
		return 0
	def test(self):
		if False:
		    print('Not  a rectangle')
		    # How to stop execution
		    raise SystemExit
class square(shape):
	def get(self):
		print('Enter  any  side  of  square :  ' , end = '\t')
		# How to read the side
		pass
	def area(self):
		return 0
	def peri(self):
		return 0
	def test(self):
		pass
def menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End of menu function
def operation(s):
	# How to read inputs to object 's'
	s.get()
	# How to test inputs are valid (or) not
	s.test()
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' ,  s.peri())
# End of the function
# shape() # Error as can't instantiate abstract class shape with abstract methods area, peri, test
while  True:
	menu()
	ch = eval(input('Enter  choice  :  '))
	match   ch:
		case  1:
				# How to call operation() function
				operation(triangle())
		case  2:
				# How to call operation() function
				operation(circle())
		case  3:
				# How to call operation() function
				operation(rectangle())
		case  4:
				# How to call operation() function
				operation(square())
		case  5:
				# How to stop execution
				raise SystemExit
	# End  of  match
# End of while  loop
print('Good Bye')


# Find  outputs (Home work)
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
a . m3() # m3  method  of  ggc  class
a . m2() # m2  method  of    gc  class
a . m1() # m1  method  of  child  class'''
# parent() # Error as can't instantiate abstract class parent with abstract methods m1, m2, m3
# child() # Error as can't instantiate abstract class child with abstract methods m2, m3
# gc() # Error as can't instantiate abstract class gc with abstract method m3


# Save in any file of cwd
from p1 import mod1
print(mod1.x)
mod1.f1()
a = mod1.c1()
a.m1()
print(p1 . mod1 . x)
print()
print()
from p1.p2 import mod2
print(mod2.x)
mod2.f1()
b = mod2.c1()
b.m1()
print(p1 . p2 . mod2 . x)
from p1 import p2 , mod2
from p2 import mod2
# Reason is that, package/module names must be imported before using qualified names like p1.mod1.x.


# Save in any file of cwd

from p1.mod1 import *
print(x)
f1()
a = c1()
a.m1()
print()
print()
from p1.p2.mod2 import *
print(x)
f1()
b = c1()
b.m1()
from p1 import mod1 . *

# Reason is that, wildcard import brings members directly into the current namespace; qualified package access needs package import first.