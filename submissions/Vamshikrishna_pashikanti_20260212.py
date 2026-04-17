# int()  function  demo  program
print(int(10.8))  #  10 ,Converts  10.8  to  10
print(int(True)) #   1,Converts   True  to   1
print(int(False))# 0, Converts False to 0
print(int('25'))# 25,Converts  '25'  to  25
print(int('0075'))# 75
print(int(0B11010))   #   16 + 8 + 2 = 26
print(0B11010)   #   26
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 =3 239
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0 = 42937
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0 = 42937
print(int(3 + 4j))  # error because it cannot converted complex into int
print(int('25.4'))  # error because strng float cannot converted into int
print(int('Ten'))   # error because string cannot conveted into int


'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

2) Conversion  of  binary  number  to  decimal  number
    ----------------------------------------------------------
          16    8   4   2    1  --->  Weights
	       1     1    0   1    0   --->  16 + 8 + 2 =  26

3) Conversion  of  octal  number  to  decimal  number
    ---------------------------------------------------------
        512   64   8    1  --->  Weights
	      6      2    4   7  --->  6 * 512 + 2 * 64 + 4 * 8 + 7 * 1  = 3239

4) Conversion  of  hexa-decimal  number  to  decimal  number
    ------------------------------------------------------------------
        4096   256   16    1  --->  Weights
	      A        7      B     9  --->  10 * 4096 + 7 * 256 + 11 * 16 + 9 * 1  = 42937
'''

# float()  function  demo  program
print(float(25))       #   25.0
print(float(True))     #   1.0
print(float(False))    # 0.0
print(float('92'))     # 92.0
print(float('36.4'))   #36.4
print(float('0075'))   #75.0
print(float(0B1010101))# 64 + 16 + 4 + 1 = 85.0 i.e, binary converted into float
print(float(0O6247))   # 6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239.0, octal numbr into float 
print(float(0XA7B9))   #10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937.0, octal number into float
print(float(3 + 4j))   # error complex number cannot be onverted into float
print(float('Ten'))    # error string cannot conveted into float values

# complex()  function  demo  program
print(complex(3 , 4))      #(3+4j)
print(complex(0 , 4))      #  4j
print(complex(3))          # (3+0j)
print(complex(3.8 , 4.6))  # (3.8 + 4.6j)
print(complex(3.8))        # (3.8+0j)
print(complex(3 , 4.5))    # (3 + 4.5j)
print(complex(True , False))# (1+0j)
print(complex(True))        #  (1+0j)
print(complex(False))       #0j
print(complex(True , 4))    # (1+ 4j)
print(complex('3'))         #  (3+0j)
print(complex('3.8'))       # (3.8+0j)
print(complex(3 , '4'))     # error2nd argument cannot be a string
print(complex('3' , 4))     #error
print(complex('3' , '4'))   # error if botharguments are string
print(complex('Ten') )      #error string is connot be complex

#  bool()  function  demo  program
print(bool(0))         # False, 0 indicates false
print(bool(10))        # True, all non empt strings are true
print(bool(-25))       #  True
print(bool(0.0))       # False, due to 0
print(bool(0.1))       # True
print(bool(0 + 0j))    # False, because both are zero's
print(bool(10 + 20j))  # True
print(bool(-15j))      # True
print(bool('False'))   #True
print(bool(''))        #False, empty string is treated as false
print(bool('Hyd'))     # True
print(bool(' '))       # True
print(bool('True'))    #True

# str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8))  #'10.8'
print(str(3 + 4j)) #'3 +4j'
print(str(True))   # 'True'
print(str(False))  # 'False'
print(str(None))   # 'None'

# oct()  function  demo  program
print(oct(195))  #0O303, decimal to octal
print(oct(0B10101110010))  #0O2562, binary to octal
print(oct(0xA7B9)) # 0O123671, hexadecimal to octal

# hex()  function  demo  program
print(hex(25))  #0X19, ie decimal to hexadecimal
print(hex(0B10101111010111)) #0X2BD7,ie, binary to hexadecimal
print(hex(0O6247)) #0XCA7, i.e, octal to hexadecimal



