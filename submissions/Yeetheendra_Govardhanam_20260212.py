#Topic-1
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #Dayal
print(a[7 : ]) # Dayal Sarma
print(a[ : 6]) #Sankar
print(a[ : ])  #Sankar Dayal Sarma
print(a[:  : ])  #Sankar Dayal Sarma
print(a[1 : 10 : 2])   #akrDy
print(a[0 : : 2]) #Sna_aa_am
print(a[1 : : 2]) #akrDylSra
print(a[-5 : -1]) #Sarm 
print(a[::-1])  #reversed string 
print(a[-1:-5:-1]) #amra
print(a[ : : -2]) #arSlyDrka
print(a[3 : -3]) #kar Dayal Sarma
print(a[2 : -5]) #nkar Dayal_
print(a[-1:-5]) #empty str set is +1 it is moving to positive side
print(a[3 : 3]) # empty str 


#   0      1      2      3      4       5       6           7       8       9     10     11     12           13     14       15      16     17
#   S      a      n      k      a       r                    D       a       y      a       l                     S       a         r       m       a
#  -18   -17   -16   -15    -14   -13    -12        -11     -10    -9     -8    -7      -6          -5      -4       -3      -2      -1
#Topic-2
 # int()  function  demo  program
print(int(10.8))  #  10
print(int(True)) #   1
print(int(False)) # 0
print(int('25')) # 25
print(int('0075')) #75
print(int(0B11010))   #   16 + 8 + 2 = 26
print(0B11010)   #   26
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(int(3 + 4j))  # error cannot type cast
print(int('25.4'))  # error cannot type cast
print(int('Ten'))   # error cannot type cast

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
#Topic-3
 # float()  function  demo  program
print(float(25))   #   25.0
print(float(True))    #   1.0
print(float(False)) #0. 0
print(float('92')) #92. 0
print(float('36.4')) #36.4
print(float('0075')) #75. 0
print(float(0B1010101))  # with decimal int to float object num.0 I.e 85.0
print(float(0O6247)) # with decimal int to float object num.0 i.e 3239.0
print(float(0XA7B9)) # with decimal int to float object num.0 I.e 42937. 0
print(float(3 + 4j)) # error cannot type cast
print(float('Ten'))# error cannot type cast
'''
float()   function
--------------------
1) What  does  float(x)  do  ?  ---> Converts  object  'x'  to  float

#Topic-4
 complex()   function
-----------------------
1) What  does  complex(3 , 4)  do  ?  --->  Returns  3 + 4j

2) What  does  complex(3.8)  do ? --->  Returns  3.8 + 0j

3) What  does  complex('9.5')  do ?  --->  Returns  9.5 + 0j

4) Is  complex(3 , '4')  valid ?  ---> No  becoz  2nd  arg  can  not  be  a  string

5) In  other  words,  arg1  can  be  a  string  but  not  arg2

6) Is  complex('3' , 4)  valid ?  ---> No  becoz  2nd  argument  is  not  permitted  when  1st  argument  is  a  string
'''
 # complex()  function  demo  program
print(complex(3 , 4)) #3 + 4j
print(complex(0 , 4)) #0 + 4j
print(complex(3)) #3+0j
print(complex(3.8 , 4.6)) 3.8 + 4.6j
print(complex(3.8)) 3.8 +0j
print(complex(3 , 4.5)) 3 + 4.5j
print(complex(True , False)) 1 + 0j
print(complex(True)) 1+0j
print(complex(False)) 0j
print(complex(True , 4)) 1+ 4j
print(complex('3')) 3+0j
print(complex('3.8')) 3.8 +0j
print(complex(3 , '4'))  #error no string in second place 
print(complex('3' , 4))  # no element after string 
print(complex('3' , '4'))  # no element after string
print(complex('Ten')) # error cannot type cast

#Topic-5
 #  bool()  function  demo  program
print(bool(0)) #False
print(bool(10)) #True
print(bool(-25))  #  True
print(bool(0.0)) #False
print(bool(0.1)) # True
print(bool(0 + 0j)) #False
print(bool(10 + 20j)) #True
print(bool(-15j)) # True
print(bool('False')) #True
print(bool('')) #False 
print(bool('Hyd')) #True 
print(bool(' ')) #True
print(bool('True')) #True


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

#Topic-6
 # str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8)) # ‘10.8’
print(str(3 + 4j)) # ’3 + 4j’ 
print(str(True)) # ‘True’ 
print(str(False)) # ‘False’
print(str(None)) # ‘None’ 

'''
What  does  str(x)  do ?  ---> Converts  object  'x'  to  string
'''
#Topic-7
 # oct()  function  demo  program
print(oct(195))  #0o303
print(oct(0B10101110010))  #0o2562
print(oct(0xA7B9)) #0o123671

'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
                    'x'  can  be  binary / decimal / hexa-decimal  number
''' 

#Topic-8
# hex()  function  demo  program
print(hex(25))  #0x19
print(hex(0B10101111010111)) #0x2bd7
print(hex(0O6247)) #0xca7

'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
                     'x'  can  be  binary / decimal / octal  number
'''
