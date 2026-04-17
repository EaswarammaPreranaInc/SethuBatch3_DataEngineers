Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without  using  pre-defined
complex  object

'''1) First  rational  number  --->  3 + 4i
   Second  rational  number ---> 5 + 6i
   What  is  the  sum  ?  --->  8 + 10i
   What  is  the  difference  ?  --->  -2 - 2i
   What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) = 15 + 18i + 20i - 24 =  -9 + 38i
   What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =  (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =  (15 - 18i + 20i + 24) / (25 + 36) = 
				'''																																			#39 / 61 + 2i / 61

import  math
class  complex:
	def  get(self):
		self.real=int(input("enter real value:"))
		self.img=int(input("enter imaginaru value:"))
  #How  to  read  real  and  imag
	def    __str__(self):
		if self.img>=0:
			return f"{self.real}+{self.img}i"
		else:
			return f"{self.real} - {abs(self.img)}i"

		#How  to  return  real  and  imag  in  the  form  of  3 + 4i  (or)  3 - 4i
	def  __add__(a ,  b):
		res=complex()
		res.real=a.real+b.real
		res.img=a.img+b.img
		return res
#How  to  add  objects  a  and  b
	def  __sub__(a ,  b):
		res=complex()
		res.real=a.real-b.real
		res.img=a.img-b.img
		return res
		#How  to  subtract  objects  a  and  b
	def  __mul__(a ,  b):
		res=complex()
		res.real=a.real*b.real-a.img*b.img
		res.img=a.real*b.real+a.img*b.img
  
		return res
#How  to  multiply  objects  a  and   b
	def __truediv__(a, b):
			res = complex()
			denom = b.real**2 + b.img**2
			res.real = (a.real * b.real + a.img * b.img) / denom
			res.img = (a.img * b.real - a.real * b.img) / denom
			return res
  #How  to  divide  objects   a  and  b
# End  of  the  class
a=complex()
b=complex()
a.get()
b.get()

print('Sum :  ' , a+b)
print('Difference :  ' , a-b)
print('Product :  ' ,  a*b)
print('Division  : ' , a/b)

#  RATIONAL CLASS WITH OPERATOR OVERLOADING


class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))      # read numerator
        self.den = int(input("Enter denominator: "))    # read denominator

    def __gt__(self, b):
        return self.num * b.den > b.num * self.den      # cross product >

    def __lt__(self, b):
        return self.num * b.den < b.num * self.den      # cross product <

    def __eq__(self, b):
        return self.num * b.den == b.num * self.den     # cross product ==

    def __ge__(self, b):
        return self.num * b.den >= b.num * self.den     # cross product >=

    def __le__(self, b):
        return self.num * b.den <= b.num * self.den     # cross product <=

    def __ne__(self, b):
        return self.num * b.den != b.num * self.den     # cross product !=


# create objects
a = Rat()      # object 'a'
b = Rat()      # object 'b'

# read inputs
a.get()        # read 1st rational
b.get()        # read 2nd rational

# comparisons
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

#  INNER CLASS METHOD CALLS

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


o = outer()        # create outer object
o.m1()             # call outer method

i = outer.inner()  # create inner object
i.m1()

outer.inner().m1()   # another way

o2 = outer()
i2 = o2.inner()
i2.m1()              # one more way



#  EMP WITH INNER DATE CLASS


class emp:
    def __init__(self):
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        self.d = self.date()     # create date object

    def disp(self):
        print(self.empno, self.ename, self.sal)
        self.d.disp()            # call date disp

    class date:
        def __init__(self):
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            print(self.dd, self.mm, self.yy)


e = emp()    # object 'e'
e.disp()


#  OUTER WITH INNER1 & INNER2

class outer2:
    def __init__(self):
        self.x = 25
        self.i1 = self.inner1()   # create inner1 object
        self.i2 = self.inner2()   # create inner2 object

    def disp(self):
        print(self.x)

    class inner1:
        def disp(self):
            print('1st inner class method')

    class inner2:
        def disp(self):
            print('2nd inner class method')


o = outer2()    # object 'o'

o.disp()        # outer disp
o.i1.disp()     # inner1 disp
o.i2.disp()     # inner2 disp



#  c1 AND c2 CLASSES

class c1:
    def __init__(self):
        print('outer class c1 constructor')

    class c2:
        def __init__(self):
            print('inner class c2 constructor')

class c2:
    def __init__(self):
        print('outer class c2 constructor')


obj1 = c1()        # create c1 object
obj2 = c1.c2()     # create inner c2 object
obj3 = c2()        # create outer c2 object



#  SAME NAME INNER & OUTER CLASS


class c3:
    def __init__(self):
        print('outer class constructor')

    class c3:
        def __init__(self):
            print('inner class constructor')


o = c3()        # outer object
i = c3.c3()     # inner object

i2 = o.c3()     # another way
i3 = c3().c3()  # one more way