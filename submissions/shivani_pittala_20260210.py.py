a = 10.8
print(a)	---> 10.8
print(type(a))  ---> <class 'float'>
print(id(a))    ---> 1000
b = 25.
print(b)	---> 25.0
print(type(b))  ---> <class 'float'>
c = .689
print(c)	---> 0.689
d = 3.4E2
print(d)	---> 340
print(type(d))	---> <class 'float'>
e = 9.62e-2
print(e)	---> 0.0962
print(9.8.2)	---> throws error bcz no double float 




# complex object demo program
a = 3 + 4j
print(a)	  ---> <3+4j>
print(type(a))	  ---> <class 'complex'>
print(id(a))	  ---> 3000
print(a . real)	  ---> 3.0
print(a . imag)   ---> 4.0
print(type(a . real))  ---> <class 'float'>
print(type(a . imag))  ---> <class 'float'>




 # Find outputs (Home work)
a = 6j
print(a)  	---> 6j
print(type(a))  ---> <class 'complex'>
print(a.real)   ---> 0.0
print(a.imag)   --->6.0
print(5 + j6)   ---> throws error bcz imag should be before j
print(3 + 4i)   ---> throws error bcz there is no i 
print(4+j)      ---> throws error bcz there is no imag in it
print(4 + 1j)   ---> 4+1j
print(4 + 0j)   ---> 4+0j


 # bool object demo program  
a = True
print(a)	--->True
print(type(a))  ---> <class 'bool'>
print(id(a))    ---> 5000
b = False
print(b)	 --->False
print(type(b))	 ---> <class'bool'>
print(True + True)   --->2
print(True + False)	 --->1
print(False + True)	 --->1
print(False + False)	 --->0
print(True + True + True)	 --->3
print(25 + 10.8 + True)	 --->36.8
print(True > False)  	 --->True
print(True)	 ---> True
print(False)	 ---> False
print(true)	 ---> trows error bcz t is not capital
print(false)	 ---> trows error bcz f is not capital



 # Find  outputs 
a = 0O6247	    
print(a)	   --->3239
print(type(a))	   ---><class 'int'>
print(id(a))	   ---> 60000		 
b = 0o6247
print(id(b))	   --->60000
print(b)	   --->3239
c = 3239
print(c)	   --->3239
print(id(c))	   --->60000
print(0o9248)      --->60000


 # Find  outputs  
a = 0XA7B9
print(a)          --->42937
print(type(a))    ---><class 'int'>
b = 0xBEEF
print(b)          --->48879
print(A7B9)       --->trows error bcz a7b9 is not defined
print('A7B9')     ---> A7B9
print(0XBEER)     ---> trows error bcz oxahecta doesnt support g letter 
print(0XHYD)      ---> trows error bcz oxahecta doesnt support h and y letter 
print(0xA7G9B)    ---> trows error bcz oxahecta doesnt support letter G


# Find outputs
a = 9248
print(a)          --->9248
print(type(a))    ---> < class 'int'>









