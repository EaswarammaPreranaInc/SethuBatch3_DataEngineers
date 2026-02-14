# Float object demo program
a = 10.8 # 10.8 is a object and a is the reference
print(a)
print(type(a)) # 10.8 is a float class object
print(id(a)) # address of the object

b = 25.
print(b)
print(type(b)) # 25. is a float class object

c = .689 # it is a float class object
print(c)

d = 3.4E2
'''this is a martissan exponent where is before E is fractionalnumber,
after E is exponent and the number after E is the number of times 10's
multiplied.'''
print(d)
print(type(d)) # it is converted from exponent to float object 

e = 9.62e-2
print(e) # 9.62/100 # e-2 represent 100 and '-' represent Dividing


# Complex object demo program
a = 3 + 4j
print(a) # 3 is real number and 4 is imag # j represent imag 
print(type(a)) # this is a complex class object
print(id(a)) # address of the complex object 

print(a.real) # real part
print(a.imag) # imag part

print(type(a.real)) # real value stored as float
print(type(a.imag)) # imag value stored as float

a = 6j
print(a)
print(type(a)) # python VM will assume real part as zero(0.0)

print(a.real)
print(a.imag)

# print(5 + j6) # invalid because j should be behind imag part
# print(3 + 4i) # invalid because i is there instead of J
# print(4+j) # invalid because there is no imag part

print(4 + 1j) # valid
print(4 + 0j) # valid


# Bool object demo program (Home work)
a = True
print(a)
print(type(a))
print(id(a))

b = False
print(b)
print(type(b))

print(True + True)
print(True + False)
print(False + True)
print(False + False)
print(True + True + True)

print(25 + 10.8 + True)

print(True > False)
print(True)
print(False)

# print(true) # NameError
# print(false) # NameError


a = 0O6247 # this is a Octal 
print(a)
print(type(a))
print(id(a))

b = 0o6247
print(id(b))
print(b)

c = 3239
print(c)
print(id(c))

# print(0o9248) # invalid digit in octal literal


# Find outputs for Hexa-decimal (Home work)
a = 0XA7B9
print(a)
print(type(a))

b = 0xBEEF
print(b)

# print(A7B9) # NameError
print('A7B9') # prints string

# print(0XBEER) # invalid hexadecimal literal
# print(0XHYD) # invalid hexadecimal literal
# print(0xA7G9B) # invalid hexadecimal literal


# Find outputs (Home work)
a = 9248
print(a)
print(type(a))
