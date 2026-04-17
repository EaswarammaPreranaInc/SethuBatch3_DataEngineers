#  //  operator  demo  program
print(9 // 2)   #O/P:  prev  integer(4.5)   = 4
print(9.0 // 2)  #O/P :   prev  integer(4.5)   = 4.0
print(9 // 2.0)   #O/P :  prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #O/P:   prev  integer(4.5)   = 4.0
print(10.5 // 2) #O/P: prev integer(5.25) = 5
print(10 // 3)   #O/P: prev integer(3.33) = 3
print(10.0 // 3) #O/P :prev integer(3.33) = 3
print(8.5 // 3)  #O/P :prev integer(2.5) = 2
print(18 // 4)   #O/P :prev interger (4.5) =4
print(-18 // 4)  #O/P :prev interger (-4.5)=-5
print(-(18 // 4))  #O/P:  (-(4)) --> -4



 # Find outputs
print(7 / 0) #O/P:error
print(7 // 0) #O/P:error
print(7 % 0) #O/P:error


 # ** operator demo program
print(3 ** 4)  #O/P :3 ^ 4 = 81
print(10 ** -2) #O/P: 10^-2 = 1/(10^2) = 0.01
print(4 * 3 * 2) #O/P: 24
print(3 + 4 * 5 - 32 / 2 ** 3) #O/P: 19.0  


#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #O/P:  True  
print(9 >= 9)  #O/P:   True
print(9 >= 12)  #O/P:  False 
print(6 <= 8)  #O/P:True
print(6 <= 6)	#O/P:True
print(6 <= 4)	#O/P:False
print(9 != 7)	#O/P:True
print(6 == 8)	#O/P:False
print(True  >  False)    #O/P: True
print(3 + 4j == 3 + 4j)	#O/P: True
print(3 + 4j == 5 + 6j)	#O/P:False
print(3 + 4j != 5 + 6j)	#O/P:True
print(10 == 10.0)	#O/P:True
print(3 + 4j >  3 + 4j)	#O/P:TypeError


 #  Find  outputs  (Home  work)
print('Rama' > 'Rajesh')   # O/P : True
print('Rama' < 'Sita')     # O/P : True
print('Hyd' == 'Hyd')       # O/P : True
print('Rama' <= 'Ramana')      # O/P : True
print('Rama  Rao' >= 'Rama')  # O/P : True
print('Hyd' != 'Sec')     # O/P : True
print('HYD' < 'hyd')     # O/P : True



 # Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  # O/P : True
print(10 >= 20 < 30) # O/P : False
print(10 < 20 > 30)   # O/P : False
print(1 < 2 < 3 < 4)   # O/P : True
print(1 < 2 > 3 > 1)  # O/P : False
print(4 > 3 >= 3 > 2)   # O/P : True


 #  or  operator  demo program
print(True or False) # O/P : True
print(False or True)   # O/P : True
print(True or True)  # O/P : True
print(False or False)  # O/P : False
print(10 or 20)     # O/P : 10
print(0 or 20)          # O/P : 20
print(-25 or 0)    # O/P : -25
print('' or 35)  # O/P : 35
print(6j or 'Hyd')  # O/P : 6j
print(0.0 or 3 + 4j)  # O/P : (3+4j)
print('Hyd' or 10.8)   # O/P : Hyd




 # not  operator  demo  program
print(not True)   # O/P : False
print(not False) # O/P : True
print(not 25)  # O/P : False
print(not 0)  # O/P : True
print(not 'Hyd')    # O/P : False
print(not '')   # O/P : True
print(not -10)   # O/P : False
print(not not 'Hyd') # O/P : True




 #  Find   outputs (Home work)
i = 10
i = not i > 14
print(i)    # O/P : True
print(not(6 < 4 or 9 >= 5 and 6 != 6))   # O/P : True


 #  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)  # O/P :25
b =  a
print(b)  # O/P : 25
print(a  is  b) # O/P : True
x = 4
y = 5
z = x + y * 6
print(z) # O/P :34
25 = a # O/P : error
a + b = x + y # O/P :error	


# Find outputs (Home work)
a = b = c = 25
print(id(a)) #O/P :Same id
print(id(b))  #O/P : Same id
print(id(c))  #O/P : Same id
print(a, b, c)  #O/P :  25 25 25


 # Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) #O/P :25
print(y) #O/P :10.8
print(z) #O/P :'Hyd"


 # Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a) #O/P :27


 # Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) #O/P :9


 # Find outputs (Home work)
a = 3
a **= 4 
print(a) #O/P :81


 # Identity operators demo program
a = 25
b = 25
print(a is b)  #O/P : True
print(a is not b) #O/P : False
print(a == b)  #O/P : True


# Find outputs (Home work)
a = 25
b = 25
print(a is b) #O/P: True
print(a is not b) #O/P: False
print(a == b)  #O/P:True


 # Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) #O/P:True
print(a  is  not  b)#O/P:False
print(a == b)#O/P: True

x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) #O/P:False
print(x  is  not  y) #O/P: True
print(x == y) #O/P:True

m = (1,2,3,4)
n = (1,2,3,4)
print(m is n)#O/P: True (implementation dependent)
print(m is not n)#O/P: False
print(m == n)#O/P: True
print(x == m)#O/P: False


 # Find outputs (Home work)
x = [1,2,3,4]
y = [1,2,4,3]
print(x == y)#O/P: False

a = (4,1,3,2)
b = (4,2,3,1)
print(a == b)#O/P: False

p = {1,2,3,4}
q = {4,1,3,2}
print(p == q)#O/P: True

m = range(5)
n = range(5)
print(m == n)#O/P: True


# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  #O/P:False
print(a  ==  b) #O/P:False


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)               # True
print(19 in list)               # False
print(14 not in list)           # True
print(15 not in list)           # False
s = 'Hyd is green city'
print('is' in s)                # True
print('was' in s)               # False
print('g' in s)                 # True
print('z' in s)                 # False
print(' ' in s)                 # True
print('gre' in s)               # True
print('yd i' in s)              # True
print('' in s)                  # True
print('' not in s)              # False


#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26 -->error
print(--a)      # 25
print(a--)      # SyntaxError
print(a--1)     # SyntaxErrorprint(-a) 

#  Semicolon  demo  program
print('One');
print('Two');
print('Three');
print('Hyd')  ;   print('Sec')  ;  print('Cyb')


#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math.pow(-2,-3))          # -0.125
print(math.pow(10,-2))          # 0.01
print(math . pow(4 , math . pow(3 , 2))) #



 # sqrt()  function  demo  program
import  math
print(math.sqrt(25))            # 5.0
print(math.sqrt(10))            # 3.162...
print(math.sqrt(6.25))          # 2.5
print(math.sqrt(True))          # 1.0
print(math.sqrt(3+4j))          # TypeError
print(math.sqrt(-16))           # ValueError
print(sqrt(49))                 # NameError




# fabs()  function  demo   program
print(math.fabs(-10))           # 10.0
print(math.fabs(-25.6))         # 25.6
print(math.fabs(20))            # 20.0
print(math.fabs(35.8))          # 35.8
print(fabs(-25))                # NameError



#  floor()  and  ceil()  functions  demo  program
import  math
print(math.floor(10.8))         # 10
print(math.ceil(10.8))          # 11
print(math.floor(25.0))         # 25
print(math.ceil(25.0))          # 25
print(math.floor(-3.5))         # -4
print(math.ceil(-3.5))          # -3
print(math.floor(-9.0))         # -9
print(math.ceil(-9.0))          # -9
print(math.floor(25.1))         # 25
print(math.ceil(25.1))          # 26
print(floor(3.5))               # NameError
print(ceil(3.5))                # NameError

