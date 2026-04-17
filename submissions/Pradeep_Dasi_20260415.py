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
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    def get(self):
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter imaginary part: "))
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"
    def __add__(a, b):
        return complex(a.real + b.real, a.imag + b.imag)
    def __sub__(a, b):
        return complex(a.real - b.real, a.imag - b.imag)
    def __mul__(a, b):
        real = a.real * b.real - a.imag * b.imag
        imag = a.real * b.imag + a.imag * b.real
        return complex(real, imag)
    def __truediv__(a, b):
        denominator = b.real**2 + b.imag**2
        real = (a.real * b.real + a.imag * b.imag) / denominator
        imag = (a.imag * b.real - a.real * b.imag) / denominator
        return complex(real, imag)
# Creating two objects
c1 = complex()
c2 = complex()
print("Enter first complex number:")
c1.get()
print("Enter second complex number:")
c2.get()
# Operations
print("Sum:", c1 + c2)
print("Difference:", c1 - c2)
print("Product:", c1 * c2)
print("Division:", c1 / c2)



class Rat:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))
        if self.den == 0:
            print("Denominator cannot be zero. Setting to 1.")
            self.den = 1
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
# Creating objects
a = Rat()
b = Rat()
print("Enter first rational number:")
a.get()
print("Enter second rational number:")
b.get()
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




class emp:
    def __init__(self):
        # initialize emp details
        self.empno = 25
        self.ename = "Rama Rao"
        self.sal = 10000.0        
        # create date class object
        self.d = self.date()
    def disp(self):
        # print emp details
        print("Emp No:", self.empno)
        print("Emp Name:", self.ename)
        print("Salary:", self.sal)        
        # call date disp()
        self.d.disp()
    class date:
        def __init__(self):
            # initialize date
            self.dd = 15
            self.mm = 8
            self.yy = 1947
        def disp(self):
            # print date
            print("Date:", self.dd, "/", self.mm, "/", self.yy)
# create object
e = emp()
# call disp()
e.disp()




class outer:
    def __init__(self):
        # initialize x
        self.x = 25
        # create inner class objects
        self.i1 = self.inner1()
        self.i2 = self.inner2()
    def disp(self):
        print(self.x)
    class inner1:
        def disp(self):
            print("1st inner class method")
    class inner2:
        def disp(self):
            print("2nd inner class method")
# create object
o = outer()
# call methods
o.disp()        # outer class
o.i1.disp()     # inner1 class
o.i2.disp()     # inner2 class




class c1:
    def __init__(self):
        print("outer class c1 constructor")
    class c2:
        def __init__(self):
            print("inner class c2 constructor")
class c2:
    def __init__(self):
        print("outer class c2 constructor")
# create c1 object
o1 = c1()
# create inner c2 object
o2 = c1.c2()
# create outer c2 object
o3 = c2()



class c2:
    def __init__(self):
        print("outer class constructor")
    class c2:
        def __init__(self):
            print("inner class constructor")
# 1) Create outer class object
o1 = c2()
# 2) Create inner class object (normal way)
o2 = c2.c2()
# 3) Create inner class object (another way using outer object)
o3 = o1.c2()
# 4) One more way (explicit reference via class)
inner_ref = c2.c2
o4 = inner_ref()