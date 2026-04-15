Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object


class Rational:
    def __init__(self,n,d):
         self.num=n
         self.num=d
   def __gt__(self,other):
          return self.num*other.den >self.den*other.num
   def __lt__(self,other):
           return self.num*other.den<self.den*other.num
    def __eq__(self,other):
            return self.num*other.den==self.den*other.num
    def __ge__(self,other):
            return self.num*other.den>=self.den*other.num
    def __le__(self,other):
            return self.num*other.den<=self.den*other.num
    def __ne__(self,other):
           return self.num*other.den!=self.den*other.num
a=Rational(2,3)
b=rational(5,9)
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(a != b)

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
[9:39 am, 15/04/2026] SRINIVAS Sir Maths: '''
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
[11:00 am, 15/04/2026] SRINIVAS Sir Maths: # Find  outputs  (Home  work)
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
How  to  call  m1()  method  of  outer  class
o=outer()
o.m1()
How  to  call  m1()  method  of  inner  class
i=inner()
i.m1()
How  to  call  m1()  method  of  inner  class  in  another  way
outer.inner().m1()
How  to  call  m1()  method  of  inner  class  in  one  more  way
i = inner()
 # Find  outputs  (Home  work)
class   emp:
	def _init_(self):
		How  to  initialize  empno , ename , sal  of  object  self  to  25 ,  'Rama  Rao' , 10000.0
                self.empno=25
                self.ename='Ramarao"
                self.sal=10000.0
		How  to  create  date  class  object
                self.date=self.date()
	def   disp(self):
		How  to  print  empno , ename , sal  of  object  self
                print(self.empno,self.ename,self.sal)
		How  to  call  disp()  method  of  date  class
                self.d.disp()
	class   date:
		def    _init_(self):
			How  to  initialize  dd , mm , yy  of  object  self  to  15 , 8  , 1947
                        self.dd=15
                        self.mm=8
                        self.yy=1947  
	          def disp(self):
			How  to  print  dd , mm , yy  of  object  self
                       print(self.dd,self.mm,self.yy)
# End  of  the  class
How  to  call  disp()  method  of  emp  class
e=Emp()
e.disp()



# Object  'e'  --->
 # Find outputs (Home  work)
class  outer:
	def  _init_(self):
		How  to  initialize  variable  'x'  of  object  self  to  25
                 self.x=25
		How  to  create  inner1  class  object
                 def inner1():
                       pass
		How  to  create  inner2  class  object
                  def inner2():
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
How  to  call   disp()  method  of outer  class
o=outer()
o.disp()
How  to  call   disp()  method  of inner1  class
oi1.disp()
How  to  call   disp()  method  of inner2  class
o.i2.disp()



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
How  to  create  c1  class  object
a=c1()
How  to  create  inner  c2  class  object
b=c1.c2()
How  to  create  outer  c2  class  object
c=c2()
 # Find  outputs  (Home  work)
class   c2:
	def  _init_(self):
		print('outer  class  constructor')
	class   c2:
		def _init_(self):
			print('inner  class  constructor')
#end of the class
How  to  create  outer  c2  class  object
o=c2()
How  to  create  inner  c2  class  object
i=c2.c2()
How  to  create  inner  c2  class  object  in  another  way
i2=o.c2()
How  to  create  inner  c2  class  object  in  one  more  way
i3=c2().c2()