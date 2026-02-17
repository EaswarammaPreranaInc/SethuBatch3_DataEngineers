# float  object  demo  program (Home  work)
a = 10.8
print(a)        #ANS = 10.8
print(type(a))  #ANS = <class 'float'>
print(id(a))    #ANS = 0.689
b = 25.
print(b)        #ANS = 25.0
print(type(b))  #ANS = <class 'float'>
c = .689
print(c)        #ANS = 0.689
d = 3.4E2
print(d)        #ANS = 340.0
print(type(d))  #ANS = <class 'float'>
e = 9.62e-2
print(e)        #ANS = 0.0962

#print(9.8.2) GIVES YOU THE ERROR




# complex object demo program
a = 3 + 4j
print(a)              #ANS = (3+4j)
print(type(a))        #ANS = <class 'complex'>
print(id(a))          #ANS = 139910635110768
print(a . real)       #ANS = 3.0
print(a . imag)       #ANS = 4.0
print(type(a . real)) #ANS = <class 'float'>
print(type(a . imag)) #ANS = <class 'float'>





# Find outputs (Home work)
a = 6j
print(a)        #ANS = 6j
print(type(a))  #ANS = <class 'complex'>
print(a.real)   #ANS = 0.0
print(a.imag)   #ANS = 6.0
#print(5 + j6)  #ANS = ERROR
#print(3 + 4i)  #ANS = ERROR
#print(4+j)     #ANS = ERROR
print(4 + 1j)   #ANS = (4+1j)
print(4 + 0j)   #ANS = (4+0j)



# bool object demo program  (Home  work)
a = True
print(a)                  #ANS = True
print(type(a))            #ANS = <class 'bool'>
print(id(a))              #ANS = 1010
b = False
print(b)                  #ANS = False
print(type(b))            #ANS = <class 'bool'>
print(True + True)        #ANS = 2
print(True + False)       #ANS = 1
print(False + True)       #ANS = 1
print(False + False)      #ANS = 0
print(True + True + True) #ANS = 3
print(25 + 10.8 + True)   #ANS = 36.8
print(True > False)       #ANS = True
print(True)               #ANS = True
print(False)              #ANS = False
#print(true)              #ANS = ERROR
#print(false)             #ANS = ERROR



# Find  outputs (Home  work)
a = 0O6247
print(a)        #ANS = 3239
print(type(a))  #ANS = <class 'int'>
print(id(a))    #ANS = 1010
b = 0o6247
print(id(b))    #ANS = 1010
print(b)        #ANS = 3239
c = 3239
print(c)        #ANS = 3239
print(id(c))    #ANS = 1010
#print(0o9248)  #ERROR




# Find  outputs  (Home  work)
a = 0XA7B9
print(a)        #ANS = 42937
print(type(a))  #ANS = <class 'int'>
b = 0xBEEF
print(b)        #ANS = 48879
#print(A7B9)
print('A7B9')   #ANS = A7B9
#print(0XBEER)
#print(0XHYD)
#print(0xA7G9B)