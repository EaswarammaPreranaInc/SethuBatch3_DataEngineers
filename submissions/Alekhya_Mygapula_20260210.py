Python HomeWork(Day2)
Alekhya Mygapula


*float
a = 10.8
print(a)   #10.8
print(type(a))  #< class float>
print(id(a)) #address 
b = 25.
print(b)  #25
print(type(b))   #<class int>
c = .689
print(c) #error
d = 3.4E2
print(d) #340.0
print(type(d)) #<claa float>
e = 9.62e-2
print(e)  #0.0962
print(9.8.2) #error due to . float value should be like 10.5


*complex
a = 3 + 4j
print(a)  #3+4j
print(type(a))
print(id(a)) #adress
print(a . real) #3
print(a . imag) #4
print(type(a . real)) #<class int>
print(type(a . imag)) #<class int>


a = 6j
print(a) #6j
print(type(a)) #< class complex
print(a.real) #0
print(a.imag) #6.0
print(5 + j6)  #error due to imag value is after j
print(3 + 4i) #error due to i
print(4+j) #error due to no imag value
print(4 + 1j) #4+1j
print(4 + 0j)#4+0j


a = True
print(a) #True
print(type(a))  #<class bool>
print(id(a)) # adress
b = False
print(b) #False
print(type(b)) #<class bool>
print(True + True) #2
print(True + False) #1
print(False + True) #1
print(False + False) #0
print(True + True + True) #3
print(25 + 10.8 + True) #36.8
print(True > False)  #True
print(True) # True
print(False) #False
print(true) # error due to t
print(false) #error dueto f


a = 0O6247
print(a)  #3239
print(type(a)) #<class int>
print(id(a))  #adress
b = 0o6247
print(id(b)) #same adress
print(b) #3239
c = 3239
print(c) #3239
print(id(c)) #<class int>
print(0o9248) #error due to 9

a = 0XA7B9
print(a) #42937
print(type(a)) #<class int>
b = 0xBEEF
print(b) #48879
print(A7B9)  #error due to A not defiened
print('A7B9') # A7B9
print(0XBEER) # error due to albhabets
print(0XHYD) #error due to h y
print(0xA7G9B) #error due to G


a = 9248
print(a) #9248
print(type(a)) #<class int>