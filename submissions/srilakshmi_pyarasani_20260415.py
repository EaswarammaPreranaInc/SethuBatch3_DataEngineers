1) Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) =39 / 61 + 2i / 61
'''
import  math
class  complex:
        def_init_(self, r=0, i=0)
	  self.real = r
	  self.imag = i

	def  get(self):
		self.real = float(input("Enter real part:")) 
		self.imag = float(input("Enter imaginary part:")) #How  to  read  real  and  imag
	def    _str_(self):
		if self.imag >= 0
		  return f"{self.real} + {self.imag}i"
                else :
		  return f"{self.real} - {abs(self.imag)}i" # How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  _add_(a ,  b):
	          return Complex(self.real + b.real, self.imag + b.imag) #How  to  add  objects  a  and  b
	def  _sub_(a ,  b):
		return complex(self.real - b.real, self.imag - b.imag) #How  to  subtract  objects  a  and  b
	def  _mul_(a ,  b):
		r = self.real*b.real - self.imag*b.imag
                i = self.real*b.imag + self.imag*b.real
                return Complex(r, i) #How  to  multiply  objects  a  and  b
	def  _truediv_(a ,  b):
		denom = b.real**2 + b.imag**2
                r = (self.real*b.real + self.imag*b.imag) / denom
                i = (self.imag*b.real - self.real*b.imag) / denom
                return Complex(r, i) #How  to  divide  objects   a  and  b
# End  of  the  class
c1 = complex() 
c2 = complex() #How  to  create  two  complex  class  objects
c1.get() #How  to  read   inputs  into  1st  object
c2.get() #How  to  read   inputs  into  2nd  object
print('Sum :  ' , c1 + c2)
print('Difference :  ' , c1 - c2)
print('Product :  ' ,  c1 * c2)
print('Division  : ' , c1/c2)

2) Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

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
		self.num = int(input("Enter numerator:"))
                self.den = int(input("Enter denominator:")) #How  to  read  numerator  and  denominator  into  object
	def _gt_(self,b):
		retrun self.num*b.den > self.den*b.num #return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise
	def _lt_(self,b):
			return self.num*b.den < self.den*b,num #return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise
	def _eq_(self,b):
		return self.num*b.den == self.den *b.num #return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise
	def _ge_(self,b):
		return self.num*b.den >= self.den *b.num #return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise
	def _le_(self,b):
			return self.num*b.den <= self.den *b.num #return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise
	def _ne_(self,b):
			return self.num*b.den != self.den *b.num #return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise
#  End  of   the  class
a = rat()
b = rat() #How  to  create  two  Rat   class  objects  'a'  and  'b'
a.get() #How  to  read  1st  rational   number  into  object  'a'
b.get() #How  to  read  2nd  rational   number  into  object  'b'
if  a > b: #1st  rational  is  >  2nd  rational  number
	print('>')
if a < b: # 1st  rational  is  <  2nd  rational  number
	print('<')
if  a == b: #rational  numbers  are  same
	print('==')
if  a>=b: # 1st  rational  is  >=  2nd  rational  number
	print('>=')
if  a<=b: # 1st  rational  is  <=  2nd  rational  number
	print('<=')
if  a!=b: #rational  numbers  are  different
	print('!=')

3) outputs
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
o = outer()
o.m1() #How  to  call  m1()  method  of  outer  class

i1 = outer.inner()
i1.m1() #How  to  call  m1()  method  of  inner  class
o.inner.m1() #How  to  call  m1()  method  of  inner  class  in  another  way
i2 = o.inner() #How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()

4) outputs  
class   emp:
	def _init_(self):
	   self.empno = 25
           self.ename = "Rama Rao"
           self.sal = 10000.0 #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
	   self.d = self.date() #How  to  create  date  class  object
	def   disp(self):
		print(self.empno, self.ename, selfsal) #How  to  print  empno , ename , sal  of  object  self
		self.d.disp() #How  to  call  disp()  method  of  date  class
	class   date:
		def    _init_(self):
			self.dd = 15
 			self.mm = 8
                        self.yy = 1947 #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
		def disp(self):
		      print(self.dd, self.mm, self.yy) #How  to  print  dd , mm , yy  of  object  self
# End  of  the  class
e = emp()
e.disp() #How  to  call  disp()  method  of  emp  class



# Object  'e'  --->

5) outputs 
class  outer:
	def  _init_(self):
		  self.x = 25 #How  to  initialize  variable  'x'  of  object  self  to  25
                  self.i1 = self.Inner1()
                  self.i2 = self.Inner2() #How  to  create  inner1  class  object #How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
o = outer() #How  to  call   disp()  method  of outer  class
o.disp()
o.i1.disp() #How  to  call   disp()  method  of inner1  class
o.i2.disp()How  to  call   disp()  method  of inner2  class


# Object  'o'  --->

6) outputs
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
o1 = c1() #How  to  create  c1  class  object
i = c1.c2()#How  to  create  inner  c2  class  object
02 = c2() #How  to  create  outer  c2  class  object

7) outputs
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
o = c2() #How  to  create  outer  c2  class  object
i1 = c2.c2() #How  to  create  inner  c2  class  object
o.c2() #How  to  create  inner  c2  class  object  in  another  way
i2 = o.c2() #How  to  create  inner  c2  class  object  in  one  more  way