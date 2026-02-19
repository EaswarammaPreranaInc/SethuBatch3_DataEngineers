#  Find  outputs
print({10 , 20}  |  {30 , 20}) # {10 , 20 , 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' , 20 : 'Vja' , 30 : 'Cyb'}
print(range(4) | range(5)) # Error, range objects can not be added
print([10 , 20]  |  [30 , 20]) # Error, lists can not be added 

#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2) #  prev int(5.25) = 5.0
print(10 // 3) # prev int(3.333) = 3
print(10.0 // 3) # prev int(3.333) = 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4)  #  -5
print(-(18 // 4))  #   -4

# Find outputs
print(7 / 0) # Error, because division by zero is not possible
print(7 // 0) # Error, because division by zero is not possible
print(7 % 0) # Error, because division by zero is not possible

# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2) # 10 ^ -2 = 0.01
print(4 * 3 * 2) # 24
print(3 + 4 * 5 - 32 / 2 ** 3) # Power first 2 ^ 3 =8 , then division , then multiplication then followed by addition and subtraction , final answer 19.0

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)  # True
print(6 <= 6) # True
print(6 <= 4) # False
print(9 != 7) # True
print(6 == 8) # False
print(True  >  False) # True
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j) # False

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana') # 
print('Rama  Rao'  >=  'Rama') #
print('Hyd'  != 'Sec')  # True
print('HYD'  <   'hyd') # True , because 'H' = 72, which is lower than 'h' = 104

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
print(-25  or  0) # -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 
print(0.0  or  3 + 4j) # 3+4j
print('Hyd'   or   10.8) # 

# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0) # True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) #  False
print(not  not  'Hyd') # True

#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))  

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) # 25
b =  a
print(b) # 25
print(a  is  b) # True
x = 4
y = 5
z = x + y * 6
print(z) # 34
25 = a # Error
a + b = x + y # Error

# Find outputs (Home work)
a = b = c = 25
print(id(a)) # Address of object 25 , 123500
print(id(b)) # Address of object 25, which is same address of a, i.e, 123500
print(id(c)) # Address of object 25, which is same address of a, b i.e, 123500
print(a , b , c) # 25 25 25

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z) # 'Hyd'

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   # a*(b+c)
print(a) # # 3*(4+5) = 27

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 # a%(3+2*4) 
print(a) # 20%11 , 9

# Find outputs (Home work)
a = 3
a **= 4 # a = a**4
print(a) # 3**4 =81

# Identity operators demo program
a = 25
b = 25
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) False, because 'a' refering to int object 15, 'b' is refering to float object 25, so both references are pointing to different objects
print(a is not b) # True
print(a == b) # True

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False, because lists are mutable, so they are created separately
print(x  is  not  y) # True
print(x == y) # True
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True, tuples are immutable and they are reusable
print(m  is  not  n) # False
print(m == n) # True
print(x == m) # False, because they are different class objects

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)  # False, because x and y have same values ,but they dont have same values at same indexes
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # False, because a and b have same values ,but they dont have same values at same indexes
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  # True, because both sets have same values 
m = range(5)
n = range(5)
print(m == n) # False

# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  # False, both are pointing and refering to two different class objects
print(a  ==  b) # False

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False, because there is no element 19 present in given list
print(14 not in list) # True as there is no element 14 present in given list
print(15 not in list) # False because element 15 is present in given list
s = 'Hyd is green city'
print( 'is' in s) # True ,because 'is' there in given str
print('was' in s) # False , there is no 'was' in given str
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) True
print('' in s) # True
print('' not in s) # True

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) # -(-a) = -(-25) = 25
print(a--) # Error
print(a--1) # a -(-1) = 25 -(-1) = 26
print(-a) # -25
print(+-a) # -25, because +(-25)
print(-+a) # -25

#  Semicolon  demo  program
print('One'); # One, because ';' at the end of statement in python is optional
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') 
''' Hyd
  Sec
  Cyb
'''

#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) # -2^ -3 , 1/(-8) = -0.125
print(math . pow(10 , -2)) # 10 ^ -2 ---> 0.01
print(math . pow(4 , math . pow(3 , 2))) # first 3^2 that is 9, then 4^9 = 262144

# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) # 5.0
print(math . sqrt(10)) # 3.16
print(math . sqrt(6.25)) # 2.5
print(math . sqrt(True)) # 1
print(math . sqrt(3+4j)) # Error, because we can find square root for complex number
print(math . sqrt(math . sqrt(256))) # First inner function is executed that is under root 256 that is 16 , then outer function is executed that is under root 16 that is 4
print(math . sqrt(math . pow(3 , 4))) # First inner function 3**4 that is 81.0 , then under root of 81.0 that is 9.0
print(math . sqrt(-16)) # Error, we can not find square root of negative numbers
print(sqrt(49)) # Error, because there is no sqrt function is defined in current module

# fabs()  function  demo   program
import  math
print(math . fabs(-10)) # 10.0
print(math . fabs(-25.6)) # 25.6
print(math . fabs(20)) # 20.0
print(math . fabs(35.8)) # 35.8
print(fabs(-25)) # Error, because there is no fabs function is defined in current module

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) # 25
print(math . ceil(25.0)) # 25
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5)) # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0)) # -9
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) # 26
print(floor(3.5)) #  Error, because there is no floor function is defined in current module
print(ceil(3.5)) #  Error, because there is no ceil  function is defined in current module

