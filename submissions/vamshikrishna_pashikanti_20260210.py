# float  object  demo  program (Home  work)
a = 10.8
print(a)       # 10.8
print(type(a)) # <class 'float'> it will print type of the object
print(id(a))   # It will print address of object a

b = 25         
print(b)       # 25
print(type(b)) # <class 'int'> it will print type of object

c = .689       
print(c)       # 0.689

d = 3.4E2
print(d)       # 3.4*10^2=340.0
print(type(d)) # < class 'float'>

e = 9.62e-2   
print(e)        # 9.62*10^-2=0.0962
print(9.8.2)    # Error because it is not a float value

# complex object demo program
a = 3 + 4j
print(a)               # 3 + 4j
print(type(a))         # <class 'complex'>
print(id(a))           # address of object a
print(a . real)        # 3.0 it will print only real value
print(a . imag)        # 4.0 it will print only imag value
print(type(a . real))  # <class 'float'>  complex values always returns to float 
print(type(a . imag))  # <class 'float'>  complex values always returns to float

# Find outputs (Home work)
a = 6j
print(a)              # 6j
print(type(a))        # < class 'float'>
print(a.real)         # 0.0 because it not given real value 
print(a.imag)         # 0.6 
print(5 + j6)         # error because complex number must be in the form of a+bj not  a+jb
print(3 + 4i)         # error because complex number must be in the form of a+bj not a+ib
print(4+j)            # 4+j
print(4 + 1j)         # 4+1j
print(4 + 0j)         # 4+0j

# bool object demo program  (Home  work)
a = True
print(a)             #True
print(type(a))       # <class 'bool'>
print(id(a))         # address of object True

b = False
print(b)               # False
print(type(b))         # <class 'bool'>
print(True + True)     # 2  -->1+1=2
print(True + False)    # 1 --> 1+0=1
print(False + True)    # 0 + 1--> 1
print(False + False)   # 0 + 0 --> 0
print(True + True + True)   # 1 + 1 + 1-->3
print(25 + 10.8 + True)     # 25+10.8+1=36.8
print(True > False)         # True --> because 1>0
print(True)                 # True
print(False)                # False
print(true)                 # error because it not true its True
print(false)                # error because it not false its False

# Find  outputs (Home  work)
a = 0O6247
print(a)        # 3239
print(type(a))  #<class 'int'>
print(id(a))    # address of object a

b = 0o6247      
print(id(b))    # address of object b
print(b)        # 3239

c = 3239
print(c)        #  3239
print(id(c))    # address of object c
print(0o9248)   # error because octal integer values from 0-7

# Find  outputs  (Home  work)
a = 0XA7B9
print(a)         #42937
print(type(a))   # <class 'int'>

b = 0xBEEF       
print(b)         # 48879
print(A7B9)      # error 
print('A7B9')    # A7B9  its a string 
print(0XBEER)    # error R is not in range of hexadecimal
print(0XHYD)     # error Y is not in range of hexadecimal
print(0xA7G9B)   # error G is not in range of hexadecimal 
