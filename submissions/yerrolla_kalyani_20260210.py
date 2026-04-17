# float  object  demo  program (Home  work)
a = 10.8
print(a) #10.8
print(type(a))#<class 'int'>
print(id(a)) #address/id of object
b = 25.
print(b) #25.0
print(type(b))#<class 'float'>
c = .689
print(c) #0.689
d = 3.4E2
print(d) #340
print(type(d)) #<class 'float'>
e = 9.62e-2
print(e) #9.62e-2
print(9.8.2) #syntax error 
__________________________________________________________________________________________--

# complex object demo program
a = 3 + 4j
print(a) #3+4j
print(type(a)) #<class 'complex'>
print(id(a)) #prints id /address of object 3+4j
print(a . real) #3.0
print(a . imag) #4.0
print(type(a . real)) #<class 'float'>
print(type(a . imag)) #<class 'float'>
_______________________________________________________________________________________

# Find outputs (Home work)
a = 6j
print(a) #6j
print(type(a))#<class'complex'>
print(a.real)#0.0
print(a.imag) #6j
print(5 + j6)   #error due to invalid complex object, j should present after 6
print(3 + 4i)  #error due to invalid complex object literal i,only j is used.
print(4+j)  #error due to invalid complex object or value ,no image value
print(4 + 1j) #4+1j
print(4 + 0j) #4+0j

_________________________________________________________________________________


# bool object demo program  (Home  work)
a = True
print(a) #True
print(type(a)) #<class 'bool'>
print(id(a)) #prints the id /address of object True
b = False
print(b) #False
print(type(b)) #<class 'bool'>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True)  #36.8
print(True > False)    #True
print(True)  #True
print(False)  #False
print(true) # error due to it is 'True' not ture
print(false)  #error due to it is'False' not false
________________________________________________________________________

# Find  outputs (Home  work)
a = 0O6247
print(a)  #3072
print(type(a))  #<class 'int'>
print(id(a))    #prints address of the object 3072                                                    
b = 0o6247
print(id(b))  #  prints address of the object 3072                                                                                           
print(b)  #25339
c = 3239
print(c) 3239
print(id(c)) #  prints address of the object 3239
print(0o9248) # error due to invalid octal number 9,8
___________________________________________________________________________

# Find  outputs  (Home  work)
a = 0XA7B9
print(a)  #43937
print(type(a)) #<class'int'>
b = 0xBEEF
print(b)  #45386
print(A7B9)  #43237 
print('A7B9') print A7B9
print(0XBEER) #error due to it is not a valid  hexa-decimal object,containing  R
print(0XHYD)#error due to it is not a valid integer or hexa-decimal object containing Y
print(0xA7G9B)#error due to it is not a valid integer or hexa-decimal object containing G

___________________________________________________________________________

# Find outputs (Home  work)
a = 9248
print(a)#9248
print(type(a)) #<class'int'>