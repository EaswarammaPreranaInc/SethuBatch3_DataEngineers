
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
		 How  to  return  real  and  imag  in  the  form  of  3 +…

import math
class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Read values
    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

    # Display in proper format
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    # Addition
    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    # Subtraction
    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    # Multiplication
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    # Division
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)
# Main program
c1 = Complex()
c2 = Complex()

print("Enter First Complex Number:")
c1.get()

print("Enter Second Complex Number:")
c2.get()

print("\nFirst Number:", c1)
print("Second Number:", c2)

print("\nSum:", c1 + c2)
print("Difference:", c1 - c2)
print("Product:", c1 * c2)
print("Division:", c1 / c2)




Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  ---> False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  ---> False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  ---> True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  ---> False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  --->  True  due  to 18 != 15

def relation (self,f1):
    self.f1 = f1
   
def __str__(self):
    return f'{self.f1}'

def __gt__(self,other):
    if self.f1 > other.f1:
        return True
    False

def __ge__(self,other):
    if self.f1 >= other.f1:
        return True
    False    
def __eq__(self,other):
    if self.f1 == other.f1:
        return True
    False
def __ne__(self,other):
    if self.f1 != other.f1:
        return True
    False
    
a = int(input('Enter a value :'))
b = int(input('emnter a value :'))

print(a > b)
print(a >= b)
print(a == b)
print (a != b)



2) Imp  point  is  cross  product

3) What  is  the  method  call  to  _gt()  method ?  # a > b   (or)  a . __gt_(b) --> a.__gt__(b)
   What  is  the  method  call  to  _lt()  …



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
How  to  call  m1()  method  of  outer  class # create a class a = outer()
						 		 a.m1()
How  to  call  m1()  method  of  inner  class # i = outer.inner()
						  i.m1() 
How  to  call  m1()  method  of  inner  class  in  another  way  # Outer.Inner().m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way # outer.inner()
i = inner()





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
How  to  call  disp()  method  of  emp  class # e = Emp()
						  e.disp()
# Object  'e'  --->



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
How  to  call   disp()  method  of outer  class # o = outer()
						    o.disp()
How  to  call   disp()  method  of inner1  class # o.i1.disp()
How  to  call   disp()  method  of inner2  class # o.i2.disp()


# Object  'o'  --->




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
How  to  create  c1  class  object # obj1 = c1()
How  to  create  inner  c2  class  object # obj_inner = c1.c2()
How  to  create  outer  c2  class  object # obj2 = c2()



class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object # obj_outer = c2()
How  to  create  inner  c2  class  object # obj_inner1 = c2.c2()
How  to  create  inner  c2  class  object  in  another  way # obj_inner2 = obj_outer.c2()
How  to  create  inner  c2  class  object  in  one  more  way # obj_inner3 = obj_outer.__class__.c2()



