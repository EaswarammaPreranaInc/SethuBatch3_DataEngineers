'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object
1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 																																		39 / 61 + 2i / 61
'''

import math

class complex:

    def get(self):
        self.real = int(input("Enter the real value:"))        #How  to  read  real  and  imag
        self.imag = int(input("Enter the imag value:"))

    def __str__(self):
        if self.imag > 0:
            return f'{self.real}+{self.imag} i'  #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
        return f'{self.real}-{abs(self.imag)}i'

    def __add__(a, b):
        c = complex()
        c.real = a.real + b.real    #How  to  add  objects  a  and  b
        c.imag = a.imag + b.imag
        return c

    def __sub__(a, b):
        c = complex()
        c.real = a.real - b.real    #How  to  subtract  objects  a  and  b
        c.imag = a.imag - b.imag
        return c

    def __mul__(a, b):
        c = complex()
        c.real = a.real * b.real - a.imag * b.imag 
        c.imag = a.real * b.imag + a.imag * b.real
        return c           #How  to  multiply  objects  a  and   b

    def __truediv__(a, b):
        c = complex()
        denom = b.real**2 + b.imag**2
        c.real =round((a.real * b.real + a.imag * b.imag)) // denom
        c.imag = round((a.imag * b.real - a.real * b.imag))//denom
        return c
         #How  to  divide  objects   a  and  b

# End  of  the  class

a = complex()
b = complex()  # How  to  create  two  complex  class  objects

a.get()  # How  to  read   inputs  into  1st  object
b.get()  # How  to  read   inputs  into  2nd  object

print('Sum :  ', a + b)
print('Difference :  ', a - b)
print('Product :  ', a * b)
print('Division  : ', a / b)


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
     What  is  the  method  call  to  _ne()  method ?  --->  a != b  (or)  a . __ne_(b)'''


import math

class Rat:

    def get(self):
        self.nr = int(input("enter nr:"))  #How  to  read  numerator  and  denominator  into  object
        self.dr = int(input("enter dr:"))

    def __gt__(self, b):
        if self.nr * b.dr > self.dr * b.nr:
            return self.nr * b.dr >= self.dr * b.nr

    def __lt__(self, b):
        if self.nr * b.dr < self.dr * b.nr:
            return self.nr * b.dr < self.dr * b.nr

    def __eq__(self, b):
        if self.nr * b.dr == self.dr * b.nr:
            return self.nr * b.dr < self.dr * b.nr

    def __ge__(self, b):
        if self.nr * b.dr >= self.dr * b.nr:
            return self.nr * b.dr >= self.dr * b.nr

    def __le__(self, b):
        if self.nr * b.dr <= self.dr * b.nr:
            return self.nr * b.dr <= self.dr * b.nr

    def __ne__(self, b):
        if self.nr * b.dr != self.dr * b.nr:
            return self.nr * b.dr != self.dr * b.nr


#  End  of   the  class

a = Rat()
b = Rat()  #How  to  create  two  Rat   class  objects  'a'  and  'b'
a.get()  #How  to  read  1st  rational   number  into  object  'a'
b.get()  #How  to  read  2nd  rational   number  into  object  'b'
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
		def _init_(self):
			print('Inner  class  constructor')
		def m1(self):
			print('Inner  class  method')
#end of the class
a=outer()#
a.m1()#How  to  call  m1()  method  of  outer  class
b=a.inner()#
outer.inner().m1()#How  to  call  m1()  method  of  inner  class
b.m1()#How  to  call  m1()  method  of  inner  class  in  another  way
a.inner().m1()#How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()#error we cannot create the inner class object directly without the outer class 
# 



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
		self.empno=25
		self.ename='Rama Rao'
		self.sal=1000.0   # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.a=self.date()#How  to  create  date  class  object
	def   disp(self):
		print(f'empno:{self.empno }' , f'ename: {self. ename}' , f'sal:  {self.sal}',sep="\n")#How  to  print  empno , ename , sal  of  object  self
		self.a.disp()#How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			self.dd=15#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.mm=8
			self.yy=1947
		def disp(self):
			  print(f"{self.dd}/{self.mm}/{self.yy}")#How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e=emp()
e.disp() #How  to  call  disp()  method  of  emp  class



# Object  'e'  --->empno=25 ,  ename='Rama  Rao' ,sal= 10000.0


# Find outputs (Home  work)
class  outer:
	def  _init_(self):
		self.x=25#How  to  initialize  variable  'x'  of  object  self  to  25
		b=outer.inner1()#How  to  create  inner1  class  object
		c=outer.inner2()#How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o=outer()#
o.m1()#How  to  call   disp()  method  of outer  class
o.inner1().m1#How  to  call   disp()  method  of inner1  class
o.inner2().m1#How  to  call   disp()  method  of inner2  class


# Object  'o'  --->x=25


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
a=c1()#How  to  create  c1  class  object
b=a.c2()#How  to  create  inner  c2  class  object
c=c2()#How  to  create  outer  c2  class  object






# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
o=c2()#How  to  create  outer  c2  class  object
i=o.c2()#How  to  create  inner  c2  class  object
a=c2.c2()#How  to  create  inner  c2  class  object  in  another  way
How  to  create  inner  c2  class  object  in  one  more  way ## not possible can only create in two ways only 