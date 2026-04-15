import math

# -------------------------------------------------
# 1) Complex class with +, -, *, / overloading
# -------------------------------------------------

class Complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def get(self):
        # How to read real and imag
        self.real = float(input("Enter real part : "))
        self.imag = float(input("Enter imaginary part : "))

    def __str__(self):
        # How to return real and imag in the form of 3 + 4i (or) 3 - 4i
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    def __add__(a, b):
        # How to add objects a and b
        return Complex(a.real + b.real, a.imag + b.imag)

    def __sub__(a, b):
        # How to subtract objects a and b
        return Complex(a.real - b.real, a.imag - b.imag)

    def __mul__(a, b):
        # How to multiply objects a and b
        real = a.real * b.real - a.imag * b.imag
        imag = a.real * b.imag + a.imag * b.real
        return Complex(real, imag)

    def __truediv__(a, b):
        # How to divide objects a and b
        denom = b.real ** 2 + b.imag ** 2
        real = (a.real * b.real + a.imag * b.imag) / denom
        imag = (a.imag * b.real - a.real * b.imag) / denom
        return Complex(real, imag)

# How to create two complex class objects
c1 = Complex()
c2 = Complex()

# How to read inputs into 1st object
print("Enter 1st complex number:")
c1.get()
# How to read inputs into 2nd object
print("Enter 2nd complex number:")
c2.get()

print("Sum        : ", c1 + c2)
print("Difference : ", c1 - c2)
print("Product    : ", c1 * c2)
print("Division   : ", c1 / c2)

# -------------------------------------------------
# 2) Rational class with >, <, ==, >=, <=, != overloading
# -------------------------------------------------

class Rat:
    def __init__(self, num=0, den=1):
        self.num = num
        self.den = den

    def get(self):
        # How to read numerator and denominator into object
        self.num = int(input("Enter numerator   : "))
        self.den = int(input("Enter denominator : "))

    def __gt__(self, b):
        # return true when rational number in object self > that of 'b'
        return self.num * b.den > b.num * self.den

    def __lt__(self, b):
        # return true when rational number in object self < that of 'b'
        return self.num * b.den < b.num * self.den

    def __eq__(self, b):
        # return true when rational numbers in objects self and 'b' are same
        return self.num * b.den == b.num * self.den

    def __ge__(self, b):
        # return true when rational number in object self >= that of 'b'
        return self.num * b.den >= b.num * self.den

    def __le__(self, b):
        # return true when rational number in object self <= that of 'b'
        return self.num * b.den <= b.num * self.den

    def __ne__(self, b):
        # return true when rational numbers in objects self and 'b' are different
        return self.num * b.den != b.num * self.den

# How to create two Rat class objects 'a' and 'b'
a = Rat()
b = Rat()

# How to read 1st rational number into object 'a'
print("Enter 1st rational number:")
a.get()
# How to read 2nd rational number into object 'b'
print("Enter 2nd rational number:")
b.get()

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

# -------------------------------------------------
# 3) Nested classes / inner classes – homework parts
# -------------------------------------------------

# 3.1 outer / inner – how to call m1()
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

# How to call m1() method of outer class
o1 = outer()
o1.m1()

# How to call m1() method of inner class
i1 = outer.inner()
i1.m1()

# How to call m1() method of inner class in another way
outer().inner().m1()

# How to call m1() method of inner class in one more way
i2 = outer.inner()
i2.m1()

# Given line in question
i = outer.inner()

# 3.2 emp + inner date class
class emp:
    def __init__(self):
        # How to initialize empno , ename , sal of object self to 25 , 'Rama Rao' , 10000.0
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        # How to create date class object
        self.d = emp.date()

    def disp(self):
        # How to print empno , ename , sal of object self
        print(self.empno, self.ename, self.sal)
        # How to call disp() method of date class
        self.d.disp()

    class date:
        def __init__(self):
            # How to initialize dd , mm , yy of object self to 15 , 8 , 1947
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            # How to print dd , mm , yy of object self
            print(self.dd, self.mm, self.yy)

# How to call disp() method of emp class
e = emp()
e.disp()

# 3.3 outer with inner1 and inner2
class outer2:
    def __init__(self):
        # How to initialize variable 'x' of object self to 25
        self.x = 25
        # How to create inner1 class object
        self.i1 = outer2.inner1()
        # How to create inner2 class object
        self.i2 = outer2.inner2()

    def disp(self):
        print(self.x)

    class inner1:
        def disp(self):
            print('1st inner class method')

    class inner2:
        def disp(self):
            print('2nd inner class method')

# Object 'o' --->
o = outer2()

# How to call disp() method of outer class
o.disp()
# How to call disp() method of inner1 class
o.i1.disp()
# How to call disp() method of inner2 class
o.i2.disp()

# 3.4 c1.c2 vs outer c2 – constructors
class c1:
    def __init__(self):
        print('outer class c1 constructor')

    class c2:
        def __init__(self):
            print('inner class c2 constructor')

# end of the class

class c2:
    def __init__(self):
        print('outer class c2 constructor')

# How to create c1 class object
c1_obj = c1()
# How to create inner c2 class object
c1_inner_c2_obj = c1.c2()
# How to create outer c2 class object
outer_c2_obj = c2()

# 3.5 same-name outer c2 and inner c2
class c2_outer:
    def __init__(self):
        print('outer class constructor')

    class c2:
        def __init__(self):
            print('inner class constructor')

# How to create outer c2 class object
co = c2_outer()

# How to create inner c2 class object
ci1 = c2_outer.c2()

# How to create inner c2 class object in another way
ci2 = co.c2()

# How to create inner c2 class object in one more way
c2_outer().c2()