Thammadaveni anusha
# int()  function  demo  program
print(int(10.8))  #  10
print(int(True)) #   1
print(int(False))   #0
print(int('25'))    #25
print(int('0075'))  #0075
print(int(0B11010))   #   16 + 8 + 2 = 26
print(0B11010)   #   26
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0=(3239) 
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0=3239
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0=42937
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0= 42937
print(int(3 + 4j))  #error bcz complex can not convert into integer
print(int('25.4'))  # 25
print(int('Ten'))   #error bcz strings can't convert into integer


'''# float()  function  demo  program
print(float(25))   #   25.0
print(float(True))    #   1.0
print(float(False))  #0.0
print(float('92'))       #92.0
print(float('36.4'))     #36.4
print(float('0075'))    # 7*8^1+5*8^0=61.0
print(float(0B1010101))    #1*2^6+1*2^4+1*2^2+1*2^0=85.0
print(float(0O6247))     #6*8^3+2*8^2+4*8^1+7*8^0=15911.0
print(float(0XA7B9))   #A*16^3+7*16^2+B*16^1+9*16^0=42937.0
print(float(3 + 4j))   #error bcz complex  can not convert to float
print(float('Ten')).   # error bcz strings can not convert to float


 float# complex()  function  demo  program
print(complex(3 , 4))    #3+4j
print(complex(0 , 4))     #0+4j
print(complex(3))      #3+0j
print(complex(3.8 , 4.6))    #3.8+4.6j
print(complex(3.8))     # 3.8+0j
print(complex(3 , 4.5))    #3+4.5j
print(complex(True , False))    #1+0j
print(complex(True))     #1+0j
print(complex(False))     # 0+1j
print(complex(True , 4)      #1+4j
print(complex('3'))       #3+0j
print(complex('3.8'))      #3.8+0j
print(complex(3 , '4'))  # error bcz 2 nd arg can not be a string
print(complex('3' , 4))  # error bcz 2 nd arg is not permitted when  1st arg is a string
print(complex('3' , '4')) #error bcz 2 nd arg is not permitted when  1st arg is a string
print(complex('Ten'))  # error  bcz strings can't converted to complex
#  bool()  function  demo  program
print(bool(0)) #False
print(bool(10)) #True
print(bool(-25))  #  True
print(bool(0.0))   #False
print(bool(0.1))   #True
print(bool(0 + 0j))  # False imag, real parts are o
print(bool(10 + 20j))    #True
print(bool(-15j))  #True
print(bool('False'))  #True
print(bool(''))     #False ( empty string) 
print(bool('Hyd'))   #True
print(bool(' '))    #True
print(bool('True'))   #True

'''# str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8))  # '10.8'
print(str(3 + 4j))  #'3+4j'
print(str(True))  #'True'
print(str(False))  #'False'
print(str(None))  #'None'

'''# oct()  function  demo  program
print(oct(195))  #0o303
print(oct(0B10101110010))  #0o2562
print(oct(0xA7B9)) #0o123671