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

import  math
class  complex:
	def  get(self):
		How  to  read  real  and  imag
	def    __str__(self):
		 How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		How  to  add  objects  a  and  b
	def  __sub__(a ,  b):
		How  to  subtract  objects  a  and  b
	def  __mul__(a ,  b):
		How  to  multiply  objects  a  and   b
	def  __truediv__(a ,  b):
		How  to  divide  objects   a  and  b
# End  of  the  class
How  to  create  two  complex  class  objects
How  to  read   inputs  into  1st  object
How  to  read   inputs  into  2nd  object
print('Sum :  ' , ???)
print('Difference :  ' , ???)
print('Product :  ' ,  ??)
print('Division  : ' , ???)'''


#code
import math
class complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def get(self):
        self.real = float(input("Enter the real part: "))
        self.imag = float(input("Enter the imaginary part: "))

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return complex(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return complex(real_part, imag_part)

# Create two complex class objects
c1 = complex()
c2 = complex()
# Read inputs into 1st object
print("Enter the first complex number:")
c1.get()
# Read inputs into 2nd object
print("Enter the second complex number:")
c2.get()
print('Sum :  ', c1 + c2)
print('Difference :  ', c1 - c2)
print('Product :  ', c1 * c2)
print('Division  : ', c1 / c2)









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

import  math
class  Rat:
	def  get(self):
			 How  to  read  numerator  and  denominator  into  object
	def __gt__(self,b):
			return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def __lt__(self,b):
			return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def __eq__(self,b):
			return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def __ge__(self,b):
			return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def __le__(self,b):
			return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def __ne__(self,b):
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
	print('!=')'''


#code
import math
class Rat:
    def get(self):
        self.numerator = int(input("Enter numerator: "))
        self.denominator = int(input("Enter denominator: "))

    def __gt__(self, b):
        return self.numerator * b.denominator > b.numerator * self.denominator

    def __lt__(self, b):
        return self.numerator * b.denominator < b.numerator * self.denominator

    def __eq__(self, b):
        return self.numerator * b.denominator == b.numerator * self.denominator

    def __ge__(self, b):
        return self.numerator * b.denominator >= b.numerator * self.denominator

    def __le__(self, b):
        return self.numerator * b.denominator <= b.numerator * self.denominator

    def __ne__(self, b):
        return self.numerator * b.denominator != b.numerator * self.denominator

# Create two Rat class objects 'a' and 'b'
a = Rat()
b = Rat()
# Read 1st rational number into object 'a'
a.get()
# Read 2nd rational number into object 'b'
b.get()
# Compare the rational numbers and print the results
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
How  to  call  m1()  method  of  outer  class #1st  way 
#o = outer()
#o.m1()
How  to  call  m1()  method  of  inner  class
#i = outer().inner()
#i.m1()
How  to  call  m1()  method  of  inner  class  in  another  way
#i = outer.inner()
#i.m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way
#i = outer().inner()
#i.m1()





# Find  outputs  (Home  work)
'''class   emp:
	def __init__(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
		How  to  create  date  class  object
	def   disp(self):
		How  to  print  empno , ename , sal  of  object  self
		How  to  call  disp()  method  of  date  class
	class   date:
		def    __init__(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
			How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
How  to  call  disp()  method  of  emp  class



# Object  'e'  ---> emp  class
'''
class emp:
    def __init__(self):
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        self.d = self.date()  # Create an object of the date class

    def disp(self):
        print(f"Emp No: {self.empno}, Name: {self.ename}, Salary: {self.sal}")
        self.d.disp()  # Call the disp method of the date class

    class date:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            print(f"Date: {self.dd}/{self.mm}/{self.yy}")       
# Create an object of the emp class
e = emp()
e.disp()  # Call the disp method of the emp class





''' Find outputs (Home  work)
class  outer:
	def  __init__(self):
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
'''

class  outer:
    def  __init__(self):
        self.x = 25
        self.inner1_obj = self.inner1()
        self.inner2_obj = self.inner2()
    def  disp(self):
        print(self.x)
    class   inner1:
        def  disp(self):
            print('1st  inner  class  method')
    class  inner2:
        def  disp(self):
            print('2nd  inner  class  method')
#end of the class
# Object  'o'  --->
o = outer()
# Call disp() method of outer class
o.disp()
# Call disp() method of inner1 class
o.inner1_obj.disp()
# Call disp() method of inner2 class
o.inner2_obj.disp()





'''# Find  outputs  (Home  work)
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
How  to  create  c1  class  object
How  to  create  inner  c2  class  object
How  to  create  outer  c2  class  object'''



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
# How  to  create  c1  class  object
c1_obj = c1()
# How  to  create  inner  c2  class  object
c1_c2_obj = c1.c2()
# How  to  create  outer  c2  class  object 
c2_obj = c2()
