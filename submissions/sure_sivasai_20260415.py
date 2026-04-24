#1.
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
class complex:
	def  get(self):
		self.real = int(input('Enter real value : '))
		self.imag = int(input('Enter img value : '))
	def    __str__(self):
		if self.imag < 0:
			return f'{self.real} - {-1*self.imag}i'
		else:
			return f'{self.real} + {self.imag}i'
	def  __add__(a , b):
		add = complex()
		add.real = a.real + b.real
		add.imag = a.imag + b.imag
		return add
	def  __sub__(a ,  b):
		sub = complex()
		sub.real = a.real-b.real
		sub.imag = a.imag-b.imag
		return sub
	def  __mul__(a ,  b):
		mul = complex()
		mul.real = (a.real*b.real)-(a.imag*b.imag)
		mul.imag = (a.real*b.imag)+(a.imag*b.real)
		return mul
	def  __truediv__(a ,  b):
		div = complex()
		div.real = ((a.real*b.real) + (a.imag*b.imag)) / ((b.real*b.real) + (b.imag*b.imag))
		div.imag = ((a.imag*b.real) - (a.real*b.imag)) / ((b.real*b.real) + (b.imag*b.imag))
		return div
# End  of  the  class
a = complex()
b = complex()
a.get()
b.get()
print('Sum :  ' ,a+b)
print('Difference :  ' ,a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)

#---------------------------------------------
#2.

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
class  rat:
    def  get(self):
        self.n = int(input('Enter numerator : '))
        self.d = int(input('Enter denominator : '))
    def __gt__(self,b):
        return  True if (self.n*b.d) > (self.d*b.n) else False
    def __lt__(self,b):
        return  True if (self.n*b.d) < (self.d*b.n) else False
    def __eq__(self,b):
        return  True if (self.n*b.d) == (self.d*b.n) else False
    def __ge__(self,b):
        return  True if (self.n*b.d) >= (self.d*b.n) else False
    def __le__(self,b):
        return  True if (self.n*b.d) >= (self.d*b.n) else False
    def __ne__(self,b):
        return  True if (self.n*b.d) >= (self.d*b.n) else False
#  End  of   the  class
#How  to  create  two  Rat   class  objects  'a'  and  'b'
a = rat()
b = rat()
#How  to  read  1st  rational   number  into  object  'a'
a.get()
#How  to  read  2nd  rational   number  into  object  'b'
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

#-----------------------------------------------------------

#3.Find  outputs  (Home  work)
class outer:
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
o = outer()
o.m1()                # How  to  call  m1()  method  of  outer  class
i = o.inner()
i.m1()                # How  to  call  m1()  method  of  inner  class
outer.inner().m1()    # How  to  call  m1()  method  of  inner  class  in  another  way
i = outer.inner()     # How  to  call  m1()  method  of  inner  class  in  one  more  way
i.m1()
#i = inner()

#-------------------------------------

#4.Find  outputs  (Home  work)
class emp:
	def __init__(self):
		#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		#How  to  create  date  class  object
		self.d = self.date()
	def disp(self):
		#How  to  print  empno , ename , sal  of  object  self
		print(self.__dict__)
		#How  to  call  disp()  method  of  date  class
		self.d.disp()
	class date:
		def    __init__(self):
			#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd = 15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			#How  to  print  dd , mm , yy  of  object  self
			print(self.__dict__)
# End  of  the  class
#How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()

#------------------------------------------------------

#5.Find outputs (Home  work)
class  outer:
	def  __init__(self):
		#How  to  initialize  variable  'x'  of  object  self  to  25
		self.x = 25
		#How  to  create  inner1  class  object
		self.i = self.inner1()
		#How  to  create  inner2  class  object
		self.j = self.inner2()
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
#How  to  call   disp()  method  of outer  class
o.disp()
#How  to  call   disp()  method  of inner1  class
o.inner1().disp()
#How  to  call   disp()  method  of inner2  class
o.inner2().disp()

# Object  'o'  --->

#---------------------------------------------------------

#6.Find  outputs  (Home  work)
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
#How  to  create  c1  class  object
c = c1()
#How  to  create  inner  c2  class  object
i = c.c2()
#How  to  create  outer  c2  class  object
d = c2()

#-------------------------------------------------

#7.Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
#How  to  create  outer  c2  class  object
c = c2()
#How  to  create  inner  c2  class  object
d = c.c2()
#How  to  create  inner  c2  class  object  in  another  way
e = c2.c2()
#How  to  create  inner  c2  class  object  in  one  more  way
f = c2.c2
f()

















