import  math
class  complex:
	def  get(self):
		self.real = int(input('Enter a number:'))
		self.imag = int(input('Enter a number:'))
	def __str__(self):
		if self.imag < 0:
			return eval(f'{self.real}-{self.imag}'+'j')
		if self.imag > 0:
			return eval(f'{self.real}+{self.imag}'+'j')
			
	def  __add__(a ,  b):
		return a.__str__()+b.__str__()
	def  __sub__(a ,  b):
		return a.__str__()-b.__str__()
	def  __mul__(a ,  b):
		return a.__str__()*b.__str__()
	def  __truediv__(a ,  b):
		return a.__str__()/b.__str__()
# End  of  the  class
a = complex()
b = complex()
a.get()
b.get()
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
			self.nr = int(input('1:'))
			self.dr = int(input('2:'))
	def __gt__(self,b):
			if self.nr/self.dr > b.nr/b.dr:
				return  True
	def __lt__(self,b):
			if self.nr/self.dr < b.nr/b.dr:
			    return True
			
	# def __eq__(self,b):
	# 		if self.nr/self.dr == b.nr/b.dr:
	# 		    return  True 
	# def __ge__(self,b):
	# 		if self.nr/self.dr >= b.nr/b.dr:
	# 		    return  True 
	# def __le__(self,b):
	# 		if self.nr/self.dr <= b.nr/b.dr:
	# 		    return  True 
#  End  of   the  class
a = Rat()
b = Rat()
a.get()
b.get()
if  a.__gt__():
	print('>')
if  a.__lt__():
	print('<')
# if  a.__eq__():
# 	print('==')
# if  a.__ge__():
# 	print('>=')
# if  a.__le__():
# 	print('<=')



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
a = outer()
a.m1
a = outer.inner()
a.m1()
outer.inner.m1(a)
a = outer()
a.inner.m1()
#i = inner() # Error

# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.00 
		global a
		a = emp.date()
	def   disp(self):
		print(self.empno, self.ename, self.sal)
		a.disp()
	class   date:
		def    __init__(self):
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			print(self.dd, self.mm, self.yy)
# End  of  the  class
b = emp()
b.disp()



# Object  'e'  --->

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25
		global a
		global b
		a = outer.inner1()
		b = outer.inner2() #How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer() #How  to  call   disp()  method  of inner1  class
i = outer.inner(o)


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
a = c1()
b = c1.c2()
c = c2()


# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2()
b = c2.c2()
c = a.c2()
