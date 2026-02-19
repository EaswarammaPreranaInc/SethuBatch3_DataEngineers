# Find outputs (Home work)
a = 3  
a **= 4 
print(a) # 81

# Identity operators demo program
a = 25
b = 25
print(a  is  b) #True
print(a  is  not  b) # False
print(a == b) # True

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b) # False
print(a is not b) # True
print(a == b) # True

# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) # True
print(a  is  not  b) # False
print(a == b)  # True
print()

x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) # False
print(x  is  not  y) # True
print(x == y) # True
print()

m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) #True
print(m  is  not  n) # False
print(m == n) # True
print(x == m) # False


# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False 
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b) # False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True
m = range(5)
n = range(5)
print(m == n)# True


# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b) # False  
print(a  ==  b) # False

# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) #True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city'
print( 'is' in s)# True
print('was' in s) # False
print('g' in s)# True
print('z' in s)#False
print(' ' in s)# True
print('gre' in s)# True
print('yd i' in s)# True
print('' in s) # True
print('' not in s)# False


#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)    # 25
print(a--)    #error
print(a--1)    # 26
print(-a)      #-25
print(+-a)     #-25  
print(-+a)     #-25


#  Semicolon  demo  program
print('One');
print('Two');
print('Three');
print('Hyd')  ;   print('Sec')  ;  print('Cyb')


#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) #-0.125
print(math . pow(10 , -2)) #0.01
print(math . pow(4 , math . pow(3 , 2)))#262144.0


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
 

# sqrt()  function  demo  program
import  math
print(math . sqrt(25)) #5
print(math . sqrt(10)) #3.16
print(math . sqrt(6.25))#2.5
print(math . sqrt(True))#1.0
print(math . sqrt(3+4j)) # error as arg can't be complex
print(math . sqrt(math . sqrt(256)))# 4.0
print(math . sqrt(math . pow(3 , 4)))# 9.0
print(math . sqrt(-16)) # error
print(sqrt(49)) # error



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



# fabs()  function  demo   program
import  math
print(math . fabs(-10)) # 10
print(math . fabs(-25.6))  # 25.6
print(math . fabs(20)) # 20
print(math . fabs(35.8))# 35.8
print(fabs(-25))# error


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
print(math . ceil(25.0))# 25
print(math . floor(-3.5)) # -4
print(math . ceil(-3.5))  # -3
print(math . floor(-9.0)) # -9
print(math . ceil(-9.0))#-9
print(math . floor(25.1))# 25
print(math . ceil(25.1)) # 26
print(floor(3.5))# error
print(ceil(3.5))#error


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  --->  In  math  module
'''
