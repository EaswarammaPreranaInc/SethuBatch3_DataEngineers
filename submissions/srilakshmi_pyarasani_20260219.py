1) outputs
print({10 , 20}  |  {30 , 20})#{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#{10: 'Hyd', 20: 'Vja', 30: 'Cyb'}
print(range(4) | range(5)) #Error because in range it is not permitted
print([10 , 20]  |  [30 , 20]) #Error because in list it is not permitted

2) operator  demo  program outputs
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)#5.0
print(10 // 3)#3
print(10.0 // 3)#3.0
print(8.5 // 3)#2.0
print(18 // 4)#4
print(-18 // 4)#-5
print(-(18 // 4))#-4

3) outputs
print(7 / 0)#Error because it is not valid
print(7 // 0)#Error because it is not valid
print(7 % 0)#Error because it is not valid

4) ** operator demo program outputs
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)#0.01
print(4 ** 3 ** 2)#262144
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0

5) Relational  operators  demo  program outputs
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)# True
print(6 <= 6)#True
print(6 <= 4)#False
print(9 != 7)#True
print(6 == 8)#False
print(True  >  False)#True
print(3 + 4j == 3 + 4j)#True
print(3 + 4j == 5 + 6j)#False
print(3 + 4j != 5 + 6j)#True
print(10 == 10.0)#True
print(3 + 4j >  3 + 4j)#Error because it is not valid

6) outputs
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')#True
print('Rama  Rao'  >=  'Rama')#True
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#True


7) Chaining  relational  operators outputs
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)#False
print(1 < 2 < 3 < 4)#True
print(1 < 2 > 3 > 1)#False
print(4 > 3 >= 3 > 2)#True


8)  or  operator  demo program outputs
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)#-25
print(''  or  35)#35
print(6j  or  'Hyd')#36j
print(0.0  or  3 + 4j)#3+4j
print('Hyd'   or   10.8)#Hyd


9) not  operator  demo  program outputs
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)#True
print(not  'Hyd')#False
print(not  '')#True
print(not  -10)#False
print(not  not  'Hyd')#True

10) outputs
i = 10
i = not  i > 14
print(i) #True
print(not(6 < 4  or  9 >= 5  and  6 != 6))#True


11) Assignment  operators  demo  program outputs
a = 25
print(a)#25
b =  a
print(b)#25
print(a  is  b)#True
x = 4
y = 5
z = x + y * 6
print(z)#34
25 = a
a + b = x + y

12) outputs
a = b = c = 25
print(id(a))# Address of object a 
print(id(b))# same address
print(id(c))# same address
print(a , b , c)

13) Multiple  Assignment 
x , y , z = 25 , 10.8 , 'Hyd'
print(x)#25
print(y)#10.8
print(z)#Hyd

14) outputs 
a , b , c = 3 , 4 , 5
a *= b + c   
print(a)#27

15) outputs 
a = 20
a %= 3 + 2 * 4 
print(a)#9

16) outputs 
a = 3
a **= 4 
print(a)#81

17) Identity operators demo program outputs
a = 25
b = 25
print(a  is  b)#True
print(a  is  not  b)#False
print(a == b)#True

18) outputs
a = 25
b = 25.0
print(a is b)#False
print(a is not b)#True
print(a == b)#True

19) outputs 
a = 'Hyd'
b = 'Hyd'
print(a  is  b)#True
print(a  is  not  b)#False
print(a == b)#True
print()#Empty
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)#False
print(x  is  not  y)#True
print(x == y)#True
print()#Empty
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)#True
print(m  is  not  n)#False
print(m == n)#True
print(x == m)#False

20) outputs 
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  #False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  #True
m = range(5)
n = range(5)
print(m == n)#True

21) outputs 
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  #False
print(a  ==  b)#False

22) Membership operators demo program outputs
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#True
print(19 in list)#False
print(14 not in list)#True
print(15 not in list)#False
s = 'Hyd is green city'
print( 'is' in s)#True
print('was' in s)#False
print('g' in s)#True
print('z' in s)#False
print(' ' in s)#True
print('gre' in s)#True
print('yd i' in s)#True
print('' in s)#True
print('' not in s)#False

23) ++  and  --  operators  demo  program outputs
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) #25
print(a--)#Error
print(a--1)#26
print(-a)#-25
print(+-a)#-25
print(-+a)#-25

24) Semicolon  demo  program outputs
print('One');#One
print('Two');#Two
print('Three');#Three
print('Hyd')  ;  #Hyd
print('Sec')  ; #Sec
 print('Cyb')#Cyb

25) pow()  function  demo  program outputs
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))#-0.125
print(math . pow(10 , -2))#0.01
print(math . pow(4 , math . pow(3 , 2)))#262144.0


26) sqrt()  function  demo  program outputs
import  math
print(math . sqrt(25))#5.0
print(math . sqrt(10))#3.16
print(math . sqrt(6.25))#2.5
print(math . sqrt(True))#1.0
print(math . sqrt(3+4j))#Error because it is not valid
print(math . sqrt(math . sqrt(256)))#4.0
print(math . sqrt(math . pow(3 , 4)))#9.0
print(math . sqrt(-16))#Error because it is not valid
print(sqrt(49))#Error because it is not valid

27) fabs()  function  demo   program outputs
import  math
print(math . fabs(-10))#10.0
print(math . fabs(-25.6))#25.6
print(math . fabs(20))#20.0
print(math . fabs(35.8))#35.8
print(fabs(-25))#Error because it is not valid


28)  floor()  and  ceil()  functions  demo  program outputs
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0))#25
print(math . ceil(25.0))#25
print(math . floor(-3.5))#-4
print(math . ceil(-3.5))#-3
print(math . floor(-9.0))#-9
print(math . ceil(-9.0))#-9
print(math . floor(25.1))#25
print(math . ceil(25.1))#26
print(floor(3.5))#Error because it is not valid
print(ceil(3.5))#Error because it is not valid



