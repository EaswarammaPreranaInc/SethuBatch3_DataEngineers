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
import  math
class  complex:
	def  get(self):
		self.real = float(input('Enter the real part: '))
		self.imag = float(input('Enter the imaginary part : '))
		

	def    __str__(self):
		if self.image >= 0:
			return f'{self.real} + {self.imag}i'
		else :
			return f'{self.real} - {abs(self.imag)}i'
		

	def  __add__(a ,  b):
		res = complex()
		res.real = a.real + b.real
		res.imag = a.imag + b.imag
		return res
	


	def  __sub__(a ,  b):
		res = complex()
		res.real = a.real - b.real
		res.imag = a.imag - b.imag
		return res
	

	def  __mul__(a ,  b):
		res= complex()
		res.real = a.real*b.real - a.imag*b.imag
		res.imag = a.real*b.imag + a.imag*b.real
		return res

	def  __truediv__(a ,  b):
		res= complex()
		dr = b.real**2 + b.imag**2
		res.real = (a.real*b.real + a.imag*b.imag)/dr
		res.imag = (a.imag*b.real - a.real*b.imag)/dr
		
# End  of  the  class
a = complex()
b  = complex()
a.get()
b.get()
print('Sum :  ' , a + b)
print('Difference :  ' , a - b)
print('Product :  ' ,  a*b)
print('Division  : ' , a / b)
	  


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
        self.nr = int(input("Enter numerator: "))
        self.dr = int(input("Enter denominator: "))
    
    def __gt__(self, b):
        return self.nr * b.dr > b.nr * self.dr

    def __lt__(self, b):
        return self.nr * b.dr < b.nr * self.dr
    
    def __eq__(self, b):
        return self.nr * b.dr == b.nr * self.dr
    
    def __ge__(self, b):
        return self.nr * b.dr >= b.nr * self.dr
    
    def __le__(self, b):
        return self.nr * b.dr <= b.nr * self.dr
\
    def __ne__(self, b):
        return self.nr * b.dr != b.nr * self.dr

a = Rat()
b = Rat()

a.get()
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

# Find outputs (Home  work)
class  outer:
	def  __init__(self):
		self. x= 25
		self.inner1 = outer.inner1
		self.inner2 = outer.inner2
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
a.disp()
a.inner1().disp()
a.inner2().disp()



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
a = c1()
b = a.c2()
c = c2()

 # Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2()
b = a.c2()
b = c2.c2()
c2 = c2.c2()
