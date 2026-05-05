#  Find  outputs  (Home  work)
class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1()#Overridden Method
x = child()
x . m1()#Overriding Method





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
c . marriage() #Love Marrirage
c . property() #One Crore
c . study()	#Studies only	Entertainment




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
x . m1() #m1 method of parent class
x . m2() #m2 method of parent class
x . m3() #error
x = child()
x . m1() #m1 method of child class
x . m2() #m2 method of parent class
x . m3() #m3 method of child class




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
print(c . add(10 , 20))	     #error
print(super(child , c) . add(40,50)) #90




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
print(c . add(10 , 20 , 30))# child method
			      60
print(c . add(10 , 20))     #child method
			      33




#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20) #child method  ----> x:{10}	y:{20}
c . m1(30 , 40)		#child method  ----> x:{30}	y:{40}





# Find  outputs (Home  work)
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
c1()  #error cuz its a proper abstract class
c2()  #works can create an c2 class object cus its not an abstract class
c3()  #works can create an c3 class object cus its not an abstract class
c4()  #works can create an c4 class object cus its not an abstract class
c5()  #error


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
		 How  to  read  value  of  'a' #self.a=float(input("enter value of a:"))
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
		How  to  read  the  3  sides  of  triangle
		self.a = float(input("a: "))
        	self.b = float(input("b: "))
        	self.c = float(input("c: "))		
	def   area(self):		
		s = (self.a + self.b + self.c) / 2
        	return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
	def   peri(self):
		return  perimeter  of  triangle     #return self.a + self.b + self.c
	def   test(self):
		if  self.a+self.b>self.c or self.b+self.c>self.c or self.c+self.a>b:
				pass
		else:
			print('Not    a  triangle')
			break
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		How  to  read  radius #self.a=float(input("enter radius of circle:"))
	def   area(self):
		return 3.14159 * self.r ** 2
	def   peri(self):
		return 2 * 3.14159 * self.r
	def  test(self):
		if  self.a<0
		    print('Radius  can  not  be  -ve')
		    break
cclass square(shape):

    def get(self):
        self.a = float(input("Enter side: "))

    def test(self):
        if self.a <= 0:
            print("Invalid side")
            return False
        return True

    def area(self):
        return self.a ** 2

    def peri(self):
        return 4 * self.a


# 🔹 Menu Function
def menu():
    print("\n1. Triangle")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")


# 🔹 Operation Function
def operation(s):
    s.get()
    if s.test():
        print("Area:", s.area())
        print("Perimeter:", s.peri())


# 🔹 Main Program
while True:
    menu()
    ch = int(input("Enter choice: "))

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
            print("Good Bye")
            break
        case _:
            print("Invalid choice")
#  Object  's'   --->





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
a . m3()
a . m2()
a . m1()
parent() 
child()  
gc()

'''
m3 method of ggc class
m2 method of gc class
m1 method of child class
'''



# Save  in  any  file  of  cwd
How  to  import  mod1  of  package  p1  with  from  statement #from p1 import mod1
How  to  print  object  'x'  of   mod1  in  package  p1       #print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1     #mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1  obj=mod1.c1
									obj.m1()

print(p1 . mod1 . x)  #error p1 is not imported
print()
print()

How  to  import  mod2  of  sub-package  p2  in  package  p1  with  from  statement	#from p1.p2 import mod2
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1		#print(mod2.x)
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1		#mod2.f1()
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1	#obj=mod2.c1()
												 obj.m1()
print(p1 . p2 . mod2 . x)  	#error p1,p2 is not imported	
from  p1  import   p2 . mod2  
from  p2  import  mod2




# Save  in  any  file  of  cwd
How  to  import  members  of  mod1  in   package  p1 		#from p1 import mod1
How  to  print  object  'x'  of   mod1  in  package  p1		#print(mod1.x)
How  to  call  function  f1()  of   mod1  in  package  p1	#mod1.f1()
How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1	#obj=mod1
									 obj.m1()
print()
print()
How  to  import  members  of  mod2  in  sub-package  p2  of   package  p1	#from p2.p1 import mod2
How  to  print  object  'x'  of   mod2  in  sub-package  p2  of  package  p1	#print(mod2.x)
How  to  call  function  f1()  of   mod2  in  sub-package  p2  of  package  p1	#mod2.f1()
How  to  call  method  m1()  of  class   c1   in  mod2  of  sub-package  p2  in  package  p1 	#obj=mod2.c1()
												 obj.m1()
