# int()  function  demo  program
print(int(10.8))  #  10
print(int(True)) #   1
print(int(False)) #0
print(int('25')) # 25.0
print(int('0075')) #
print(int(0B11010))   #   16 + 8 + 2 = 26
print(0B11010)   #   26
print(int(0O6247)) #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(0O6247)  #  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0
print(int(0XA7B9)) #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(0XA7B9)  #   10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1  + 9 * 16 ^ 0
print(int(3 + 4j)) # Error 
print(int('25.4'))  #25
print(int('Ten'))   # #Error becoz string can't be change becoz it is immutable.



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
  --- - ----------------------------------------------------------------------
        4096   256   16    1  --->  Weights
	  A    7     B     9  --->  10 * 4096 + 7 * 256 + 11 * 16 + 9 * 1  = 42937
'''
# float()  function  demo  program
print(float(25))   #   25.0
print(float(True))    #   1.0
print(float(False))   # 0
print(float('92'))    # 92.0
print(float('36.4'))   # 36.4
print(float('0075'))   # 75.0
print(float(0B1010101))  #85.0
print(float(0O6247)) #3239.0
print(float(0XA7B9)) #42937.0
print(float(3 + 4j)) #Error becoz string can't be change becoz it is immutable.
print(float('Ten')) #Error becoz string can't be change becoz it is immutable.




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
print(complex(3 , 4)) #return 3+4j
print(complex(0 , 4)) #return 0+4j
print(complex(3)) #return 3+0j
print(complex(3.8 , 4.6)) #returns 3.8+4.6j
print(complex(3.8)) #return 3.8+0j
print(complex(3 , 4.5)) #return 3+4.5j
print(complex(True , False)) #1+0j
print(complex(True)) # 1+0j
print(complex(False)) #0
print(complex(True , 4)) #1+4j
print(complex('3')) #3+0j
print(complex('3.8')) #3.8+0j
print(complex(3 , '4'))  #Error becoz  2nd  argument  is  not  permitted  when  1st  argument  is  a  string
print(complex('3' , 4))  #3+4j
print(complex('3' , '4')) #Error becoz  2nd  argument  is  not  permitted  when  1st  argument  is  a  string
print(complex('Ten')) #Error becoz  2nd  argument  is  not  permitted  when  1st  argument  is  a  string

#  bool()  function  demo  program
print(bool(0)) #False
print(bool(10))  #True
print(bool(-25))  #  True
print(bool(0.0)) #False
print(bool(0.1)) #False
print(bool(0 + 0j)) #False
print(bool(10 + 20j))#True
print(bool(-15j)) #True
print(bool('False'))  #True
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

# str()  function  demo  program
print(str(25))    #  '25'
print(str(10.8))  # '10.8'
print(str(3 + 4j)) # '3+4j'
print(str(True))  # 'True'
print(str(False)) # 'Flase'
print(str(None)) # 'None'


'''
What  does  str(x)  do ?  ---> Converts  object  'x'  to  string
'''

# oct()  function  demo  program
print(oct(195))  #0o303
                        195/8 =>reminder is 3 and quosent 24
                        24/8 =>reminder is 0 and quosent 3
                         3/8 =>reminder is 3
print(oct(0B10101110010))  # 1     0    1     0    1    1   1  0   0  1 0
                           1024   512  256   128  64   32  16  8   4  2  1
                           -----------------------------------------------------
                            1024+       256+       64+  32+16+2=1394

                         1394/8=>reminder is 2 qosent is 174
                          174/8 =>reminder is 6 quosent is 21
                            21/8 =>reminder is 5 quosent is 5
                              5/8=>reminder is 2 quosent is 0 =>0o2652

print(oct(0xA7B9))   #4096 256 16 1
                     10   7   11 9
                  -------------------
                    40960+256*6+16*11+1*9=42937
               #42937 ÷ 8 = 5367 remainder 1
                5367 ÷ 8 = 670 remainder 7
                670 ÷ 8 = 83 remainder 6
                83 ÷ 8 = 10 remainder 3
                10 ÷ 8 = 1 remainder 2
                1 ÷ 8 = 0 remainder 1
          =>0o176321
'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where
								                    'x'  can  be  binary / decimal / hexa-decimal  number

# hex()  function  demo  program
print(hex(25))  #25/16=>reminder is 9 and quosent is 1
                 1/16 =>reminder is 1 and quosent is 0
      so in hex decimal we take reverse first 1 and then 9 =>0x19
print(hex(0B10101111010111)) #   1    0     1     0     1    1    1     1   0  1  0  1  1  1
                                8192 4096  2048  1024  512   256  128  64  32  16 8  4  2  1
                 --------------------------------------------------------------------------------
                                 8192+2048+512+256+128+64+16+4+2+1=>11223
#11223/16=>reminder is 7 qosent is 707
  707/16=>reminder is 13    qosent is 43
    43/16 =>reminder is 11 qosent is  2
     2/16=>reminder is 2 qosent is 0
so we need to in reverse=>ox2bd7

print(hex(0O6247)) 

512   64   8    1  --->  Weights
6      2    4   7  --->  6 * 512 + 2 * 64 + 4 * 8 + 7 * 1  = 3239
#3239/16=>reminder is 7 qosent is 202
202/16=>reminder is 10 qosent is 12
12/16=>reminder is 12 qosent is 0

so we need reverse=>0xca7

'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number


