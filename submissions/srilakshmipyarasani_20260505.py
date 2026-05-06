1) outputs 
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1() #Overridden Method
x = child()
x . m1() #Overriding Method

2) outputs  
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
c . marriage()#Love Marriage
c . property()#One Crore
c . study()#Studies <tab> + Entertainment

3) outputs   
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
x . m1()#m1  method  of  parent  class
x . m2()#m2  method  of  parent class
x . m3()#Error because m3 is not defined  
x = child()
x . m1()#m1  method  of  child  class
x . m2()#m2  method  of  Parent  class
x . m3()#m3  method  of  child  class

4) outputs  
class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30)) #60
print(c . add(10 , 20))#Error because z is not given
print(super(child , c) . add(40,50))#90

5) outputs 
class  parent:
	def  add(self , x , y):
		print('parent  method')
		return  x + y
class  child(parent):
	def   add(self , x , y , z = 3):
		print('child  method')#Child Method
		return  x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30))#60
print(c . add(10 , 20))#33

6) outputs  
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)#child  method  --->  x  :  10  	  y  :  20
c . m1(30 , 40)#child  method  --->  x  :  30  	  y  :  40

7) outputs 
from  abc  import  ABC , abstractmethod
class  c1(ABC):
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c1  class  constructor')
class  c2(ABC):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c2  class  constructor')
class  c3:
	@abstractmethod
	def  m1(self):
		pass
	def  _init_(slef):
		print('c3  class  constructor')
class  c4(c1):
	def  m1(self):
		pass
	def  _init_(slef):
		print('c4  class  constructor')
class  c5(c1):
	def  _init_(slef):
		print('c1  class  constructor')
# End  of  the  class
c1()#Error because it is not valid
c2()
c3() 
c4() 
c5()

8) Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

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
	   How  to  read  value  of  'a'
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
		   self.a = float(input('Side a: '))
                   self.b = float(input('Side b: '))
                   self.c = float(input('Side c: ')) #How  to  read  the  3  sides  of  triangle		
	def   area(self):		
	    s = (self.a + self.b + self.c) / 2
            return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c)) #return  area  of  triangle
	def   peri(self):
	   return self.a + self.b + self.c #return  perimeter  of  triangle
	def   test(self):
		if (self.a + self.b > self.c and
                    self.b + self.c > self.a and
                    self.c + self.a > self.b):
                    return True
                else:
                    print('Not a triangle')
                    return False
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		self.a = float(input()) #How  to  read  radius
	def   area(self):
		return 3.14159 * self.a ** 2 #return  area  of  circle
	def   peri(self):
		return 2 * 3.14159 * self.a #return  circumference  of circle
	def  test(self):
		self.r < 0:
	        print('Radius cannot be -ve')
                return False
        return True
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		self.a = float(input())
                self.b = float(input()) #How  to  read  length  and  breadth		
	def   area(self):
		return self.a * self.b #return  area  of  rectangle
	def   peri(self):
		return 2 * (self.a + self.b) #return  perimeter  of  triangle
	def  test(self):
		if self.a == self.b: #if  length  and   breadth  same
		    print('Not  a rectangle')
		     return False
                return True #How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		self.a = float(input()) #How  to  read  the  side
	def   area(self):
		return self.a ** 2 #return  area  of  square
	def   peri(self):
		return 4 * self.a #return  perimeter  of  square
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
	s.get() #How  to  read  inputs  to  object  's'
	if not s.text(): 
		return #How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' , round(s.area(),2))
	print('Perimeter  :  ' ,  round(s.peri(),2)
# End  of  the  function
shape()  
while  True:  
	menu()
	ch = eval(input('Enter  choice  :  ')) 
	match   ch:
		case  1:
			operation (triangle()) #How  to  call  operation()  function
		case  2:
			operation (circle()) #How  to  call  operation()  function
		case  3:
			operation (rectangle()) #How  to  call  operation()  function
		case  4:
			operation(square()) #How  to  call  operation()  function
		case  5:
				How  to  stop  execution
	# End  of  match
# End of while  loop
print('Good  Bye')


#  Object  's'   --->

9) outputs 
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
a . m3()#m3  method  of  ggc  class
a . m2()#m2  method  of    gc  class
a . m1()#m1  method  of  child  class
parent() #Error because not possible
child()  #Error because not possible
gc()#Error because not possible

10) Save  in  any  file  of  cwd
from p1 import mod1 #How  to  import  mod1  of  package  p1  with  from  statement
print(mod1.x) #How  to  print  object  'x'  of   mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of   mod1  in  package  p1
obj = mod1.c1()
obj.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print(p1 . mod1 . x)  #Error not valid
print()
print()
from p1.mod1 import x, f1, c1 #How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement
print(x) #How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
obj = c1() 
obj.m1() #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
print(p1 . p2 . mod2 . x)  
from  p1  import   p2 . mod2  
from  p2  import  mod2

11) Save  in  any  file  of  cwd
from p1.mod1 import * #How  to  import  members  of  mod1  in   package  p1
print(x) #How  to  print  object  'x'  of   mod1  in  package  p1
f1() #How  to  call  function  f1()  of   mod1  in  package  p1
obj = c1() 
obj.m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
from p1.p2.mod2 import * #How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1
print(x) #How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1
f1() #How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1
obj = c1() 
obj.m1() #How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1
from  p1  import  mod1 . *#Error because it is not valid



