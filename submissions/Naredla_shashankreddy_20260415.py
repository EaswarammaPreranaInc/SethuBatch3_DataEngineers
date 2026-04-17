Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 
																																							39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		self.real=int(input('Enter real part: '))
		self.imag=int(input('Enter imaginary part: '))
	def    __str__(self):
		return f'{self.real}+{self.imag}i' if self.imag>0 else f'{self.real}{self.imag}i'
	def  __add__(a ,  b):
		c=complex()
		c.real=a.real+b.real
		c.imag=a.imag+b.imag
		return c
	def  __sub__(a ,  b):
		c=complex()
		c.real=a.real-b.real
		c.imag=a.imag-b.imag
		return c
	def  __mul__(a ,  b):
		c=complex()
		c.real=a.real*b.real-a.imag*b.imag
		c.imag=a.real*b.imag+b.real*a.imag
		return c
	def  __truediv__(a ,  b):
		c=complex()
		c.real=(a.real*b.real+a.imag*b.imag)/(math.pow(b.real,2)+math.pow(b.imag,2))
		c.imag=(a.real*b.imag-b.real*a.imag)/(math.pow(b.real,2)+math.pow(b.imag,2))
		return c
# End  of  the  class
a=complex()# How  to  create  two  complex  class  objects
b=complex()
a.get()# How  to  read   inputs  into  1st  object
b.get()# How  to  read   inputs  into  2nd  object
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)



'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  ---> False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  ---> False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  ---> True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  --->  True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  __gt__()  method ?  ---> a > b   (or)  a . __gt__(b)
     What  is  the  method  call  to  __lt__()  method ?  ---> a < b  (or)  a . __lt__(b)
     What  is  the  method  call  to  __eq__()  method ?  --->  a == b   (or)  a . __eq__(b)
     What  is  the  method  call  to  __ge__()  method ?  --->  a >= b   (or) a . __ge__(b)
     What  is  the  method  call  to  __le__()  method ?  ---> a <= b  (or)  a . __le__(b)
     What  is  the  method  call  to  __ne__()  method ?  --->  a != b  (or)  a . __ne__(b)
'''
import  math
class  Rat:
	def  get(self):
		self.num=int(input('Enter numerator: '))
		self.den=int(input('Enter denominator: '))
	def __gt__(self,b):
			return  True  if self.num*b.den>self.den*b.num else False
	def __lt__(self,b):
			return  True  if self.num*b.den<self.den*b.num else False
	def __eq__(self,b):
			return  True  if self.num*b.den==self.den*b.num else False
	def __ge__(self,b):
			return  True  if self.num*b.den>=self.den*b.num else False
	def __le__(self,b):
			return  True  if self.num*b.den<=self.den*b.num else False
	def __ne__(self,b):
			return  True  if self.num*b.den!=self.den*b.num else False
#  End  of   the  class
a=Rat()# How  to  create  two  Rat   class  objects  'a'  and  'b'
b=Rat()
a.get()# How  to  read  1st  rational   number  into  object  'a'
b.get()# How  to  read  2nd  rational   number  into  object  'b'
if  a  > b:
	print('>')
if  a  <  b:
	print('<')
if  a==b:
	print('==')
if  a>=b:
	print('>=')
if  a<= b:
	print('<=')
if  a!=b:
	print('!=')

# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o=outer()
o.m1()# How  to  call  m1()  method  of  outer  class
i=o.inner()
i.m1()# How  to  call  m1()  method  of  inner  class
outer().inner().m1()# How  to  call  m1()  method  of  inner  class  in  another  way
o.inner().m1()# How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()  #error
'''
Outer  class  constructor
Outer  class  method
Inner  class  constructor
Inner  class  method
Outer  class  constructor
Inner  class  constructor
Inner  class  method
Inner  class  constructor
Inner  class  method

'''


class   emp:
	def __init__(self):
		# How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno=25
		self.ename='Rama Rao'
		self.sal=10000.0
		d=self.date() # How  to  create  date  class  object

	def   disp(self):
		# How  to  print  empno , ename , sal  of  object  self
		print(self.empno)
		print(self.ename)
		print(self.sal)
		# How  to  call  disp()  method  of  date  class
		d=self.date()
		d.disp()
	class   date:
		def    __init__(self):
			# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd=15
			self.mm=8
			self.yy=1947
		def disp(self):
			# How  to  print  dd , mm , yy  of  object  self
			print(self.dd)
			print(self.mm)
			print(self.yy)
# End  of  the  class
e=emp()
e.disp()# How  to  call  disp()  method  of  emp  class



# Object  'e'  --->empno=25, ename=='Rama Rao', sal=10000.0



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25 # How  to  initialize  variable  'x'  of  object  self  to  25
		a=self.inner1() # How  to  create  inner1  class  object
		b=self.inner2() # How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o=outer()
o.disp() # How  to  call   disp()  method  of outer  class
a=o.inner1()
a.disp() # How  to  call   disp()  method  of inner1  class
b=o.inner2()
b.disp() # How  to  call   disp()  method  of inner2  class


# Object  'o'  ---> x=25


# Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('outer  class  c1  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def __init__(self):
		print('outer  class  c2  constructor')
#end of the class
a=c1() # How  to  create  c1  class  object
b=a.c2() # How  to  create  inner  c2  class  object
c=c2() # How  to  create  outer  c2  class  object


# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a=c2()# How  to  create  outer  c2  class  object
b=a.c2()# How  to  create  inner  c2  class  object
c=c2().c2()# How  to  create  inner  c2  class  object  in  another  way
d=c2.c2()# How  to  create  inner  c2  class  object  in  one  more  way