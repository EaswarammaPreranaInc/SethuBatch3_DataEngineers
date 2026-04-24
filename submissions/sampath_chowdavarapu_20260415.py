'
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 39 / 61 + 2i / 61
'''
import  math
class  complex:
	def  get(self):
		How  to  read  real  and  imag
	def    _str_(self):
		 How  to  return  real  and  imag  in  the  form  of  3 +…

'''
class Complex:
    def __init__(self, r=0, i=0):
        self.r = r
        self.i = i
    def get(self):
        self.r = int(input("Enter real part: "))
        self.i = int(input("Enter imaginary part: "))

    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {abs(self.i)}i"

    # Addition
    def __add__(a, b):
        return Complex(a.r + b.r, a.i + b.i)

    # Subtraction
    def __sub__(a, b):
        return Complex(a.r - b.r, a.i - b.i)

    # Multiplication
    def __mul__(a, b):
        real = a.r * b.r - a.i * b.i
        imag = a.r * b.i + a.i * b.r
        return Complex(real, imag)

    # Division
    def __truediv__(a, b):
        denom = b.r**2 + b.i**2
        real = (a.r * b.r + a.i * b.i) / denom
        imag = (a.i * b.r - a.r * b.i) / denom
        return Complex(real, imag)


c1 = Complex()
c2 = Complex()

# Input
print("Enter first complex number")
c1.get()

print("Enter second complex number")
c2.get()

sum_res  = c1 + c2
diff_res = c1 - c2
mul_res  = c1 * c2
div_res  = c1 / c2

# Output
print("Sum:", sum_res)
print("Difference:", diff_res)
print("Product:", mul_res)
print("Division:", div_res)


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
    def __init__(self, n=0, d=1):
        self.n = n
        self.d = d

    def get(self):
        self.n = int(input("Enter numerator: "))
        self.d = int(input("Enter denominator: "))

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __gt__(self, b):
        return self.n * b.d > self.d * b.n

    def __lt__(self, b):
        return self.n * b.d < self.d * b.n

    def __eq__(self, b):
        return self.n * b.d == self.d * b.n

    def __ge__(self, b):
        return self.n * b.d >= self.d * b.n

    def __le__(self, b):
        return self.n * b.d <= self.d * b.n

    def __ne__(self, b):
        return self.n * b.d != self.d * b.n


a = Rat()
b = Rat()

print("Enter first rational number")
a.get()

print("Enter second rational number")
b.get()


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
How  to  call  m1()  method  of  outer  class #Outer().m1()
How  to  call  m1()  method  of  inner  class #Outer().inner()m1()
How  to  call  m1()  method  of  inner  class  in  another  way 
# a= Outer()
   b=a. inner()
	b.m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()
i.m1()

 # Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		#How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		self.empn0 = 25
		self.ename = 'Rama Rao'
		self.sal = 10000.0
		
		#How  to  create  date  class  object
		d = date()
	def   disp(self):
		#How  to  print  empno , ename , sal  of  object  self
		print(self.empn0, self.ename, self.sal)
		#How  to  call  disp()  method  of  date  class
		date().disp()
	class   date:
		def    _init_(self):
			#How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
			self.dd =15
			self.mm = 8
			self.yy = 1947
		def disp(self):
			#How  to  print  dd , mm , yy  of  object  self
			print(f '{self.dd} - {self.mm} - {self.yy}')
# End  of  the  class
How  to  call  disp()  method  of  emp  class
# e= emp()
e.disp()



# Object  'e'  ---> empno, ename, sal

 # Find outputs (Home  work)
class  outer:
	def  _init_(self):
		/*How  to  initialize  variable  'x'  of  object  self  to  25
		How  to  create  inner1  class  object
		How  to  create  inner2  class  object*/
		self.x = 25
		i1 = self.inner1()
		i2 = self.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')		
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
How  to  call   disp()  method  of outer  class # Outer().disp()
How  to  call   disp()  method  of inner1  class #Outer().inner1().disp()
How  to  call   disp()  method  of inner2  class #Outer().inner2().disp()



# Object  'o'  ---> x, i1, i2


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
How  to  create  c1  class  object  #c1()
How  to  create  inner  c2  class  object #c1().c2()
How  to  create  outer  c2  class  object #c2()


 # Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object  #c2()
How  to  create  inner  c2  class  object  #c2().c2()
How  to  create  inner  c2  class  object  in  another  way  a= c2()
								a.c2()
How  to  create  inner  c2  class  object  in  one  more  way  b = c2.c2()