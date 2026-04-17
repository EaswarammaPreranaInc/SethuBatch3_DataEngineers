# int()  function  demo  program
print(int(10.8))   #  Converts  10.8  to  10
print(int(True))    #  Converts   True  to   1
print(int(False)) # Converts False to 0
print(int('25')) #  Converts  '25'  to  25
print(int('0075')) #  Converts  '0075'  to   75
print(int(0B11010)) #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(0B11010)  #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(int(0O6247))  #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(0O6247)   #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(int(0XA7B9))   #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(0XA7B9)  #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
#print(int(3 + 4j)) #  Error  :  complex  number  can not be converted to int
#print(int('25.4')) #  Error :  string  float  can not be converted to int
#print(int('Ten'))  #  Error :  'Ten'  can not be converted to int

# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True))  #  Converts   True  to  1.0
print(float(False))  #  Converts  False  to  0.0
print(float('92'))  #  Converts  '92'  to   92.0
print(float('36.4'))  #  Converts   '36.4'   to   36.4
print(float('0075'))  #  Converts   '0075'  to  75.0
print(float(0B1010101)) # Converts  binary  number  to  decimal  number  i.e.  64 + 16 + 4 + 1 = 85.0
print(float(0O6247))  # Converts  octal   number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239.0
print(float(0XA7B9))   # Converts   hexa-decimal   number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937.0
#print(float(3 + 4j)) #  Error : complex number  can  not  be  converted to  float
#print(float('Ten'))   #  Error :  'Ten'  can  not  be  converted to  float

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

# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a)) # class range
print(a) # range (10, 50, 5)
print(*a) # 10 15 20 25 30 35 40 45
print(id(a)) #
print(len(a)) # 8
print(*a[2 : 7] , sep = ' , ') # 20,25,30,35,40
print(*a[ : : -1]) # 45 40 35 30 25 20 15 10
a[4] = 32 # error
print(a * 2) # error

#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',') # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b) #  0 1 2 3 4
c = range(10 , 1 , -1) 
print(*c , sep = '...') #10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d) # -10, -9, -8 , -7, -6, -5 ,-4, -3, -2, -1
e = range(-10)
print(*e) # nothing
f = range(2 , 2)
print(*f) #nothing
g = range(10 , 11 , 0.1) # error
h = range('A' , 'F') # error

#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)
a , b , c = r  
print(a , b , c) #  10,13,16
r = range(3)   # 0,1,2
x , y = r   # error
p , q  , r , s = r  # not executed
a , b , c = *r  # not executed
m = r   # not executed
print(id(r))   # not executed
print(id(m))  # not executed

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a) # [25, 10.8, Hyd, True, 3+4j, None, Hyd , 25]
print(*a) # 25 10.8 Hyd True 3+4j None Hyd 25
print(type(a)) class list
print(id(a))  #error
print(len(a))# 8
a[2] = 'Sec'
print(a) # [25,10.8 ,Sec  , True, 3+4j, None, Hyd, 25]
print(a[2 : 5]) #[ 'sec' , True , 3+4j]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a)  # []
a . append(25)
a . append(10.8)
a . append('Hyd')
a . append(True)
print(a)  # 25 , 10.8 , Hyd , True
a . remove('Hyd')
print(a) # 25 , 10.8, True
a . remove('25')
print(a) #10.8,True

#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a) [25, 10.8 , 'Hyd']
print(id(a))
print(a * 3) [25, 10.8, 'Hyd' ,25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd' ]
print(a * 2) # [25, 10.8, 'Hyd' ,25 , 10.8 , 'Hyd']
print(a * 1) # [25, 10.8 , 'Hyd']
print(a * 0) # [ ]
print(a * -1) # [ ]
print(a * 4.0) # error
a = a * 3 
print(a) # [25, 10.8, 'Hyd' ,25 , 10.8 , 'Hyd' , 25 , 10.8 , 'Hyd' ]
print(id(a))
a = [25]
print(a , id(a)) # 25
print(a * a)  # error

# list()  function  demo  program
a = list('Hyd')
print(a) # [ 'H' , 'y' , 'd' ]
print(type(a)) # class list
print(len(a)) # 3
b = (10 , 20 , 15 , 18)
print(list(b)) # [10, 20, 15, 18]
print(list(range(5))) # [ 1, 2, 3, 4, 5]
print(list(25)) # error

# Find  outputs
a = [ ]
print(type(a)) # class list
print(a) # [ ]
print(len(a)) # 0
b = list()
print(b) # [ ]
print(len(b)) # 0

# Slice  demo  program (Home  work)
#        0      1          2         3         4        5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5         -4      -3       -2        -1
print(list[2 : 7]) # 3+4j, 'Hyd' , True, None, 10.8
print(list[ : : ]) #  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:]) # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) # ['Hyd' , 10.8, None, True, 'Hyd', (3+4j), 10.8,  25]
print(list[ : : 2])  #  list[0 : 8 : 2]   --->  List  from  indexes  0  to  7  in steps  of  2  i.e.   [25 , 3+4j , True , 10.8]
print(list[1 : : 2]) # 10.8, 'Hyd' , None, 'Hyd']
print(list[ : : -2]) # [ 'Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2])  #   list[-2 : -9 : -2]   --->  List  from  indexes  -2  to  -8  in steps  of  -2  i.e.   [10.8 , True , 3+4j , 25]
print(list[1 : 4]) # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1]) # [True, None, 10.8]
print(list[3 : -3]) # [ 'Hyd' , True]
print(list[2 : -5])  # [(3+4j)]
print(list[-1:-5]) # [ ]


#  Find  outputs  (Home  work)
#        0       1      2          3         4        5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5] # ['Hyd', True]
print('x : ' , x) # x : Hyd
print('y : ' , y) # y : True
for  x  in  list[2:7]: # [(3+4j), 'Hyd', True, None, 10.8]
print(x) # (3+4j) #Hyd # True # None # 10.8

#  Find  outputs  (Home  work)
#     0     1     2    3     4
a = [10 , 20 , 30 , 40 , 50]
print(a , id(a)) # [10,20,30,40,50]
a[1 : 4] = [60 , 70]
print(a , id(a)) # [10,60,70,50]
a[2: 4] = [100 , 200 ,  300]
print(a , id(a)) # [ 10,60,100,200,300]

#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # error
print(a[1:]) # error