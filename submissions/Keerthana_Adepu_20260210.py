
... Float Object Homework
... 
... a = 10.8
... print(a) #10.8
... print(type(a)) #class ‘float’
... print(id(a)) #address of the float object 10.8
... 
... b = 25.
... print(b) #25.0
... print(type(b)) #class ‘float’
... 
... c = .689
... print(c) #0.689
... 
... d = 3.4E2
... print(d) #3.4*10^2
... print(type(d)) #class ‘float’
... 
... e = 9.62e-2
... print(e) #9.62*10^-2
... 
... print(9.8.2) #error because a decimal (float) can only contain one period
... 
... 
... Complex Object Homework
... 
... a = 3 + 4j
... print(a) #3 + 4j
... print(type(a)) #class ‘complex’
... print(id(a)) #address of complex object 3 + 4j
... 
... print(a . real) #3.0
... print(a . imag) #4.0
... print(type(a . real)) #class ‘float’
... print(type(a . imag)) #class ‘float’
... 

Outputs Homework

a = 6j
print(a) #6j
print(type(a)) #class ‘complex’

print(a.real) #0.0
print(a.imag) #6.0

print(5 + j6)  #error because the ‘j’ should be after the imag part of the object, not before

print(3 + 4i) #error because complex number is represented by ‘j’ not ‘i’

print(4+j) #error because there is no number before the imag part of the complex number
print(4 + 1j) #4 + 1j
print(4 + 0j) #4 + 0j


Bool Object Homework

a = True
print(a) #True
print(type(a)) #class ‘bool’
print(id(a)) #address of bool object True

b = False
print(b) #False
print(type(b)) #class ‘bool’

print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True) #36.8

print(True > False) #True

print(True) #True
print(False) #False

print(true) #error because the ‘t’ in True needs to be capital ‘T’
print(false) #error because the ‘f’ in False needs to be capital ‘F’


Outputs Homework #2

a = 0O6247
print(a) #3239
print(type(a)) #class ‘int’
print(id(a)) #address of object a

b = 0o6247
print(id(b)) #address of object b, which is the same as object a because python reuses an object if the output is the same
print(b) #3239

c = 3239
print(c) #3239
print(id(c)) #address of object c, and object b and a, because python reuses an object if the output is the same

print(0o9248) #error because an octal integer’s range is 0-7 so 9 should not exist


Outputs Homework #3

a = 0XA7B9
print(a) #42937
print(type(a)) #class ‘int’

b = 0xBEEF
print(b) #48879
print(A7B9)  #error because the prefix of the hexadecimal integer is not written beforehand
print('A7B9') #A7B9
print(0XBEER) #error because an hexadecimal can only contain numbers from 0-7 and A-F
print(0XHYD) #error because an hexadecimal can only contain numbers from 0-7 and A-F
print(0xA7G9B) #error because an hexadecimal can only contain numbers from 0-7 and A-F


Outputs Homework #4

a = 9248
print(a) #9248
