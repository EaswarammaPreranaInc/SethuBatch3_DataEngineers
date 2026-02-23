 #  Find  outputs
print({10 , 20}  |  {30 , 20})#{10, 20, 30} 
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#{10 : 'Hyd' , 20 : 'Sec',30 : 'Cyb' , 20 : 'Vja'}
print(range(4) | range(5))#error
print([10 , 20]  |  [30 , 20])#error

 #  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)#prev integer(5.25)= 5.0
print(10 // 3)#prev integer(3.33)=3.0
print(10.0 // 3)#prev integer(3.33)=3.0
print(8.5 // 3)#prev integer(2.83)=2.0
print(18 // 4)#prev integer(4.5)=4.0
print(-18 // 4)  #  Tricky#-5
print(-(18 // 4))  #  Tricky#-4


 # Find outputs
print(7 / 0)#0
print(7 // 0)#0
print(7 % 0)#0

# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)#10^-2=100=0.1
print(4 * 3 * 2)#24
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8) # True
print(6 <= 6)#True
print(6 <= 4)#false
print(9 != 7)#True
print(6 == 8)#false
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#true
print(3 + 4j == 5 + 6j)# false
print(3 + 4j != 5 + 6j)#false
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#error

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')#True
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#true

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)#false
print(1 < 2 < 3 < 4)#True
print(1 < 2 > 3 > 1)#false
print(4 > 3 >= 3 > 2)#True
 
#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)#0
print(''  or  35)#35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#3+4j
print('Hyd'   or   10.8)#'Hyd' 

# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)#true
print(not  'Hyd')# true
print(not  '')#false
print(not  -10)#false
print(not  not  'Hyd')#true

 #  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)#true
print(not(6 < 4  or  9 >= 5  and  6 != 6))#true

 #  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)#25
b =  a
print(b)#25
print(a  is  b)#true
x = 4
y = 5
z = x + y * 6
print(z)#40
25 = a#error
a + b = x + y#error

 # Find outputs (Home work)
a = b = c = 25
print(id(a))#Address of object (25)
print(id(b))#address of object(25)
print(id(c))#address of object(25)
print(a , b , c)#25 25 25

 # Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 #a = a%3+(2*4)=10.8
print(a)#10.8

 # Find outputs (Home work)
a = 3
a **= 4 #a=a**4
print(a)#81

 # Identity operators demo program
a = 25
b = 25
print(a  is  b)#true
print(a  is  not  b)#false
print(a == b)#true

 # Find outputs (Home work)
a = 25
b = 25.0
print(a is b)#false
print(a is not b)#false
print(a == b)#true

 # Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)#true
print(a  is  not  b)#false
print(a == b)#true
print()
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)#false
print(x  is  not  y)#false
print(x == y)#true
print()
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)#true
print(m  is  not  n)#false
print(m == n)#true
print(x == m)#true

# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #false
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  #false
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)# true 
m = range(5)
n = range(5)
print(m == n)#true

 # Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  #false
print(a  ==  b)#true

 # Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#true
print(19 in list)#false
print(14 not in list)#false
print(15 not in list)#false
s = 'Hyd is green city'
print( 'is' in s)#true
print('was' in s)#false
print('g' in s)#true
print('z' in s)#false
print(' ' in s)#true
print('gre' in s)#true
print('yd i' in s)#true
print('' in s)#true
print('' not in s)#false

 #  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)#-(-a)=-a=-25
print(a--)#(a-)-=a+=25+
print(a--1)#a-(-1)=a+1=25+1=26
print(-a)#-25
print(+-a)#-25
print(-+a)#error

 #  Semicolon  demo  program
print('One');#one
print('Two');#two
print('Three');#three
print('Hyd')  ;   print('Sec')  ;  print('Cyb')#'Hyd','Sec',Cyb'
 #pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))#-2^-3=-8
print(math . pow(10 , -2))#10^-2=0.01
print(math . pow(4 , math . pow(3 , 2)))#4*3^2=4*9=262.144


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
print(math . sqrt(25))#120
print(math . sqrt(10))#100
print(math . sqrt(6.25))#39.0
print(math . sqrt(True))#1
print(math . sqrt(3+4j))#error
print(math . sqrt(math . sqrt(256)))#65536
print(math . sqrt(math . pow(3 , 4)))#729
print(math . sqrt(-16))#4
print(sqrt(49))#error



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
print(math . fabs(-10))#11.0
print(math . fabs(-25.6))#26.0
print(math . fabs(20))#19.5
print(math . fabs(35.8))#35.0
print(fabs(-25))#-25.5


'''
fabs()  function
-------------------
1) What  does  fabs(-ve  value)  do ?  --->  Returns  +ve   value

2) What  does  fabs(+ve  value)  do ?  --->  Returns  same  value

3) What  is  the  result  of  fabs(integer (or) float)  --->  Always  float  irrespective  of  the  argument
'''

floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0))#24
print(math . ceil(25.0))#26
print(math . floor(-3.5))#-3
print(math . ceil(-3.5))#-4
print(math . floor(-9.0))#-8
print(math . ceil(-9.0))#-8
print(math . floor(25.1))#26
print(math . ceil(25.1))#24
print(floor(3.5))#4
print(ceil(3.5))#3


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  --->  In  math  module
'''
