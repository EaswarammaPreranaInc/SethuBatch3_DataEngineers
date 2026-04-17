# int()  function  demo  program
print(int(10.8))        #  Converts  10.8  to  10
print(int(True))        #  Converts   True  to   1
print(int(False))       # Converts False to 0
print(int('25'))        #  Converts  '25'  to  25
print(int('0075'))      #  Converts  '0075'  to   75
print(int(0B11010))     #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(0B11010)          #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(int(0O6247))      #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(0O6247)           #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(int(0XA7B9))      #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(0XA7B9)           #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
#print(int(3 + 4j)) #  Error  :  complex  number  can not be converted to int
#print(int('25.4')) #  Error :  string  float  can not be converted to int
#print(int('Ten'))  #  Error :  'Ten'  can not be converted to int

# float()  function  demo  program

print(float(25))    #  Converts  25  to  25.0
print(float(True))  #  Converts   True  to  1.0
print(float(False)) #  Converts  False  to  0.0
print(float('92'))  #  Converts  '92'  to   92.0
print(float('36.4'))  #  Converts   '36.4'   to   36.4
print(float('0075'))  #  Converts   '0075'  to  75.0
print(float(0B1010101)) # Converts  binary  number  to  decimal  number  i.e.  64 + 16 + 4 + 1 = 85.0
print(float(0O6247))    # Converts  octal   number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239.0
print(float(0XA7B9))    # Converts   hexa-decimal   number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937.0
#print(float(3 + 4j))   #  Error : complex number  can  not  be  converted to  float
#print(float('Ten'))    #  Error :  'Ten'  can  not  be  converted to  float

# complex()  function  demo  program
print(complex(3 , 4)) # (3+4j)
print(complex(0 , 4)) #  4j
print(complex(3)) # (3+0j)
print(complex(3.8 , 4.6)) # (3.8 + 4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3 + 4.5j)
print(complex(True , False)) # (1+0j)
print(complex(True)) #  (1+0j)
print(complex(False)) #  0j
print(complex(True , 4)) # (1+ 4j)
print(complex('3')) #  (3+0j)
print(complex('3.8')) # (3.8+0j)
#print(complex(3 , '4')) #  Error :  2nd  argument  can  not  be  a  string
#print(complex('3' , 4)) #  Error :  2nd  argument  is   not  permitted  as  first argument is  a  string
#print(complex('3' , '4'))  #  Error :  2nd  argument  is   not  permitted  as  first argument is  a  string
#print(complex('Ten')) #  Error  :  'Ten'  can  not  be converted  to  complex

#  bool()  function  demo  program
print(bool(0))   #  False  due  to  0
print(bool(10))  # True :   10  is  non-zero
print(bool(-25)) # True  :  -25   is  non-zero
print(bool(0.0)) # False  due to  0.0
print(bool(0.1)) # True  :  0.1  is non-zero
print(bool(0 + 0j)) # False :  Both  real  and  imag  are  zeroes
print(bool(10 + 20j)) # True :  real  is  non-zero
print(bool(-15j)) # True :  imag  is  non-zero
print(bool('False')) #  True :  'False'  is  non-empty  string
print(bool('')) #False  due  to  empty  string
print(bool('Hyd')) #True  :  'Hyd'  is  a  non-empty  string
print(bool(' ')) #True  : ' '  is  non-empty  string
print(bool('True')) #True  :  'True'  is  non-empty  string

# str()  function  demo  program
print(str(25))    #  Converts   25   to  '25'
print(str(10.8)) #  Converts  10.8  to  '10.8'
print(str(3 + 4j))  #  Converts  3+4j  to  '3+4j'
print(str(True))  #  Converts   True    to  'True'
print(str(False))  #  Converts   False  to  'False'
print(str(None))  #  Converts  None  to  'None'

# oct()  function  demo  program
print(oct(195))  #0o303
print(oct(0B10101110010)) # 002562 
print(oct(0xA7B9))  # 42937

# hex()  function  demo  program
print(hex(25))  #19
print(hex(0B10101111010111)) # 0X2BD7
print(hex(0O6247)) #3239
