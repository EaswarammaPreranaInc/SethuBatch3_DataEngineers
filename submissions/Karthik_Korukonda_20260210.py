a = 10.8 
print(a) #10.8 
print(type(a)) #<class 'float'> 
print(id(a)) #10000 
b = 25. 
print(b) #25.0 
print(type(b)) #<class 'float'> 
c = .689 
print(c) #0.689 
d = 3.4E2 
print(d) # 3.4*10^2 = 340.0 
print(type(d)) #<class 'float'>  mantissa  
e = 9.62e-2 
print(e) 9.62*10^-2 = 0.0962 
print(9.8.2) # error due to syntax 
# complex object demo program 
a = 3 + 4j 
print(a) #3+4j 
print(type(a)) #<class 'float'> 
print(id(a)) #10000 
print(a . real) #3.0 
print(a . imag) #4.0 
print(type(a . real)) #<class 'float'> 
print(type(a . imag)) #<class 'float'> 
# Find outputs (Home work) 
a = 6j 
print(a) 6j 
print(type(a)) <class 'complex'> 
print(a.real) #0.0 
print(a.imag) #6.0 
print(5 + j6)  # error  j should be after imag 
print(3 + 4i) # error should use j instead of i  
print(4+j) # error  
print(4 + 1j)# 4+1j 
print(4 + 0j) #4+0j 
a = True 
print(a) #True 
print(type(a)) #<class 'bool'> 
print(id(a)) #10000 
b = False 
print(b) #False  
print(type(b)) #<class 'bool'> 
print(True + True) #2 
print(True + False) #1 
print(False + True) #1 
print(False + False) #0 
print(True + True + True) #3 
print(25 + 10.8 + True) #36.8 
print(True > False)  #True 
print(True) #True 
print(False) #False 
print(true) #Error 
print(false)#Error should use capitals for T and F 
a = 0O6247 
print(a) #3239 
print(type(a)) #<class 'int'> 
print(id(a))  #1000 
b = 0o6247 
print(id(b)) #1000 
print(b) #3239 
c = 3239 
print(c) #3239 
print(id(c)) #1000 
print(0o9248) #Error as octal only have 0-7 
# Find  outputs  (Home  work) 
a = 0XA7B9 
print(a) #42937 
print(type(a)) #1000 
b = 0xBEEF  
print(b) 48879 
print(A7B9)  #Error as there is no prefix of hexadecimal 
print('A7B9') #A7B9 
print(0XBEER) #error as hexadecimal only takes upto F 
print(0XHYD) # error as hexadecimal only takes upto F 
print(0xA7G9B) #error as hexadecimal only takes upto F 
a = 9248 
print(a) 9248 
print(type(a)) <class 'int'> 