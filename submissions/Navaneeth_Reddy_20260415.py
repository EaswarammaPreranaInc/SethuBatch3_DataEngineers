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
        self.real = int(input("Enter real number: "))
        self.imag = int(input("Enter imaginary number: "))

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}-{abs(self.imag)}i"

    def __add__(a, b):
        c = complex()
        c.real = a.real + b.real
        c.imag = a.imag + b.imag
        return c

    def __sub__(a, b):
        c = complex()
        c.real = a.real - b.real
        c.imag = a.imag - b.imag
        return c

    def __mul__(a, b):
        c = complex()
        c.real = a.real * b.real - a.imag * b.imag
        c.imag = a.real * b.imag + a.imag * b.real
        return c

    def __truediv__(a, b):
        c = complex()
        den = b.real**2 + b.imag**2
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
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    def __gt__(self, b):
        return self.num * b.den > b.num * self.den

    def __lt__(self, b):
        return self.num * b.den < b.num * self.den

    def __eq__(self, b):
        return self.num * b.den == b.num * self.den

    def __ge__(self, b):
        return self.num * b.den >= b.num * self.den

    def __le__(self, b):
        return self.num * b.den <= b.num * self.den

    def __ne__(self, b):
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
o=outer()
i=outer().inner()
a=o.inner()
#i = inner()#Error



# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self.x=25
	class inner1:
		pass
	class inner2:
		pass
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

i1=outer.inner1()
i1.disp()
i2=outer.inner2()
i2.disp()


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
a=c1()
a.c2()
b=c2()

# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a=c2()
b=a.c2()

c=c2.c2
d=c()

d=c2.c2()