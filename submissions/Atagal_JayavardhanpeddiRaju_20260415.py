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
		How  to  read  real  and  imag
	def    _str_(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  _add_(a ,  b):
		How  to  add  objects  a  and  b
	def  _sub_(a ,  b):
		How  to  subtract  objects  a  and  b
	def  _mul_(a ,  b):
		How  to  multiply  objects  a  and   b
	def  _truediv_(a ,  b):
		How  to  divide  objects   a  and  b
# End  of  the  class
How  to  create  two  complex  class  objects
How  to  read   inputs  into  1st  object
How  to  read   inputs  into  2nd  object
print('Sum :  ' , ???)
print('Difference :  ' , ???)
print('Product :  ' ,  ??)
print('Division  : ' , ???)




class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def get(self):
        s = input("Enter complex number : ")
        c = complex(s)  
        self.real = c.real
        self.imag = c.imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(a, b):
        return Complex(a.real + b.real, a.imag + b.imag)

    def __sub__(a, b):
        return Complex(a.real - b.real, a.imag - b.imag)

    def __mul__(a, b):
        return Complex(a.real*b.real - a.imag*b.imag,
                       a.real*b.imag + a.imag*b.real)

    def __truediv__(a, b):
        denom = b.real**2 + b.imag**2
        return Complex((a.real*b.real + a.imag*b.imag)/denom,
                       (a.imag*b.real - a.real*b.imag)/denom)

c1 = Complex()
c2 = Complex()

print("Enter first complex number:")
c1.get()

print("Enter second complex number:")
c2.get()

print("Sum :", c1 + c2)
print("Difference :", c1 - c2)
print("Product :", c1 * c2)
print("Division :", c1 / c2)



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
			 How  to  read  numerator  and  denominator  into  object
	def _gt_(self,b):
			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
How  to  create  two  Rat   class  objects  'a'  and  'b'
How  to  read  1st  rational   number  into  object  'a'
How  to  read  2nd  rational   number  into  object  'b'
if  1st  rational  is  >  2nd  rational  number
	print('>')
if  1st  rational  is  <  2nd  rational  number
	print('<')
if  rational  numbers  are  same
	print('==')
if  1st  rational  is  >=  2nd  rational  number
	print('>=')
if  1st  rational  is  <=  2nd  rational  number
	print('<=')
if  rational  numbers  are  different
	print('!=')


class Rat:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den

    # Read numerator and denominator
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    # Greater than
    def __gt__(self, b):
        return self.num * b.den > b.num * self.den

    # Less than
    def __lt__(self, b):
        return self.num * b.den < b.num * self.den

    # Equal to
    def __eq__(self, b):
        return self.num * b.den == b.num * self.den

    # Greater than or equal to
    def __ge__(self, b):
        return self.num * b.den >= b.num * self.den

    # Less than or equal to
    def __le__(self, b):
        return self.num * b.den <= b.num * self.den

    # Not equal to
    def __ne__(self, b):
        return self.num * b.den != b.num * self.den


# ---- Main Program ----

# Create objects
a = Rat()
b = Rat()

# Input
print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Comparisons
if a > b:
    print(">")

if a < b:
    print("<")

if a == b:
    print("==")

if a >= b:
    print(">=")

if a <= b:
    print("<=")

if a != b:
    print("!=")


# Find  outputs  
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
How  to  call  m1()  method  of  outer  class  # o = outer() o.m1()
How  to  call  m1()  method  of  inner  class #i = outer.inner() i.m1()
How  to  call  m1()  method  of  inner  class  in  another way# o = outer() i = o.inner() i.m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way to call #outer().inner().m1()
i = inner()


# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		How  to  create  date  class  object
	def   disp(self):
		How  to  print  empno , ename , sal  of  object  self
		How  to  call  disp()  method  of  date  class
	class   date:
		def    _init_(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
How  to  call  disp()  method  of  emp  class


class emp:
    def __init__(self):
        self.empno = 25
        self.ename = "Rama Rao"
        self.sal = 10000.0

        self.d = self.date()

    def disp(self):
        print("Emp No:", self.empno)
        print("Emp Name:", self.ename)
        print("Salary:", self.sal)

        self.d.disp()

    class date:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            print("Date:", self.dd, "-", self.mm, "-", self.yy)

e = emp()
e.disp()


# Find outputs (Home  work)
class  outer:
	def  _init_(self):
		How  to  initialize  variable  'x'  of  object  self  to  25
		How  to  create  inner1  class  object
		How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
How  to  call   disp()  method  of outer  class
How  to  call   disp()  method  of inner1  class
How  to  call   disp()  method  of inner2  class

class outer:
    def __init__(self):
        self.x = 25

        self.i1 = self.inner1()
        self.i2 = self.inner2()

    def disp(self):
        print(self.x)

    class inner1:
        def disp(self):
            print("1st inner class method")

    class inner2:
        def disp(self):
            print("2nd inner class method")

o = outer()
o.disp()
o.i1.disp()
o.i2.disp()


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
How  to  create  c1  class  object
How  to  create  inner  c2  class  object
How  to  create  outer  c2  class  object

class c1:
    def __init__(self):
        print("outer class c1 constructor")

    class c2:
        def __init__(self):
            print("inner class c2 constructor")
class c2:
    def __init__(self):
        print("outer class c2 constructor")

# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object #o = c2()
How  to  create  inner  c2  class  object #i = c2.c2()
How  to  create  inner  c2  class  object  in  another  way #o = c2()
i = o.c2()
How  to  create  inner  c2  class  object  in  one  more  way #c2().c2()


