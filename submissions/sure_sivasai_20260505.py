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
x . m1()#m1  method  of  parent  class
x . m2()#m2  method  of  parent class
#x . m3() #error 
x = child()
x . m1()#m1  method  of  child  class
x . m2()#m2  method  of  parent class
x . m3()#m3  method  of  child  class


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
c . marriage()#Love Marriage
c . property()#One Crore
c . study()#Studies only  + Entertainment      


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
#print(c . add(10 , 20))#error
print(super(child , c) . add(40,50))#90

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
print(c . add(10 , 20 , 30))#Child method 60
print(c . add(10 , 20))#child method 33

#Find  outputs  (Home  work)
class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)#child method ----> x:10 y:20
c . m1(30 , 40)#child method ----> x:30 y:40

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
#c1()  #error 
c3() #c3  class  constructor
c4() #c4  class  constructor
#c5()


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
import math
from abc import ABC, abstractmethod

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


class triangle(shape):
    def get(self):
        print("Enter 3 sides of triangle")
        self.a = int(input("Side 1: "))
        self.b = int(input("Side 2: "))
        self.c = int(input("Side 3: "))

    def test(self):
        if not (self.a + self.b > self.c and 
                self.b + self.c > self.a and 
                self.a + self.c > self.b):
            print("Not a valid triangle")
            exit()

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


class circle(shape):
    def get(self):
        self.r = int(input("Enter radius: "))

    def test(self):
        if self.r <= 0:
            print("Invalid radius")
            exit()

    def area(self):
        return 3.14159 * self.r ** 2

    def peri(self):
        return 2 * 3.14159 * self.r


class rectangle(shape):
    def get(self):
        self.l = int(input("Length: "))
        self.b = int(input("Breadth: "))

    def test(self):
        if self.l <= 0 or self.b <= 0:
            print("Invalid dimensions")
            exit()

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)


class square(shape):
    def get(self):
        self.s = int(input("Side: "))

    def test(self):
        if self.s <= 0:
            print("Invalid side")
            exit()

    def area(self):
        return self.s ** 2

    def peri(self):
        return 4 * self.s


def menu():
    print("\n1. Triangle")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")


def operation(s):
    s.get()
    s.test()
    print("Area:", s.area())
    print("Perimeter:", s.peri())


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
a . m3()#m3  method  of  ggc  class
a . m2()#m2  method  of  gc  class
a . m1()#m1  method  of  child  class
#parent() #error
#child()  #error
#gc()#error