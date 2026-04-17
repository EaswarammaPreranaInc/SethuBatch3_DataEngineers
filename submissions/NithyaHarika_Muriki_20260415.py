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
import math
class complex:

    def get(self):
        self.real = int(input("Enter real number: "))
        self.imag = int(input("Enter imaginary number: "))

    def _str_(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}-{abs(self.imag)}i"

    def _add_(a, b):
        c = complex()
        c.real = a.real + b.real
        c.imag = a.imag + b.imag
        return c

    def _sub_(a, b):
        c = complex()
        c.real = a.real - b.real
        c.imag = a.imag - b.imag
        return c

    def _mul_(a, b):
        c = complex()
        c.real = a.real * b.real - a.imag * b.imag
        c.imag = a.real * b.imag + a.imag * b.real
        return c

    def _truediv_(a, b):
        c = complex()
        den = b.real*2 + b.imag*2
        c.real = (a.real * b.real + a.imag * b.imag) / den
        c.imag = (a.imag * b.real - a.real * b.imag) / den
        return c


# End of class

c1 = complex()
c2 = complex()

print("Enter first complex number")
c1.get()

print("Enter second complex number")
c2.get()

print("Sum:", c1 + c2)
print("Difference:", c1 - c2)
print("Product:", c1 * c2)
print("Division:", c1 / c2)



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
import math

class Rat:

    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    def _gt_(self, b):
        return self.num * b.den > b.num * self.den

    def _lt_(self, b):
        return self.num * b.den < b.num * self.den

    def _eq_(self, b):
        return self.num * b.den == b.num * self.den

    def _ge_(self, b):
        return self.num * b.den >= b.num * self.den

    def _le_(self, b):
        return self.num * b.den <= b.num * self.den

    def _ne_(self, b):
        return self.num * b.den != b.num * self.den


# End of class

# Creating objects
a = Rat()
b = Rat()

# Reading inputs
print("Enter first rational number")
a.get()

print("Enter second rational number")
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
a=outer()
a.m1()
b = outer().inner()
b.m1()
c= a.inner()
c.inner()
i = inner()#error


# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empno =25
		self,ename = "Rama Rao"
		self.sal = 10000.0
		a = date()
	def   disp(self):
		print(f"{Empno:{self.empno},Ename:{self.ename},Salary:{self.sal}}")
		a.disp()
	class   date:
		def    _init_(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd= 15
			self.mm = 8
			self.yy= 1947
		def disp(self):
			print(f"{'{dd}:{mm}:{yy}}")
# End  of  the  class
b=emp()
b.disp()



# Object  'e'  --->


# Find outputs (Home  work)
class  outer:
	def  _init_(self):
		self.x=25
		a = outer().inner1()
		b = outer().inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
c = outer()
c.disp()
b.disp()
a.disp()


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
a=c1()
b = c1().inner()
c = c2()


# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
a=c2()
b=a.c2()
c=c2().c2()
i=inner()