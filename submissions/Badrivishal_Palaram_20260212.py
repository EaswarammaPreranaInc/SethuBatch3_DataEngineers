# int() function demo program
print(int(10.8)) #O/P : 10
print(int(True)) #O/P : 1
print(int(False)) #O/P : 0
print(int('25')) #O/P : 25
print(int('0075')) #O/P : 75
print(int(0B11010)) #O/P : 16 + 8 + 2 = 26
print(0B11010) #O/P : 26
print(int(0O6247)) #O/P : 6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(0O6247) #O/P : 6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(int(0XA7B9)) #O/P : 10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0
print(0XA7B9) #O/P : 10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0
print(int(3 + 4j)) #O/P : error ,Complex cannot be converted to int .
print(int('25.4')) #O/P : error, string can only be converted when it has a integer not float,complex.
print(int('Ten')) #O/P : error, python cannot convert words to integers directly.
int() function
----------------
1) What does int(x) do ? #O/P : ---> Converts object 'x' to integer
2) Conversion of binary number to decimal number
By multiplying each binary digit to its corresponding 2 power
eg: 1 0 1 1
2³ 2² 2¹ 2⁰
=(1×2^3)+(0×2^2)+(1×2^1)+(1×2^0)
=(1×8)+(0×4)+(1×2)+(1×1)
=8+0+2+1
=11
# float() function demo program
print(float(25)) #O/P : 25.0
print(float(True) #O/P : 1.0
print(float(False)) #O/P : 0.0
print(float('92')) #O/P : 92.0
print(float('36.4')) #O/P : 36.4
print(float('0075')) #O/P : 75.0
print(float(0B1010101)) #O/P : 1010101 = 85 = 85.0
print(float(0O6247)) #O/P : 0o6247 = 3239 =3239.0
print(float(0XA7B9)) #O/P : 0xa7b9 = 42937= 42937.0
print(float(3 + 4j)) #O/P : errror
print(float('Ten')) #O/P : error
float() function
--------------------
1) What does float(x) do ? ---> #O/P : Converts object 'x' to float
complex() function
1) What does complex(3 , 4) do ? ---> #O/P : Returns 3 + 4j
2) What does complex(3.8) do ? ---> #O/P : Returns 3.8 + 0j
3) What does complex('9.5') do ? #O/P : Returns 9.5 + 0j
4) Is complex(3 , '4') valid ? ---> #O/P : No becoz 2nd arg can not be a string
5) In other words, arg1 can be a string but not arg2
6) Is complex('3' , 4) valid ? ---> #O/P : No becoz 2nd argument is not permitted when 1st
argument is a string
# complex() function demo program
print(complex(3 , 4)) #O/P : (3+4j)
print(complex(0 , 4)) #O/P : 4j
print(complex(3)) #O/P : (3+0j)
print(complex(3.8 , 4.6)) #O/P : (3.8+4.6j)
print(complex(3.8)) #O/P : (3.8+0j)
print(complex(3 , 4.5)) #O/P : (3+4.5j)
print(complex(True , False)) #O/P : (1+0j)
print(complex(True)) #O/P : (1+0j)
print(complex(False)) #O/P : 0j
print(complex(True , 4)) #O/P : (1+4j)
print(complex('3')) #O/P : (3+0j)
print(complex('3.8')) #O/P : (3.8+0j)
print(complex(3 , '4')) #O/P : TypeError
print(complex('3' , 4)) #O/P : TypeError
print(complex('3' , '4')) #O/P : TypeError
print(complex('Ten')) #O/P : ValueError
# bool() function demo program
print(bool(0)) O/P: False
print(bool(10)) O/P: True
print(bool(-25)) O/P: True
print(bool(0.0)) O/P: False
print(bool(0.1)) O/P: True
print(bool(0 + 0j)) O/P: False
print(bool(10 + 20j)) O/P: True
print(bool(-15j)) O/P: True
print(bool('False')) O/P: True
print(bool('')) O/P: False
print(bool('Hyd')) O/P: True
print(bool(' ')) O/P: # True
print(bool('True')) O/P: True
bool() function
------------------
1) What does bool(x) do ? ---> O/P: Converts object 'x' to True / False
2) Is 0 True (or) False ? ---> O/P: False
What about non-zero ? O/P: True
3) Is ''(i.e. Empty string) True (or) False ? ---> O/P: False
What about non-empty string ? O/P: True
4) When is x + yj treated as False ? ---> O/P: When both 'x' and 'y' are zeroes
When is x + yj treated as True ? ---> O/P: When either 'x' is non-zero (or) 'y' is non-zero
# str() function demo program
print(str(25)) #O/P : '25'
print(str(10.8)) #O/P :'10.8'
print(str(3 + 4j)) #O/P :'(3+4j)'
print(str(True)) #O/P : 'True'
print(str(False)) #O/P :'False'
print(str(None)) #O/P : 'None'
What does str(x) do ? #O/P : ---> Converts object 'x' to string
# oct() function demo program
print(oct(195)) #O/P : '0o303' = 3×8^2+0×8^1+3×8^0 = 195
print(oct(0B10101110010)) #O/P : '0o1272' = 1×8^3+2×8^2+7×8^1+2×8^0 = 698
print(oct(0xA7B9)) #O/P : '0o247671' = 2×8^5+4×8^4+7×8^3+6×8^2+7×8^1+1×8^0 =85945
oct() function
-----------------
1) What does oct(x) do ? #O/P : ---> Converts object 'x' to octal number where
'x' can be binary / decimal / hexa-decimal number
# hex() function demo program
print(hex(25)) #O/P : '0x19' , 1×16^1+9×16^0 =25
print(hex(0B10101111010111)) #O/P : '0x2bd7' , 2×16^3+11×16^2+13×16^1+7×16^0 = 11223
print(hex(0O6247)) #O/P : '0xca7' , 12×16^2+10×16^1+7×16^0
=12×256+10×16+7 =3072+160+7
= 3072 + 160 + 7=3072+160+7
hex() function
------------------
1) What does hex(x) do ? ---> #O/P : Converts object 'x' to hexa-decimal number where
'x' can be binary /
decimal / octal number
