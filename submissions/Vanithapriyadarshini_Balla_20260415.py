import  math
class  complex:
	def  get(self):
		self.r=eval(input("Enter real for 1st "))
		self.im=eval(input("Enter imag for 1st "))
	def    __str__(self):
		return f'{self.r} + {self.im}i'
	def  __add__(a ,  b):
		c=complex()
		c.r=a.r+b.r
		c.im=(a.im+b.im)
		return c
	def  __sub__(a ,  b):
		c = complex()
		c.r = a.r - b.r
		c.im = a.im - b.im
		return c
	def  __mul__(a ,  b):
		c = complex()
		c.r = a.r*b.r - a.im*b.im
		c.im = a.r*b.im + a.im*b.r
		return c
	def  __truediv__(a ,  b):
		c = complex()
		dn = b.r**2 + b.im**2
		c.r = math.floor((a.r*b.r + a.im*b.im) / dn,2)
		c.im = math.floor((a.im*b.r - a.r*b.im) / dn)
		return c
# End  of  the  class
a=complex()
b=complex()
a.get()
b.get()
print('Sum :  ' , a.__add__(b))
print('Difference :  ' , a.__sub__(b))
print('Product :  ' ,  a.__mul__(b))
print('Division  : ' , a.__truediv__(b))

import  math
class  Rat:
	def  get(self):
			self.nr=eval(input("Enter 1st num nr : "))
			self.dr=eval(input("Enter 1st num dr : "))
	def __gt__(self,b):
		print(self.nr*b.dr > self.dr*b.nr)
 #return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
		print(self.nr*b.dr < self.dr*b.nr)
	def __eq__(self,b):
		print(self.nr*b.dr == self.dr*b.nr) #return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
		print(self.nr*b.dr >= self.dr*b.nr) #return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
		print(self.nr*b.dr <= self.dr*b.nr) #return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
		print(self.nr*b.dr != self.dr*b.nr)#return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a=Rat()
b=Rat()
a.get()
b.get()
if  a.__gt__(b):
	print('>')
if  a.__lt__(b):
	print('<')
if  a.__eq__(b):
	print('==')
if  a.__ge__(b):
	print('>=')
if  a.__le__(b):
	print('<=')
if  a.__ne__(b):
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
o.m1()
i=o.inner()
i.m1()
outer().inner().m1()
outer.inner().m1()
#i = inner()# error, bcz we cannot call inner class without outer class obj 


# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno=25
		self.ename='Rama Rao'
		self.sal=10000.0 #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.date()
	def   disp(self):
		print(self.empno)
		print(self.ename)
		print(self.sal)
		self.date().disp() #How  to  call  disp()  method  of  date  class
	class   date:
		def __init__(self):
			self.dd=15
			self.mm=8
			self.yy=1947 #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			print(self.dd)
			print(self.mm)
			print(self.yy)
# End  of  the  class
eo=emp()
eo.disp()

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25
		self.inner1()
		self.inner2()
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
o.disp()
o.inner1().disp()
o.inner2().disp()



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
a=c1() #How  to  create  c1  class  object
b=a.c2() #How  to  create  inner  c2  class  object
c=c2()#How  to  create  outer  c2  class  object

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
o=c2()
i1=o.c2()
i2=c2.c2()
i3=c2().c2()