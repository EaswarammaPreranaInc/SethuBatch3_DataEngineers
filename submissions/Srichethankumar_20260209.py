# float  object  demo  program (Home  work)
a = 10.8
print(a)  #10.8
print(type(a)) #<class 'float'>
print(id(a))  #address of the object 10.8 may be 1000.
b = 25.
print(b) #25.0 becoz there is no value there after decimal so zero.
print(type(b)) #<class 'float'>
c = .689
print(c) #0.689 becoz there is no value before decimal so it is consider as zero.
d = 3.4E2
print(d) #3.4*10^2 =>340.0
print(type(d)) #<class 'float'>
e = 9.62e-2
print(e) #9.62*10^-2 =>0.096
print(9.8.2)  #Error A number can have only one decimal point.



------------------------------------------------------------------------------------------------------

# complex object demo program
a = 3 + 4j
print(a) #3+4j
print(type(a)) #<class 'complex'>
print(id(a)) #address of the object 3+4j may be 2000.
print(a . real) #3.0
print(a . imag) #4.0
print(type(a . real)) #<class 'float'>
print(type(a . imag)) #<class 'float'>


--------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = 6j
print(a) # 6j
print(type(a)) #<class 'complex'>
print(a.real) #0.0
print(a.imag) #6.0
print(5 + j6)  #Error becoz j must should be after a number.
print(3 + 4i)  #Error becoz i not consider in complex.
print(4+j) #Error becoz j should not there only.
print(4 + 1j) #4+1j
print(4 + 0j) #4+0j

----------------------------------------------------------------------------------------------------------

# bool object demo program  (Home  work)
a = True
print(a) #1
print(type(a)) #<class 'int'>
print(id(a)) #address of the object 1 may be 1000.
b = False
print(b) #0
print(type(b)) #<class 'int'>
print(True + True) #1+1=2
print(True + False) #1+0=1
print(False + True) #0+1=1
print(False + False) #0+0=0
print(True + True + True) #1+1+1=3
print(25 + 10.8 + True) #36.8
print(True > False)  #True
print(True) #True
print(False) #True
print(true) #Error Becoz T should be capital letter.
print(false)#Error Becoz F should be Capital letter.

------------------------------------------------------------------------------------------------------------

# Find  outputs (Home  work)
a = 0O6247        512  64  8  1         
print(a) #         6  2   4  7   
                ----------------    
                   3072    128 +   32 +  7=3239
print(type(a)) #<class 'float'>
print(id(a))  #address of the object 3239 may be 3000.
b = 0o6247  
print(id(b))     #address of the object 3239 same as before address may be 3000.
print(b)    #3239
c = 3239 
print(c) #3239
print(id(c)) #address of the object 3239 same as before address may be 3000.
print(0o9248) #Error becoz python don't convert direct octal to decimal Equvalients.


---------------------------------------------------------------------------------------------

# Find  outputs  (Home  work)
a = 0XA7B9
print(a)         4096      256   16    1 
                  10        7     11   9
               ---------------------------
                    40960+ 1792 +176 + 9 =>42937
print(type(a))  #<class 'float'>
b = 0xBEEF
print(b)  # 4096      256   16    1 
             11        14   14    15
           --------------------------
             45056+  3584+  224 +  15 =>48879
print(A7B9)  #Error comes becoz python don't convert direct hexa to decimal equvalients.
print('A7B9')  #A7B9  Becoz it is String.
print(0XBEER)  #Error comes becoz python don't convert direct hexa to decimal equvalients.
print(0XHYD)  #Error comes becoz python don't convert direct hexa to decimal equvalients.
print(0xA7G9B) #Error comes becoz python don't convert direct hexa to decimal equvalients.



-----------------------------------------------------------------------------------------------------



# Find outputs (Home  work)
a = 9248
print(a)  #9248
print(type(a)) #<class 'int'>



















