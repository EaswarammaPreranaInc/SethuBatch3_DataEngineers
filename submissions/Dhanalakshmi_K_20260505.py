#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1() # Output: Overridden  Method
x = child()
x . m1() # Output: Overriding  Method

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
x . m1() # m1  method  of  parent  class
x . m2() # m2  method  of  parent class
x . m3()  # Error due to there is no m3 method in parent class
x = child()
x . m1() # m1  method  of  child  class
x . m2() # m2  method  of  parent class
x . m3() # m3  method  of  child  class

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
c . marriage() # Love marriage
c . property() # Studies only 
c . study() # Studies only + Enterainment 

# Find  outputs  (Home  work)
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))  # 60
print(c . add(10 , 20)) # Error due to less number of arguments 
print(super(child , c) . add(40,50)) # 90  

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
print(c . add(10 , 20 , 30)) # 60
print(c . add(10 , 20)) # 33

#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20) # child  method  --->  x  :  10  \t  y  :  20'
c . m1(30 , 40)  # child  method  --->  x  :  30  \t  y  :  40'

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
c1()  # Error
c2()  # c2  class  constructor 
c3() # c3  class  constructor
c4()  # c4  class  constructor
c5() # error

'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  ---> sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  --->  a * b  where  'a'  is  length and  'b'  is  breadth
     What  is  the  perimter  of  rectangle ?  ---> 2 * (a + b)

5) What  is  the  area  of  square ?  --->   a ^ 2
    What  is  the  perimeter  of  square  ?  --->  4 * a
'''
import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		 self.a=float(input("Enter a value : "))
	@abstractmethod
	def   area(self):
		pass
	@abstractmethod
	def  peri(self):
		pass
	@abstractmethod
	def  test(self):
		pass
class  triangle(shape):
	def   get(self):
		print('Enter  3  sides  of  triangle')
		super().get()
		self.b=float(input("Enter b value : "))	
		self.c=float(input("Enter c value : "))	
		self.s = (self.a + self.b + self.c) / 2
	def   area(self):		
		return  math.sqrt(self.s ((self.s -self.a)(self.s -self.b)*(self.s -self.c)))
	def   peri(self):
		return  self.a + self.b + self.c
	def   test(self):
		if (self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a):
				pass
		else:
			print('Not    a  triangle')
			exit()
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		super().get()
	def   area(self):
		return  math.pi * self.a **2
	def   peri(self):
		return  2*math.pi*self.a
	def  test(self):
		if self.a <0:
			print('Radius  can  not  be  -ve')
			exit()
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		super().get()
		self.b=float(input("Enter b value : "))		
	def   area(self):
		return  self.a * self.b
	def   peri(self):
		return  2*(self.a + self.b)
	def  test(self):
		if  self.a == self.b:
			print('Not  a rectangle')
			exit()
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		super().get()
	def   area(self):
		return  self.a**2
	def   peri(self):
		return  4 * self.a
	def  test(self):
		pass
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	s.get()
	s.test()
	print('Area  :  ' ,  s.area())
	print('Perimeter  :  ' ,  s.peri())
# End  of  the  function
shape()  
while  True:  
	menu()
	ch = eval(input('Enter  choice  :  ')) 
	match   ch:
		case  1:
				operation(triangle())
		case  2:
				operation(circle())
		case  3:
				operation(rectangle)
		case  4:
				operation(square())
		case  5:
				exit()
	# End  of  match
# End of while  loop
print('Good  Bye')

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
a . m3() # m3  method  of  ggc  class
a . m2() # m2  method  of    gc  class
a . m1() # m1  method  of    child class
parent() # Error
child()  # Error
gc() # Error

# Save  in  any  file  of  cwd
from p1 import mod1
print(mod1.x)#How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1()#How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1.c1()#How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
a.m1()
print(p1 . mod1 . x) # Error  
print()
print()
from p1.p2 import mod2 #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(mod2.x)#How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
mod2.f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a = mod2.c1()#How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
a.m1()
print(p1 . p2 . mod2 . x)  #Error
from  p1  import   p2 . mod2   # Error
from  p2  import  mod2 # Error

# Save  in  any  file  of  cwd
from p1.mod1 import x as x1, f1 as f11, c1 as c11 # How  to  import  members  of  mod1  in   package  p1
print(x1) #How  to  print  object  'x'  of   mod1  in  package  p1
f11() #How  to  call  function  f1()  of   mod1  in  package  p1
a=c11() 
a.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
a=c1()
a.m1() #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
#from  p1  import  mod1 . * #Error