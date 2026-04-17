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
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))	
    
    def    __str__(self):       
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
	
    
    def  __add__(a ,  b):
        c = complex()
        c.real = a.real + b.real
        c.imag = a.imag + b.imag
        return c
	
    def  __sub__(a ,  b):
		c = complex()
        c.real = a.real - b.real
        c.imag = a.imag - b.imag
        return c
	
    def  __mul__(a ,  b):
        c = complex()
        c.real = a.real*b.real - a.imag*b.imag
        c.imag = a.real*b.imag + a.imag*b.real
        return c	
        
    def  __truediv__(a ,  b):

        c.real = (a.real*b.real + a.imag*b.imag) / denom
        c.imag = (a.imag*b.real - a.real*b.imag) / denom
        return c


# End  of  the  class
x = complex()
y = complex()
print("Enter First Complex Number")
x.get()
print("Enter Second Complex Number")
y.get()
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Division:", x / y)






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
import  math
class  Rat:
	def  get(self):
        self.num = num
        self.den = den
	def __gt__(self,b):
        return self.nr * b.dr > self.dr * b.nr
	def __lt__(self,b):
        return self.nr * b.dr < self.dr * b.nr  
	def __eq__(self,b):
		return   self.nr * b.dr == self.dr * b.nr
	def __ge__(self,b):
			return   self.nr * b.dr >= self.dr * b.nr
	def __le__(self,b):
			return   self.nr * b.dr <= self.dr * b.nr
	def __ne__(self,b):
			return  self.nr * b.dr != self.dr * b.nr
#  End  of   the  class
a = Rat()
b = Rat()
How  to  read  1st  rational   number  into  object  'a'
How  to  read  2nd  rational   number  into  object  'b'
if  a > b:
	print('>')
if  a < b:
	print('<')
if  a == b:
	print('==')
if  a >= b:
	print('>=')
if  a <= b:
	print('<=')
if  a != b:
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
o = outer()
o.m1()
i = outer.inner()
i.m1()
i = outer().inner()
i = inner()


 



# Find  outputs  (Home  work)
class   emp:
	def __init__(self):
        self.empno = 25
        self.ename = "Rama Rao"
        self.sal   = 10000.0
        
        self.d = self.date() 
        
	def   disp(self):
        print(self.empno, self.ename, self.sal)
        self.d.disp()
        
	class   date:
		def    __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947
		def disp(self):
                    print(self.dd, self.mm, self.yy)# End  of  the  class
e = emp()
e.disp()


# Object  'e'  --->




# Find outputs (Home  work)
class  outer:
	def  __init__(self):
        self.x = 25
        self.i1 = self.inner1()
        self.i2 = self.inner2()
	
    def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer()
o.disp()
o.i1.disp()
o.i2.disp()



# Object  'o'   -----> x = 25




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
x = c1() 
y = c1.c2()
z = c2() 





# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
x = c2()
y = c2.c2()
o = c2()          
z = o.c2() 
How  t