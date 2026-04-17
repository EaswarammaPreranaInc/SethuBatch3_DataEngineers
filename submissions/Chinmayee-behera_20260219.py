#  Find  outputs
print({10 , 20}  |  {30 , 20})# {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'}) #{10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5)) #error because range can never be added or concatenated
print([10 , 20]  |  [30 , 20]) #error  because list can't be concatenated 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2) # 5.0
print(10 // 3)  # 3
print(10.0 // 3) # 3.0
print(8.5 // 3) # 2.0
print(18 // 4)  # 4
print(-18 // 4)  #  Tricky # -5
print(-(18 // 4))  #  Tricky # -4


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

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs
print(7 / 0) # ZeroDivisionError
print(7 // 0) # ZeroDivisionError
print(7 % 0) # ZeroDivisionError


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2) # 0.01
print(4 ** 3 ** 2) # 12
print(3 + 4 * 5 - 32 / 2 ** 3) #  3 + 4 * 5 - 32 / 8 --> 3 + 20 - 32 / 8 --> 3+20-4.0  --> 23-4.0 --> 19.0





'''
**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a ** b  ** c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  --->  Left  to  right

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8) #True
print(6 <= 6) #True
print(6 <= 4) #false
print(9 != 7) #True
print(6 == 8) #False
print(True  >  False) #True
print(3 + 4j == 3 + 4j) #True
print(3 + 4j == 5 + 6j) #False
print(3 + 4j != 5 + 6j) #True
print(10 == 10.0) #True
print(3 + 4j >  3 + 4j) #error because > can't be used with complex and complex

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana') #True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') #True



'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->   Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? --->  1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  ---> 65  to  90
     What  are  the  unicode  values  of  'a'  to   'z'  ?  --->  	97  to  122
     What  are  the  unicode  values  of   '0'  to  '9' ?  --->  48  to  57
     What  is  the  unicode  value  of   '$' ?  --->  36
     What  is  the  unicode  value  of  space ?  ---> 32

7) What  is  another  name  of  unicode ?  --->  Extended  Ascii (American  standard  code  for  information  and  interchange)
'''

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30) #false
print(1 < 2 < 3 < 4) #True
print(1 < 2 > 3 > 1) #false
print(4 > 3 >= 3 > 2) #True

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0) #-25
print(''  or  35) #35
print(6j  or  'Hyd') #6j
print(0.0  or  3 + 4j) # 3 + 4j
print('Hyd'   or   10.8) #Hyd





'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  --->  When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0) #True
print(not  'Hyd') # False
print(not  '') #True
print(not  -10) #False
print(not  not  'Hyd') #True



'''
not  operator
----------------
1) What  does  not  operator  do ?  --->  Complement  operation

2) Is  not  a  unary  operator  ?  --->  Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  ---> Right  to  Left
    What  is  the  associativity  of  binary  operators ?  ---> Left  to  Right  except  for  **
'''

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) # i > 14 → 10 > 14 → False, not False → True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # --> (not(6 < 4  or  True  and  False)) --> (not(False  or  False)) --> True

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) # 25
b =  a
print(b) # 25
print(a  is  b) #True
x = 4
y = 5
z = x + y * 6
print(z) #34
25 = a # error because 25 is not reference, reference can't be int object
a + b = x + y # error because reference can't be 2 operands 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Find outputs (Home work)
a = b = c = 25
print(id(a)) # address of object 25
print(id(b)) # address of object 25
print(id(c)) # address of object 25
print(a , b , c)  # 25 25 25


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) # 25
print(y) #10.8
print(z) # 'Hyd'

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   # --> a= a (b+c) --> a= 3 *(4+5) --> 3*9 -->27
print(a)  # 27

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 #20 %(3+8) --> 20 % 11 -->1.0
print(a)  # 9

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = 3
a **= 4  #-->a= a4 --> 3 * (4) --> 81
print(a) # 81

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Identity operators demo program
a = 25
b = 25
print(a  is  b) # True
print(a  is  not  b) #false
print(a == b) #true

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) #True
print(a is not b) #false
print(a == b) #true

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b) # True
print() # Empty
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False
print(x  is  not  y) # True
print(x == y) # True
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) # True
print(m  is  not  n) # False
print(m == n) # True
print(x == m) # error because x is not determined

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #false
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) #false
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) #true
m = range(5)
n = range(5)
print(m == n) #true

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  #false
print(a  ==  b) #false

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
print('z' in s) #False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) # False

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) # -(-a)= +a = 25
print(a--) # ERROR 
print(a--1) # a -(-1)= 25+1 =26
print(-a) # -25
print(+-a) # +(-25) = -25
print(-+a) # -25

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Semicolon  demo  program
print('One');
print('Two');
print('Three');
print('Hyd')  ;   print('Sec')  ;  print('Cyb') # One<next line>Two <next line>Three<next line>Hyd<next line>Sec<next line>Cyb

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))  #(-2)^-3 =-81
print(math . pow(10 , -2))  # 0.01
print(math . pow(4 , math . pow(3 , 2))) # 262144


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
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) # 5
print(math . sqrt(10)) # 3.16227766017
print(math . sqrt(6.25)) # 2.5
print(math . sqrt(True)) # 1
print(math . sqrt(3+4j)) # ERROR because complex object don't have sqrt
print(math . sqrt(math . sqrt(256))) # 4
print(math . sqrt(math . pow(3 , 4))) # 9
print(math . sqrt(-16)) # ERROR because negative integer doesn't have sqrt() value
print(sqrt(49)) # ERROR because sqrt() is not in math module and not defined 



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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# fabs()  function  demo   program
import  math
print(math . fabs(-10)) # 10.0
print(math . fabs(-25.6)) # 25.6
print(math . fabs(20)) # 20.0
print(math . fabs(35.8)) # 35.8
print(fabs(-25)) # error


'''
fabs()  function
-------------------
1) What  does  fabs(-ve  value)  do ?  --->  Returns  +ve   value

2) What  does  fabs(+ve  value)  do ?  --->  Returns  same  value

3) What  is  the  result  of  fabs(integer (or) float)  --->  Always  float  irrespective  of  the  argument
'''

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) # 25
print(math . ceil(25.0))  # 25
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5))  # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0))  # -9
print(math . floor(25.1)) # 25
print(math . ceil(25.1))  # 26
print(floor(3.5)) #error
print(ceil(3.5))  #error




----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------












