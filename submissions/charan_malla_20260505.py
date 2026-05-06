class  parent:
	def  m1(self):
		print('Overridden  Method')
class  child(parent):
	def  m1(self):
		print('Overriding  Method')
# End  of  the  class
x = parent()
x . m1()  
x = child()
x . m1()
'''
overidden method
overidding method
'''


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
x . m1()
x . m2()
#x . m3()  #error
x = child()
x . m1()
x . m2()
x . m3()

'''
m1  method  of  parent  class
m2  method  of  parent class
m1  method  of  child  class
m2  method  of  parent class
m3  method  of  child  class'
'''


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
c . marriage()
c . property()
c . study()
'''
Love Marriage
One  Crore
Studies only 
 + Entertainment
'''


class  parent:
	def  add(self , x , y):
		return  x + y
class  child(parent):
	def   add(self , x , y , z):
		return   x + y + z
# End  of  the  class
c = child()
print(c . add(10 , 20 , 30)) 
#print(c . add(10 , 20)) error
print(super(child , c) . add(40,50))

'''
60
90
'''



class  parent:
	def   m1(self , a , b , /):
		print(F'parent  method  --->   a  :  {a}  \t  b  :  {b}')
class  child(parent):
	def   m1(self , x , y):
		print(F'child  method  --->  x  :  {x}  \t  y  :  {y}')
# End of the class
c = child()
c . m1(x = 10 , y = 20)
c . m1(30 , 40)
'''
child  method  --->  x  :  10, y:20
child  method  --->  x  :  30  y  : 40 
'''


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
		print('c5 class  constructor')
# End  of  the  class
#c1()  
c2() 
#c3() error because it child class ABC and it has abstract method  
c4() 
#c5() error because it child class ABC and it has abstract method  
#c5()

'''

c2  class  constructor

c4  class  constructor

'''




import   math
from  abc  import  *
class  shape(ABC):
	def   get(self):
		pass
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
		self.a=float(input("enter value side 1"))	
		self.b=float(input("enter value side 2"))	
		self.c=float(input("enter value side 3"))	
		self.s=(self.a + self.b + self.c) / 2
	def   area(self):		
		return math.sqrt(self.s * (self.s - self.a) *  (self.s -self. b) * (self.s -self. c))
	def   peri(self):
		return self.a + self.b + self.c
	def   test(self):
		if  self.a + self.b > self.c and self.a + self.c>self.b and self.b + self.c >self.a:
				return True
		
		else:
			print('Not    a  triangle')
			return False
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		self.r=float(input("enter radius : "))
	def   area(self):
		return  3.14159 * self.r **2 
	def   peri(self):
		return   2 * 3.14159 * self.r

	def  test(self):
		if  self.r <0:
			print('Radius  can  not  be  -ve')
			return False
		return True
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		self.l=float(input("enter length : "))
		self.b=float(input("enter breadth : "))
	def   area(self):
		return  self.l*self.b
	def   peri(self):
		return  2*(self.l+self.b)
	def  test(self):
		if  self.l==self.b:
			print('Not  a rectangle')
			return False
		return True
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		self.s=float(input("enter the any side : "))
	def   area(self):
		return  self.s*self.s
	def   peri(self):
		return  self.s*4
	def  test(self):
		if self.s<=0:
			print("invalid inputs")
			return False
		return True
			
def   menu():
	print('1. Triangle')
	print('2. Circle')
	print('3. Rectangle')
	print('4. Square')
	print('5. Exit')
# End  of  menu  function
def   operation(s):
	s.get()
	if s.test():
		print('Area  :  ' , s.area())
		print('Perimeter  :  ' ,s.peri())   
# End  of  the  function

while  False:  
	menu()
	ch = eval(input('Enter  choice  :  ')) 
	match   ch:
		case  1:
			s=triangle()
			operation(s)
		case  2:
			s=circle()
			operation(s)
		case  3:
			s=rectangle()
			operation(s)
		case  4:
			s=square()
			operation(s)
		case  5:
			break
	# End  of  match
# End of while  loop
print('Good  Bye')




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
a . m3() #m3  method  of  ggc  class
a . m2() #m2  method  of  gc  class
a . m1()#m1  method  of  child  class
#arent()  error
#child()  error
#gc() error

'''

'''