#  Find  outputs
print({10 , 20}  |  {30 , 20})#OUTPUT:{10,20,30}
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})#OUTPUT:{10 : 'Hyd' , 20 : 'Sec',30 : 'Cyb' , 20 : 'Vja'}
print(range(4) | range(5))#OUTPUT:error
print([10 , 20]  |  [30 , 20])#OUTPUT:error


#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)   = 4
print(9.0 // 2)  #    prev  integer(4.5)   = 4.0
print(9 // 2.0)   #   prev  integer(4.5)   = 4.0
print(9.0 // 2.0)   #   prev  integer(4.5)   = 4.0
print(10.5 // 2)#OUTPUT:5.0
print(10 // 3)#OUTPUT:3
print(10.0 // 3)#OUTPUT:3.0
print(8.5 // 3)#OUTPUT:2.0
print(18 // 4)#OUTPUT:4
print(-18 // 4)#OUTPUT:-4
print(-(18 // 4)) #OUTPUT:4


# Find outputs
print(7 / 0)#OUTPUT:error
print(7 // 0)#OUTPUT:error
print(7 % 0)#OUTPUT:error


# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2)#OUTPUT:0.01
print(4 * 3 * 2)#OUTPUT:24
print(3 + 4 * 5 - 32 / 2 ** 3)#OUTPUT:21

#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8)#OUTPUT:True
print(6 <= 6)#OUTPUT:True
print(6 <= 4)#OUTPUT:False
print(9 != 7)#OUTPUT:True
print(6 == 8)#OUTPUT:False
print(True  >  False)#OUTPUT:True
print(3 + 4j == 3 + 4j)#OUTPUT:True
print(3 + 4j == 5 + 6j)#OUTPUT:False
print(3 + 4j != 5 + 6j)#OUTPUT:True
print(10 == 10.0)#OUTPUT:True
print(3 + 4j >  3 + 4j)#OUTPUT:False


#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana')#OUTPUT:True
print('Rama  Rao'  >=  'Rama')#OUTPUT:True
print('Hyd'  != 'Sec')#OUTPUT:False
print('HYD'  <   'hyd')#OUTPUT:False

# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30)#OUTPUT:False
print(1 < 2 < 3 < 4)#OUTPUT:True
print(1 < 2 > 3 > 1)#OUTPUT:False
print(4 > 3 >= 3 > 2)#OUTPUT:True

#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0)#OUTPUT:-25
print(''  or  35)#OUTPUT:35
print(6j  or  'Hyd')#OUTPUT:6j
print(0.0  or  3 + 4j)#OUTPUT:3+4j
print('Hyd'   or   10.8)#OUTPUT:'Hyd'


# not  operator  demo  program
print(not  True)  #   False
print(not  False) #   True
print(not  25) #   False
print(not  0)#OUTPUT:1
print(not  'Hyd')#OUTPUT:False
print(not  '')#OUTPUT:True
print(not  -10)#OUTPUT:False
print(not  not  'Hyd')#OUTPUT:True


#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i)#OUTPUT:
print(not(6 < 4  or  9 >= 5  and  6 != 6))#OUTPUT:


#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a)#OUTPUT:25
b =  a
print(b)#OUTPUT:25
print(a  is  b)#OUTPUT:True
x = 4
y = 5
z = x + y * 6
print(z)#OUTPUT:34
25 = a  #OUTPUT:error, reference should be variable
a + b = x + y #OUTPUT:error, reference should be variable

# Find outputs (Home work)
a = b = c = 25
print(id(a))#OUTPUT:Address of int object 25
print(id(b))#OUTPUT:Address of int object 25
print(id(c))#OUTPUT:Address of int object 25
print(a , b , c)#OUTPUT:25 25 25



# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x)#OUTPUT:25
print(y)#OUTPUT:10.8
print(z)#OUTPUT:'Hyd'



# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a) #OUTPUT:17 



# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a)#OUTPUT:9



# Find outputs (Home work)
a = 3
a **= 4 
print(a)#OUTPUT:81



# Identity operators demo program
a = 25
b = 25
print(a  is  b)#OUTPUT:True
print(a  is  not  b)#OUTPUT:False
print(a == b)#OUTPUT:True

# Find outputs (Home work)
a = 25
b = 25.0
print(a is b)#OUTPUT:False
print(a is not b)#OUTPUT:True
print(a == b)#OUTPUT:False


# Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b)#OUTPUT:True
print(a  is  not  b)#OUTPUT:False
print(a == b)#OUTPUT:True
print()#OUTPUT:
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y)#OUTPUT:False
print(x  is  not  y)#OUTPUT:True
print(x == y)#OUTPUT:True
print()#OUTPUT:
m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n)#OUTPUT:True
print(m  is  not  n)#OUTPUT:False
print(m == n)#OUTPUT:True
print(x == m)#OUTPUT:False


# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) #OUTPUT:False.List compare values and order
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  #OUTPUT:False,Sets compare only values
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q)  #OUTPUT:True
m = range(5)
n = range(5)
print(m == n)#OUTPUT:True



# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)#OUTPUT:False
print(a  ==  b)#OUTPUT:False


# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)#OUTPUT:list[2]
print(19 in list)#OUTPUT:True
print(14 not in list)#OUTPUT:True
print(15 not in list)#OUTPUT:True
s = 'Hyd is green city'
print( 'is' in s)#OUTPUT:True
print('was' in s)#OUTPUT:False
print('g' in s)#OUTPUT:True
print('z' in s)#OUTPUT:False
print(' ' in s)#OUTPUT:True
print('gre' in s)#OUTPUT:True
print('yd i' in s)#OUTPUT:True
print('' in s)#OUTPUT:False
print('' not in s)#OUTPUT:True




#  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a)#OUTPUT:-(-a)=25
print(a--)#OUTPUT:(a-)- error
print(a--1)#OUTPUT:26
print(-a)#OUTPUT:-25
print(+-a)#OUTPUT:-25
print(-+a)#OUTPUT:-25


#  Semicolon  demo  program
print('One'); #OUTPUT:error
print('Two'); #OUTPUT:error
print('Three');  #OUTPUT:error
print('Hyd')  ;   #OUTPUT:error
print('Sec')  ;  #OUTPUT:error
print('Cyb') #OUTPUT:Cyd


#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3))#OUTPUT:1/-8
print(math . pow(10 , -2))#OUTPUT:0.01
print(math . pow(4 , math . pow(3 , 2)))#OUTPUT:4^9


# sqrt()  function  demo  program
import  math
print(math . sqrt(25))#OUTPUT:5.0
print(math . sqrt(10))#OUTPUT:3.16
print(math . sqrt(6.25))#OUTPUT:2.5
print(math . sqrt(True))#OUTPUT:1
print(math . sqrt(3+4j))#OUTPUT:error
print(math . sqrt(math . sqrt(256)))#OUTPUT:4.0
print(math . sqrt(math . pow(3 , 4)))#OUTPUT:9.0
print(math . sqrt(-16))#OUTPUT:error
print(sqrt(49))#OUTPUT:error



# fabs()  function  demo   program
import  math
print(math . fabs(-10))#OUTPUT:10.0
print(math . fabs(-25.6))#OUTPUT:25.6
print(math . fabs(20))#OUTPUT:20.0
print(math . fabs(35.8))#OUTPUT:35.8
print(fabs(-25))#OUTPUT:error



#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0))#OUTPUT:25
print(math . ceil(25.0))#OUTPUT:25
print(math . floor(-3.5))#OUTPUT:-4
print(math . ceil(-3.5))#OUTPUT:-3
print(math . floor(-9.0))#OUTPUT:-9
print(math . ceil(-9.0))#OUTPUT:-9
print(math . floor(25.1))#OUTPUT:25
print(math . ceil(25.1))#OUTPUT:26
print(floor(3.5))#OUTPUT:error
print(ceil(3.5))#OUTPUT:error