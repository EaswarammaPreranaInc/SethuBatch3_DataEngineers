'''
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
		self.real = int(input("Enter real input: "))
		self.img = int(input("Enter img input : "))
	def    __str__(self):
		if self.img < 0:
			return f'{self.real} - {abs(self.img)}i'
		else:
			return f'{self.real} + {self.img}i'
	def  __add__(a ,  b):
		c = complex()
		c.real = a.real + b.real
		c.img = a.img + b.img
		return c
	def  __sub__(a ,  b):
		c = complex()
		c.real = a.real - b.real
		c.img = a.img - b.img
		return c
	def  __mul__(a ,  b):
		c = complex()
		c.real = (a.real*b.real)-(a.img*b.img)
		c.img = (a.real*b.img)+(a.img*b.real)
		return c
	def  __truediv__(a ,  b):
		#How  to  divide  objects   a  and  b
		c = complex()
		if b.img < 0:
			temp = int(math.pow(b.real,2) + math.pow(b.img,2))
			c.real = (a.real*b.real)-(a.img*b.img)
			c.img = (a.real*b.img)+(a.img*b.real)
		else:
			temp = int(math.pow(b.real,2) + math.pow(b.img,2))
			c.real = (a.real*b.real)+(a.img*b.img)
			c.img = (a.img*b.real)-(a.real*b.img)
		if c.img < 0:
			return f'{c.real}/{temp} - {abs(c.img)}/{temp}i'
		else:
			return f'{c.real}/{temp} + {c.img}/{temp}i'		    
		    
# End  of  the  class
a = complex()
b = complex()
a.get()
b.get()
print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)

''' Output:
Enter real input: 3
Enter img input : 4
Enter real input: 5
Enter img input : 6
Sum :   8 + 10i
Difference :   -2 - 2i
Product :   -9 + 38i
Division  : 39/61 + 2/61i
'''
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

3) What  is  the  method  call  to  _gt()  method ?  ---> a > b   (or)  a . __gt_(b)
     What  is  the  method  call  to  _lt()  method ?  ---> a < b  (or)  a . __lt_(b)
     What  is  the  method  call  to  _eq()  method ?  --->  a == b   (or)  a . __eq_(b)
     What  is  the  method  call  to  _ge()  method ?  --->  a >= b   (or) a . __ge_(b)
     What  is  the  method  call  to  _le()  method ?  ---> a <= b  (or)  a . __le_(b)
     What  is  the  method  call  to  _ne()  method ?  --->  a != b  (or)  a . __ne_(b)
'''
import  math
class  Rat:
	def get(self):
		self.nr = int(input("Enter the numerator : "))
		self.dr = int(input("Enter the denominator : "))
	def __gt__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 > c2
	def __lt__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 < c2
	def __eq__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 == c2
	def __ge__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 >= c2
	def __le__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 <= c2
	def __ne__(self,b):
		c1 = self.nr*b.dr
		c2 = b.nr*self.dr
		return c1 != c2

#  End  of   the  class
a = Rat()
b = Rat()
a.get()
b.get()
if  a > b :
	print(f'{a.nr}/{a.dr} > {b.nr}/{b.dr}')
if  a < b :
	print(f'{a.nr}/{a.dr} < {b.nr}/{b.dr}')
if  a == b :
	print(f'{a.nr}/{a.dr} == {b.nr}/{b.dr}')
if  a >= b :
	print(f'{a.nr}/{a.dr} >= {b.nr}/{b.dr}')
if  a <= b :
	print(f'{a.nr}/{a.dr} <= {b.nr}/{b.dr}')
if  a != b:
	print(f'{a.nr}/{a.dr} != {b.nr}/{b.dr}')

''' Output:
Enter the numerator : 2
Enter the denominator : 3
Enter the numerator : 5
Enter the denominator : 9
2/3 > 5/9
2/3 >= 5/9
2/3 != 5/9

'''
# Find  outputs  (Home  work)
class   outer:
	def  _init_(self):
		print('Outer  class  constructor')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def _init_(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer() # Outer  class  constructor
o.m1() # Outer  class  method
i = o.inner() # Inner  class  constructor
i.m1() # Inner  class  method
a = outer.inner() # Inner  class  constructor
a.m1() # Inner  class  method
b = outer().inner().m1() # Outer  class  constructor <nextline> Inner  class  constructor <nextline> Inner  class  method
i = inner() # Error because inner class is not created directly

# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25
		self.ename ='Rama Rao'
		self.sal = 10000.0
		self.d = emp.date()
	def   disp(self):
		print(f'Empno : {self.empno} Ename : {self.ename} Sal : {self.sal} ')
		self.d.disp()
	class  date:
		def __init__(self):
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			print(f'Date : {self.dd}-{self.mm}-{self.yy}')
# End  of  the  class
e = emp()
e.disp()

# Object  'e'  ---> empno = 25 , ename = 'Rama Rao' , sal = 10000.0 , d = emp.date()

''' Outputs:
Empno : 25 Ename : Rama Rao Sal : 10000.0 
Date : 15-8-1947
'''

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25
		self.in1 = outer.inner1()
		self.in2 = outer.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer()
o.disp()
o.in1.disp()
o.in2.disp()

# Object  'o'  ---> x = 25 , in1 = outer.inner1() , in2 = outer.inner2()

''' Output:
25
1st  inner  class  method
2nd  inner  class  method
'''

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
c_out = c1()
c_in = c_out.c2()
c = c2()

''' Output:
outer  class  c1  constructor
inner  class  c2  constructor
outer  class  c2  constructor
'''
# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
c_outer = c2() # outer  class  constructor
c_inner1 = c_outer.c2() # inner  class  constructor
c_inner2 = c2.c2() # inner  class  constructor
c_inner3 = c2().c2() # outer  class  constructor <nextline> inner  class  constructor

''' Output:
outer  class  constructor
inner  class  constructor
inner  class  constructor
outer  class  constructor
inner  class  constructor
'''