# float  object  demo  program (Home  work)
a = 10.8
print(a) #10.8
print(type(a)) #<class 'float'>
print(id(a)) #address of object-->2000
b = 25.
print(b) #25
print(type(b)) #<class 'float'>
c = .689 
print(c) #0.689
d = 3.4E2
print(d) #3.4*10^2
print(type(d)) # <class 'float'>
e = 9.62e-2
print(e) #9.62*10^-2
print(9.8.2)# error in float there are no 2 decimals.
=====================================================================================================
# complex object demo program
a = 3 + 4j
print(a) #3+4j
print(type(a))#<class'complex'>
print(id(a))# address of object-->3000
print(a . real)#3.0
print(a . imag)#4.0
print(type(a . real))#<class 'float'>
print(type(a . imag))#<class 'float'>
====================================================================================================
# Find outputs (Home work)
a = 6j
print(a) #6j
print(type(a))# <class 'complex'>
print(a.real)#0.0
print(a.imag)#6.0
print(5 + j6)  #error-->j should be after imag
print(3 + 4i) #error--> there is no i in python it is only indicated as j
print(4+j) #error --> there should be atleast a number before j
print(4 + 1j)#4+1j
print(4 + 0j)#4+0j
========================================================================================================
# bool object demo program  (Home  work)
a = True
print(a)#True
print(type(a))#<class 'bool'>
print(id(a))#address of object-->4000
b = False
print(b)#False
print(type(b))# <class 'bool'>
print(True + True)#2
print(True + False)#1
print(False + True)#1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#36.8
print(True > False)  #True
print(True)#True
print(False)#False
print(true)#error it is not defined because it is True not true
print(false)#error it is not defined because it is False not false
================================================================================================================
# Find  outputs (Home  work)
a = 0O6247
print(a)# equivalent to decimal-3239
print(type(a))#<class 'int'>
print(id(a)) #address of object-->5000 
b = 0o6247
print(id(b))#same address-->5000
print(b)#equivalent to decimal-3239
c = 3239
print(c)#3239
print(id(c))#same address-->5000
print(0o9248)#error->there is no 8,9 because octal it has 0-7
======================================================================================================================
# Find  outputs  (Home  work)
a = 0XA7B9
print(a) #equivalent of decimal->42937
print(type(a))#<class 'int'>
b = 0xBEEF
print(b) #equivalent of decimal->48879
print(A7B9)  #error->0x is not there
print('A7B9')#A7B9
print(0XBEER)# error->hexadecimal has 0-9 digits a-f or A-F alphabets. there is no R
print(0XHYD)#error->hexadecimal has 0-9 digits a-f or A-F alphabets. there is no H,Y
print(0xA7G9B)#error->hexadecimal has 0-9 digits a-f or A-F alphabets. there is no G
================================================================================================================================
# Find outputs (Home  work)
a = 9248
print(a) #9248
print(type(a))# <class 'int'>
