#  Find  outputs
print({10 , 20}  |  {30 , 20}) # {10 , 20 , 30} because set union operators
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10 : 'Hyd' , 20 : 'Vja' , 30 : 'Cyb'} because dict union operators
print(range(4) | range(5)) # range(0 , 5) because range union operators
print([10 , 20]  |  [30 , 20]) # error because list does not support union operators





#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)  #  prev  integer(5.25)   = 5.0
print(10 // 3)  #  prev  integer(3.3333)   = 3
print(10.0 // 3)  #  prev  integer(3.3333)   = 3.0
print(8.5 // 3)  #  prev  integer(2.8333)   = 2.0
print(18 // 4)   #  prev  integer(4.5)   = 4 
print(-18 // 4)  #  prev interger(-4.5)  = -5
print(-(18 // 4))  #  prev  integer(4.5)   = -4





# Find outputs
print(7 / 0)  # error because of division by zero
print(7 // 0)  # error because of floor division by zero
print(7 % 0)  # error because of modulus by zero




# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)  #  10 ^ -2 = 0.01
print(4 ** 3 ** 2)  # 4 ^ (3 ^ 2) = 4 ^ 9 = 
print(3 + 4 * 5 - 32 / 2 ** 3)  # 3 + 4 * 5 - 32 / 2 ** 3 = 3 + 20 - 32 / 8 = 3 + 20 - 4 =







#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)  #   True
print(6 <= 6) #   True
print(6 <= 4) #  False
print(9 != 7)  #  True
print(6 == 8)  #  False
print(True  >  False)  #  True 
print(3 + 4j == 3 + 4j)  #  True
print(3 + 4j == 5 + 6j)  #  False
print(3 + 4j != 5 + 6j)  #  True
print(10 == 10.0)  #  True
print(3 + 4j <  3 + 4j)   # error






#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')  #  True :  
print('Rama  Rao'  >=  'Rama')  #  True :  'Rama  Rao' > 'Rama' because of the extra characters after 'Rama'
print('Hyd'  != 'Sec')  #  True
print('HYD'  <   'hyd')  #  True :  'H' < 'h' because of the ASCII values of the characters




# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)  #  False
print(1 < 2 < 3 < 4)  #  True
print(1 < 2 > 3 > 1)  #  False
print(4 > 3 >= 3 > 2)  #  True







#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)  #  -25
print(''  or  35) #  35
print(6j  or  'Hyd')  #  6j
print(0.0  or  3 + 4j)   #  3 + 4j
print('Hyd'   or   10.8)  #  'Hyd'




# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)  #   True
print(not  'Hyd') #   False
print(not  '')  #   True
print(not  -10)  #   False
print(not  not  'Hyd')  #   True 









#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)  # false because 10>14 is true  (not true = false)
print(not(6 < 4  or  9 >= 5  and  6 != 6))  # dont know




#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)  # 25
b =  a
print(b)  # 25
print(a  is  b)    # True because a and b refer to the same obj in memory
x = 4
y = 5
z = x + y * 6
print(z)   # 34
25 = a  # error because 25 is a value so its not useful for referencing an obj in memory
a + b = x + y   # error because a + b is an expression and expressions cannot be assigned a value








# Find outputs (Home work)
a = b = c = 25
print(id(a))   # address of the id of the value 25
print(id(b))   # address of the id of the value 25
print(id(c))  # address of the id of the value 25
print(a , b , c)  # 25 25 25 because a , b and c all refer to the same obj in memory which has the value 25




# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)  # 25
print(y)  # 10.8
print(z)  # 'Hyd'






# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a)  # 27






# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) # error









# Find outputs (Home work)
a = 3
a **= 4 
print(a)  # 81




# Identity operators demo program
a = 25
b = 25
print(a  is  b)  # true
print(a  is  not  b)  # false
print(a == b)  # true




# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)  # false 
print(a is not b)  # true
print(a == b)  # true






# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # true
print(a  is  not  b)  # false
print(a == b)  # true
print() # empty 
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]
print(x is y)  # false
print(x  is  not  y) # true
print(x == y) # true
print() # empty
m = (1 , 2 , 3 , 4)  
n = (1 , 2 , 3 , 4)
print(m  is  n)   # true
print(m  is  not  n)  # false
print(m == n) # true
print(x == m) # false because of list and tuple objects



# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)   # false because of list and tuple objects
print(a  ==  b)  # true because the values in the list and tuple are the same




# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)  # True because 15 is an element of the list
print(19 in list)  # False because 19 is not an element of the list
print(14 not in list)   # True because 14 is not an element of the list
print(15 not in list)   # False because 15 is an element of the list
s = 'Hyd is green city'
print( 'is' in s)   # True because 'is' is a substring of s
print('was' in s)  # False because 'was' is not a substring of s
print('g' in s)  # True because 'g' is a character in s
print('z' in s)  # False because 'z' is not a character in s
print(' ' in s)  # True because ' ' (space) is a character in s
print('gre' in s) # True because 'gre' is a substring of s
print('yd i' in s) # True because 'yd i' is a substring of s
print('' in s)  # True because '' (empty string) is a substring of every string
print('' not in s)  # False because '' (empty string)





#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)  #  -(-a) = -(-25) = 25
print(a--)  #  (a-)-  = a- = 25-   --->  Error
print(a--1)  #  a - (-1)  = 25 - (-1) = 25 + 1 = 26
print(-a)  #  -25
print(+-a)   #  +(-a) = -a = -25
print(-+a)   #  -(+a) = -a = -25




#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) #  (-2) ^ (-3) = -1/8 =
print(math . pow(10 , -2))  #  10 ^ (-2) = 1/100 = 0.01
print(math . pow(4 , math . pow(3 , 2)))  # 4 ^ (3 ^ 2) = 4 ^ 9 =




# sqrt()  function  demo  program
import  math
print(math . sqrt(25))  # 5.0
print(math . sqrt(10))  
print(math . sqrt(6.25)) 
print(math . sqrt(True)) # 1.0 because True is treated as 1 in numeric contexts
print(math . sqrt(3+4j))  
print(math . sqrt(math . sqrt(256))) # sqrt(16) = 4.0
print(math . sqrt(math . pow(3 , 4)))  # sqrt(81) = 9.0
print(math . sqrt(-16))  # error because of negative numders
print(sqrt(49))  # error because of not def it






# fabs()  function  demo   program
import  math
print(math . fabs(-10))
print(math . fabs(-25.6))
print(math . fabs(20))
print(math . fabs(35.8))
print(fabs(-25))






#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0))  # 25
print(math . ceil(25.0))  # 25
print(math . floor(-3.5))  #  -4
print(math . ceil(-3.5))  #  -3
print(math . floor(-9.0))  #  -9
print(math . ceil(-9.0))  #  -9
print(math . floor(25.1))  # 25
print(math . ceil(25.1))  # 26
print(floor(3.5))  # error because of not def it
print(ceil(3.5))  # error because of not def it







