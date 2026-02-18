day - 3 python

# int()  function  demo  program
print(int(10.8))  >>  10
print(int(True))  >>  1
print(int(False))  >>  0
print(int('25'))  >>  25
print(int('0075'))  >>  75
print(int(0B11010))  >>  26
print(0B11010)  >>  26
print(int(0O6247))  >>  3239
print(0O6247)  >>  3239
print(int(0XA7B9))  >>  42937
print(0XA7B9)  >>  42937
print(int(3 + 4j))  >> error #not possible with complex numbers  
print(int('25.4'))  >>  25
print(int('Ten'))  >>  error #object should be number not a alphabet or special character


print(float(25))  >>  25.0
print(float(True))  >>  1.0
print(float(False))  >>  0
print(float('92'))  >>  92.0
print(float('36.4'))  >>  36.4
print(float('0075'))  >>  75.0
print(float(0B1010101))  >>  85.0
print(float(0O6247))  >>  3239.0
print(float(0XA7B9))  >>  42937.0
print(float(3 + 4j))  >>  error
print(float('Ten'))  >>  error


complex()   function
-----------------------
1) What  does  complex(3 , 4)  do  ?  >>  3+4j  
2) What  does  complex(3.8)  do ?  >>  3.8+0j
3) What  does  complex('9.5')  do ?  >>  9.5+0j
4) Is  complex(3 , '4')  valid ?  >>  no because 2nd arg is not be string, if 1st arg will it can possible
6) Is  complex('3' , 4)  valid ?  >>  no because 1st arg is string but 2nd arg is not permitted(no-sequence object)


# complex()  function  demo  program
print(complex(3 , 4))  >>  3+4j
print(complex(0 , 4))  >>  4j
print(complex(3))  >>  3+0j
print(complex(3.8 , 4.6))  >>  3.8+4.6j
print(complex(3.8))  >>  3.8+0j
print(complex(3 , 4.5))  >>  3+4.5j
print(complex(True , False))  >>  1+0j
print(complex(True))  >>  1+0j
print(complex(False))  >>  0
print(complex(True , 4))  >>  1+4j
print(complex('3'))  >>  3+0j
print(complex('3.8'))  >>  3.8+0j
print(complex(3 , '4'))  >>  error
print(complex('3' , 4))  >>  error
print(complex('3' , '4'))  >>  error
print(complex('Ten'))  >> error


#  bool()  function  demo  program
print(bool(0))  >>  False
print(bool(10))  >>  True
print(bool(-25))  >>  True
print(bool(0.0))  >>  False
print(bool(0.1))  >>  True
print(bool(0 + 0j))  >>  False
print(bool(10 + 20j))  >>  True
print(bool(-15j))  >>  True
print(bool('False'))  >>  True
print(bool(''))  >>  False
print(bool('Hyd'))  >>  True
print(bool(' '))  >>  True
print(bool('True'))  >>  True


# str()  function  demo  program
print(str(25))  >>  '25'
print(str(10.8))  >>  '10.8'
print(str(3 + 4j))  >>  '3 + 4j'
print(str(True))  >>  'True'
print(str(False))  >>  'False'
print(str(None))  >>  'None'


# oct()  function  demo  program
print(oct(195))  >>  0o303
print(oct(0B10101110010))  >>  0o2562  #4 2 1
print(oct(0xA7B9))  >>  0o123671  #firstly convert hexa(8 4 2 1) to octal(4 2 1)


# hex()  function  demo  program
print(hex(25))  0x19
print(hex(0B10101111010111)) >> 0o2bd7  #8 4 2 1
print(hex(0O6247))  >> 0xca7  #8 4 2 1
