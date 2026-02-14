02.10 11:40 PM
# float  object  demo  program
a = 10.8
print(a)  #output is 10.8
print(type(a))  #output is <class 'float'>
print(id(a))  #address of an object  a (139584284569104)
b = 25. 
print(b)  #25.0
print(type(b))  #<class 'float'>
c = .689
print(c)  #0.689
d = 3.4E2
print(d)  #340.0
print(type(d))  #<class 'float'>
e = 9.62e-2
print(e)  #0.0962
print(9.8.2)  #error because it has 2 decimals
---------------------------------//------------------------------------
# complex object demo program
a = 3 + 4j
print(a)  #(3+4j)
print(type(a))  #<class 'complex'>
print(id(a))   # Address of an object a is 139584284562096
print(a . real)  # 3.0
print(a . imag)   # 4.0 
print(type(a . real))  #  <class 'float'>
print(type(a . imag))    # <class 'float'>
-----------------------------//----------------------------------------
# Find outputs (Home work)
a = 6j
print(a)  # 6j
print(type(a))   # <class 'complex'>
print(a.real)     # 0.0
print(a.imag)    # 6.0
print(5 + j6)   # error because j must be always after the number
print(3 + 4i)    #error because i is not valid as imaginary but only j
print(4+j)        #eroor because it doesn't has imaginary number
print(4 + 1j)   # (4+1j)
print(4 + 0j)    # (4+0j)
-----------------------------//----------------------------------------
# bool object demo program  (Home  work)
a = True
print(a)   # True
print(type(a))     # <class 'bool'>
print(id(a))       # 10557792
b = False
print(b)       # False
print(type(b))    # <class 'bool'>
print(True + True)    # 2
print(True + False)    # 1
print(False + True)    # 1
print(False + False)    # 0
print(True + True + True)     # 3
print(25 + 10.8 + True)    # 36.8
print(True > False)    # True
print(True)      # False
print(False)      # False
print(true)      # error because t is small letter
print(false)      # error because f is small letter
--------------------------------//-------------------------------------
a = 0O6247
print(a)   # 3239
 print(type(a))    # <class'int'>
 print(id(a))       # 132813280615216
b = 0o6247
 print(id(b))      # 132813280615536
print(b)              #3239
c = 3239
print(c)           #3239
 print(id(c))          # 132813280616240 
print(0o9248)     #error because  octal numbers from  0 to 7
-----------------------------//----------------------------------------
a = 0XA7B9
print(a)       #42937
print(type(a))    #<class 'int'>
b = 0xBEEF
print(b)     #48879
print(A7B9)     # It is a name error that means A7B9 is not recognised as a defined variable.
print(0XHYD)      #syntax error: invalid hexadecimal 
print(0xA7G9B)      #error G is not hexa decimal
-------------------------------//--------------------------------------
a = 9248
print(a)    #9248
print(type(a))    #<class 'int'>
