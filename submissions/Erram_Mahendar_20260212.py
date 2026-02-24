***
print(int(10.8)) # 10
print(int(True)) # 1
print(int(False)) # 0
print(int('25')) # 25
print(int('0075')) # 75


print(int(0B11010)) # 26
print(0B11010) # 26


print(int(0O6247)) # 3239
print(0O6247) # 3239


print(int(0XA7B9)) # 42937
print(0XA7B9) # 42937


print(int(3 + 4j)) # Error (Cannot convert complex to int)
print(int('25.4')) # Error (Invalid literal for int)
print(int('Ten')) # Error (Invalid literal for int)


***
print(float(25)) # 25.0
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float('92')) # 92.0
print(float('36.4')) # 36.4
print(float('0075')) # 75.0


print(float(0B1010101)) # 85.0
print(float(0O6247)) # 3239.0
print(float(0XA7B9)) # 42937.0


print(float(3 + 4j)) # Error (Cannot convert complex to float)
print(float('Ten')) # Error (Invalid literal for float)


***


print(complex(3 , 4)) # (3+4j)
print(complex(0 , 4)) # 4j
print(complex(3)) # (3+0j)
print(complex(3.8 , 4.6)) # (3.8+4.6j)
print(complex(3.8)) # (3.8+0j)
print(complex(3 , 4.5)) # (3+4.5j)


print(complex(True , False)) # (1+0j)
print(complex(True)) # (1+0j)
print(complex(False)) # 0j
print(complex(True , 4)) # (1+4j)


print(complex('3')) # (3+0j)
print(complex('3.8')) # (3.8+0j)


print(complex(3 , '4')) # Error (Second argument cannot be string)
print(complex('3' , 4)) # Error (Second argument not allowed when first is string)
print(complex('3' , '4')) # Error
print(complex('Ten')) # Error (Invalid literal)


***


print(bool(0)) # False
print(bool(10)) # True
print(bool(-25)) # True


print(bool(0.0)) # False
print(bool(0.1)) # True


print(bool(0 + 0j)) # False
print(bool(10 + 20j)) # True
print(bool(-15j)) # True


print(bool('False')) # True
print(bool('')) # False
print(bool('Hyd')) # True
print(bool(' ')) # True
print(bool('True')) # True


***


print(str(25)) # 25
print(str(10.8)) # 10.8
print(str(3 + 4j)) # (3+4j)
print(str(True)) # True
print(str(False)) # False
print(str(None)) # None


***


print(oct(195)) # 0o303
print(oct(0B10101110010)) # 0o2562
print(oct(0xA7B9)) # 0o123671


***


print(hex(25)) # 0x19
print(hex(0B10101111010111)) # 0x2bd7
print(hex(0O6247)) # 0xca7







