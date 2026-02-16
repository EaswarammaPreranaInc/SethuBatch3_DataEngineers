# float  object  demo  program (Home  work)
a = 10.8
print(a) # 10.8
print(type(a)) # <class ‘int’>
print(id(a)) # 1000
b = 25.
print(b) # 25.0
print(type(b)) # <class ‘float’>
c = .689
print(c) # 0.689
d = 3.4E2
print(d) # 3.4 * 10^2 = 340
print(type(d)) # <class ‘float’>
e = 9.62e-2
print(e) # 9.6 * 10^-2 = 0.096
print(9.8.2)

# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) # <class ‘complex’>
print(id(a)) # 140000
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # <class ‘float’>
print(type(a . imag)) # <class ‘float’>





# Find outputs (Home work)
a = 6j
print(a) # Error due to there is no real number
print(type(a)) # Error due to there is no real number
print(a.real) # Error due to there is no real number
print(a.imag) # Error due to there is no real number
print(5 + j6)  # Error due to ‘j’ should be after 6
print(3 + 4i) # Error , because in python imag part of complex number is represented by ‘j’.
print(4+j) # Error due to no mention of imag number in
print(4 + 1j) # 4 + 1j
print(4 + 0j) # 4+0j

# bool object demo program  (Home  work)
a = True
print(a) # True
print(type(a)) # <class ‘bool’>
print(id(a)) # 15000
b = False
print(b) # False
print(type(b)) # <class ‘bool’>
print(True + True) # 2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) # 3
print(25 + 10.8 + True) # 36.8
print(True > False)  # True
print(True) #True
print(False) #False
print(true) # Error due to ‘t’, T should be capital letter in keyword “ True”
print(false) # Error due to ‘f’, Fshould be capital letter in keyword “False”
# Find  outputs (Home  work)
a = 0O6247
print(a) # 3239, which is decimal equivalent value for 0O6247octal number
print(type(a)) # <class ‘int’>
print(id(a))  # 160000
b = 0o6247
print(id(b)) #160000
print(b) # 3239, which is decimal equivalent value for 0O6247octal number
c = 3239
print(c) # 3239
print(id(c)) #160000
print(0o9248)# Error because octal number does not have ‘9’ digit.

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) # 42937
print(type(a)) # <class ‘int’>
b = 0xBEEF
print(b) # 48879
print(A7B9)  #Error
print('A7B9') # A7B9
print(0XBEER) # Error due to Hexa Decimal number does not have letter ‘R’.
print(0XHYD) # Error due to Hexa Decimal does not support letter ‘H’ and ‘ D’
print(0xA7G9B) # Error due to Hexa Decimal does not support letter ‘G’

# Find outputs (Home  work)
a = 9248
print(a) # 9248
print(type(a)) # <class ‘int’>
