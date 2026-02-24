#  Find  outputs
print({10 , 20}  |  {30 , 20})
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})
#print(range(4) | range(5))
#print([10 , 20]  |  [30 , 20])

#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)
print(10 // 3)
print(10.0 // 3)
print(8.5 // 3)
print(18 // 4)
print(-18 // 4)  #  Tricky
print(-(18 // 4))  #  Tricky

# Find outputs
#print(7 / 0)
#print(7 // 0)
#print(7 % 0)
#[11:47, 19/02/2026] SSSSD SRINIVAS GULLAPALLI Python Sir: # ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)
print(4 * 3 * 2)
print(3 + 4 * 5 - 32 / 2 ** 3)

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)
print(6 <= 6)
print(6 <= 4)
print(9 != 7)
print(6 == 8)
print(True  >  False)
print(3 + 4j == 3 + 4j)
print(3 + 4j == 5 + 6j)
print(3 + 4j != 5 + 6j)
print(10 == 10.0)
#print(3 + 4j >  3 + 4j)

#Find outputs Home  work
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')
print('Rama  Rao'  >=  'Rama')
print('Hyd'  != 'Sec')
print('HYD'  <   'hyd')

# Chaining  relational  opeartors  (Home work)(function) def print(
   # *values: object
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 > 1)
print(4 > 3 >= 3 > 2)

#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)
print(''  or  35)
print(6j  or  'Hyd')
print(0.0  or  3 + 4j)
print('Hyd'   or   10.8)

# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)
print(not  'Hyd')
print(not  '')
print(not  -10)
print(not  not  'Hyd')

#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)
b =  a
print(b)
print(a  is  b)
x = 4
y = 5
z = x + y * 6
print(z)
#25 = a
#a + b = x + y

# Find outputs (Home work)
a = b = c = 25
print(id(a))
print(id(b))
print(id(c))
print(a , b , c)

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)
print(y)
print(z)

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a)

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a)

# Find outputs (Home work)
a = 3
a **= 4 
print(a)

# Identity operators demo program
a = 25
b = 25
print(a  is  b)
print(a  is  not  b)
print(a == b)

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)
print(a is not b)
print(a == b)

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)
print(a  is  not  b)
print(a == b)
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)
print(x  is  not  y)
print(x == y)
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)
print(m  is  not  n)
print(m == n)
print(x == m)

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) 
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  
m = range(5)
n = range(5)
print(m == n)

# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  
print(a  ==  b)

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)
print(19 in list)
print(14 not in list)
print(15 not in list)
s = 'Hyd is green city'
print( 'is' in s)
print('was' in s)
print('g' in s)
print('z' in s)
print(' ' in s)
print('gre' in s)
print('yd i' in s)
print('' in s)
print('' not in s)

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
#print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)
#print(a--)
print(a--1)
print(-a)
print(+-a)
print(-+a)

#  Semicolon  demo  program
print('One');
print('Two');
print('Three');
print('Hyd')  ;   print('Sec')  ;  print('Cyb')

#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))
print(math . pow(10 , -2))
print(math . pow(4 , math . pow(3 , 2)))

# sqrt()  function  demo  program
import  math
print(math . sqrt(25))
print(math . sqrt(10))
print(math . sqrt(6.25))
print(math . sqrt(True))
#print(math . sqrt(3+4j))
print(math . sqrt(math . sqrt(256)))
print(math . sqrt(math . pow(3 , 4)))
#print(math . sqrt(-16))
#print(sqrt(49))

# fabs()  function  demo   program
import  math
print(math . fabs(-10))
print(math . fabs(-25.6))
print(math . fabs(20))
print(math . fabs(35.8))
#print(fabs(-25))

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0))
print(math . ceil(25.0))
print(math . floor(-3.5))
print(math . ceil(-3.5))
print(math . floor(-9.0))
print(math . ceil(-9.0))
print(math . floor(25.1))
print(math . ceil(25.1))
#print(floor(3.5))
#print(ceil(3.5))
