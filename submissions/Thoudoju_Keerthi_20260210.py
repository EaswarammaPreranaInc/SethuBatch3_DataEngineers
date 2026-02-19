# FLOAT OBJECT DEMO PROGRAM
------------------------------
a = 10.8
print(a)
Output: 10.8

print(type(a))
Output: <class 'float'>

print(id(a))
Output: Address of object 10.8 is printed

b = 25.
print(b)
Output: 25.0

print(type(b))
Output: <class 'float'>

c = .689
print(c)
Output: 0.689

d = 3.4E2
print(d)
Output: 340.0

print(type(d))
Output: <class 'float'>

e = 9.62e-2
print(e)
Output: 0.0962

print(9.8.2)
Output: Error

#COMPLEX OBJECT DEMO PROGRAM
----------------------------
a = 3 + 4j
print(a)
Output: 3+4j

print(type(a))
Output: <class 'complex'>

print(id(a))
Output: Address of object 3+4j is printed

print(a.real)
Output: 3.0

print(a.imag)
Output: 4.0

print(type(a.real))
Output: <class 'float'>

print(type(a.imag))
Output: <class 'float'>

FIND OUTPUTS (COMPLEX)
a = 6j
print(a)
Output: 6j

print(type(a))
Output: <class 'complex'>

print(a.real)
Output: 0.0

print(a.imag)
Output: 6.0

print(5 + j6)
Output: Error (should be 5 + 6j)

print(3 + 4j)
Output: 3 + 4j

print(4 + j)
Output: Error (imaginary must be explicit like 4+1j)

print(4 + 1j)
Output: 4+1j

print(4 + 0j)
Output: 4+0j

BOOL OBJECT DEMO PROGRAM
--------------------------
a = True
print(a)
Output: True

print(type(a))
Output: <class 'bool'>

print(id(a))
Output: Address of bool object True is printed

b = False
print(b)
Output: False

print(type(b))
Output: <class 'bool'>

BOOL OPERATIONS
---------------
print(True + True)
Output: 2

print(True + False)
Output: 1

print(False + True)
Output: 1

print(False + False)
Output: 0

print(True + True + True)
Output: 3

print(True + 10.25 + 10.8 + True)
Output: 22.05
(True = 1, False = 0)

print(True > False)
Output: True

print(True)
Output: True

print(False)
Output: False

print(true)
Output: Error (must be True)

print(false)
Output: Error (must be False)

OCTAL NUMBER DEMO
-----------------
a = 0o6247
print(a)
Output: 3239 (converted to decimal equivalent)

print(type(a))
Output: <class 'int'>

print(id(a))
Output: Address of int object 3239

b = 0o6247
print(id(b))
Output: Same as address of a

print(b)
Output: 3239 (converted to decimal equivalent)

c = 3239
print(c)
Output: 3239 (converted to decimal equivalent)

print(id(c))
Output: Same address as refernce b because int is immutable and reusable

print(0o9248)
Output: Error (9 not allowed in octal)

HEXADECIMAL NUMBER DEMO
------------------------
a = 0xA789
print(a)
Output: 42937 (converted to decimal equivalent)

print(type(a))
Output: <class 'int'>

b = 0xBEEF
print(b)
Output: 48879 (converted to decimal equivalent)

print(ATB9)
Output: Error ( T is not allowed in hexadecimal)

print('ATB9')
Output: ATB9

print(0xBEER)
Output: Error (R not allowed)

print(0xHYD)
Output: Error (H and Y not allowed)

print(0xA7G98)
Output: Error (G not allowed)

FINAL FIND OUTPUT
------------------
a = 9248

print(a)
Output: 9248

print(type(a))
Output: <class 'int'>


