# 1
class c1:
    def __del__(self):
        print('Destructor')
        global b
        b = self

a = c1()
del a
print('Hello')
# Output:
# Destructor
# Hello
# b contains reference to deleted object

# 2
class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def simplify(self):
        g = self.gcd(abs(self.num), self.den)
        self.num //= g
        self.den //= g
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        return Rational(num, den)
    
    def __sub__(self, other):
        num = self.num * other.den - other.num * self.den
        den = self.den * other.den
        return Rational(num, den)
    
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)
    
    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Rational(num, den)

r1 = Rational(2, 3)
r2 = Rational(5, 9)
print(f"2/3 + 5/9 = {r1 + r2}")
print(f"2/3 - 5/9 = {r1 - r2}")
print(f"2/3 * 5/9 = {r1 * r2}")
print(f"2/3 / 5/9 = {r1 / r2}")

r3 = Rational(0, 9)
print(f"2/3 + 0/9 = {r1 + r3}")
print(f"2/3 - 0/9 = {r1 - r3}")

# 3
class c1:
    def __add__(a, b):
        print(10 + 20)

a = c1()
b = c1()

# 4
class c1:
    def __init__(self, y):
        self.x = y
    def __gt__(m, n):
        print('_gt_ method : ', m.x, n.x)
        return m.x > n.x

a = c1(10)
b = c1(20)
print(a > b)
print(a < b)

print("\nObject 'a' ---> x=10")
print("Object 'b' ---> x=20")

# 5
class c1:
    def __init__(self, y):
        self.x = y
    def __ge__(m, n):
        print('_ge_ method : ', m.x, n.x)
        return m.x > n.x

a = c1(10)
b = c1(20)
print(a >= b)
print(a <= b)

# 6
class c1:
    def __init__(self, y):
        self.x = y
    def __eq__(m, n):
        print('_eq_ method : ', m.x, n.x)
        return m.x == n.x

a = c1(10)
b = c1(20)
print(a == b)
print(a != b)

# 7
a = c1(25)
b = c1(25)
print(a == b)
print(a != b)
print(a.x != b.x)

# 8
class c1:
    def __init__(self, y):
        self.x = y
    def __ne__(m, n):
        print('_ne_ method : ', m.x, n.x)
        return m.x != n.x

a = c1(25)
b = c1(25)
print(a != b)
print(a == b)
print(a is b)

# 9
a = c1(10)
b = a
print(a != b)
print(a == b)

# 10
class c1:
    def __gt__(a, b):
        print(10 > 20)
        print(a > b)

a = c1()
b = c1()
print(a > b)

# 11
class c1:
    def __init__(self, y):
        self.x = y
    def __gt__(p, q):
        print('c1 class _gt_ method : ', p.x, q.x)
        return p.x > q.x

class c2:
    def __init__(self, y):
        self.x = y
    def __gt__(p, q):
        print('c2 class _gt_ method : ', p.x, q.x)
        return p.x > q.x

a = c1(10)
b = c1(20)
a > b
a < b
m = c2(30)
n = c2(40)
a < m
n < b

# 12
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 250
    def __mul__(x, y):
        print('_mul_ method of class c1')
        return 25 * 8

class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8
    def __mul__(x, y):
        print('_mul_ method of class c2')
        return 8 * 25

a = c1()
b = c2()
print(a * b)
print(b * a)

# 13
class c1:
    def __add__(x, y):
        return '_add_ method of class c1'

class c2:
    pass

a = c1()
b = c1()
print('a + b : ', a + b)
print('7 + 8 : ', 7 + 8)

# 14
class c1:
    def __init__(self, y):
        self.x = y
    def __add__(p, q):
        if isinstance(p.x, (int, float)) and isinstance(q.x, (int, float)):
            return p.x + q.x
        else:
            return str(p.x) + str(q.x)

a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')
print('Sum : ', a + b)
print('Join : ', m + n)

print("\nObject a ---> x=10")
print("Object b ---> x=20")
print("Object m ---> x='10'")
print("Object n ---> x='20'")