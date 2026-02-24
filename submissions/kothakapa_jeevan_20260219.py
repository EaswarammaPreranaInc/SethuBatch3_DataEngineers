#  Find  outputs
print({10 , 20}  |  {30 , 20}) ---> { 10, 20, 30 }
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})---> { 10:Hyd, 20:Vja, 30:Cyb}
print(range(4) | range(5)) ---> error
print([10 , 20]  |  [30 , 20]) ---> [10,20,30,20]

#  //  operator  demo  program
print(9 // 2)   #  prev  integer(4.5)---> 4
print(9.0 // 2)  #    prev  integer(4.5) ---> 4.0
print(9 // 2.0)   #   prev  integer(4.5) ---> 4.0
print(9.0 // 2.0)   #   prev  integer(4.5) --> 4.0
print(10.5 // 2) ---> 5.25


print(10.0 // 3) --> 3.0  ---> 3.33
print(8.5 // 3) ---> 2.83
print(18 // 4) ---> 4.5
print(-18 // 4)  #  Tricky ---> -5
print(-(18 // 4))  #  Tricky ---> -4



# Find outputs
print(7 / 0) ---> error
print(7 // 0) ---> error
print(7 % 0) ---> error


# ** operator demo program
print(3 ** 4)  #   3 ^ 4 = 81
print(10 ** -2) --> 0.01
print(4 ** 3 ** 2)--> 262144
print(3 + 4 * 5 - 32 / 2 ** 3) --> 19



#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #   True  
print(9 >= 9)  #   True
print(9 >= 12)  #  False 
print(6 <= 8) ---> True
print(6 <= 6) ---> True
print(6 <= 4) ---> False
print(9 != 7) ---> True
print(6 == 8) ---> False
print(True  >  False) ---> True
print(3 + 4j == 3 + 4j) ---> True
print(3 + 4j == 5 + 6j) ----> False
print(3 + 4j != 5 + 6j) ---> True
print(10 == 10.0) ---> True
print(3 + 4j >  3 + 4j) ---> False

#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')  #  True :  'm' > 'j'
print('Rama'  <  'Sita')   #   True :   'R' < 'S'
print('Hyd'  ==  'Hyd')  #  True
print('Rama'  <=   'Ramana') --> True
print('Rama  Rao'  >=  'Rama') ---> True 
print('Hyd'  != 'Sec') --> True
print('HYD'  <   'hyd') ---> True 


# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)  #   True
print(10 >= 20 < 30)  #  False
print(10 < 20 > 30) ---> False
print(1 < 2 < 3 < 4) ---> True
print(1 < 2 > 3 > 1) ---> False
print(4 > 3 >= 3 > 2)---> True

#  or  operator  demo program
print(True  or  False)  #   True
print(False  or  True)  #   True
print(True  or  True) #  True
print(False  or   False) #  False
print(10  or  20)  #   10
print(0   or  20)  #  20
print(-25  or  0) ---> -25
print(''  or  35) ---> 35
print(6j  or  'Hyd') ---> 6j
print(0.0  or  3 + 4j) ---> 3+4j
print('Hyd'   or   10.8) ---> Hyd


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
print(i) ---> True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) --> True

#  Assignment  operators  demo  program  (Home  work)
a = 25
print(a) ---> 25
b =  a
print(b) ---> 25
print(a  is  b) ---> True
x = 4
y = 5
z = x + y * 6
print(z) ---> 34
25 = a ---> error
a + b = x + y ---> error


[12:32 PM, 2/19/2026] +91 99482 50500: # Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'
print(x) ----> 25
print(y) ----> 10.8
print(z) ----> Hyd 
[12:37 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c   
print(a)   ---> 27

[12:37 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a) --->  9

[12:37 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a = 20
a **= 4 
print(a) ---> 160000


[12:40 PM, 2/19/2026] +91 99482 50500: # Identity operators demo program
a = 25
b = 25
print(a  is  b) ---> True
print(a  is  not  b) ---> False
print(a == b) ---> True

[12:40 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a = 25
b = 25.0
print(a is b) ---> False
print(a is not b) ---> True
print(a == b) True

[12:41 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a = 'Hyd'
b = 'Hyd'
print(a  is  b) ---> False
print(a  is  not  b) ---> False
print(a == b) --> True
print() ---> empty (not error)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 3 , 4]
print(x is y) ---> False
print(x  is  not  y) --> True
print(x == y) ---> True
print() ---> empty

m = (1 , 2 , 3 , 4)
n = (1 , 2 , 3 , 4)
print(m  is  n) ---> False
print(m  is  not  n) -->True
print(m == n) ---> True
print(x == m) ---> False

[12:41 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) --> False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  ---> False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) --->True
 
m = range(5)
n = range(5)
print(m == n) ---> True
[12:41 PM, 2/19/2026] +91 99482 50500: # Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b)  --->  False
print(a  ==  b)  --->  False

[12:43 PM, 2/19/2026] +91 99482 50500: # Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) ---> True
print(19 in list) ---> False
print(14 not in list) ---> True
print(15 not in list) --> False

s = 'Hyd is green city'
print( 'is' in s) ---> True
print('was' in s) ---> False
print('g' in s) ---> True
print('z' in s) ---> False
print(' ' in s) ---> True
print('gre' in s) ---> True
print('yd i' in s) ---> True
print('' in s) --->True
print('' not in s) --> False

[12:46 PM, 2/19/2026] +91 99482 50500: #  ++  and  --  operators  demo  program
a = 25
print(++a)  #   +(+a) = +a = +25 = 25
print(a++)   #  (a+)+  = a+ = 25+   --->  Error
print(a++1)  #  a + (+1)  =  25 + 1 = 26
print(--a) ---> 25
print(a--) ---> error
print(a--1) --> 26
print(-a) --> -25
print(+-a) --> -25
print(-+a) --> -25

[12:46 PM, 2/19/2026] +91 99482 50500: #  Semicolon  demo  program
print('One'); ---> One
print('Two'); ---> Two
print('Three'); --> Three
print('Hyd')  ;   print('Sec')  ;  print('Cyb') 
   ---> Hyd 
        Sec
        Cyb

[12:56 PM, 2/19/2026] +91 99482 50500: #pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8
print(math . pow(-2 , -3)) ---> -0.125
print(math . pow(10 , -2)) ---> 0.01
print(math . pow(4 , math . pow(3 , 2))) ---> 262144.0




[1:03 PM, 2/19/2026] +91 99482 50500: # sqrt()  function  demo  program
import  math
print(math . sqrt(25)) ---> 5
print(math . sqrt(10))---> 3.16
print(math . sqrt(6.25)) ---> 2.5
print(math . sqrt(True)) ---> 1.0
print(math . sqrt(3+4j)) ---> error ( complex not applies for sqrt() )
print(math . sqrt(math . sqrt(256))) ---> 4.0
print(math . sqrt(math . pow(3 , 4)))---> 9.0

print(math . sqrt(-16)) ---> error ( negative values may raise error)
print(sqrt(49)) ---> error  ---> (here we have to impport math module explicitly)


[1:04 PM, 2/19/2026] +91 99482 50500: # fabs()  function  demo   program
import  math
print(math . fabs(-10)) --> 10.0
print(math . fabs(-25.6)) --> 25.6
print(math . fabs(20)) --> 25
print(math . fabs(35.8)) --> 35.8
print(fabs(-25))--> error

# floor()  and  ceil()  functions  demo  program

import  math
print(math . floor(10.8))  #  10
print(math . ceil(10.8))  #   11
print(math . floor(25.0)) --> 25
print(math . ceil(25.0)) --> 25
print(math . floor(-3.5)) --> -4
print(math . ceil(-3.5)) --> -3
print(math . floor(-9.0))--> -9
print(math . ceil(-9.0)) --> -9
print(math . floor(25.1)) --> 25
print(math . ceil(25.1))---> 26
print(floor(3.5)) --> error 
print(ceil(3.5)) --> error

