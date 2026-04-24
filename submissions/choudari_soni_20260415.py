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
        self.real = float(input("Enter real part: "))
        self.imag = float(input("Enter imag part: "))

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.imag = self.imag + other.imag
        return result

    def __sub__(self, other):
        result = Complex()
        result.real = self.real - other.real
        result.imag = self.imag - other.imag
        return result

    def __mul__(self, other):
        result = Complex()
        result.real = self.real * other.real - self.imag * other.imag
        result.imag = self.real * other.imag + self.imag * other.real
        return result

    def __truediv__(self, other):
        result = Complex()
        denom = other.real**2 + other.imag**2
        result.real = (self.real * other.real + self.imag * other.imag) / denom
        result.imag = (self.imag * other.real - self.real * other.imag) / denom
        return result
c1 = Complex()
print("Enter 1st complex number:")
c1.get()
c2 = Complex()
print("\nEnter 2nd complex number:")
c2.get()
print("\nSum        :", c1 + c2)
print("Difference :", c1 - c2)
print("Product    :", c1 * c2)
print("Division   :", c1 / c2)

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
class Rat:
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.den = int(input("Enter denominator: "))

    def __gt__(self, b):
        return self.num * b.den > self.den * b.num
    def __lt__(self, b):
        return self.num * b.den < self.den * b.num
    def __eq__(self, b):
        return self.num * b.den == self.den * b.num
    def __ge__(self, b):
        return self.num * b.den >= self.den * b.num
    def __le__(self, b):
        return self.num * b.den <= self.den * b.num
    def __ne__(self, b):
        return self.num * b.den != self.den * b.num
# create objects
a = Rat()
b = Rat()
print("Enter 1st rational number:")
a.get()
print("\nEnter 2nd rational number:")
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
 
# Find  outputs  (Home  work)
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
print("Call outer class method:")
o = outer()
o.m1()
print("\nCall inner class method (Method 1):")
i = outer.inner()
i.m1()
print("\nCall inner class method (Method 2):")
outer.inner().m1()
print("\nCall inner class method (Method 3):")
o2 = outer()
i2 = o2.inner()
i2.m1()

# Find  outputs  (Home  work)
class emp:
    def __init__(self):
        self.empno = 25
        self.ename = 'Rama Rao'
        self.sal = 10000.0
        self.d = self.date()
    def disp(self):
        # print employee details
        print("Emp No :", self.empno)
        print("Emp Name :", self.ename)
        print("Salary :", self.sal)
        self.d.disp()
    class date:
        def __init__(self):
            # initialize date
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            # print date
            print("Date :", self.dd, "/", self.mm, "/", self.yy)
e = emp()
e.disp()


# Object  'e'  --->

# Find outputs (Home  work)
class outer:
    def __init__(self):
        self.x = 25
        self.i1 = self.inner1()
        self.i2 = self.inner2()
    def disp(self):
        print(self.x)
    class inner1:
        def disp(self):
            print('1st inner class method')
    class inner2:
        def disp(self):
            print('2nd inner class method')
o = outer()
print("Outer class disp():")
o.disp()
print("\nInner1 class disp():")
o.i1.disp()
print("\nInner2 class disp():")
o.i2.disp()


# Object  'o'  --->

# Find  outputs  (Home  work)
class c1:
    def __init__(self):
        print('outer class c1 constructor')
    class c2:
        def __init__(self):
            print('inner class c2 constructor')
class c2:
    def __init__(self):
        print('outer class c2 constructor')
print("Create c1 object:")
o1 = c1()
print("\nCreate inner c2 object:")
i = c1.c2()
print("\nCreate outer c2 object:")
o2 = c2()

# Find  outputs  (Home  work)
class c2:
    def __init__(self):
        print('outer class constructor')
    class c2:
        def __init__(self):
            print('inner class constructor')
print("Outer c2 object:")
o = c2()
print("\nInner c2 object (Method 1):")
i1 = c2.c2()
print("\nInner c2 object (Method 2):")
i2 = o.c2()
print("\nInner c2 object (Method 3):")
c2.c2()