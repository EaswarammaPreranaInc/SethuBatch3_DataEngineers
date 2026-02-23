# float  object  demo  program (Home  work)
a = 10.8
print(a)   # 10.8
print(type(a))    #<class 'float'>
print(id(a))    #Address of object 10.8
b = 25.
print(b)   #25
print(type(b))    #<class 'int'>
c = .689
print(c)    # 0.689
d = 3.4E2
print(d)    #340.0
print(type(d))  #<class 'float'>
e = 9.62e-2
print(e)    #0.0962
print(9.8.2)   # error, bcz decimal value contains only one decimal point.
# complex object demo program
a = 3 + 4j
print(a)    #3 + 4j
print(type(a))    #<class 'complex'>
print(id(a))   #Address of the object 3+4j
print(a . real)   #3.0	
print(a . imag)   #4.0
print(type(a . real))   #<class 'float'>
print(type(a.imag))  #<class 'float'>
# Find outputs (Home work)
a = 6j
print(a)    #error, bcz it is not in the proper complex obj.
print(type(a))    # error, bcz it is not in the proper complex obj.
print(a.real)    # error, bcz it is not in the proper complex obj.
print(a.imag)    # error, bcz it is not in the proper complex obj.
print(5 + j6)   # invalid, bcz imag should be before j.
print(3 + 4i)   # invalid, bcz it should be j but not i.
print(4+j)   #invalid, bcz imag should be given.
print(4 + 1j)     # 4+1j
print(4 + 0j)   # 4+0j
# bool object demo program  (Home  work)
a = True	
print(a)   # True
print(type(a))   # <class 'bool'>
print(id(a))   # Address of object True.
b = False
print(b)    #False
print(type(b))    # <class 'bool'>
print(True + True)   # 2
print(True + False)   #1
print(False + True)   #1
print(False + False)   #0
print(True + True + True)    #3
print(25 + 10.8 + True)   #36.8
print(True > False)  # True
print(True)    #True
print(False)  #False
print(true)    #invalid, bcz t should be T.
print(false)    #invalid, bcz f should be F.
# Find  outputs (Home  work)
a = 0O6247
print(a)   #3239
print(type(a))   #<class 'int'>
print(id(a))    #address of object 3239.
b = 0o6247
print(id(b))    #Same as address of obj 3239
print(b)   #3239
c = 3239
print(c)   #3239
print(id(c))    # same as address of object 3238
print(0o9248)   # invalid,  bcz octal integer permits only 0 to 7 digits.
# Find  outputs  (Home  work)
a = 0XA7B9
print(a)     #42937
print(type(a))   #<class 'int'>
b = 0xBEEF
print(b)   #48879
print(A7B9)  # invalid, bcz it is not in proper integer format.
print('A7B9')   # A7B9
print(0XBEER)   # invalid, bcz Hexa decimal integer permits  only 0 to 9 digits and A to F alphabets. 
print(0XHYD)   # invalid, bcz Hexa decimal integer permits only 0 to 9 and A to F.
print(0xA7G9B)    # invalid, bcz Hexa decimal integer permits only 0 to 9 and A to F.
# Find outputs (Home  work)
a = 9248
print(a)   # 9248
print(type(a))     # <class 'int'>
