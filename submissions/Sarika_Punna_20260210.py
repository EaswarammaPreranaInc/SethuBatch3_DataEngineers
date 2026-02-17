#Python Homework (Tuesday Feb 10 2026)

# float object demo program (Homework)
a = 10.8
print(a) #10.8
print(type(a)) #<class int>
print(id(a)) # address of object 10.8 (1000)
b = 25.
print(b) #error there is no number after a decimal point
print(type(b))
c = .689#error 
print(c)
d = 3.4E2 # d refers to an object (3.4×10 power 2)
print(d) # 340
print(type(d)) #<class tint>
e = 9.62e-2
print(e)#0.0962 (prints the value of 9.6×10 power -2)
print (9.8.2) # error floating object cannot have two decimal points

# complex object demo program
a = 3 + 4j
print(a) # 3+4j
print(type(a)) #<class complex>
print(id(a)) # address of object (1000)
print(a .real)#3.0
print(a .imag)#4.0
print(type(a .real)) #<class float>
print(type(a. imag)) #<class float>

# Find outputs (Homework)
a = 6j
print(a) #6j
print(type(a)) #< class complex>
print(a.real) #0.0
print(a.imag) #6.0
print(5 + j6)  #5+6j
print(3 + 4i) # error complex should have j not i
print(4+j) # error complex should have j not i 
print(4 + 1j) # error complex should have j not i 
print(4 + 0j) 4+0j

# bool object demo program (Homework)
a = True
print(a) # True
print(type(a)) #<class bool>
print(id(a)) # address of object True(1000)
b = False
print(b)#False
print(type(b)) #<class bool>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True) #31.8(25+10.8+1)
print(True > False) #True
print(True) #True
print(False) #False
print(true) #error T should be capital not small
print(false) # error f should be capital (F) not small(f)

# Find outputs (Homework)
a = 0O6247 # stores decimal equivalent of 0O6247
print(a) # prints decimal equivalent of an octal integer(0O6247)
print(type(a)) #<class int>
print(id(a))  #adress of an object (1000)
b = 0o6247
print(id(b)) # address of an object same as in last print statement (1000) because both a,b refers to same object
print(b) # prints decimal equivalent of an octal integer 0O6247
c = 3239
print(c) #3239
print(id(c)) # address of object 3239 same as previous address (1000) because c refers to the same object as a,b
print(0o9248) # error octal integer can have only 0-7 cannot have 8,9

# Find  outputs  (Homework)
a = 0XA7B9
print(a) # prints decimal equivalent of an hexadecimal integer 0XA7B9
print(type(a)) #<class int>
b = 0xBEEF 
print(b) # prints decimal equivalent of an hexadecimal integer 0xBEEF
print(A7B9)  # error hexadecimal should have a prefix 0X
print('A7B9') #prints  A7B9 as a string 
print(0XBEER) # error hexadecimal can have only 0-9, a-f
print(0XHYD) # error hexadecimal can only have 0-9, a-f
print(0xA7G9B) # error hexadecimal can only have 0-9, a-f

# Find outputs (Homework)
a = 9248
print(a) #9248
print(type(a)) #<class int>
