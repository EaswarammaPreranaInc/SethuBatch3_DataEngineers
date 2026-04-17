#----- Float Object Demo -----

a=10.8
print(a)         # 10.8
print(type(a)) # <class 'float'>
print(id(a))    # 2000 
b=25.
print(b)         # 25.0
print(type(b))   # <class 'float'>
c=.689
print(c)        # 0.689
d=3.4E2
print(d)        # 340.0
print(type(d))   # <class 'float'>
e=9.62e-2
print(e)         # 0.0962
#print(9.8.2)    # Error (invalid number with two decimal points)


#----- Complex Object Demo -----

a=3+4j
print(a)           # (3+4j)
print(type(a))     # <class 'complex'>
print(id(a))      # 3000
print(a.real)     # 3.0
print(a.imag)      # 4.0
print(type(a.real)) # <class 'float'>
print(type(a.imag)) # <class 'float'>


#----- Find Outputs -----

a=6j
print(a)        # 6j
print(type(a)) # <class 'complex'>
print(a.real) # 0.0
print(a.imag) # 6.0
#print(5+j6) # Error (complex number must be written as 6j)
#print(3+4i) # Error (Python uses j not i for imaginary numbers)
#print(4+j)  # Error (j is not defined)
print(4+1j) # (4+1j)
print(4+0j) # (4+0j)


#----- Bool Object Demo -----

a=True
print(a)        # True
print(type(a)) # <class 'bool'>
print(id(a))   # 4000
b=False
print(b)        # False
print(type(b))   # <class 'bool'>
print(True+True) # 2
print(True+False) # 1
print(False+True) # 1
print(False+False) # 0
print(True+True+True) # 3
print(25+10.8+True) # 36.8
print(True>False) # True
print(True)        # True
print(False)      # False
#print(true) # Error (T should be in capital)
#print(false) # Error (F should be in capital)


#----- Octal Number Demo -----

a=0O6247
print(a) # 3239
print(type(a)) # <class 'int'>
print(id(a)) # 1000
b=0o6247
print(id(b)) # 1000
print(b)     # 3239
c=3239
print(c)     # 3239
print(id(c)) # 1000
#print(0o9248) # Error (octal allows digits 0 to 7 only)


#----- Hexadecimal Number Demo -----

a=0XA7B9
print(a) # 42937
print(type(a)) # <class 'int'>
b=0xBEEF
print(b) # 48879
#print(A7B9) # Error (treated as undefined variable)
print('A7B9') # A7B9
#print(0XBEER) # Error (R not allowed in hexadecimal)
#print(0XHYD) # Error (H,Y not allowed in hexadecimal)
#print(0xA7G9B) # Error (G not allowed in hexadecimal)


#----- Integer Demo -----

a=9248
print(a) # 9248
print(type(a)) # <class 'int'>