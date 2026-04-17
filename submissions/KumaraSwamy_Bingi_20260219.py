#  Find  outputs
print({10 , 20}  |  {30 , 20}) # {10 , 20 , 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' , 20 : 'Vja' , 30 : 'Cyb'}
print(range(4) | range(5)) # Error range is immutable and does not support the union operator
print([10 , 20]  |  [30 , 20]) # Error list is mutable and does not support the union operator


#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)  #   prev  integer(5.25)   = 5.0
print(10 // 3) #  prev  integer(3.3333)   = 3
print(10.0 // 3) #  prev  integer(3.3333)   = 3.0
print(8.5 // 3)   #  prev  integer(2.8333)   = 2.0
print(18 // 4)  #  prev  integer(4.5)   = 4
print(-18 // 4)  #  Tricky #  prev  integer(-4.5)   = -5
print(-(18 // 4))  #  Tricky #  prev  integer(-4.5)   = -4


# Find outputs
print(7 / 0) # Error 
print(7 // 0) # Error
print(7 % 0) # Error



# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2) #  10 ^ -2 = 0.01
print(4 * 3 * 2) # 24
print(3 + 4 * 5 - 32 / 2 ** 3) # 3 + 4 * 5 - 32 / 2 ** 3 => 3 + 20 - 32 / 8 => 3 + 20 - 4 => 19.0


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8) #   True
print(6 <= 6) #   True
print(6 <= 4) #   False
print(9 != 7) #   True
print(6 == 8) #   False
print(True  >  False) #   True
print(3 + 4j == 3 + 4j) #   True
print(3 + 4j == 5 + 6j) #   False
print(3 + 4j != 5 + 6j) #   True
print(10 == 10.0) #   True (integer 10 and float 10.0 are considered equal in value)
print(3 + 4j >  3 + 4j) #   False (complex numbers cannot be compared using > or <) 



#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana') # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True (uppercase letters are considered smaller than lowercase letters in ASCII)


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False because 10 >= 20 is False
print(10 < 20 > 30) #  False because 20 > 30 is False
print(1 < 2 < 3 < 4) #  True
print(1 < 2 > 3 > 1) #  False because 2 > 3 is False
print(4 > 3 >= 3 > 2) # True (4 > 3 is True, 3 >= 3 is True, 3 > 2 is True)


#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0) #  -25
print(''  or  35) #  35
print(6j  or  'Hyd') #  6j (non-empty complex number is considered True, so it returns the first operand)
print(0.0  or  3 + 4j) #  3 + 4j (0.0 is considered False, so it returns the second operand)
print('Hyd'   or   10.8) #  Hyd (non-empty string is considered True, so it returns the first operand)


# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0) #   True
print(not  'Hyd') #   False (non-empty string is considered True, so not of it is False)
print(not  '') #   True (empty string is considered False, so not of it is True)
print(not  -10) #   False (non-zero number is considered True, so not of it is False)
print(not  not  'Hyd') #   True (not of a non-empty string is False, and not of that is True)


#  Find   outputs (Home work)
i = 10
i = not  i > 14 #
print(i) # True (i > 14 is False, so not of it is True, and i is assigned that value)
print(not(6 < 4  or  9 >= 5  and  6 != 6))# True


#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)
b =  a
print(b)
print(a  is  b) # True (both a and b refer to the same integer object 25 )
x = 4
y = 5
z = x + y * 6
print(z) # 4 + 5 * 6 => 4 + 30 => 34
25 = a # Error
a + b = x + y # Error


# Find outputs (Home work)
a = b = c = 25
print(id(a))
print(id(b))
print(id(c))
print(a , b , c) # 25 25 25


# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z)  # Hyd


# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a) # 3 * (4 + 5) => 3 * 9 => 27


# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) # 20 % (3 + 2 * 4) => 20 % (3 + 8) => 20 % 11 => 9


# Find outputs (Home work)
a = 3
a **= 4 
print(a) # 3 ** 4 => 81


# Identity operators demo program
a = 25
b = 25
print(a  is  b) # True its less than 256
print(a  is  not  b) # False
print(a == b) # True


# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) # False (a is an integer object and b is a float object, so they are not the same object)
print(a is not b) # True 
print(a == b) # True (a and b have the same value of 25, so they are considered equal in value)


# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print()  
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False (x and y are two different list objects)
print(x  is  not  y) # True
print(x == y) # True (x and y have the same contents, so they are considered equal in value)
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True
print(m  is  not  n) # False
print(m == n) # True (m and n have the same contents, so they are considered equal in value)
print(x == m) # False (x is a list and m is a tuple, so they are not equal in value)


# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False (x and y have different contents, so they are not equal in value)
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # False (a and b have different contents, so they are not equal in value)
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  # True (p and q have the same contents, so they are considered equal in value)
m = range(5)
n = range(5)
print(m == n) # True (m and n represent the same range of numbers, so they are considered equal in value)


# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  # False (a is a list and b is a tuple, so they are not the same object)
print(a  ==  b) # False (a is a list and b is a tuple, so they are not equal in value)



# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True (space character is present in the string)
print('gre' in s) #True
print('yd i' in s) # True
print('' in s) #True
print('' not in s) # False



#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) #  -(-a) = -(-25) = 25
print(a--) #  (a-)-  = a- = 25-   --->  Error
print(a--1) #  a - (-1)  = 25 - (-1) = 25 + 1 = 26
print(-a) # -25
print(+-a) # +(-a) = -(a) = -25
print(-+a) # -(+a) = -(a) = -25

#  Semicolon  demo  program
print('One'); # One
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') # Hyd Sec Cyb all are printed in 3 separate lines


#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) #  (-2) ^ (-3) = -1/(-2)^3 = -1/-8 = 0.125
print(math . pow(10 , -2)) #  10 ^ (-2) = 1/10^2 = 1/100 = 0.01
print(math . pow(4 , math . pow(3 , 2))) #  4 ^ (3 ^ 2) = 4 ^ 9 = 262144


# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) # 5.0
print(math . sqrt(10)) # 3.16
print(math . sqrt(6.25)) # 2.5
print(math . sqrt(True)) # 1.0
print(math . sqrt(3+4j)) # 2.0 + 1.0j
print(math . sqrt(math . sqrt(256))) # 4.0 (sqrt(256) = 16.0, and sqrt(16.0) = 4.0)
print(math . sqrt(math . pow(3 , 4)))# 9.0 (pow(3, 4) = 81.0, and sqrt(81.0) = 9.0)
print(math . sqrt(-16)) # Error 
print(sqrt(49)) # Error because sqrt is not defined without math. 

# fabs()  function  demo   program
import  math
print(math . fabs(-10)) # 10.0
print(math . fabs(-25.6)) # 25.6
print(math . fabs(20)) # 20.0
print(math . fabs(35.8)) # 35.8
print(fabs(-25)) # Error because fabs is not defined without math.


#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) # 25
print(math . ceil(25.0)) # 25
print(math . floor(-3.5)) # -4 (floor of a negative number is the next lower integer)
print(math . ceil(-3.5)) # -3 (ceil of a negative number is the next higher integer)
print(math . floor(-9.0)) # -9 (floor of -9.0 is -9)
print(math . ceil(-9.0)) # -9 (ceil of -9.0 is -9)
print(math . floor(25.1)) # 25 (floor of 25.1 is the next lower integer)
print(math . ceil(25.1)) # 26 (ceil of 25.1 is the next higher integer)
print(floor(3.5)) # Error because floor is not defined without math.
print(ceil(3.5)) # Error because ceil is not defined without math.



