#1
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
import math

class complex:
    def get(self):
        self.r = int(input('Enter the real part: '))
        self.i = int(input('Enter the imaginary part: '))

    def __str__(self):
        if self.i >= 0:
            return f'{self.r} + {self.i}i'
        else:
            return f'{self.r} - {abs(self.i)}i'

    def __add__(a, b):
        res = complex()
        res.r = a.r + b.r
        res.i = a.i + b.i
        return res

    def __sub__(a, b):
        res = complex()
        res.r = a.r - b.r
        res.i = a.i - b.i
        return res

    def __mul__(a, b):
        res = complex()
        res.r = a.r * b.r - a.i * b.i
        res.i = a.r * b.i + a.i * b.r
        return res

    def __truediv__(a, b):
        res = complex()
        denom = b.r**2 + b.i**2
        res.r = (a.r * b.r + a.i * b.i) / denom
        res.i = (a.i * b.r - a.r * b.i) / denom
        return res


# Create objects
x = complex()
y = complex()

x.get()
y.get()

# Operations
print('Sum:', x + y)
print('Difference:', x - y)
print('Product:', x * y)
print('Division:', x / y)


#2
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
import math

class Rat:
    def get(self):
        self.n = int(input('Enter the numerator: '))
        self.d = int(input('Enter the denominator: '))

    def __str__(self):
        return f'{self.n} / {self.d}'

    # Greater than
    def __gt__(self, b):
        return self.n * b.d > b.n * self.d

    # Less than
    def __lt__(self, b):
        return self.n * b.d < b.n * self.d

    # Equal to
    def __eq__(self, b):
        return self.n * b.d == b.n * self.d

    # Greater than or equal
    def __ge__(self, b):
        return self.n * b.d >= b.n * self.d

    # Less than or equal
    def __le__(self, b):
        return self.n * b.d <= b.n * self.d

    # Not equal
    def __ne__(self, b):
        return self.n * b.d != b.n * self.d


# Create objects
a = Rat()
b = Rat()

a.get()
b.get()

print(a)
print(b)

print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)




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
a . m1() # How  to  call  m1()  method  of  outer  class

b = a . inner()
b . m1() # How  to  call  m1()  method  of  inner  class

c = outer . inner()
c . m1() # How  to  call  m1()  method  of  inner  class  in  another  way

outer() . inner() . m1() # How  to  call  m1()  method  of  inner  class  in  one  more  way

i = inner() # error , inner class object can only be created with the help of outer class name or outer class object



# Find  outputs  (Home  work)
class   emp:
    def __init__(self):
        self . empno = 25
        self . ename = 'Rama Rao'
        self . sal = 10000.0
        # How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
        global c
        c = emp . date() # How  to  create  date  class  object
    def   disp(self):
        print(self . empno)
        print(self . ename)
        print(self . sal)
        # How  to  print  empno , ename , sal  of  object  self
        c . disp() # How  to  call  disp()  method  of  date  class

    class date:
        def    __init__(self):
            self . dd = 15
            self . mm = 8
            self . yy = 1947
            # How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
        def disp(self):
            print(self . dd)
            print(self . mm)
            print(self . yy)
                    # How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp()
e . disp() # How  to  call  disp()  method  of  emp  class

# Object  'e'  ---> empno = 25 , ename = 'Rama Rao' , sal = 10000.0 , c = inner class object


# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self . x = 25 # How  to  initialize  variable  'x'  of  object  self  to  25
		self . y = self . inner1() # How  to  create  inner1  class  object
		self . z = self . inner2() # How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
a = outer()
a . disp() # How  to  call   disp()  method  of outer  class
a . y . disp() # How  to  call   disp()  method  of inner1  class
a . z . disp() # How  to  call   disp()  method  of inner2  class


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
a = c1() # How  to  create  c1  class  object
b = a . c2() # How  to  create  inner  c2  class  object
c = c2() # How  to  create  outer  c2  class  object


# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2() # How  to  create  outer  c2  class  object
b = a . c2() # How  to  create  inner  c2  class  object
c = c2 . c2() # How  to  create  inner  c2  class  object  in  another  way
d = c2() . c2() # How  to  create  inner  c2  class  object  in  one  more  way


