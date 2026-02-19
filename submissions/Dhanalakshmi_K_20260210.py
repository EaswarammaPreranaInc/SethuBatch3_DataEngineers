# float object demo program (Home work) 
a = 10.8
print(a)  # 10.8
print(type(a)) # <class 'float'> 
print(id(a)) # address of object a 
b = 25.
print(b) # 25.0
print(type(b)) # <class 'float'>
c = .689
print(c) # 0.689 
d = 3.4E2
print(d) # 340
print(type(d)) # < class 'float'> 
e = 9.62e-2
print(e) # 0.0962
print(9.8.2) # ERROR because 9.8.2 is not a particular decimal number.


# complex object demo program 
a = 3 + 4j
print(a) # 3+4j
print(type(a)) # <class 'complex'> 
print(id(a)) # address of object a 
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # <class 'float'> 
print(type(a . imag)) # <class 'float'>
 


# Find outputs (Home work) 
a = 6j
print(a) # 6j
print(type(a)) # <class 'complex'> 
print(a.real) # 0.0
print(a.imag) #6.0
print(5 + j6) # ERROR because j should be after 6
print(3 + 4i) # ERROR because i can't be used in python hence it should be j 
print(4+j) # ERROR because imag value is not present
print(4 + 1j) # 4+1j print(4 + 0j) # 4+0j



# bool object demo program (Home work) 
a = True
print(a) # True
print(type(a)) # <class 'bool'> 
print(id(a)) # address of the object a 
b = False
print(b) # False 
print(type(b)) # <class 'bool'> 
print(True + True) # 2 
print(True + False) # 1 
print(False + True) # 1
print(False + False) # 0 
print(True + True + True) # 3 
print(25 + 10.8 + True) # 36.8 
print(True > False) # True 
print(True) # True 
print(False) # False
print(true) # ERROR because t should be capital letter in any Keyword 
print(false) # ERROR because f should be capital


# Find outputs (Home work) 
a = 0O6247
print(a) # 3239 
print(type(a)) # <class 'int'>
print(id(a)) # address of the object a 
b = 0o6247
print(id(b)) # address of the object b 
print(b) # 3239
c = 3239
print(c) # 3239
print(id(c)) # address of the object c
print(0o9248) # ERROR because octal integer should be from 0-8 only.



# Find outputs (Home work) 
a = 0XA7B9
print(a) # 42937 
print(type(a)) # <class 'int'> 
b = 0xBEEF
print(b) # 48879
print(A7B9) # ERROR because there is no reference for the object and no prefix indication.
print('A7B9') # A7B9
print(0XBEER) # ERROR because hexa-decimal integer should be from 0-9 and A-F or a-f. R can't be used.
print(0XHYD) # ERROR because hexa-decimal integer should be from 0-9 and A-F or a-f. H and Y can't be used.
print(0xA7G9B) # ERROR because hexa-decimal integer should be from 0-9 and A-F or a-f. G can't be used.



# Find outputs (Home work) a = 9248
print(a) # 9248 print(type(a)) # <class 'int'>

