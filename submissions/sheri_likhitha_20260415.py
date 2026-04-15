class complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def get(self):
        self.real = int(input("Enter real part: "))
        self.imag = int(input("Enter imaginary part: "))

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


# Creating two complex objects
c1 = complex()
c2 = complex()

print("Enter first complex number:")
c1.get()

print("Enter second complex number:")
c2.get()

# Performing operations
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

    # a > b  →  a.num/a.den > b.num/b.den  → cross multiply
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

# Reading inputs
print("Enter first rational number:")
a.get()

print("Enter second rational number:")
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








class outer:
    def __init__(self):
        print("Outer class constructor")

    def m1(self):
        print("Outer class method")

    class inner:
        def __init__(self):
            print("Inner class constructor")

        def m1(self):
            print("Inner class method")


# 1) Outer class method
o = outer()
o.m1()

# 2) Inner class method (Way 1)
i1 = outer.inner()
i1.m1()

# 3) Inner class method (Way 2)
o2 = outer()
i2 = o2.inner()
i2.m1()

# 4) Inner class method (Way 3)
outer.inner().m1()



#outputs:

Outer class constructor
Outer class method

Inner class constructor
Inner class method

Outer class constructor
Inner class constructor
Inner class method

Inner class constructor
Inner class method








class emp:
    def __init__(self):
        # Initialize employee details
        self.empno = 25
        self.ename = "Rama Rao"
        self.sal = 10000.0

        # Create date class object
        self.d = emp.date()

    def disp(self):
        # Print employee details
        print("Emp No:", self.empno)
        print("Emp Name:", self.ename)
        print("Salary:", self.sal)

        # Call date class disp()
        self.d.disp()

    class date:
        def __init__(self):
            # Initialize date
            self.dd = 15
            self.mm = 8
            self.yy = 1947

        def disp(self):
            # Print date
            print("Date:", self.dd, "-", self.mm, "-", self.yy)


# Create object
e = emp()

# Call emp class disp()
e.disp()

#outputs:
Emp No: 25
Emp Name: Rama Rao
Salary: 10000.0
Date: 15 - 8 - 1947






class outer:
    def __init__(self):
        # Initialize x
        self.x = 25

        # Create inner class objects
        self.i1 = outer.inner1()
        self.i2 = outer.inner2()

    def disp(self):
        print(self.x)

    class inner1:
        def disp(self):
            print("1st inner class method")

    class inner2:
        def disp(self):
            print("2nd inner class method")


# Create object
o = outer()

# Call outer class disp()
o.disp()

# Call inner1 class disp()
o.i1.disp()

# Call inner2 class disp()
o.i2.disp()


#outputs:
25
1st inner class method
2nd inner class method







class c1:
    def __init__(self):
        print("outer class c1 constructor")

    class c2:
        def __init__(self):
            print("inner class c2 constructor")


class c2:
    def __init__(self):
        print("outer class c2 constructor")


# Create c1 class object
o1 = c1()

# Create inner c2 class object
i = c1.c2()

# Create outer c2 class object
o2 = c2()


#outputs:
outer class c1 constructor
inner class c2 constructor
outer class c2 constructor





class c2:
    def __init__(self):
        print("outer class constructor")

    class c2:
        def __init__(self):
            print("inner class constructor")


# Create outer class object
o = c2()

# Create inner class object (Way 1)
i1 = c2.c2()

# Create inner class object (Way 2)
o2 = c2()
i2 = o2.c2()

# Create inner class object (Way 3)
i3 = c2().c2()


#outputs:
outer class constructor
inner class constructor
outer class constructor
inner class constructor
outer class constructor
inner class constructor