a = 10.8
print(a)                 #prints 10.8
print(type(a))           #prints <class 'float'>
print(id(a))             #prints address of object as a sample 123456
b = 25.                    
print(b)                 #prints 25
print(type(b))           #prints <class 'int'>
c = .689 
print(c)                 #prints 0.689
d = 3.4E2
print(d)                 #prints 340.0
print(type(d))           #prints <class 'float'>
e = 9.62e-2
print(e)                 #prints 0.0962
print(9.8.2)             #Error


a = 3 + 4j
print(a)                 #prints (3+4j)
print(type(a))           #prints <class 'complex'>
print(id(a))             #prints some address of object 123456
print(a . real)          #prints 3.0
print(a . imag)          #prints 4.0
print(type(a . real))    #prints <class 'float'>
print(type(a . imag))    #prints <class 'float'>

a = 6j                   
print(a)                 #prints 6j
print(type(a))           #prints <class 'complex>
print(a.real)            #prints 0.0
print(a.imag)            #prints 6.0
print(5 + j6)            #prints Error
print(3 + 4i)            #prints Error
print(4+j)               #prints Error
print(4 + 1j)            #prints (4+1j)
print(4 + 0j)            #prints (4+0j)


a = True
print(a)                 #prints True
print(type(a))           #prints <class 'bool'>
print(id(a))             #prints some address like 12346
b = False                  
print(b)                 #prints False
print(type(b))           #prints bool
print(True + True)       #prints 2
print(True + False)      #prints 1
print(False + True)      #prints 1
print(False + False)     #prints 0
print(True + True + True)#prints 3
print(25 + 10.8 + True)  #prints 36.8
print(True > False)      #prints True
print(True)              #prints True
print(False)             #print False
print(true)              #print Error
print(false)             #print Error


a = 0O6247
print(a)                 #prints 3239
print(type(a))           #prints <class 'int'>
print(id(a))             #prints some address 123456
b = 0o6247         
print(id(b))             #prints some address 123456888
print(b)
c = 3239
print(c)                 #prints 3639
print(id(c))             #prints some address 
print(0o9248)            #prints Error because octal can have 0-7 only 



a = 0XA7B9              
print(a)                 #prints 42937
print(type(a))           #prints <class 'int'>
b = 0xBEEF
print(b)                 #prints 48879
print(A7B9)              #prints Error
print('A7B9')            #prints A7B9 as a string
print(0XBEER)            #prints Error due to diff alpha not in range of A-F
print(0XHYD)             #prints Error due to diff alpha not in range of A-F
print(0xA7G9B)           #prints Error due to diff alpha not in range of A-F



a = 9248
print(a)                 #prints 9248
print(type(a))           #prints <class 'int'> 