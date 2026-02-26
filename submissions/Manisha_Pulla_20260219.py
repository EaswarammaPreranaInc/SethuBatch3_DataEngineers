#  Find  outputs
print({10 , 20}  |  {30 , 20}) #Output: {10, 20, 30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})  #Output:
print(range(4) | range(5))  #Output: {10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print([10 , 20]  |  [30 , 20])  #Output: [10,20,30]
#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)  #Output:5.0
print(10 // 3)  #Output:3
print(10.0 // 3)  #Output:3.0
print(8.5 // 3)  #Output:2.0
print(18 // 4)  #Output:4
print(-18 // 4)  #  Tricky  #Output:-5
print(-(18 // 4))  #  Tricky  #Output:-4


'''
//  operator
--------------
1) What  is  the  result  of  integer // integer ?  ---> Integer  quotient
    What  is  the  result  of  integer // float ?  --->  Float  quotient  with  .0
    What  is  the  result  of  float // integer ?  --->	Float  quotient  with  .0
    What  is  the  result  of  float // float ?  ---> Float  quotient  with  .0

2) What  is  the  result  of  integer / integer ?  --…
# Find outputs
print(7 / 0) #Output:Error
print(7 // 0) #Output: Error
print(7 % 0) #Output: Error
# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2) #Output:0.01
print(4 * 3 * 2) #Output:24
print(3 + 4 * 5 - 32 / 2 ** 3) #Output:19.0





'''
**  operator
---------------
1) What  is  **  operator  called ?  --->  Exponential  operator

2) What  is  the  result  of  a ** b ?  ---> a ^ b

3) What  is  the  result  of  a * b  * c ?   --->  a ^ b ^ c

4) What  is  the  associativity  of  **  operator ?  ---> Right  to  left
    What  is  the  associativity  of  remaining  arithmetic  operators ?  --->  Left  to  right
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8) #Output: True
print(6 <= 6) #Output: True
print(6 <= 4) #Output: False
print(9 != 7) #Output: True
print(6 == 8) #Output: False
print(True  >  False) #Output: True
print(3 + 4j == 3 + 4j) #Output: True
print(3 + 4j == 5 + 6j) #Output: False
print(3 + 4j != 5 + 6j) #Output: True
print(10 == 10.0) #Output: True
print(3 + 4j >  3 + 4j) #Output: Error
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana') #Output: True
print('Rama  Rao'  >=  'Rama') #Output: True
print('Hyd'  != 'Sec') #Output: True
print('HYD'  <   'hyd') #Output: True



'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->   Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? --->  1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  '…
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30) #Output:
print(1 < 2 < 3 < 4) #Output:
print(1 < 2 > 3 > 1) #Output:
print(4 > 3 >= 3 > 2) #Output:
#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0) #Output: -25
print(''  or  35) #Output: 35
print(6j  or  'Hyd') #Output: 6j
print(0.0  or  3 + 4j) #Output: 3+4j
print('Hyd'   or   10.8) #Output: "Hyd





'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  --->  When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''
# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0) #Output: True
print(not  'Hyd') #Output: False
print(not  '') #Output: True
print(not  -10) #Output: False
print(not  not  'Hyd') #Output: True



'''
not  operator
----------------
1) What  does  not  operator  do ?  --->  Complement  operation

2) Is  not  a  unary  operator  ?  --->  Yes  due  to  single  operand
    What  about  and ,  or ? ---> Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  ---> Right  to  Left
    What  is  the  associativity  of  binary  operators ?  ---> Left  to  Right  except  for  **
'''
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) #Output:True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) #Output:True
#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) #Output:25
b =  a
print(b) #Output:25
print(a  is  b) #Output:True
x = 4
y = 5
z = x + y * 6
print(z) #Output:34
25 = a
a + b = x + y
# Find outputs (Home work)
a = b = c = 25
print(id(a)) #Output:Address of an object
print(id(b)) #Output:Address of an object
print(id(c)) #Output:Address of an object
print(a , b , c) #Output:25 25 25
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) #Output:25
print(y) #Output:10.8
print(z) #Output:'Hyd'
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a) #Output:27
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) #Output: 9
# Find outputs (Home work)
a = 3
a **= 4 
print(a) #Output:81
# Identity operators demo program
a = 25
b = 25
print(a  is  b) #Output:True
print(a  is  not  b) #Output:False
print(a == b) #Output: True
# Find outputs (Home work) 
a = 25
b = 25.0
print(a is b) #Output: False
print(a is not b) #Output: True
print(a == b) #Output: True
# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) #Output:True
print(a  is  not  b) #Output: False
print(a == b) #Output: True
print() #Output:Empty
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) #Output:False
print(x  is  not  y) #Output:True
print(x == y) #Output:True
print() #Output:
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) #Output:True
print(m  is  not  n) #Output:False
print(m == n) #Output:True
print(x == m) #Output:Error
# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #Output: False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) #Output: False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) #Output: True
m = range(5)
n = range(5)
print(m == n) #Output: True
# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b) #Output: False
print(a  ==  b) #Output: False
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) #Output: True
print(19 in list) #Output: False
print(14 not in list) #Output: True
print(15 not in list) #Output: False
s = 'Hyd is green city'
print( 'is' in s) #Output: True
print('was' in s) #Output: False
print('g' in s) #Output: True
print('z' in s) #Output: False
print(' ' in s) #Output: True
print('gre' in s) #Output:True
print('yd i' in s) #Output: True
print('' in s) #Output: True
print('' not in s) #Output: False
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) #Output: -25
print(a--) #Output: Error
print(a--1) #Output: 26
print(-a) #Output:-25
print(+-a) #Output:-25
print(-+a) #Output:-25
#  Semicolon  demo  program
print('One'); #Output: 'One'
print('Two'); #Output: 'Two'
print('Three'); #Output: 'Three'
print('Hyd')  ;   print('Sec')  ;  print('Cyb') #Output:'Hyd'
                                                        'Sec'
                                                        'Cyb'
#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) #Output:-0.125
print(math . pow(10 , -2)) #Output:0.01
print(math . pow(4 , math . pow(3 , 2))) #Output:262144.0


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
    Whic…
# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) #Output:5.0
print(math . sqrt(10)) #Output:3.162
print(math . sqrt(6.25)) #Output:2.5
print(math . sqrt(True)) #Output:1.0
print(math . sqrt(3+4j)) #Output:Error
print(math . sqrt(math . sqrt(256))) #Output:4
print(math . sqrt(math . pow(3 , 4))) #Output:9.0
print(math . sqrt(-16)) #Output: Error
print(sqrt(49)) #Output: Error



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
    Whic…
# fabs()  function  demo   program
import  math
print(math . fabs(-10)) #Output:10
print(math . fabs(-25.6)) #Output:25
print(math . fabs(20)) #Output:20
print(math . fabs(35.8)) #Output:35.8
print(fabs(-25)) #Output:Error


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
print(math . floor(25.0)) #Output:25
print(math . ceil(25.0)) #Output:25
print(math . floor(-3.5)) #Output:-4
print(math . ceil(-3.5)) #Output:-3
print(math . floor(-9.0)) #Output:-9
print(math . ceil(-9.0)) #Output:-9
print(math . floor(25.1)) #Output:25
print(math . ceil(25.1)) #Output:26
print(floor(3.5)) #Output:Error
print(ceil(3.5)) #Output:Error


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  --->  In  math  module
'''