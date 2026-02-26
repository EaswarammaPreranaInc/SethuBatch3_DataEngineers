Home Work- (10/02/2026)

a = 10.8
print(a)            # 10.8
print(type(a))      # <class 'float'>
print(id(a))        # memory address (varies)
b = 25.
print(b)            # 25.0
print(type(b))      # <class 'float'>
c = .689
print(c)            # 0.689
d = 3.4E2
print(d)            # 340.0
print(type(d))      # <class 'float'>
e = 9.62e-2
print(e)            # 0.0962
print(9.8.2)        # SyntaxError: invalid syntax
----------------------------------------------------------------
a = 3 + 4j
print(a)                # (3+4j)
print(type(a))          # <class 'complex'>
print(id(a))            # memory address (varies)
print(a.real)           # 3.0
print(a.imag)           # 4.0
print(type(a.real))     # <class 'float'>
print(type(a.imag))     # <class 'float'>
a = 6j
print(a)            # 6j
print(type(a))      # <class 'complex'>
print(a.real)       # 0.0
print(a.imag)       # 6.0
print(5 + j6)       # SyntaxError
print(3 + 4i)       # SyntaxError
print(4+j)          # NameError: name 'j' is not defined
print(4 + 1j)       # (4+1j)
print(4 + 0j)       # (4+0j)
a = True
print(a)                # True
print(type(a))          # <class 'bool'>
print(id(a))            # memory address (varies)
b = False
print(b)                # False
print(type(b))          # <class 'bool'>
print(True + True)      # 2
print(True + False)     # 1
print(False + True)     # 1
print(False + False)    # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False)     # True
print(True)             # True
print(False)            # False
print(true)             # NameError
print(false)            # NameError
a = 0O6247
print(a)            # 3239
print(type(a))      # <class 'int'>
print(id(a))        # memory address (varies)
b = 0o6247
print(id(b))        # memory address (may be same as a)
print(b)            # 3239
c = 3239
print(c)            # 3239
print(id(c))        # memory address (may be same)
print(0o9248)       # SyntaxError: invalid digit
a = 0XA7B9
print(a)            # 42937
print(type(a))      # <class 'int'>
b = 0xBEEF
print(b)            # 48879
print(A7B9)         # NameError
print('A7B9')       # A7B9
print(0XBEER)       # SyntaxError
print(0XHYD)        # SyntaxError
print(0xA7G9B)      # SyntaxError
a = 9248
print(a)            # 9248
print(type(a))      # <class 'int'>