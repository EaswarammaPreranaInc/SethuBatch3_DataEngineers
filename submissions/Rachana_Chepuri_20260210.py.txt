# float  object  demo  program (Home  work)
a = 10.8
print(a) # 10.8
print(type(a)) # <class'int'>
print(id(a)) # address of an object a
b = 25. 
print(b)  # 25.0
print(type(b)) #  <class 'float'>
c = .689
print(c) # 0.689
d = 3.4E2
print(d) # 340.0
print(type(d)) # <class 'int'>
e = 9.62e-2
print(e)  # 0.0962
print(9.8.2)  # error because it has 2 decimal numbers


____________________________________________________________________________________


# complex object demo program
a = 3 + 4j  
print(a)  # 3+4j
print(type(a)) # <class'complex'>
print(id(a))  # address of an object a
print(a . real)  # 3.0
print(a . imag)  # 4.0
print(type(a . real))  # <class 'float'>
print(type(a . imag))  # <class 'float'>


_____________________________________________________________________


# Find outputs (Home work)
a = 6j
print(a)  # 6j
print(type(a)) # <class'complex'>
print(a.real)  # 0.0
print(a.imag)  # 6.0
print(5 + j6)  # error  because j  is always after imag number
print(3 + 4i)  # error because i is not valid
print(4+j)     # error because it doesn't has imag number
print(4 + 1j)  # 4+1j
print(4 + 0j)  # 4+0j


_______________________________________________________________


# bool object demo program  (Home  work)
a = True
print(a) # True
print(type(a)) # <class 'bool'>
print(id(a))   # address of the object a
b = False
print(b)  # False 
print(type(b))  # <class'bool'>
print(True + True) # 2
print(True + False) # 1
print(False + True) # 1
print(False + False) # 0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False)  # True   
print(True)  # True
print(False)  # False
print(true)   # error  because t is not capital
print(false)  # error  because f is not capital

______________________________________________________________


# Find  outputs (Home  work)
a = 0O6247
print(a)  # 3239
print(type(a))  # <class'int'>
print(id(a))   # address of an object 3239
b = 0o6247
print(id(b)) # same address of an object 3239
print(b)  # 3239
c = 3239
print(c)  # 3239
print(id(c)) # same address of an object 3239  
print(0o9248) # error because  octal numbers from  0 to 7

_________________________________________________________________


# Find  outputs  (Home  work)
a = 0XA7B9
print(a)  # 42937
print(type(a)) # <class'int'>
b = 0xBEEF
print(b)  # 48879
print(A7B9)   # error because decimal number not contain alphabets
print('A7B9') # A7B9
print(0XBEER) # error because R is not hexa decimal
print(0XHYD)  # error because H,Y are not hexa decimal
print(0xA7G9B) # error because G is not hexa decimal

______________________________________________________________________

# Find outputs (Home  work)
a = 9248
print(a) # 9248
print(type(a))  # <class'int'>