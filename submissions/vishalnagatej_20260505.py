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
		a = self.a     # How  to  read  value  of  'a'
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
		a = self.a   #  to  read  the  3  sides  of  triangle	
		b = self.b	
		c = self.c
	def   area(self):
		s = self.a + self.b + self.c / 2		
		return  math.sqrt(s * (s - self.a) *  (s - self.b) * (s - self.c))  # area  of  triangle
	def   peri(self):
		return  self.a + self.b  + self.c    # perimeter  of  triangle
	def   test(self):
		if  self.a + self.b > self.c or self.b + self.c > self.a or self.c + self.a > self.b  # sum  of  every  2  sides  should  be  >   3rd   side
				pass
		else:
			print('Not    a  triangle')
			exit()  # How  to  stop  execution
class   circle(shape):
	def   get(self):
		print('Enter  radius  of  circle  : ' , end = '\t')
		r = self.r       # How  to  read  radius
	def   area(self):
		return  3.14159 * self.r ** 2     # area  of  circle
	def   peri(self):
		return  2 * 3.14159 * self.r     # circumference  of circle
	def  test(self):
		if  self.r < 0:
		    print('Radius  can  not  be  -ve')
        # exit()     # How  to  stop  execution
class   rectangle(shape):
	def  get(self):
		print('Enter  length  and  breadth  of  rectangle')
		l = self.r       # How  to  read  length  and  breadth		
		b = self.b
	def   area(self):
		return  self.l * self.b         # area  of  rectangle
	def   peri(self):
		return  2 * (self.l + self.b)   # perimeter  of  triangle
	def  test(self):
		if  self.l == self.b :
		    print('Not  a rectangle')
		    # exit()  # How  to  stop  execution
class   square(shape):
	def   get(self):
		print('Enter  any  side  of  square :  ' , end =  '\t')
		a = self.a
	def   area(self):
		return  self.a ** 2     # area  of  square
	def   peri(self):
		return  4 * self.a      # perimeter  of  square
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
	How  to  read  inputs  to  object  's'
	How  to  test  inputs  are  valid  (or)  not
	print('Area  :  ' ,  ???)
	print('Perimeter  :  ' ,  ???)
# End  of  the  function
shape()  
while  True:  
	menu()
	ch = eval(input('Enter  choice  :  ')) 
	match   ch:
		case  1:
				How  to  call  operation()  function
		case  2:
				How  to  call  operation()  function
		case  3:
				How  to  call  operation()  function
		case  4:
				How  to  call  operation()  function
		case  5:
				How  to  stop  execution
	# End  of  match
# End of while  loop
print('Good  Bye')


#  Object  's'   --->