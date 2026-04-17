# int()  function  demo  program 
print(int(10.8))  #  10 
print(int(True)) #   1 
print(int(False)) #0 
print(int('25')) #25 
print(int('0075')) #75 
print(int(0B11010))   #   16 + 8 + 2 = 26 
print(0B11010)   #   26 
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239 
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239 
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0= 42937 
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0 = 42937 
print(int(3 + 4j))  #Error 
print(int('25.4'))  #Error 
print(int('Ten'))   #Error 
''' 
int()  function ---------------- 
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer 
2) Conversion  of  binary  number  to  decimal  number -------------------------------------------------------… 
# float()  function  demo  program 
print(float(25))   #   25.0 
print(float(True))    #   1.0 
print(float(False)) #0.0 
print(float('92')) #92.0 
print(float('36.4'))#36.4 
print(float('0075'))#75.0 
print(float(0B1010101))#85.0 
print(float(0O6247)) #3239.0 
print(float(0XA7B9)) #42937.0 
print(float(3 + 4j)) #Error 
print(float('Ten')) #Error 
''' 
f
 loat()   function -------------------- 
1) What  does  float(x)  do  ?  ---> Converts  object  'x'  to  float 
# complex()  function  demo  program 
print(complex(3 , 4)) #(3+4j) 
print(complex(0 , 4)) #(4j) 
print(complex(3)) #(3+0j) 
print(complex(3.8 , 4.6)) #(3.8+4.6j) 
print(complex(3.8)) #(3.8+0j) 
print(complex(3 , 4.5))  #(3+4.5j) 
print(complex(True , False)) #(1+0j) 
print(complex(True)) #(1+0j) 
print(complex(False))  #0j 
print(complex(True , 4)) #(1+4j) 
print(complex('3')) #(3+0j) 
print(complex('3.8')) #(3.8+0j) 
print(complex(3 , '4'))  #Error 
print(complex('3' , 4))  #Error 
print(complex('3' , '4')) #Error 
print(complex('Ten')) #Error 
#  bool()  function  demo  program 
print(bool(0)) #False 
print(bool(10)) #True 
print(bool(-25))  #  True 
print(bool(0.0)) #False 
print(bool(0.1)) #True 
print(bool(0 + 0j)) #False 
print(bool(10 + 20j)) #True 
print(bool(-15j)) #True 
print(bool('False'))  #True 
print(bool(''))  #False 
print(bool('Hyd'))  #True 
print(bool(' '))  #True 
print(bool('True'))  #True 
''' 
bool()  function ------------------ 
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False 
2) Is  0  True  (or)  False ? --->  False 
What  about  non-zero ?  ---> True 
3) Is  ''(i.e.  Empty  string)  True  (or) False ?  ---> False 
What  about  non-empty  string ?  --->  
True 
4) When  is  x + yj  treated  as  False ?  --->  When  both  'x'  and  'y'  are  zeroes 
When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non
zero 
''' 
# str()  function  demo  program 
print(str(25))    #  '25' 
print(str(10.8)) #’10.8’ 
print(str(3 + 4j)) #’3+4j’ 
print(str(True)) #’True’ 
print(str(False)) #’False’ 
print(str(None)) #’None’ 
''' 
What  does  str(x)  do ?  ---> Converts  object  'x'  to  string 
''' 
# oct()  function  demo  program 
print(oct(195))  # 0O303 
print(oct(0B10101110010))  # 0O2562 
print(oct(0xA7B9)) # 0O123671 
''' 
oct()  function ----------------- 
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where 
'x'  can  be  binary / decimal / hexa-decimal  number 
# hex()  function  demo  program 
print(hex(25))  #0X19 
print(hex(0B10101111010111)) #0X2bd7 
print(hex(0O6247)) #0XCA7 
''' 
hex()  function ------------------ 
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where 
'x'  can  be  binary / decimal / octal  number