'''Home  work on 10-02-26'''


# float  object  demo  program
a = 10.8
print(a)#10.8
print(type(a))#<class 'float'>
print(id(a))#  address of an object a
b = 25.

print(b)#25.0
print(type(b))#<class 'float'>
c = .689
print(c)# 0.689
d = 3.4E2
print(d)#==>3.4*10^2=340.0
print(type(d))#<class 'float'>
e = 9.62e-2
print(e)#==>9.62*10^-2=0.0962
print(9.8.2)# error due to it has two  Decimals pointes

# complex object demo program
a = 3 + 4j
print(a)#3+4j
print(type(a))#<class 'complex'>
print(id(a))# address of an object a
print(a . real)#3.0
print(a . imag)#4.0
print(type(a . real))#<class 'complex'>
print(type(a . imag))#<class 'complex'>


#Find outputs
a = 6j
print(a)#6j
print(type(a))#<class 'complex'>
print(a.real)#0.0
print(a.imag)#6.0
print(5 + j6)#error due to imag will be starting  number
print(3 + 4i)# error due to 'i' become  'j' in python  there is no 'i'imag in python
print(4+j) # error due to no j values
print(4 + 0j)#4+0j


# bool object demo program
a = True
print(a)#True
print(type(a))#<class 'bool'>
print(id(a))# memory address of an object
b = False
print(b)#false
print(type(b))#<class 'bool'>
print(True + True)#2
print(True + False)#1
print(False + True)#1
print(False + False)#0
print(True + True + True)#3
print(25 + 10.8 + True)#37.8
print(True > False)#True
print(True)#True
print(False)#False
print(true)#error due to pre defined key word Should start with capital letter
print(false)#error due to pre defined key word Should start with capital letter


# Find  outputs
a = 0O6247
print(a)#3239
print(type(a))#<class ' Int'>
print(id(a))# memory address of an object a
b = 0o6247
print(id(b))# memory address of an object a
print(b)#3239
c = 3239
print(c)#3239
print(id(c))# memory address of an object
print(0o9248)#0o9248

# Find  outputs
a = 0XA7B9
print(a)#42937
print(type(a))#<class 'int'>
b = 0xBEEF
print(b)#48879
print(A7B9)#error due to It should be start with 0X or 0x
print('A7B9')#A7B9
print(0XBEER)##error due It accepts alphabets From A to F Only
print(0XHYD)#error due It accepts alphabets From A to F Only
print(0xA7G9B)##error due It accepts alphabets From A to F Only


# Find outputs
a = 9248
print(a)#9248
print(type(a))<class 'int'>