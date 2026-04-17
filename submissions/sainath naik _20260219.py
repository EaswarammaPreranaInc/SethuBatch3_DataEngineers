#  Find  outputs
print({10 , 20}  |  {30 , 20})  # {10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'hyd',20 : 'vja' 30:'cyb'}
print(range(4) | range(5))  #error
print([10 , 20]  |  [30 , 20]) # error


#  //  operator  demo  program
print(9 // 2)     #  prev  integer(4.5)  = 4
print(9.0 // 2)   #    prev  integer(4.5)  = 4.0
print(9 // 2.0)   #   prev  integer(4.5)  = 4.0
print(9.0 // 2.0) #   prev  integer(4.5)  = 4.0
print(10.5 // 2)  #   prev  integer(5.25)  = 5.0
print(10 // 3)     # prev  integer (3.33) = 3
print(10.0 // 3)   # prev  integer (3) = 3.0
print(8.5 // 3)     # prev  integer (2.2) =2.0
print(18 // 4)   # prev integer (4.5)= 4
print(-18 // 4)  #  prev  integer (-4.5)=-5
print(-(18 // 4))  # prev  integer (4.5)=4

# Find outputs
print(7 / 0)  # error
print(7 // 0) # error
print(7 % 0) # error

# ** operator demo program
print(3 ** 4)   # 3^4 = 81
print(10 ** -2) # 10^-2=0.01
print(4 * 3 * 2) # 4 ^ 9=26
print(3 + 4 * 5 - 32 / 2 ** 3) #19.0


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False
print(6 <= 8) # True
print(6 <= 6) # True
print(6 <= 4) # False
print(9 != 7) # True
print(6 == 8) # False
print(True  >  False)  # True
print(3 + 4j == 3 + 4j)  # True
print(3 + 4j == 5 + 6j)  # False
print(3 + 4j != 5 + 6j)  # True
print(10 == 10.0)        # True
print(3 + 4j >  3 + 4j)  # error


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)  # False
print(1 < 2 < 3 < 4) # True
print(1 < 2 > 3 > 1) # False
print(4 > 3 >= 3 > 2) # True



#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)  # -25
print(''  or  35)  # 35
print(6j  or  'Hyd')  # 6j
print(0.0  or  3 + 4j) # 3+4j
print('Hyd'   or   10.8) # hyd


# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)  #  True
print(not  'Hyd') # False
print(not  '')   # True
print(not  -10)  # False
print(not  not  'Hyd') # True



#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)       # 25
b =  a
print(b)        # 25
print(a  is  b) # True
x = 4
y = 5             
z = x + y * 6 # 4+5*6=34
print(z)      #34
25 = a         # error
a + b = x + y  #error


# Find outputs (Home work)
a = b = c = 25
print(id(a))  # address of object = 25
print(id(b))  # address of object = 25
print(id(c))  # address of object = 25
print(a , b , c)  # (25 25 25)


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)  # 25
print(y) # 10.8
print(z) # hyd


# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   ##a=a*(b+c) a=3*9=27
print(a)  # 27



# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 #a=a %(3+2*4)a=20%11=9
print(a) # 9


# Find outputs (Home work)
a = 3
a **= 4 #a=a**(4)a=3**4
print(a) # 81


# Identity operators demo program
a = 25
b = 25
print(a  is  b)     # true
print(a  is  not  b) # false
print(a == b)        # true



# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) # false
print(a is not b) # true
print(a == b) # true


# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)     # true
print(a  is  not  b) # false
print(a == b)        # true
print()          # nothing
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)         # false
print(x  is  not  y)  # true
print(x == y)         # true
print()  # nothing
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)       # true
print(m  is  not  n)  # false
print(m == n)         # true
print(x == m)         # false




# Find outputs (Home work)
x = [1 , 2 , 3 , 4]   
y = [1 , 2 , 4 , 3]
print(x == y)       # false
a = (4 , 1 , 3 , 2) 
b = (4 , 2 , 3 , 1)
print(a == b)         # false
p = {1 , 2 , 3 , 4}   
q = {4 , 1 , 3 , 2}
print(p == q)       # true
m = range(5)
n = range(5)           
print(m == n)  # true




# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)   # false
print(a  ==  b)   #false


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)  # true
print(19 in list)   # false
print(14 not in list) # true
print(15 not in list)  # false
s = 'Hyd is green city'
print( 'is' in s)    # true
print('was' in s) # false
print('g' in s)   # true
print('z' in s)   # false
print(' ' in s)   # true
print('gre' in s) # true
print('yd i' in s) # true
print('' in s)     # true
print('' not in s) # false


#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)  #  -(-a)=+a=+25=35
print(a--)  # (a-)-=a+=25+ =error
print(a--1) #  a-(-1)=a+1=25+1=26
print(-a)   # -25
print(+-a)  # -25
print(-+a)  # -25



#  Semicolon  demo  program
print('One');  # one
print('Two');  # two  
print('Three'); # three
print('Hyd')  ;   print('Sec') ; print('Cyb') # (hyd <next line sec <next line cyb <next line)



#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))  #-2^-3 =-0.125
print(math . pow(10 , -2))  # 10^-2=0.01
print(math . pow(4 , math . pow(3 , 2)))  # math pow (4,9)=4^9



# sqrt()  function  demo  program
import  math
print(math . sqrt(25))  # 5.0
print(math . sqrt(10))  # 3.16
print(math . sqrt(6.25)) # 2.5
print(math . sqrt(True)) # 1.0
print(math . sqrt(3+4j))  # error
print(math . sqrt(math . sqrt(256)))   #(16.0)=4.0
print(math . sqrt(math . pow(3 , 4)))  # (81.0)=9.0
print(math . sqrt(-16))   # error
print(sqrt(49))     # error




# fabs()  function  demo   program
import  math
print(math . fabs(-10))  # 10.0
print(math . fabs(-25.6)) # 25.6
print(math . fabs(20))   # 20.0
print(math . fabs(35.8))  # 35.8
print(fabs(-25))         # error


#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))   #   11
print(math . floor(25.0))  # 25
print(math . ceil(25.0))   # 25
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) # 26
print(floor(3.5)) # name error
print(ceil(3.5)) # name error









