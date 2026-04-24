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


# output : 

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    # Read values
    def get(self):
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter imaginary part: "))

    # Display in form a + bi or a - bi
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
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    # Division
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)


# ---- Main Program ----

# Create two objects
c1 = Complex()
c2 = Complex()

print("Enter first complex number:")
c1.get()

print("Enter second complex number:")
c2.get()

# Operations
print("Sum :", c1 + c2)
print("Difference :", c1 - c2)
print("Product :", c1 * c2)
print("Division :", c1 / c2)


#-----------------------------------------------------

# Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

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


# output : 

class Rat:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den

    # Read numerator and denominator
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        while self.den == 0:
            print("Denominator cannot be zero. Enter again.")
            self.den = int(input("Enter denominator: "))

    # Display rational number
    def __str__(self):
        return f"{self.num}/{self.den}"

    # Greater than >
    def __gt__(self, b):
        return self.num * b.den > b.num * self.den

    # Less than <
    def __lt__(self, b):
        return self.num * b.den < b.num * self.den

    # Equal ==
    def __eq__(self, b):
        return self.num * b.den == b.num * self.den

    # Greater than or equal >=
    def __ge__(self, b):
        return self.num * b.den >= b.num * self.den

    # Less than or equal <=
    def __le__(self, b):
        return self.num * b.den <= b.num * self.den

    # Not equal !=
    def __ne__(self, b):
        return self.num * b.den != b.num * self.den


# ---- Main Program ----

# Create objects
a = Rat()
b = Rat()

print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

# Comparisons
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

#------------------------------------------

class outer:
    def __init__(self):
        print('Outer class constructor')

    def m1(self):
        print('Outer class method')

    class inner:
        def __init__(self):
            print('Inner class constructor')

        def m1(self):
            print('Inner class method')


# ---- Method Calls ----

# 1) Call m1() of outer class
o = outer()
o.m1()

# 2) Call m1() of inner class (way 1)
i = outer.inner()
i.m1()

# 3) Call m1() of inner class (way 2)
o2 = outer()
i2 = o2.inner()
i2.m1()

# 4) Call m1() of inner class (way 3 - direct one line)
outer.inner().m1()

# output : 

Outer class constructor
Outer class method

Inner class constructor
Inner class method

Outer class constructor
Inner class constructor
Inner class method

Inner class constructor
Inner class method

#------------------------------------

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



# Object  'e'  --->

# output :

Emp No: 25
Emp Name: Rama Rao
Salary: 10000.0
Date: 15 / 8 / 1947

#-------------------------------------

## Find outputs (Home  work)
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

# ---- Main ----

# Create outer object
o = outer()

# Call outer class method
o.disp()

# Call inner1 class method
o.i1.disp()

# Call inner2 class method
o.i2.disp()
#end of the class
How  to  call   disp()  method  of outer  class
How  to  call   disp()  method  of inner1  class
How  to  call   disp()  method  of inner2  class


# Object  'o'  --->

# output : 

25
1st inner class method
2nd inner class method

#------------------------------------------

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
# ---- Object Creation ----

# 1) Create c1 class object
o1 = c1()

# 2) Create inner c2 class object
i = c1.c2()

# 3) Create outer c2 class object
o2 = c2()
#end of the class
How  to  create  c1  class  object
How  to  create  inner  c2  class  object
How  to  create  outer  c2  class  object

# output : 

outer class c1 constructor
inner class c2 constructor
outer class c2 constructor

#-----------------------------------------

# Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
       # ---- Object Creation ----

# 1) Create outer c2 object
o = c2()

# 2) Create inner c2 object (way 1)
i1 = c2.c2()

# 3) Create inner c2 object (way 2)
o2 = c2()
i2 = o2.c2()

# 4) Create inner c2 object (way 3 - one line)
c2.c2()
#end of the class
How  to  create  outer  c2  class  object
How  to  create  inner  c2  class  object
How  to  create  inner  c2  class  object  in  another  way
How  to  create  inner  c2  class  object  in  one  more  way

# output : 

outer class constructor
inner class constructor
outer class constructor
inner class constructor
inner class constructor