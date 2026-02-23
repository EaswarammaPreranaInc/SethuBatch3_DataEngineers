Day - 1 python

# float  object  demo  program (Home  work)
a = 10.8
print(a)   -->>  10.8
print(type(a))  -->> <class 'float'>
print(id(a))  -->>  #returns address of an object
b = 25.
print(b)  -->>  25.0
print(type(b))  -->>  <class 'float'>
c = .689 
print(c)  -->>  0.689
d = 3.4E2
print(d)  -->> 340.0  # 3.4 * 10**2
print(type(d))  -->>  <class 'float'>
e = 9.62e-2
print(e)   -->>  0.0962  #9.62 * 10**-2
print(9.8.2)  -->> error 


# complex object demo program
a = 3 + 4j
print(a)  -->>  3+4j	 											
print(type(a))  -->> <class 'complex'>
print(id(a))  -->>  #returns address of an object
print(a . real)  -->>  3.0
print(a . imag)  -->>  4.0
print(type(a . real))  -->> <class 'float'>
print(type(a . imag))  -->> <class 'float'>


# Find outputs (Home work)
a = 6j
print(a)  -->>  6j
print(type(a))  -->> <class 'complex'>
print(a.real)  -->>  0
print(a.imag)  -->> 6.0
print(5 + j6)  -->>  error
print(3 + 4i)  -->>  error
print(4+j)     -->>  error
print(4 + 1j)  -->>  4+1j
print(4 + 0j)  -->>  4+0j


# bool object demo program  (Home  work)
a = True
print(a)  -->>  True
print(type(a))  -->>  <class 'bool'>
print(id(a))  -->>  #returns address of an object
b = False
print(b)  -->>  False
print(type(b))  -->>  <class 'bool'>
print(True + True)  -->>  2
print(True + False)  -->>  1
print(False + True)  -->>  1
print(False + False)  -->>  0
print(True + True + True)  -->>  3
print(25 + 10.8 + True)  -->>  36.8
print(True > False)  -->>  True
print(True)  -->>  True
print(False) -->>  False
print(true)  -->>  error
print(false) -->>  error


# Find  outputs (Home  work)
a = 0O6247
print(a)  -->>  3239
print(type(a))  -->>  <class 'int'>
print(id(a))  -->>  #returns address of an object (octal integer)
b = 0o6247  
print(id(b))  -->>  #returns address of an object (octal integer)
print(b)  -->>  3239
c = 3239
print(c)  -->> 3239
print(id(c))  -->>  
print(0o9248)  -->> error # it is an octal integer (digits upto 0 to 7)


# Find  outputs  (Home  work)
a = 0XA7B9
print(a)  -->>  42937
print(type(a))  -->> <class 'int'>
b = 0xBEEF                    
print(b)  -->>  48879  
print(A7B9)  -->> error # improper integer
print('A7B9')  -->> A7B9 # it is an string
print(0XBEER)  -->> error #the range of hexadecimal integer upto A-F
print(0XHYD)   -->> error #out of hexadecimal range
print(0xA7G9B)  -->> error #out of hexadecimal range


# Find outputs (Home  work)
a = 9248
print(a)  -->>  9248
print(type(a))  -->>  <class 'int'>