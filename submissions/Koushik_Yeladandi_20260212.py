# int()  function  demo  program
print(int(10.8))  #  10
print(int(True)) #   1
print(int(False)) # 0
print(int('25'))  # Error
print(int('0075')) # Error
print(int(0B11010))   #   16 + 8 + 2 = 26
print(0B11010)   #   26
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(int(3 + 4j))  # 3.0 , 4.0
print(int('25.4'))  #Error
print(int('Ten'))   #Error


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
    -------------------------------------------------------…









# float()  function  demo  program
print(float(25))   #   25.0
print(float(True))    #   1.0
print(float(False))  # 0.0
print(float('92'))  #  Error
print(float('36.4')) #Error
print(float('0075'))   #Error
print(float(0B1010101))      # 85.0       #  64 32 16 8 4 2 1
                                              1  0  1 0 1 0 1  = 64+16+4+1= 85


print(float(0O6247))    # 3239.0           # 512  64  8    1
                                              6   2   4    7  = 3239
                                             
print(float(0XA7B9))   # 42937.0


print(float(3 + 4j))   # 30 , 4.0
print(float('Ten'))   # Error




'''
float()   function
--------------------
1) What  does  float(x)  do  ?  ---> Converts  object  'x'  to  float
complex()   function
-----------------------
1) What  does  complex(3 , 4)  do  ?  --->  Returns  3 + 4j

2) What  does  complex(3.8)  do ? --->  Returns  3.8 + 0j

3) What  does  complex('9.5')  do ?  --->  Returns  9.5 + 0j

4) Is  complex(3 , '4')  valid ?  ---> No  becoz  2nd  arg  can  not  be  a  string

5) In  other  words,  arg1  can  be  a  string  but  not  arg2

6) Is  complex('3' , 4)  valid ?  ---> No  becoz  2nd  argument  is  not  permitted  when  1st  argument  is  a  string






 # complex()  function  demo  program
print(complex(3 , 4))   # 3+4j

print(complex(0 , 4))  # 0+4j
 
print(complex(3))    # 3+0j

print(complex(3.8 , 4.6)) # 3.8+4.6j

print(complex(3.8)) # 3.8+0j

print(complex(3 , 4.5))  #  3+4.5j

print(complex(True , False))  # 1+0j

print(complex(True))   # 1+0j

print(complex(False))  #  0+0j

print(complex(True , 4))  # 1+4j

print(complex('3'))   #3+0j

print(complex('3.8'))  #  3.8+0j

print(complex(3 , '4'))   # Error

print(complex('3' , 4))    # Error

print(complex('3' , '4'))  # Error
 
print(complex('Ten'))   # Error








#  bool()  function  demo  program
print(bool(0))  # false

print(bool(10))  # True
print(bool(-25))  #  True
print(bool(0.0))  # False
print(bool(0.1))  # True
print(bool(0 + 0j))  # False
print(bool(10 + 20j)) # True
print(bool(-15j))  #True
print(bool('False'))  # True
print(bool(''))    # False
print(bool('Hyd'))  #  True
print(bool(' '))   # True
print(bool('True'))  # True



'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ? --->  False
    What  about  non-zero ?  ---> True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  ---> False
    What  about  non-empty  string ?  --->	 True

4) When  is  x + yj  treated  as  False ?  --->  When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as  True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''





# str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8))   # '10.8'
print(str(3 + 4j))  # '3+4j'
print(str(True))    #  'True'
print(str(False))   # 'True'
print(str(None))   # 'None'


'''
What  does  str(x)  do ?  ---> Converts  object  'x'  to  string
'''





 # oct()  function  demo  program
print(oct(195))  
print(oct(0B10101110010))  
print(oct(0xA7B9)) 


'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number



  


# hex()  function  demo  program
print(hex(25))  
print(hex(0B10101111010111)) 
print(hex(0O6247)) 


'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number