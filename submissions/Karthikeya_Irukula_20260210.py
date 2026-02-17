# 10/02/2026
# Karthikeya Irukula 

# float object demo program (Home work)
a = 10.8
print(a) #10.8
print(type(a)) # <class 'float'>
print(id(a)) # address of object 10.8
b = 25.
print(b) # 25.0
print(type(b)) # <class 'float'>
c = .689
print(c) #0.689
d = 3.4E2
print(d) # 3.4*10^2 = 340.0
print(type(d)) # <class 'float'> Mantissa
e = 9.62e-2
print(e) # 0.0962
print(9.8.2) # Error due to syntax/More decimal points

# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) # <class 'complex'>
print(id(a)) # address of object 3+4j
print(a . real) #3.0
print(a . imag)# 4.0
print(type(a . real)) #<class 'float'>
print(type(a . imag)) #<class 'float'>

# Find outputs (Home work)
a = 6j
print(a) #6j
print(type(a)) #<class 'complex'>
print(a.real) #0.0
print(a.imag)#6.0
print(5 + j6) #Error due to j place. j should be after imag
print(3 + 4i) # Error due to i it should be j
print(4+j) #Error due to no integer/value in imaginary
print(4 + 1j) #4+1j
print(4 + 0j) #4+0j

# bool object demo program (Home work)
a = True
print(a) # True
print(type(a)) <class 'bool'>
print(id(a)) #Address of object True
b = False
print(b) #False
print(type(b)) #<class 'bool'>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#36.8
print(True > False) # True
print(True) #True
print(False) # False
print(true) #Error true replace True
print(false) #Error false instead False

# Find outputs (Home work)
a = 0O6247
print(a) #3239
print(type(a)) #<class 'int'>
print(id(a)) #Address of object 3239
b = 0o6247
print(id(b)) #Address of object 3239
print(b)#3239
c = 3239
print(c) #3239
print(id(c)) #Address of object 3239
print(0o9248) #Error due to octal contains values 0-7

# Find outputs (Home work)
a = 0XA7B9
print(a) # 42937
print(type(a)) # <class 'int'>
b = 0xBEEF
print(b) #48879
print(A7B9) #Error due to no prefix in hexadecimal
print('A7B9')#A7B9
print(0XBEER) #Error due to Hexadecimal until F
print(0XHYD) #Error due to Hexadecimal until F
print(0xA7G9B) #Error due to Hexadecimal until F

# Find outputs (Home work)
a = 9248
print(a) #9248
print(type(a)) #<class 'int'>