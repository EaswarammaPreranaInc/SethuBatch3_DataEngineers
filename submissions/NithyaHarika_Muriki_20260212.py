# int() function demo program print(int(10.8)) # 10
print(int(True)) # 1
print(int(False))#OUTPUT: 0 print(int('25')) #OUTPUT:25 print(int('0075')) #OUTPUT:0075 print(int(0B11010)) # 16 + 8 + 2 = 26
print(0B11010) # 26 print(int(0O6247)) #OUTPUT:3239 print(0O6247) #OUTPUT:3239 print(int(0XA7B9)) #OUTPUT: 42937 print(0XA7B9) # OUTPUT : 42937
print(int(3 + 4j)) #OUTPUT: error, object must be string, a number
print(int('25.4')) #OUTPUT:error
print(int('Ten')) #OUTPUT: error, invalid object for int()


# float() function demo program print(float(25)) # 25.0
print(float(True)) # 1.0 print(float(False)) #OUTPUT:0.0 print(float('92')) #OUTPUT:92.0 print(float('36.4')) #OUTPUT:36.4 print(float('0075')) #OUTPUT:0075.0 print(float(0B1010101)) #OUTPUT:89.0
print(float(0O6247)) #OUTPUT: 42937
print(float(0XA7B9)) #OUTPUT: 42937.0
print(float(3 + 4j)) #OUTPUT:error
print(float('Ten'))#OUTPUT: error, could not convert string to literal
 
# complex() function demo program print(complex(3 , 4)) #OUTPUT:3+4j print(complex(0 , 4)) #OUTPUT:0+4j print(complex(3)) #OUTPUT:3+0j print(complex(3.8 , 4.6)) #OUTPUT: 3.8+4.6j print(complex(3.8)) #OUTPUT:3.8+0j print(complex(3 , 4.5)) #OUTPUT:3+4.5j print(complex(True , False)) #OUTPUT:1 + 0j print(complex(True)) #OUTPUT:1 +0j print(complex(False)) #OUTPUT:0+0j print(complex(True , 4)) #OUTPUT:1+4j print(complex('3')) #OUTPUT:3 + 0j print(complex('3.8')) #OUTPUT:3.8+0j print(complex(3 , '4')) #OUTPUT:error print(complex('3' , 4)) #OUTPUT: error print(complex('3' , '4')) #OUTPUT:error print(complex('Ten')) #OUTPUT: error



# bool() function demo program print(bool(0)) #OUTPUT:False print(bool(10)) #OUTPUT:True print(bool(-25)) # True print(bool(0.0)) #OUTPUT:False print(bool(0.1)) #OUTPUT:True print(bool(0 + 0j)) #OUTPUT:False print(bool(10 + 20j)) #OUTPUT:True print(bool(-15j)) #OUTPUT:True print(bool('False')) #OUTPUT:True print(bool('')) #OUTPUT:False print(bool('Hyd')) #OUTPUT:True
 
print(bool(' ')) #OUTPUT:True print(bool('True')) #OUTPUT:True



# str() function demo program print(str(25)) # '25' print(str(10.8)) #OUTPUT:10.8
print(str(3 + 4j)) #OUTPUT:3+4j print(str(True)) #OUTPUT:’True’ print(str(False)) #OUTPUT:’False’ print(str(None)) #OUTPUT:’None’

# oct() function demo program print(oct(195)) #OUTPUT:0O303 print(oct(0B10101110010)) #OUTPUT:0O2562 print(oct(0xA7B9)) #OUTPUT:0O123671

# hex() function demo program print(hex(25)) #OUTPUT:0X19
print(hex(0B10101111010111)) #OUTPUT:0X2BD7 print(hex(0O6247)) #OUTPUT:0XCA7
