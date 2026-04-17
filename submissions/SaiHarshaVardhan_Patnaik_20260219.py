#  Find  outputs
print({10 , 20}  |  {30 , 20}) # {10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) # {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5)) # Error
print([10 , 20]  |  [30 , 20]) # Error 

#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)  = 4 
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2) # 5
print(10 // 3) # 3
print(10.0 // 3) # 3.0
print(8.5 // 3) # 2.0
print(18 // 4) # 4
print(-18 // 4)  #  Tricky -4
print(-(18 // 4))  #  Tricky -4


'''
//  operator
--------------
1) What  is  the  result  of  integer // integer ?  ---> Integer  quotient
    What  is  the  result  of  integer // float ?  --->  Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  --->	Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

2) What  is  the  result  of  integer / integer ?  --->  Float  quotient
    What  is  the  result  of  integer / float ?  ---> Float  quotient
    What  is  the  result  of  float / integer ?  ---> Float  quotient
    What  is  the  result  of  float / float ?  --->  Float  quotient

3) What  does  /  operator  do ?  --->  Performs  division  and  returns  float  quotient
     What  does  //  operator do ?  --->  Same  as  /  operator  but  the  result  of  previous-integer(Result  of  /)

4) When  is  the  result  of  //  operator  integer ?  --->  When  both  the  operands  are  integers
    When  is  the  result  of   //  operator  float  with  .0 ?  ---> When  at  least  one  operand  is  float
'''

#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True 

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
print(id(a)) # id of object 25
print(id(b)) # id of object 25
print(id(c)) # id of object 25
print(a , b , c) #  25 25 25

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) # 10.8
print(z) # Hyd

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a) # 27

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) # 9

# Find outputs (Home work)
a = 3
a **= 4 
print(a) # 81

# Identity operators demo program
a = 25
b = 25
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) # True
print(a is not b) # False 
print(a == b) # True 

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True 
print() # 
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False 
print(x  is  not  y) # True 
print(x == y) # True
print() #
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True
print(m  is  not  n) # False 
print(m == n) # True 
print(x == m) # False 

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # True
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # True
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True
m = range(5)
n = range(5)
print(m == n) # True 

# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b) # False 
print(a  ==  b) # False 

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # False
print(15 not in list) # True
s = 'Hyd is green city' 
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False 
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) #True
print('' in s) # True
print('' not in s) # False 

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) # 25
print(a--) # 25
print(a--1) # 26
print(-a) # -25
print(+-a) # -25
print(-+a) # -25 

#  Semicolon  demo  program
print('One'); # One
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') # Hyd
                                                  Sec
                                                  Cyb

#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8.0
print(math . pow(-2 , -3)) # -0.125
print(math . pow(10 , -2)) # 0.01
print(math . pow(4 , math . pow(3 , 2))) # 262144.0


'''
pow()  function
-----------------
1) What  does  pow(a , b)  do ?  ---> Returns  a ^ b

2) Where  is  pow()  function  defined ?  --->  In  math  module

3) What  are  the  two  ways  to  obtain  a ^ b ? --->  a ** b   and   math . pow(a , b)

4) Can  a  module  be  used  without  import ?  ---> No

5) What  is  the  pre-requisite  to  use  a  module ?  --->  It  needs  to  be  imported

6) What  is  a  nested  call ?  --->  A  function  call  inside  another  function  call
												      Eg:  math . pow(a , math . pow(b , c))

7) math . pow(a , math . pow(b , c))
    Which  call  is  executed  first ?  --->  Inner  call  is  executed  before  outer  call
'''

# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) # 5.0
print(math . sqrt(10)) # 3.162277660168379
print(math . sqrt(6.25)) #2.549509756796392
print(math . sqrt(True)) # 1
print(math . sqrt(3+4j)) # Error
print(math . sqrt(math . sqrt(256))) # 4
print(math . sqrt(math . pow(3 , 4))) # 9
print(math . sqrt(-16)) # Error
print(sqrt(49)) # Error



'''
sqrt()  function
-------------------
1) What  does  sqrt(x)  do ?  --->  Returns  square  root  of  'x'

2) Where  is  sqrt()  function  defined ?  --->  In  math  module

3) math . sqrt(x)
    Where  is  sqrt()  function  searched ?  ---> In  math  module

4) sqrt(x)
    Where  is   sqrt()  function  searched ? ---> In  current  module  (or)  program

5) Can  sqrt(-ve  value)  be  determined ?  ---> No  and  it  leads  to  error

6) math . sqrt(math . pow(x , y));
    Which  function  is  executed  first ? --->  Inner  function  is  executed  before  outer  function
'''

# fabs()  function  demo   program
import  math
print(math . fabs(-10)) # 10 
print(math . fabs(-25.6)) # 25.6
print(math . fabs(20)) # 20
print(math . fabs(35.8)) #35.6
print(fabs(-25)) # Error


'''
fabs()  function
-------------------
1) What  does  fabs(-ve  value)  do ?  --->  Returns  +ve   value

2) What  does  fabs(+ve  value)  do ?  --->  Returns  same  value

3) What  is  the  result  of  fabs(integer (or) float)  --->  Always  float  irrespective  of  the  argument
'''

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) # 25
print(math . ceil(25.0)) # 25
print(math . floor(-3.5)) # -3
print(math . ceil(-3.5)) # -4
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0)) # -10
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) # 26
print(floor(3.5)) # 3
print(ceil(3.5)) # 4


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  --->  In  math  module
'''