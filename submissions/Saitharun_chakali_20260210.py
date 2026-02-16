# float  object  demo  program (Home  work)

a = 10.8            # reference ‘a’ points class float object
print(a)              # gives content of reference ‘a’
print(type(a))     # prints <class ‘float’ >
print(id(a))         #prints address (or)Id of reference ‘a’ 

b = 25.               # reference ‘b’ points class float object
print(b)               # gives content of reference ‘b’
print(type(b))      # prints <class ‘float’>

c = .689              # reference ‘c’ points class float object
print(c)                # gives content of reference ‘c’

d = 3.4E2            # reference ‘d’ points class float object
print(d)                # gives content of reference ‘d’
print(type(d))       # prints <class ‘float’ >

e = 9.62e-2         # reference ‘e’ points class float object 
print(e)                # gives content of reference ‘e’ ie 0.0962
print(9.8.2)          # invalid syntax


# complex object demo program
a = 3 + 4j                      # reference ‘a’ points class complex object 
print(a)                          # gives content of reference ‘a’ ie 3+4j
print(type(a))                 # prints <class ‘complex’>
print(id(a))                     # prints id (or) address of ‘a’
print(a . real)                 # prints real value of ‘a’ ie 3.0
print(a . imag)               # prints imag value of ‘a’ ie 4.0
print(type(a . real))        # prints <class ‘float’>
print(type(a . imag))      # prints <class ‘float’>

# Find outputs (Home work)
a = 6j                 # reference ‘a’ points class complex object 
print(a)              # gives content of reference ‘a’ ie 6j
print(type(a))     # prints <class ‘complex’>
print(a.real)       #  output = 0.0
print(a.imag)     # output = 6.0
print(5 + j6)       # invalid syntax
print(3 + 4i)       # invalid syntax
print(4+j)           # invalid syntax
print(4 + 1j)       # output = 4+1j
print(4 + 0j)       # output = 4+0j

#bool object demo program  (Home  work)
a = True                                   # reference ‘a’ points class bool object 
print(a)                                     # gives content of reference ‘a’ ie True
print(type(a))                            # <class ‘bool’>
print(id(a))                                # prints id ( or ) address of bool object

b = False                                  # reference ‘b’ points class bool object 
print(b)                                     # gives content of reference ‘b’ ie False
print(type(b))                            # <class ‘bool’>
print(True + True)                     # prints ‘2’
print(True + False)                   # prints ‘1’
print(False + True)                   # prints ‘1’
print(False + False)                  # prints ‘0’
print(True + True + True)          # prints ‘3’
print(25 + 10.8 + True)             # prints ‘36.8’
print(True > False)                   # prints True
print(True)                                # prints True
print(False)                               # prints False
print(true)                                 # invalid
print(false)                                # invalid


# Find  outputs (Home  work)
a = 0O6247       # reference ‘a’ points class int object 
print(a)              # gives decimal equivalent to ‘a’ ie 3239
print(type(a))     # prints <class ‘int’>
print(id(a))         # prints address (or) id of  int object

b = 0o6247        # reference ‘b’ points class int object 
print(id(b))          # prints address (or) id of  int object
print(b)               # gives decimal equivalent to ‘b’ ie 3239


c = 3239            # reference ‘c’ points to  class int object 
print(c)               # prints integer output 3239
print(id(c))          # prints address (or) id of  int object
print(0o9248)     # invalid 


# Find  outputs  (Home  work)
a = 0XA7B9            # reference ‘a’ points class int object 
print(a)                    # gives decimal equivalent to ‘a’
print(type(a))           # prints <class ‘int’>


b = 0xBEEF            # reference ‘b’ points class int object 
print(b)                    # gives decimal equivalent to ‘b’
print(A7B9)             # invalid syntax
print('A7B9')            # prints A7B9
print(0XBEER)        # invalid syntax
print(0XHYD)          # invalid syntax
print(0xA7G9B)      # invalid syntax



# Find outputs (Home  work)
a = 9248            # reference ‘a’ points to class int object 
print(a)              # gives content of reference ‘a’ ie ‘9248’
print(type(a))    # prints <class ‘int’>
