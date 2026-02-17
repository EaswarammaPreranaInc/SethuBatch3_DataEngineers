1. # int()  function  demo  program
print(int(10.8)) -------  10
print(int(True)) -------  1
print(int(False)) -------0
print(int('25')) -------25
print(int('0075')) -------75
print(int(0B11010)) -------   #   16 + 8 + 2 = 26
print(0B11010)  ------- #   26
print(int(0O6247)) ------- #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0=3239
print(0O6247) -------  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0=3239
print(int(0XA7B9)) ------- #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0=42937
print(0XA7B9) ------- #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0=42937
print(int(3 + 4j))  ------- error(complex cannot convert to int)
print(int('25.4'))  -------error(string float cannot convert to int)
print(int('Ten'))   -------error(string cannot convert to int)

2. # float()  function  demo  program
print(float(25))   -------  25.0
print(float(True))    ------- 1.0
print(float(False)) -------0.0
print(float('92')) -------92.0
print(float('36.4')) -------36.40
print(float('0075')) -------75.0
print(float(0B1010101)) -------1 * 2 ^ 6+ 0 * 2 ^ 5 + 1 * 2 ^ 4  + 0 * 2 ^ 3+ 1 * 2 ^ 2+ 0 * 2 ^ 1  +1 * 2 ^ 0 =64+16+4+1 =85
print(float(0O6247)) -------6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0=3239.0
print(float(0XA7B9)) -------10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0=42937.0
print(float(3 + 4j)) ------- error(complex number)
print(float('Ten')) -------error(given as str)


3. # complex()  function  demo  program
print(complex(3 , 4)) -------3+4j
print(complex(0 , 4)) -------4j
print(complex(3)) -------3+0j
print(complex(3.8 , 4.6)) -------3.8+4.6j
print(complex(3.8)) -------3.8+0j
print(complex(3 , 4.5)) -------3+4.5j
print(complex(True , False)) -------1+0j
print(complex(True)) -------1+0j
print(complex(False)) -------0j
print(complex(True , 4)) -------1+4j
print(complex('3')) -------3+0j
print(complex('3.8')) -------3.8+0j
print(complex(3 , '4'))  -------error(second cant be string)
print(complex('3' , 4))  -------error(2nd cant be permitted if 1st is string)
print(complex('3' , '4')) -------error(2nd cant be permitted if 1st is string)
print(complex('Ten')) -------(string cannot convert to complex)

4. #  bool()  function  demo  program
print(bool(0)) -------False
print(bool(10)) -------True
print(bool(-25)) -------  True
print(bool(0.0)) -------False
print(bool(0.1)) -------True
print(bool(0 + 0j)) -------False
print(bool(10 + 20j)) -------True
print(bool(-15j)) -------True
print(bool('False'))  -------True
print(bool('')) -------False
print(bool('Hyd')) -------True
print(bool(' ')) -------True
print(bool('True')) -------True

5. # str()  function  demo  program
print(str(25))   -------  '25'
print(str(10.8)) -------’10.8’
print(str(3 + 4j)) -------‘3+4j’
print(str(True)) -------‘True’
print(str(False)) -------‘False’
print(str(None)) -------‘None’

6. # oct()  function  demo  program
print(oct(195)) ------- 0o303
print(oct(0B10101110010))  -------0o2562
print(oct(0xA7B9)) -------0o123671

7. # hex()  function  demo  program
print(hex(25))  -------0x19
print(hex(0B10101111010111)) -------0x2bd7
print(hex(0O6247)) -------0xca7
