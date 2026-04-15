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
		self.r=int(input('Enter real part of the complex number'))
		self.i=int(input('Enter image part of the complex number'))
	def    __str__(self):
		if self.i > 0:
			return f'{self.r} + {self.i}i'
		return f'{self.r} - {-self.i}i'
        #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		add=complex()
		add.r=a.r+b.r
		add.i=a.i+b.i
		return add.__str__()
	def  __sub__(a ,  b):
		sub=complex()
		sub.r=a.r-b.r
		sub.i=a.i-b.i
		return sub.__str__()
	def  __mul__(a ,  b):
		mul=complex()
		mul.r=(a.r*b.r)-(a.i*b.i)
		mul.i=(a.r*b.i)+(a.i*b.r)
		return mul.__str__()
		#How  to  multiply  objects  a  and   b
	def  __truediv__(a ,  b):
		div=complex()
		den=b.r**2 + b.i**2 
		div.r=(a.r*b.r)+(a.i*b.i)
		div.i=(a.r*b.i)-(a.i*b.r)
		if div.i > 0:
			return f'{div.r}/{den} + {div.i}/{den}i'
		return f'{div.r}/{den} - {-div.i}/{den}i'
# End  of  the  class
a=complex()
b=complex()#How  to  create  two  complex  class  objects
a.get()#How  to  read   inputs  into  1st  object
b.get()#How  to  read   inputs  into  2nd  object
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

3) What  is  the  method  call  to  _gt()  method ?  ---> a > b   (or)  a . __gt_(b)
     What  is  the  method  call  to  _lt()  method ?  ---> a < b  (or)  a . __lt_(b)
     What  is  the  method  call  to  _eq()  method ?  --->  a == b   (or)  a . __eq_(b)
     What  is  the  method  call  to  _ge()  method ?  --->  a >= b   (or) a . __ge_(b)
     What  is  the  method  call  to  _le()  method ?  ---> a <= b  (or)  a . __le_(b)
     What  is  the  method  call  to  _ne()  method ?  --->  a != b  (or)  a . __ne_(b)
'''
import  math
class  Rat:
	def  get(self):
			self.nr=int(input('Enter numerator: '))
			self.dr=int(input('Enter numerator: '))
	def _gt_(self,b):
			if self.nr*b.dr > self.dr*b.nr:
				return True
			return False # when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			if self.nr*b.dr < self.dr*b.nr:
				return True
			return False #
			#return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
			if self.nr*b.dr == self.dr*b.nr:
				return True
			return False
			#return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
			if self.nr*b.dr >= self.dr*b.nr:
				return True
			return False
			#return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
		if self.nr*b.dr <= self.dr*b.nr:
			return True
		return False
			#return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
		if self.nr*b.dr != self.dr*b.nr:
				return True
		return False
			#return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a=Rat()#How  to  create  two  Rat   class  objects  'a'  and  'b'
b=Rat()
a.get()#How  to  read  1st  rational   number  into  object  'a'
b.get()#How  to  read  2nd  rational   number  into  object  'b'
if  a>b:
	print('>')
if  a<b:
	print('<')
if  a==b:
	print('==')
if  a  >=  b:
	print('>=')
if  a <= b:
	print('<=')
if  a!=b:
	print('!=')

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
outer().m1()#How  to  call  m1()  method  of  outer  class
outer().inner().m1()#How  to  call  m1()  method  of  inner  class
i=outer.inner()
i.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner() # error

# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		self.empno=25
		self.ename='Rama Rao'#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.sal=10000.0
		d=emp.date()
	def   disp(self):
		print(self.empno,self.ename,self.sal)#How  to  print  empno , ename , sal  of  object  self
		self.d.disp()#How  to  call  disp()  method  of  date  class
	class   date:
		def    _init_(self):
			self.dd=15
			self.mm=8
			self.yy=1947#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(self.dd, self.mm,self.yy)#How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
emp().disp()#How  to  call  disp()  method  of  emp  class



# Object  'e'  ---> # Find outputs (Home  work)
class  outer:
	def  _init_(self):
		self.x=25#How  to  initialize  variable  'x'  of  object  self  to  25
		i1=outer.inner1()#How  to  create  inner1  class  object
		i2=outer.inner2()#How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
outer.disp()#How  to  call   disp()  method  of outer  class
outer.inner1().disp()#How  to  call   disp()  method  of inner1  class
outer.inner2().disp()#How  to  call   disp()  method  of inner2  class


# Object  'o'  --->
# Find  outputs  (Home  work)
class   c1:
	def  _init_(self):
		print('outer  class  c1  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  c2  constructor')
#end of the class
class  c2:
	def _init_(self):
		print('outer  class  c2  constructor')
#end of the class
c=c1()#How  to  create  c1  class  object
ci=c.c2()#How  to  create  inner  c2  class  object
co=c2()#How  to  create  outer  c2  class  object

# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
c2o=c2()#How  to  create  outer  c2  class  object
c2i=c2.c2()#How  to  create  inner  c2  class  object
c2i=c2o.c2()#How  to  create  inner  c2  class  object  in  another  way
c2i=c2().c2()#How  to  create  inner  c2  class  object  in  one  more  way