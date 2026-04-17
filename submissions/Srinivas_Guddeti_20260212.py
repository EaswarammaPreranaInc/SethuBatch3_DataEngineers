
print(int(10.8))  #  10
print(int(True)) #   1
print(int(False)) #0  
print(int('25'))  #25
print(int('0075'))  #75
print(int(0B11010))   #26
print(0B11010)      #26
print(int(0O6247))   #3239
print(0O6247)       #3239
print(int(0XA7B9)) #42937
print(0XA7B9)       #42937
#print(int(3 + 4j))  #error int argument should be in string and should not be a complex number
#print(int('25.4'))  #error string representing a float, not an integer.
#print(int('Ten'))  #error argument should be numeric number not letters


#float()  function  demo  program

print(float(25))   #   25.0
print(float(True))    #   1.0
print(float(False))  #0.0
print(float('92'))    #92.0
print(float('36.4'))   #36.4
print(float('0075'))    #75.0 
print(float(0B1010101))  #85.0
print(float(0O6247))   # 3239.0
print(float(0XA7B9))   #42937.0
#print(float(3 + 4j))    #Error: float argument must be a string or real number, not 'complex'
#print(float('Ten'))   #Error  str should be in numeric not letters



#complex()  function  demo  program

print(complex(3 , 4))  #(3+4j)
print(complex(0 , 4))   #(0+4j)
print(complex(3))       #(3+0j)
print(complex(3.8 , 4.6))   #(3.8+4.6j)
print(complex(3.8))    # (3.8+0j)
print(complex(3 , 4.5))    #  (3+4.5j)
print(complex(True , False))  #(1+0j)
print(complex(True))          #(1+0j)
print(complex(False))         #(0j)
print(complex(True , 4))   #(1+4j)
print(complex('3'))       #(3+0j)
print(complex('3.8'))      #(3.8+0j)
#print(complex(3 , '4'))  #error second argument should not be in string
#print(complex('3' , 4))   #error argument should not be in string
#print(complex('3' , '4'))  #error both arguments are in string
#print(complex('Ten'))     #error argument should be numeric 



#bool()  function  demo  program

print(bool(0))    #False
print(bool(10))    #true
print(bool(-25))  #  True
print(bool(0.0))    # False
print(bool(0.1))    #True
print(bool(0 + 0j))  # False
print(bool(10 + 20j)) #True
print(bool(-15j))      #True
print(bool('False'))     #True
print(bool(''))     #False
print(bool('Hyd'))    #True
print(bool(' '))     #True  space is character so true
print(bool('True')) #True


#str()  function  demo  program

print(str(25))    #  '25'
print(str(10.8))   # '10.8'
print(str(3 + 4j))   # '3+4j'
print(str(True))    #'True'
print(str(False))    #'False'
print(str(None))    #'None'


#oct()  function  demo  program

print(oct(195))  #0o303
print(oct(0B10101110010))  #0o2562
print(oct(0xA7B9))     #0o123671



# hex()  function  demo  program

print(hex(25))                 # 0x19
print(hex(0B10101111010111))   # 0x2bd7
print(hex(0O6247))             # 0xca7














