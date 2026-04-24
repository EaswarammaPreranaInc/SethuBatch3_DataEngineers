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
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get(self):
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter image part: "))
        #How  to  read  real  and  imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
        #How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i

    def __add__(a, b):
        return complex(a.real + b.real, a.imag + b.imag)
        #How  to  add  objects  a  and  b

    def __sub__(a, b):
        return complex(a.real - b.real, a.imag - b.imag)
        #How  to  subtract  objects  a  and  b

    def __mul__(a, b):
        real = a.real * b.real - a.imag * b.imag
        imag = a.real * b.imag + a.imag * b.real
        return complex(real, imag)
        #How  to  multiply  objects  a  and   b

    def __truediv__(a, b):
        dr = b.real**2 + b.imag**2
        real = (a.real * b.real + a.imag * b.imag) / dr
        imag = (a.imag * b.real - a.real * b.imag) / dr
        return complex(real, imag)
        #How  to  divide  objects   a  and  b

# End  of  the  class

c1 = complex()
c2 = complex()   #How  to  create  two  complex  class  objects

print("Enter first complex number:")
c1.get() #How  to  read   inputs  into  1st  object

print("Enter secund complex number:")
c2.get() #How  to  read   inputs  into  2nd  object

print('Sum :  ' , c1 + c2)
print('Difference :  ' , c1 - c2)
print('Product :  ' ,  c1 * c2)
print('Division  : ' , c1 / c2)

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
        self.nr = int(input("Enter numerator: "))
        self.dr = int(input("Enter denominator: "))  #How  to  read  numerator  and  denominator  into  object

    def __gt__(self, b):
        return self.nr * b.dr > b.nr * self.dr  #return  true  when  rational  number  in  object self  >  that  of  'b'  and  false  otherwise

    def __lt__(self, b):
        return self.nr * b.dr < b.nr * self.dr  #return  true  when  rational  number  in  object  self  <  that  of  'b'  and  false  otherwise

    def __eq__(self, b):
        return self.nr * b.dr == b.nr * self.dr  #return  true  when  rational  numbers  in  objects  self   and  'b'  are  same  and  false  otherwise

    def __ge__(self, b):
        return self.nr * b.dr >= b.nr * self.dr  #return  true  when  rational  number  in  object self  >=  that  of  'b'  and  false  otherwise

    def __le__(self, b):
        return self.nr * b.dr <= b.nr * self.dr  #return  true  when  rational  number  in  object self  <=  that  of  'b'  and  false  otherwise

    def __ne__(self, b):
        return self.nr * b.dr != b.nr * self.dr  #return  true  when  rational  numbers  in  objects  self   and  'b'  are  different  and  false  otherwise

#  End  of   the  class

a = Rat()
b = Rat()  #How  to  create  two  Rat   class  objects  'a'  and  'b'

a.get()  #How  to  read  1st  rational   number  into  object  'a'
b.get()  #How  to  read  2nd  rational   number  into  object  'b'

if a > b:  #1st  rational  is  >  2nd  rational  number
    print('>')

if a < b:  #1st  rational  is  <  2nd  rational  number
    print('<')

if a == b:  #rational  numbers  are  same
    print('==')

if a >= b:  #1st  rational  is  >=  2nd  rational  number
    print('>=')

if a <= b:  #1st  rational  is  <=  2nd  rational  number
    print('<=')

if a != b:  #rational  numbers  are  different
    print('!=')

'''Find  outputs  (Home  work)'''
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
#How  to  call  m1()  method  of  outer  class
o = outer() #Outer  class  constructor
o.m1() # Outer  class  method
#How  to  call  m1()  method  of  inner  class
i = outer.inner() #Inner  class  constructor
i.m1() # Inner  class  method
#How  to  call  m1()  method  of  inner  class  in  another  way
o2 = outer() #Outer  class  constructor
i2 = o2.inner() #Inner  class  constructor
i2.m1() # Inner  class  method
#How  to  call  m1()  method  of  inner  class  in  one  more  way
outer.inner().m1() # Inner  class  constructor <next line> Inner  class  method
#i = inner()  # Error--it is mandatory to  call with outer
'''Find  outputs  (Home  work)'''
class emp:
    def __init__(self):
        #How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        #How  to  create  date  class  object
        self.d = emp.date()
    def disp(self):
        #How  to  print  empno , ename , sal  of  object  self
        print(self.empno, self.ename, self.sal)
        #How  to  call  disp()  method  of  date  class
        self.d.disp()
    class date:
        def __init__(self):
            #How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
            self.dd = 15
            self.mm = 8
            self.yy = 1947
        def disp(self):
            #How  to  print  dd , mm , yy  of  object  self
            print(self.dd, self.mm, self.yy)
# End  of  the  class
#How  to  call  disp()  method  of  emp  class
e = emp()
e.disp()
'''Find outputs (Home  work)'''
class  outer:
	def  __init__(self):
		self.x = 25#How  to  initialize  variable  'x'  of  object  self  to  25
		self.i1 = outer.inner1()#How  to  create  inner1  class  object
		self.i2 = outer.inner2()#How  to  create  inner2  class  object
	def  disp(self):
		print(self . x)
	class   inner1:
		def  disp(self):
			print('1st  inner  class  method')
	class  inner2:
		def  disp(self):
			print('2nd  inner  class  method')
#end of the class
#How  to  call   disp()  method  of outer  class
o=outer()
o.disp()
#How  to  call   disp()  method  of inner1  class
o.i1.disp()
#How  to  call   disp()  method  of inner2  class
o.i2.disp()

'''Find  outputs  (Home  work)'''
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
#How  to  create  c1  class  object
a = c1()
#How  to  create  inner  c2  class  object
b= c1.c2()
#How  to  create  outer  c2  class  object
c = c2()

'''Find  outputs  (Home  work)'''
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
#How  to  create  outer  c2  class  object
a = c2()
#How  to  create  inner  c2  class  object
b = c2.c2()
#How  to  create  inner  c2  class  object  in  another  way
x = a.c2()
#How  to  create  inner  c2  class  object  in  one  more  way
y = c2().c2()



