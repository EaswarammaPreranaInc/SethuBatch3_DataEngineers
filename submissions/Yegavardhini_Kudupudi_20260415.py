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
		self.real = int(input('Enter first rational number : ')) #  How  to  read  real  and  imag
                self.imag = int(input('Enter second rational number : '))
	def    __str__(self):
                 if self.imag >= 0:
		     return  F'{self . real}+{self.imag}i'  # How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
                 else:
                     return f'{self.real} - {-self.imag}i'
	def  __add__(self,other):
                c=complex()  # How  to  add  objects  a  and  b
                c.real = self.real + other.real
                c.imag = self.imag + other.imag
                return c
	def  __sub__(a ,  b):
		c = complex() # How  to  subtract  objects  a  and  b
                c.real = self.real - other.real
                c.imag = self.imag - other.imag
                return c
	def  __mul__(a ,  b):
		c = complex() # How  to  multiply  objects  a  and   b
                c.real =  self.real * other.real - self.imag * other.imag
                c.imag = self.real * other.imag + self.imag * other.real
                return c
        def  __truediv__(a ,  b):
		c = complex() # How  to  divide  objects   a  and  b
                denom = other.real**2 + other.imag**2
                c.real = (self.real * other.real + self.imag * other.imag) / denom
                c.imag = (self.imag * other.real - self.real * other.imag) / denom
                return c
# End  of  the  class
a = complex() # How  to  create  two  complex  class  objects
b = complex()
a.get() # How  to  read   inputs  into  1st  object
b.get() # How  to  read   inputs  into  2nd  object
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
		self.nr = int(input('Enter numerator : ')) #  How  to  read  numerator  and  denominator  into  object
                self.dr = int(input('Enter denominator : '))
                while self.dr == 0:
                    self.dr = int(input('Denominator cannot be zero, re-enter: '))
	def __gt__(self,b):
			return  self.nr * b.dr > self.dr * b.nr  # true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return  self.nr * b.dr < self.dr * b.nr  # true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return  self.nr * b.dr == self.dr * b.nr # true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return  self.nr * b.dr >= self.dr * b.nr # true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return  self.nr * b.dr <= self.dr * b.nr # true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
			return  self.nr * b.dr != self.dr * b.nr # true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = Rat() # How  to  create  two  Rat   class  objects  'a'  and  'b'
b = Rat()
a.get() # How  to  read  1st  rational   number  into  object  'a'
b.get() # How  to  read  2nd  rational   number  into  object  'b'
if a > b:
    print('>')
if a < b:
    print('<')
if a == b:
    print('==')
if a >= b:
    print('>=')
if a <= b:
    print('<=')
if a != b:
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
a=outer()
a.m1() # How  to  call  m1()  method  of  outer  class
outer.inner().m1() # How  to  call  m1()  method  of  inner  class
i = outer.inner()
   i.m1()  # How  to  call  m1()  method  of  inner  class  in  another  way
# How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25
                self.ename = 'Rama Rao'
                self.sal = 10000.0   # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.d = emp.date()  # How  to  create  date  class  object
	def   disp(self):
		print(self.empno, self.ename, self.sal) #  How  to  print  empno , ename , sal  of  object  self
		self.d.disp() # How  to  call  disp()  method  of  date  class
	class   date:
		def __init__(self):
			self.dd = 15
                        self.mm = 8
                        self.yy = 1947
# How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			 print(self.dd, self.mm, self.yy) # How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp()
e.disp() # How  to  call  disp()  method  of  emp  class



# Object  'e'  --->




# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = outer.inner1() # How  to  create  inner1  class  object
                self.i2 = outer.inner2() # How  to  create  inner2  class  object

	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a = outer()
a.disp()  # How  to  call   disp()  method  of outer  class
a.i1.disp() # How  to  call   disp()  method  of inner1  class
a.i2.disp() # How  to  call   disp()  method  of inner2  class


# Object  'o'  --->




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
b=c1.c2() # How  to  create  inner  c2  class  object
a=c2() # How  to  create  outer  c2  class  object



# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a=c2()  #  How  to  create  outer  c2  class  object
b=c2.c2() # How  to  create  inner  c2  class  object
How  to  create  inner  c2  class  object  in  another  way
How  to  create  inner  c2  class  object  in  one  more  way