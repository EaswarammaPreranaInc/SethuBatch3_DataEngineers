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
class Complex:
    def get(self):
        self.x = int(input("Enter real part: "))
        self.y = int(input("Enter imaginary part: "))

    def __str__(self):
        if self.y >= 0:
            return f'{self.x}+{self.y}i'
        else:
            return f'{self.x}{self.y}i' 

    def __add__(a, b):
        c = Complex()
        c.x = a.x + b.x
        c.y = a.y + b.y
        return c

    def __sub__(a, b):
        c = Complex()
        c.x = a.x - b.x
        c.y = a.y - b.y
        return c

    def __mul__(a, b):
        c = Complex()
        c.x = a.x * b.x - a.y * b.y
        c.y = a.x * b.y + a.y * b.x
        return c

    def __truediv__(a, b):
        c = Complex()
        denom = b.x**2 + b.y**2
        if d == 0:
            print("Division by zero not possible")
            return None
        c.x = (a.x * b.x + a.y * b.y) / d
        c.y = (a.y * b.x - a.x * b.y) / d
        return c


# Main
a = Complex()
b = Complex()

a.get()
b.get()

print("A =", a)
print("B =", b)

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
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
     What  is  the  method  call  to  _lt()  …

'''
class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        if self.den == 0:
            print("Denominator cannot be zero")
            exit()

    def __str__(self):
        return f"{self.num}/{self.den}"

    # >
    def __gt__(self, b):
        return self.num * b.den > b.num * self.den

    # <
    def __lt__(self, b):
        return self.num * b.den < b.num * self.den

    # ==
    def __eq__(self, b):
        return self.num * b.den == b.num * self.den

    # >=
    def __ge__(self, b):
        return self.num * b.den >= b.num * self.den

    # <=
    def __le__(self, b):
        return self.num * b.den <= b.num * self.den

    # !=
    def __ne__(self, b):
        return self.num * b.den != b.num * self.den


# Creating objects
a = Rat()
b = Rat()

print("Enter first rational number:")
a.get()

print("Enter second rational number:")
b.get()

print("a =", a)
print("b =", b)

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
o=outer()
o.m1()
i=o.inner()
i.m1()
i=outter().inner()
i.m1()
outter.inner.m1(i)
i = inner()#Error


# Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		 self.empno=25
                 self.ename='Rama Rao'
                 self.sal  =10000.0
		d=date()
	def   disp(self):
		print(self.empno,self.ename,self.sal)
		d.disp()
	class   date:
		def    _init_(self):
			self.dd=15
                        self.mm =8
                        self.yy =1947
		def disp(self):
			print(self.dd,self.mm,self.yy)
# End  of  the  class
a=emp()
a.disp()


# Object  'e'  --->
# Find outputs (Home  work)
class  outer:
	def  _init_(self):
                self.x=25
		i=o.inner1()
		j=o.inner2()
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o=outer()
o.disp()
i.disp()
j.disp()


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
b=a.c2()
c=c2()


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
b=c2.c2()
How  to  create  inner  c2  class  object  in  another  way
How  to  create  inner  c2  class  object  in  one  more  way