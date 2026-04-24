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
		self.real=int(input('Enter real: '))
                self.imag=int(input('Enter imag: '))
	def    __str__(self):
		 if self.imag >= 0:
                      return f"{self.real} + {self.imag}i"
                 else:
                      return f"{self.real} - {abs(self.imag)}i"
	def  __add__(a ,  b):
		res = complex()
                res.real = a.real + b.real
                res.imag = a.imag + b.imag
                return res
	def  __sub__(a ,  b):
		res = complex()
                res.real = a.real - b.real
                res.imag = a.imag - b.imag
                return res
	def  __mul__(a ,  b):
		res = complex()
                res.real = a.real*b.real - a.imag*b.imag
                res.imag = a.real*b.imag + a.imag*b.real
                return res
	def  __truediv__(a ,  b):
		res = complex()
                den = b.real**2 + b.imag**2
                res.real = (a.real*b.real + a.imag*b.imag) / den
                res.imag = (a.imag*b.real - a.real*b.imag) / den
                return res
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
	    self.nr = int(input("Enter numerator: "))
            self.dr = int(input("Enter denominator: "))
	def __gt__(self,b):
			return self.nr * b.dr > self.dr * b.nr
	def __lt__(self,b):
			return self.nr * b.dr < self.dr * b.nr
	def __eq__(self,b):
			return self.nr * b.dr == self.dr * b.nr
	def __ge__(self,b):
			return self.nr * b.dr >= self.dr * b.nr
	def __le__(self,b):
			return self.nr * b.dr <= self.dr * b.nr
	def __ne__(self,b):
			return self.nr * b.dr != self.dr * b.nr
#  End  of   the  class
a = Rat()
b = Rat()
a.get()
b.get()
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
a.m1()
b=outer.inner()
b.m1()
o = outer()
i = o.inner()
i.m1()
outer.inner().m1()
i = inner() # error



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno = 25
                self.ename = 'Rama Rao'
                self.sal = 10000.0
		self.d = self.date()
	def   disp(self):
		print("Emp No:", self.empno)
                print("Emp Name:", self.ename)
                print("Salary:", self.sal)
                self.d.disp()
	class   date:
		def    __init__(self):
			self.dd = 15
                        self.mm = 8
                        self.yy = 1947
		def disp(self):
			print("Date:", self.dd, "/", self.mm, "/", self.yy)
# End  of  the  class
e = emp()
e.disp()



# Object  'e'  --->



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x = 25
                self.i1 = self.inner1()
                self.i2 = self.inner2()
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
o.i1.disp()
o.i2.disp()


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
a = c2()
b = a.c2()
c2().c2()