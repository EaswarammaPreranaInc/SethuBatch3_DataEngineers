# float  object  demo  program (Home  work)
a = 10.8
print(a) # 10.8
print(type(a)) # class float
print(id(a)) # address of object 10.8
b = 25.
print(b) # 25
print(type(b)) # class float
c = .689
print(c) # 0.689
d = 3.4E2
print(d) # Error bcz invalid class value
print(type(d)) # Error 
e = 9.62e-2
print(e) # Error
print(9.8.2) # Error bcz incorrect class

# complex object demo program
a = 3 + 4j
print(a) # 3.0+4.0
print(type(a)) # class complex
print(id(a)) # address of object 3+4j
print(a . real) # 3.0
print(a . imag) #4.0
print(type(a . real)) # class complex
print(type(a . imag)) # class complex

# Find outputs (Home work)
a = 6j
print(a) # Error bcz object is not a correct class
print(type(a)) # Error
print(a.real) # Error
print(a.imag) # Error
print(5 + j6)  # Error bcz incorrect form 
print(3 + 4i) # Error bcz I is not valid
print(4+j) # Error real num not there
print(4 + 1j)# 4.0+1.0
print(4 + 0j)# 4.0+0.0
bool object demo program  (Home  work)
a = True
print(a) # 1
print(type(a)) # class bool
print(id(a)) # address of object True
b = False
print(b) # 0
print(type(b)) # class bool
print(True + True)# 2
print(True + False)# 1
print(False + True)# 1
print(False + False)# 0
print(True + True + True)# 3
print(25 + 10.8 + True)# 36.8
print(True > False)  # ?
print(True)# 1
print(False)# 0
print(true)# Error bcz small t
print(false)# Error bcz small f

# Find  outputs (Home  work)
a = 0O6247
print(a) # decimal value of object 0O6247
print(type(a)) # class int
print(id(a)) # address of object 0O6247
b = 0o6247
print(id(b)) # address of object 0o6247
print(b) # decimal value of object 0o6247
c = 3239
print(c) # 3239
print(id(c)) # address of object 3239
print(0o9248) # Error bcz 8 and 9 or not a octal values

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) # decimal value of object a
print(type(a)) # class int
b = 0xBEEF
print(b) # decimal value of object b
print(A7B9) # decimal value
print('A7B9') # A7B9
print(0XBEER) # decimal value
print(0XHYD) # decimal value
print(0xA7G9B) # Error

# Find outputs (Home  work)
a = 9248
print(a) # 9248
print(type(a)) # class int