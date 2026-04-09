import math

class Rat:

    # Read numerator and denominator
    def get(self):
        self.num = int(input("Enter numerator: "))
        self.denom = int(input("Enter denominator: "))
        self.test()

    # Check denominator not zero
    def test(self):
        while self.denom == 0:
            print("Denominator cannot be zero")
            self.denom = int(input("Re-enter denominator: "))

    # Print rational number
    def __str__(self):
        return f"{self.num} / {self.denom}"

    # Addition
    def add(self, a, b):
        self.num = a.num * b.denom + b.num * a.denom
        self.denom = a.denom * b.denom
        self.simplify()

    # Subtraction
    def sub(self, a, b):
        self.num = a.num * b.denom - b.num * a.denom
        self.denom = a.denom * b.denom
        self.simplify()

    # Multiplication
    def mul(self, a, b):
        self.num = a.num * b.num
        self.denom = a.denom * b.denom
        self.simplify()

    # Division
    def div(self, a, b):
        self.num = a.num * b.denom
        self.denom = a.denom * b.num
        self.simplify()

    # Simplify fraction
    def simplify(self):
        g = math.gcd(self.num, self.denom)
        self.num = self.num // g
        self.denom = self.denom // g


# -------- MAIN PROGRAM --------

# Create objects
a = Rat()
b = Rat()
c = Rat()
d = Rat()
e = Rat()
f = Rat()

# Input
print("Enter Rational Number A")
a.get()

print("\nEnter Rational Number B")
b.get()

# Operations
c.add(a, b)
d.sub(a, b)
e.mul(a, b)

# Output
print("\nSum =", c)
print("Difference =", d)
print("Product =", e)

# Division check
if b.num != 0:
    f.div(a, b)
    print("Division =", f)
else:
    print("Division is not permitted")