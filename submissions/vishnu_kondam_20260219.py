#  //  operator  demo  program
#Floor division
print(9 // 2)                                          #prev  integer(4.5)   = 4
print(9.0 // 2)                                        #prev  integer(4.5)   = 4.0
print(9 // 2.0)                                        #prev  integer(4.5)   = 4.0
print(9.0 // 2.0)                                      #prev  integer(4.5)   = 4.0
print(10.5 // 2)                                       #prev integer(5.25)=5.0
print(10 // 3)                                         #prev integer(3.33)=3
print(10.0 // 3)                                       #prev integer(3.33)=3.0
print(8.5 // 3)                                        #prev integer(2.83)= 2.0                       
print(18 // 4)                                         #prev interger(4.5)=4
print(-18 // 4)  #  Tricky                             #prev integer(-4.5)=-5
print(-(18 // 4))  #  Tricky                           #prev integer(-(4.5))=-(4)==>-4
#-------------------------------------------------------------------------------------------------------------
print(7 / 0)                                          #Error
print(7 // 0)                                         #Error
print(7 % 0)                                          #Error
#-----------------------------------------------------------------------------------------------------------
#operator demo program
print(3 ** 4)                              #81              
print(10 ** -2)                            #0.01
print(4 * 3 * 2)                           #262144
print(3 + 4 * 5 - 32 / 2 ** 3)             #19.0
#---------------------------------------------------------------------------
print(9 >= 5)                   #True
print(9 >= 9)                   #True
print(9 >= 12)                  #False
print(6 <= 8)                   #True
print(6 <= 6)                   #True
print(6 <= 4)                   #False
print(9 != 7)                   #True
print(6 == 8)                   #False
print(True  >  False)           #True
print(3 + 4j == 3 + 4j)         #True
print(3 + 4j == 5 + 6j)         #False
print(3 + 4j != 5 + 6j)         #True
print(10 == 10.0)               #True
print(3 + 4j >  3 + 4j)         #Error
#--------------------------------------------------------------------------
print('Rama'   >  'Rajesh')          #True 'm'>'j'
print('Rama'  <  'Sita')             #True 'S'>'R'
print('Hyd'  ==  'Hyd')              #True
print('Rama'  <=   'Ramana')         #True :Length matters
print('Rama  Rao'  >=  'Rama')       #True
print('Hyd'  != 'Sec')               #True
print('HYD'  <   'hyd')              #True
#---------------------------------------------------------------------------------
print(10 < 20 < 30)         #True
print(10 >= 20 < 30)        #False
print(10 < 20 > 30)         #False
print(1 < 2 < 3 < 4)        #True
print(1 < 2 > 3 > 1)        #False
print(4 > 3 >= 3 > 2)       #True
#----------------------------------------------------------------
print(True  or  False)           #True
print(False  or  True)           #True
print(True  or  True)            #True
print(False  or   False)         #False
print(10  or  20)                #10
print(0   or  20)                #20
print(-25  or  0)               #-25
print(''  or  35)               #35
print(6j  or  'Hyd')            #6j
print(0.0  or  3 + 4j)         #3+4j
print('Hyd'   or   10.8)       #Hyd
#--------------------------------------------------------------------
print(not  True)          #False
print(not  False)         #True
print(not  25)            #False
print(not  0)             #True
print(not  'Hyd')         #False
print(not  '')            #True
print(not  -10)           #False
print(not  not  'Hyd')    #True
#--------------------------------------------------------------------
i = 10                             
i = not  i > 14
print(i)                                      #True
print(not(6 < 4  or  9 >= 5  and  6 != 6))    #True
#--------------------------------------------------------------------
a = 25
print(a)                        #25
b =  a
print(b)                        #25
print(a  is  b)                 #True
x = 4
y = 5
z = x + y * 6
print(z)                       #34
25 = a                         #Error
a + b = x + y                  #Error
#---------------------------------------------------------------
a = b = c = 25
print(id(a))                  #Same address
print(id(b))                  #Same address
print(id(c))                  #Same address
print(a , b , c)              # 25 25 25
#---------------------------------------------------------------
x , y , z = 25 , 10.8 , 'Hyd'
print(x)                      #25
print(y)                      #10.8
print(z)                      #Hyd
#---------------------------------------------------------
a , b , c = 3 , 4 , 5
a *= b + c           #a=a*9 #27        
print(a)
#---------------------------------------------------------------
a = 20
a %= 3 + 2 * 4       #  a=a%11 #9
print(a)
#----------------------------------------------------
a = 3
a **= 4 
print(a)          #81
#------------------------------------------------
a = 25
b = 25
print(a  is  b)                   #True
print(a  is  not  b)              #False
print(a == b)                     #True
#---------------------------------------------------
a = 25
b = 25.0
print(a is b)                   #False
print(a is not b)               #True
print(a == b)                   #True
#---------------------------------------
a = 'Hyd'
b = 'Hyd'
print(a  is  b)            #True
print(a  is  not  b)       #False
print(a == b)              #True
print()                    
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)              #False
print(x  is  not  y)       #True
print(x == y)              #True
print()
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)
print(m  is  n)           #True
print(m  is  not  n)      #False
print(m == n)             #True
print(x == m)             #False
#============================================
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y)            #False :Order matters
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)            #False :Order matters
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}      # True
print(p == q)            
m = range(5)             
n = range(5)
print(m == n)          #True
#---------------------------------------
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)      #False
print(a  ==  b)      #False
#-------------------------------------
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)           #True
print(19 in list)           #False
print(14 not in list)       #True
print(15 not in list)       #False
s = 'Hyd is green city'    
print('is' in s)           #True
print('was' in s)           #False
print('g' in s)             #True
print('z' in s)             #False
print(' ' in s)             #True
print('gre' in s)           #True
print('yd i' in s)          #True
print('' in s)              #True
print('' not in s)          #False
#----------------------------------------
#  ++  and  --  operators  demo  program
a = 25
print(++a)   #   +(+a) = +a = +25 = 25
print(a++)   #  25+:Error
print(a++1)  #  26
print(--a)   #  25
print(a--)   #  Error
print(a--1)  #  26
print(-a)    # -25
print(+-a)   # -25
print(-+a)   # -25
#-------------------------------------------------
#  Semicolon  demo  program
print('One');     #One
print('Two');     #Two
print('Three');    #Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb')   #HYD<nextlin>Sec<nextline>Cyb
#------------------------------------------------
#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #8
print(math . pow(-2 , -3))  #-0.125
print(math . pow(10 , -2))  #0.01
print(math . pow(4 , math . pow(3 , 2)))  #262144
#--------------------------------------------
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
#----------------------------------------------------------------------------------------------
print(math.sqrt(25))              # 5.0
print(math.sqrt(10))              # 3.1622776601683795
print(math.sqrt(6.25))            # 2.5
print(math.sqrt(True))            # 1.0
print(math.sqrt(3+4j))            # Error
print(math.sqrt(math.sqrt(256)))  # 4.0
print(math.sqrt(math.pow(3, 4)))  # 9.0
print(math.sqrt(-16))             # Error
print(sqrt(49))                   # Error
#----------------------------------------------------------------------------------
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
print(math . fabs(-10))  #10.0
print(math . fabs(-25.6))  #25.6
print(math . fabs(20))  #20.0
print(math . fabs(35.8))  #35.8
print(fabs(-25))  #Error


'''
fabs()  function
-------------------
1) What  does  fabs(-ve  value)  do ?  --->  Returns  +ve   value

2) What  does  fabs(+ve  value)  do ?  --->  Returns  same  value

3) What  is  the  result  of  fabs(integer (or) float)  --->  Always  float  irrespective  of  the  argument
'''#------------------------------------------------------------------------------------------------------------------
#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))   #10
print(math . ceil(10.8))   #11
print(math . floor(25.0))  #25
print(math . ceil(25.0))   #25
print(math . floor(-3.5))  #-4
print(math . ceil(-3.5))   #-3
print(math . floor(-9.0))  #-9
print(math . ceil(-9.0))   #-9
print(math . floor(25.1))  #25
print(math . ceil(25.1))   #26
print(floor(3.5))          #3
print(ceil(3.5))           #4


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  --->  In  math  module
'''